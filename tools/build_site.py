#!/usr/bin/env python3
"""Build the GitHub Pages site (docs/) from the Markdown guide and its audits.

The Markdown files in builds/ stay the single source of truth: never edit docs/*.html by hand.

    python3 -m pip install -r tools/requirements.txt
    python3 tools/build_site.py           # rewrite docs/
    python3 tools/build_site.py --check   # exit 1 if docs/ is out of date, write nothing
"""
from __future__ import annotations

import argparse
import hashlib
import html
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

from markdown_it import MarkdownIt
from markdown_it.token import Token

ROOT = Path(__file__).resolve().parent.parent
BUILDS = ROOT / "builds"
DOCS = ROOT / "docs"
ASSETS = DOCS / "assets"
REPO_URL = "https://github.com/tusrajamaisquichui-ctrl/Warframe"

GUIDE = "protea-prime-level-cap-endurance.md"
# (source, page, title, one-line description) for each audit page
AUDITS = (
    ("audit-protea-prime-v2.md", "audit-v2.html", "Audit hostile v2",
     "Contre‑expertise de la v1.3 : 79 affirmations vérifiées, 6 erreurs critiques, 16 tests en jeu."),
    ("audit-protea-prime-v1.md", "audit-v1.html", "Audit hostile v1",
     "Audit de la v1.0 : 12 défauts relevés, corrigés en v1.1."),
)
PAGE_OF = {GUIDE: "index.html", **{src: page for src, page, _, _ in AUDITS}}


@dataclass(frozen=True)
class Panel:
    id: str
    label: str   # tab label on desktop, panel name
    short: str   # bottom tab bar label on phones
    mark: str    # "1" / "2" / "3", or an icon name
    accent: str


PANELS = (
    Panel("accueil", "Accueil", "Accueil", "home", "home"),
    Panel("bloc-1", "Socle commun", "Socle", "1", "c1"),
    Panel("bloc-2", "Endurance standard", "Endurance", "2", "c2"),
    Panel("bloc-3", "Level Cap 9999", "Level Cap", "3", "c3"),
    Panel("annexes", "Annexes", "Annexes", "book", "annex"),
)
CARDS = {  # shortcuts on the home panel
    "bloc-1": "Toujours : kit, mods, shards, stats, énergie, survie de base.",
    "bloc-2": "Socle + Molt Augmented, Nautilus Prime, arsenal Viral.",
    "bloc-3": "Socle + Arcane Escapist, Panzer Vulpaphyla, filets de survie.",
}

_SVG = '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{}</svg>'
ICONS = {
    "home": _SVG.format('<path d="M4 10.5 12 4l8 6.5V20h-5.5v-5.5h-5V20H4z"/>'),
    "book": _SVG.format('<path d="M6.5 4H19v13H6.5A2.5 2.5 0 0 0 4 19.5v-13A2.5 2.5 0 0 1 6.5 4z"/>'
                        '<path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H19v-5"/>'),
    "list": _SVG.format('<path d="M9 6h11M9 12h11M9 18h11M4.5 6h.01M4.5 12h.01M4.5 18h.01"/>'),
    "close": _SVG.format('<path d="M6 6l12 12M18 6 6 18"/>'),
    "up": _SVG.format('<path d="M12 19V5M5.5 11.5 12 5l6.5 6.5"/>'),
}
LOGO = ('<svg class="logo" viewBox="0 0 64 64" aria-hidden="true" focusable="false">'
        '<path d="M32 4 56 18v28L32 60 8 46V18z" fill="#141a22" stroke="#e9b44c" stroke-width="4" stroke-linejoin="round"/>'
        '<path fill="#e9b44c" fill-rule="evenodd" d="M24 45V19h10.5c5.8 0 9.5 3.3 9.5 8.4S40.3 35.8 34.5 35.8H30V45z'
        'm6-20.8v6.4h4.1c2.3 0 3.7-1.2 3.7-3.2s-1.4-3.2-3.7-3.2z"/></svg>')

NUMBERED = re.compile(r"^\W*?([A-Z]?\d+(?:\.\d+)*)\.?\s")
TOC_ENTRY = re.compile(r"^(?P<pre>[^\w\s]+\s+)?(?P<num>[A-Z]?\d+(?:\.\d+)*)\.?\s+(?:—\s+)?(?P<rest>.+)$")
# A section number is linked only after one of these words, so "Version 1.4" or "l'équivalent 1.2" stay text.
XREF = re.compile(r"(cf\. |\(|\ben |[Vv]oir |, |socle |\bde |fiche )([1-3]\.\d{1,2})(?!\d|\.\d)")
ANCHOR = re.compile(r'^<a id="([\w-]+)"></a>\s*$', re.M)
# Evidence labels of the audits ("**RÉFUTÉ** (…)"), coloured in their "Statut" column
STATUS = (("NON VÉRIFIÉ", "st-warn"), ("VÉRIFIÉ", "st-ok"), ("CALCULÉ", "st-calc"), ("DÉDUIT", "st-calc"),
          ("CONTESTÉ", "st-warn"), ("INCOMPLET", "st-warn"), ("PLAUSIBLE", "st-warn"), ("RÉFUTÉ", "st-bad"),
          ("PÉRIMÉ", "st-bad"), ("QUASI NUL", "st-bad"), ("FAUX", "st-bad"))
BADGE = '<span class="tag-new" title="Ajouté ou corrigé en v{v}">v{v}</span>'


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def slugify(text: str, limit: int = 48) -> str:
    text = re.sub(r"\([^)]*\)", "", text).replace("œ", "oe").replace("æ", "ae")  # drop "(v1.4)", dates…
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if len(slug) > limit:
        slug = slug[:limit + 1].rsplit("-", 1)[0]  # cut at a word boundary
    return slug or "section"


def heading_id(text: str) -> str:
    """Short, stable ids: "1.11 Survie…" -> s1-11, "C1 — …" -> c1, anything else -> slug."""
    m = NUMBERED.match(text)
    if m:
        num = m.group(1)
        return num.lower() if num[0].isalpha() else "s" + num.replace(".", "-")
    return slugify(text)


def plain(inline: Token | None) -> str:
    if inline is None:
        return ""
    parts = []
    for child in inline.children or []:
        if child.type in ("text", "code_inline"):
            parts.append(child.content)
        elif child.type in ("softbreak", "hardbreak"):
            parts.append(" ")
    return "".join(parts).strip()


def text_token(content: str) -> Token:
    tok = Token("text", "", 0)
    tok.content = content
    return tok


def html_token(content: str) -> Token:
    tok = Token("html_inline", "", 0)
    tok.content = content
    return tok


@dataclass
class Heading:
    level: int
    id: str
    text: str


@dataclass
class Doc:
    """State shared by every chunk rendered into one HTML page."""
    page: str
    version: str = ""                                       # "(vX.Y)" markers become badges
    used: set[str] = field(default_factory=set)             # ids already taken on the page
    sections: dict[str, str] = field(default_factory=dict)  # "1.11" -> "s1-11"

    def unique(self, base: str) -> str:
        cand, n = base, 2
        while cand in self.used:
            cand, n = f"{base}-{n}", n + 1
        self.used.add(cand)
        return cand


def collect_headings(tokens: list[Token], doc: Doc) -> list[Heading]:
    heads = []
    for i, tok in enumerate(tokens):
        if tok.type != "heading_open":
            continue
        text = plain(tokens[i + 1])
        hid = doc.unique(heading_id(text))
        tok.attrSet("id", hid)
        level = int(tok.tag[1])
        heads.append(Heading(level, hid, text))
        m = re.match(r"(\d\.\d{1,2}) ", text)
        if level == 3 and m:
            doc.sections.setdefault(m.group(1), hid)
    return heads


def xref_tokens(text: str, doc: Doc) -> list[Token]:
    out, pos = [], 0
    for m in XREF.finditer(text):
        target = doc.sections.get(m.group(2))
        if not target:
            continue
        if m.start(2) > pos:
            out.append(text_token(text[pos:m.start(2)]))
        link = Token("link_open", "a", 1)
        link.attrSet("href", "#" + target)
        link.attrSet("class", "xref")
        out += [link, text_token(m.group(2)), Token("link_close", "a", -1)]
        pos = m.end(2)
    if pos < len(text):
        out.append(text_token(text[pos:]))
    return out


def transform_inline(tokens: list[Token], doc: Doc, xrefs: bool) -> None:
    """Turn "(vX.Y)" markers into badges and plain section numbers ("cf. 1.11") into links."""
    tag = f"(v{doc.version})" if doc.version else None
    for i, tok in enumerate(tokens):
        if tok.type != "inline" or not tok.children:
            continue
        linkable = xrefs and tokens[i - 1].type != "heading_open"
        children, depth = [], 0
        for child in tok.children:
            depth += {"link_open": 1, "link_close": -1}.get(child.type, 0)
            if child.type != "text":
                children.append(child)
                continue
            parts = child.content.split(tag) if tag else [child.content]
            for k, part in enumerate(parts):
                if k:
                    children.append(html_token(BADGE.format(v=doc.version)))
                if part:
                    children += xref_tokens(part, doc) if linkable and depth == 0 else [text_token(part)]
        tok.children = children


def decorate_tables(tokens: list[Token]) -> None:
    """Label cells for the phone card layout and pick a layout per table."""
    i = 0
    while i < len(tokens):
        if tokens[i].type != "table_open":
            i += 1
            continue
        head, rows, row, j = [], [], None, i
        while tokens[j].type != "table_close":
            tok = tokens[j]
            if tok.type == "tr_open":
                row = []
            elif tok.type in ("th_open", "td_open"):
                inline = tokens[j + 1] if tokens[j + 1].type == "inline" else None
                (head if tok.type == "th_open" else row).append((tok, plain(inline)))
            elif tok.type == "tr_close" and row:
                rows.append(row)
            j += 1
        ncols = len(head)
        cells = [len(text) for r in rows for _, text in r]
        mean = sum(cells) / max(1, len(cells))
        widest = [max((len(r[k][1]) for r in rows if k < len(r)), default=0) for k in range(ncols)]
        narrow = [widest[k] <= 7 and len(head[k][1]) <= 12 for k in range(ncols)]
        classes = ["table-wrap"]
        # the more columns, the less text it takes before a phone screen is too narrow for them
        stack = mean >= {2: 48, 3: 24, 4: 17}.get(ncols, 12 if ncols >= 5 else 999)
        if stack:
            classes.append("stack")      # cards on phones
            if narrow[0]:
                classes.append("num-first")
        if ncols >= 6 or (ncols == 5 and not stack):
            classes.append("wide")       # readable column widths, horizontal scroll if needed
        for k, (tok, _) in enumerate(head):
            if narrow[k]:
                tok.attrJoin("class", "nw")
        for r in rows:
            for k, (tok, text) in enumerate(r):
                if k < ncols:
                    tok.attrSet("data-label", head[k][1])
                if k < ncols and narrow[k]:
                    tok.attrJoin("class", "nw")
                if not text:
                    tok.attrJoin("class", "empty")
                elif k < ncols and head[k][1].startswith("Statut"):
                    status = next((cls for word, cls in STATUS if text.upper().startswith(word)), None)
                    if status:
                        tok.attrJoin("class", status)
        tokens[i].meta["wrap"] = " ".join(classes)
        i = j + 1


def rewrite_href(href: str, page: str) -> str:
    if href.startswith("#") or re.match(r"^[a-z][a-z0-9+.-]*:", href, re.I):
        return href
    path, sep, frag = href.partition("#")
    target = PAGE_OF.get(path.rsplit("/", 1)[-1])
    if target is None:
        print(f"warning: no page for relative link {href!r}; linking to GitHub", file=sys.stderr)
        return f"{REPO_URL}/blob/HEAD/builds/{href}"
    if target == page and frag:
        return "#" + frag
    return target + (sep + frag if frag else "")


def _table_open(self, tokens, idx, options, env):
    return f'<div class="{tokens[idx].meta.get("wrap", "table-wrap")}"><table>\n'


def _table_close(self, tokens, idx, options, env):
    return "</table></div>\n"


def _link_open(self, tokens, idx, options, env):
    tok = tokens[idx]
    href = rewrite_href(tok.attrGet("href") or "", env["page"])
    tok.attrSet("href", href)
    if href.startswith(("http://", "https://")):
        tok.attrSet("target", "_blank")
        tok.attrSet("rel", "noopener")
    return self.renderToken(tokens, idx, options, env)


def _heading_close(self, tokens, idx, options, env):
    hid = tokens[idx - 2].attrGet("id")
    anchor = f'<a class="h-anchor" href="#{hid}" aria-hidden="true" tabindex="-1">#</a>' if hid else ""
    return f"{anchor}</{tokens[idx].tag}>\n"


def _blockquote_open(self, tokens, idx, options, env):
    first = next((t for t in tokens[idx + 1:] if t.type == "inline"), None)
    warn = "⚠" in plain(first)[:3]
    return f'<blockquote class="callout{" warn" if warn else ""}">\n'


def markdown() -> MarkdownIt:
    md = MarkdownIt("commonmark", {"html": True}).enable(["table", "strikethrough"])
    for name, rule in (("table_open", _table_open), ("table_close", _table_close),
                       ("link_open", _link_open), ("heading_close", _heading_close),
                       ("blockquote_open", _blockquote_open)):
        md.add_render_rule(name, rule)
    return md


@dataclass
class Chunk:
    tokens: list[Token]
    heads: list[Heading]


def parse(md: MarkdownIt, text: str, doc: Doc) -> Chunk:
    tokens = md.parse(text, {"page": doc.page})
    return Chunk(tokens, collect_headings(tokens, doc))


def render(md: MarkdownIt, chunk: Chunk, doc: Doc, xrefs: bool) -> str:
    transform_inline(chunk.tokens, doc, xrefs)
    decorate_tables(chunk.tokens)
    return md.renderer.render(chunk.tokens, md.options, {"page": doc.page})


def badge_text(text: str, version: str) -> str:
    out = esc(text)
    if version:
        out = out.replace(esc(f"(v{version})"), BADGE.format(v=version))
    return out


def toc_html(heads: list[Heading], top: int, label: str, version: str, toc_id: str) -> str:
    tree: list[tuple[Heading, list[Heading]]] = []
    for h in heads:
        if h.level == top:
            tree.append((h, []))
        elif h.level == top + 1 and tree:
            tree[-1][1].append(h)
    if len(tree) < 2:
        return ""

    def link(h: Heading) -> str:
        m = TOC_ENTRY.match(h.text)
        num, rest = (m["num"], (m["pre"] or "") + m["rest"]) if m else ("", h.text)
        num_html = f'<span class="toc-num">{esc(num)}</span>' if num else ""
        return f'<a href="#{h.id}">{num_html}<span class="toc-text">{badge_text(rest, version)}</span></a>'

    items = []
    for h, subs in tree:
        sub = "".join(f"<li>{link(s)}</li>" for s in subs)
        items.append(f"<li>{link(h)}" + (f'<ol class="toc-sub">{sub}</ol>' if sub else "") + "</li>")
    return (f'<nav class="toc" id="{toc_id}" aria-label="Sommaire : {esc(label)}">'
            f'<div class="toc-head"><span class="toc-title">Sommaire</span>'
            f'<button class="toc-close" type="button" aria-label="Fermer le sommaire">{ICONS["close"]}</button></div>'
            f'<ol class="toc-list">{"".join(items)}</ol></nav>')


def asset_url(name: str) -> str:
    digest = hashlib.sha256((ASSETS / name).read_bytes()).hexdigest()[:10]
    return f"assets/{name}?v={digest}"


def circled(mark: str) -> str:
    return chr(0x245F + int(mark)) if mark.isdigit() else ""


def tabs_html(page: str, active: str | None = None) -> str:
    """Tab bar: real tabs on the guide page, plain links back to the guide elsewhere."""
    on_guide = page == "index.html"
    out = []
    for p in PANELS:
        icon = ICONS[p.mark] if p.mark in ICONS else f'<span class="tab-mark">{p.mark}</span>'
        long_label = f"{circled(p.mark)} {p.label}".strip()
        href = f"#{p.id}" if on_guide else f"index.html#{p.id}"
        attrs = f' data-tab="{p.id}" id="tab-{p.id}"' if on_guide else ""
        cls = "tab is-current" if p.id == active else "tab"
        out.append(f'<a class="{cls}" href="{href}"{attrs} data-accent="{p.accent}">'
                   f'<span class="tab-ico">{icon}</span>'
                   f'<span class="tab-short">{esc(p.short)}</span><span class="tab-long">{esc(long_label)}</span></a>')
    return f'<nav class="tabs" aria-label="Sections du guide"><div class="tabs-inner">{"".join(out)}</div></nav>'


def header_html(home: str, context: str, chip: str) -> str:
    return (f'<header class="site-header"><div class="bar">'
            f'<a class="brand" href="{home}">{LOGO}<span class="brand-text"><span class="brand-name">Protea Prime</span>'
            f'<span class="brand-context" data-context>{esc(context)}</span></span></a>'
            f'<span class="chip chip-version">{esc(chip)}</span>'
            f'<button class="toc-toggle" type="button" aria-expanded="false" hidden>{ICONS["list"]}<span>Sommaire</span></button>'
            f"</div></header>")


def footer_html(lines: list[str]) -> str:
    return '<footer class="site-footer"><div class="inner">' + "".join(f"<p>{l}</p>" for l in lines) + "</div></footer>"


def page_html(*, title: str, description: str, body_class: str, header: str, tabs: str, main: str, footer: str) -> str:
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="theme-color" content="#0b0e13">
<meta name="color-scheme" content="dark">
<meta property="og:type" content="article">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<link rel="icon" href="assets/icon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{asset_url('style.css')}">
<script>document.documentElement.classList.add("js")</script>
<script src="{asset_url('app.js')}" defer></script>
</head>
<body class="{body_class}">
<a class="skip-link" href="#main">Aller au contenu</a>
{header}
{tabs}
<main id="main" tabindex="-1">
{main}
</main>
{footer}
<div class="toc-backdrop" hidden></div>
<button class="to-top" type="button" aria-label="Revenir en haut de la page" hidden>{ICONS['up']}</button>
</body>
</html>
"""


def guide_meta(text: str) -> dict[str, str]:
    def find(pattern: str) -> str:
        m = re.search(pattern, text, re.M)
        if not m:
            raise SystemExit(f"guide: pattern not found: {pattern}")
        return m.group(1).strip()

    title = find(r"^# (.+)$")
    name, _, subtitle = title.partition(" — ")
    version = find(r"^\*\*v(\d+\.\d+) \(\d{2}/\d{2}/\d{4}\)\*\*")  # latest journal entry
    date = find(r"^\*\*v\d+\.\d+ \((\d{2}/\d{2}/\d{4})\)\*\*")
    return {"title": title, "name": name, "subtitle": subtitle, "version": version, "date": date,
            "patch": find(r"Patch de référence : (.+?)\.?\*\*"), "hotfix": find(r"Hotfix (\d+(?:\.\d+)+)")}


def clean_chunk(text: str) -> str:
    """Drop the Markdown-only navigation (tab line, back links) and the rules between blocks."""
    lines = [l for l in text.split("\n")
             if l.strip() != "---" and not l.startswith("**Onglets :**")
             and not re.match(r"^\[↑ Onglets\]\(#onglets\)\s*$", l)]
    return "\n".join(lines).strip("\n") + "\n"


def split_guide(text: str) -> dict[str, str]:
    pieces = ANCHOR.split(text)
    chunks = {"intro": pieces[0], **dict(zip(pieces[1::2], pieces[2::2]))}
    expected = {"intro", "onglets", *(p.id for p in PANELS[1:])}
    if set(chunks) != expected:
        raise SystemExit(f"guide: anchors {sorted(set(chunks) - {'intro'})}, expected {sorted(expected - {'intro'})}")
    intro = re.sub(r"^# .+\n", "", chunks.pop("intro"), count=1)
    chunks["accueil"] = intro + "\n" + chunks.pop("onglets")
    return {k: clean_chunk(v) for k, v in chunks.items()}


def build_guide(md: MarkdownIt) -> str:
    text = (BUILDS / GUIDE).read_text(encoding="utf-8")
    meta = guide_meta(text)
    chunks = split_guide(text)
    docs_list = "".join(f"- [{title}]({src}) — {desc}\n" for src, _, title, desc in AUDITS)
    docs_list += (f"- [Dépôt GitHub]({REPO_URL}) — sources Markdown du guide et des audits ; "
                  "ce site en est généré par `tools/build_site.py`.\n")
    chunks["annexes"] = re.sub(r"^## Annexes\n", lambda m: m.group(0) + "\n### Documents\n\n" + docs_list,
                               chunks["annexes"], count=1, flags=re.M)

    doc = Doc(page="index.html", version=meta["version"], used={p.id for p in PANELS} | {"main"})
    parsed = {p.id: parse(md, chunks[p.id], doc) for p in PANELS}  # all ids first: cross-references span tabs
    short_title = f"Protea Prime v{meta['version']}"
    sections = []
    for p in PANELS:
        body = render(md, parsed[p.id], doc, xrefs=p.id != "annexes")  # old journal entries use old numbers
        label = f"{circled(p.mark)} {p.label}".strip()
        toc = toc_html(parsed[p.id].heads, 3, label, meta["version"], f"toc-{p.id}")
        top = ""
        if p.id == "accueil":
            cards = "".join(
                f'<a class="card accent-{q.accent}" href="#{q.id}"><span class="card-num">{q.mark}</span>'
                f'<span class="card-title">{esc(q.label)}</span><span class="card-text">{esc(CARDS[q.id])}</span></a>'
                for q in PANELS if q.id in CARDS)
            top = (f'<header class="hero"><p class="hero-kicker">Guide de build · Warframe</p>'
                   f'<h1>{esc(meta["name"])}<span class="sub">{esc(meta["subtitle"])}</span></h1>'
                   f'<p class="hero-meta"><span class="chip chip-version">v{meta["version"]} · {meta["date"]}</span>'
                   f'<span class="chip">Hotfix {meta["hotfix"]}</span><span class="chip">Solo</span></p></header>'
                   f'<nav class="cards" aria-label="Configurations">{cards}</nav>')
        title = f"{meta['title']} · v{meta['version']}" if p.id == "accueil" else f"{label} · {short_title}"
        sections.append(
            f'<section class="panel accent-{p.accent}{" has-toc" if toc else ""}" id="{p.id}" '
            f'data-label="{esc(label)}" data-title="{esc(title)}" aria-label="{esc(label)}">'
            f'<div class="panel-inner">{toc}<article class="prose">{top}{body}</article></div></section>')

    footer = footer_html([
        f"<strong>{esc(meta['name'])} — guide v{meta['version']}</strong> du {meta['date']} · "
        f"patch de référence : {esc(meta['patch'])}.",
        'Valeurs vérifiées sur <a href="https://wiki.warframe.com/" target="_blank" rel="noopener">wiki.warframe.com</a> ; '
        "limites et points à tester : voir l'en‑tête de l'accueil.",
        f"Page générée depuis <code>builds/{GUIDE}</code> par <code>tools/build_site.py</code> · "
        f'<a href="{REPO_URL}" target="_blank" rel="noopener">dépôt GitHub</a>.',
    ])
    return page_html(
        title=f"{meta['title']} · v{meta['version']}",
        description=(f"Guide Protea Prime v{meta['version']} : socle commun, configuration Endurance et "
                     f"configuration Level Cap 9999, en solo (Hotfix {meta['hotfix']})."),
        body_class="page-guide",
        header=header_html("#accueil", meta["subtitle"], f"v{meta['version']}"),
        tabs=tabs_html("index.html"),
        main="\n".join(sections),
        footer=footer,
    )


def build_audit(md: MarkdownIt, src: str, page: str, title: str, desc: str, guide_version: str) -> str:
    text = (BUILDS / src).read_text(encoding="utf-8")
    h1 = re.search(r"^# (.+)$", text, re.M).group(1).strip()
    body_md = re.sub(r"^# .+\n", "", text, count=1)
    doc = Doc(page=page, used={"audit", "main"})
    chunk = parse(md, body_md, doc)
    body = render(md, chunk, doc, xrefs=False)
    toc = toc_html(chunk.heads, 2, title, "", "toc-audit")
    name, _, sub = h1.partition(" — ")
    top = (f'<header class="hero"><p class="hero-kicker"><a href="index.html#annexes">Annexes</a> › {esc(title)}</p>'
           f'<h1>{esc(name)}<span class="sub">{esc(sub)}</span></h1></header>')
    main = (f'<section class="panel accent-annex{" has-toc" if toc else ""}" id="audit" data-label="{esc(title)}">'
            f'<div class="panel-inner">{toc}<article class="prose">{top}{body}</article></div></section>')
    footer = footer_html([
        f"<strong>{esc(title)}</strong> · {esc(desc)}",
        f'Retour au <a href="index.html">guide v{guide_version}</a> · page générée depuis <code>builds/{src}</code> '
        f'par <code>tools/build_site.py</code>.',
    ])
    return page_html(title=f"{title} · Protea Prime", description=desc, body_class="page-audit",
                     header=header_html("index.html", title, title.replace("Audit hostile ", "Audit ")),
                     tabs=tabs_html(page, active="annexes"), main=main, footer=footer)


def build() -> dict[Path, str]:
    md = markdown()
    guide_version = guide_meta((BUILDS / GUIDE).read_text(encoding="utf-8"))["version"]
    out = {DOCS / "index.html": build_guide(md), DOCS / ".nojekyll": ""}
    for src, page, title, desc in AUDITS:
        out[DOCS / page] = build_audit(md, src, page, title, desc, guide_version)
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build docs/ (GitHub Pages) from builds/*.md.")
    parser.add_argument("--check", action="store_true", help="exit 1 if docs/ is out of date; write nothing")
    args = parser.parse_args(argv)
    stale = []
    for path, content in build().items():
        if path.exists() and path.read_text(encoding="utf-8") == content:
            continue
        stale.append(path.relative_to(ROOT))
        if not args.check:
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(content)
    if args.check and stale:
        print("docs/ is out of date, run python3 tools/build_site.py:", *stale, sep="\n  ", file=sys.stderr)
        return 1
    print("up to date" if not stale else "wrote " + ", ".join(map(str, stale)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
