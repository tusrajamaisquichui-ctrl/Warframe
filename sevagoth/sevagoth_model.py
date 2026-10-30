#!/usr/bin/env python3
"""
Sevagoth Prime - modele de theorycraft v5 (patch 44.1.4.1, PS5, 30/10/2026).

Tout est calcule ici ; le document (sevagoth_prime_theorycraft.md) ne fait que recopier les sorties.
    python3 sevagoth_model.py                 # rapport complet
    python3 sevagoth_model.py --section nuke  # une section
    python3 sevagoth_model.py --params        # parametres + sources

Etiquettes : CONF = wiki officiel / patch notes, COMM = communaute, DED = deduit (ce modele),
TEST = hypothese a mesurer en jeu (voir tests T1..T14 du document).
v2 : sections M11 a M18 ; v3 : M19 a M23 (portee 100/190/max, Eximus Entropiques, Gloom et Archon Stretch, seuil, Arcane Circumvent) ;
v4 : M24 a M28 (portee 175/190 optimisee, Seismic Bond reel, boucle de RubyBlossom5, Viral, Entropiques apres U44) ;
v5 : M29 a M31 (calculateur de RubyBlossom5, sa build principale, eclats Emeraude en config Tempest).
Forces exprimees en multiplicateurs (2,43 = 243 %).
"""
import argparse
import itertools
import math
import random

W = "wiki.warframe.com"
# ---------------------------------------------------------------------------
# 0. PARAMETRES : (valeur, source, etiquette)
# ---------------------------------------------------------------------------
P = {
    # Sevagoth Prime / Ombre Prime (Module:Warframes/data ; rang 30 apres U34)
    "seva_health": (370, W + " Sevagoth/Prime : 270 base -> 370 rang 30", "CONF"),
    "seva_shield": (370, W + " Sevagoth/Prime : 270/370", "CONF"),
    "seva_armor": (185, W + " Sevagoth/Prime", "CONF"),
    "seva_energy": (225, W + " Sevagoth/Prime : 175/225", "CONF"),
    "sh_health": (370, W + " Sevagoth Prime's Shadow : 270/370", "CONF"),
    "sh_shield": (185, W + " Shadow : 135/185", "CONF"),
    "sh_armor": (475, W + " Shadow : 475 (corrige 40.0.3)", "CONF"),
    "sh_energy": (150, W + " Shadow : 100/150", "CONF"),
    # Competences, rang max
    "reap_cost": (25, W + " Reap", "CONF"),
    "reap_vuln": (0.50, W + " Reap : vulnerabilite 50 % x Force, posee APRES le True du meme coup", "CONF"),
    "sow_cost": (50, W + " Sow", "CONF"),
    "sow_dps": (250, W + " Sow : 250 True/s x Force, falloff jusqu'a 25 %", "CONF"),
    "detonate_pct": (0.25, W + " Reap sur cible Sow : 25 % PV actuels en True puis 25 % en Blast 4 m", "CONF"),
    "gloom_cost": (50, W + " Gloom", "CONF"),
    "gloom_drain": (0.75, W + " Gloom : 0,75 energie/s par ennemi, plafond 10", "CONF"),
    "gloom_slow": (0.35, W + " Gloom : ralentissement 35 % x Force, plafond 95 % a 272 %", "CONF"),
    "gloom_ls": (0.05, W + " Gloom : vol de vie 5 % x Force", "CONF"),
    "well_drain": (1.0, W + " Exalted Shadow : 1 %/s, cast si >= 75 %", "CONF"),
    "well_gloom": (0.1, W + " Gloom : 0,1 %/s par ennemi vivant", "CONF"),
    "sh_invuln": (5.0, W + " Exalted Shadow : 5 s invulnerable a chaque invocation", "CONF"),
    "claws_base": (250, W + " Shadow Claws Prime : 250 x Force de Sevagoth (I30/P20/S50)", "CONF"),
    "claws_heavy": (1000, W + " Module:Weapons/data HeavyAttack 1000", "CONF"),
    "claws_cc": (0.38, W + " Shadow Claws", "CONF"),
    "claws_cd": (2.6, W + " Shadow Claws", "CONF"),
    "claws_sc": (0.24, W + " Shadow Claws", "CONF"),
    "dh_cost": (75, W + " Death's Harvest", "CONF"),
    "dh_vuln": (0.50, W + " Death's Harvest : 50 % x Force de l'Ombre", "CONF"),
    "haze_cc": (0.50, W + " Shadow Haze : +50 % CC x Force de Sevagoth, additif apres mods", "CONF"),
    "roar_helminth": (0.30, W + " Roar Helminth : 30 % x Force, bonus de faction", "CONF"),
    "roar_dur": (30.0, W + " Roar : 30 s x Duree", "CONF"),
    "roar_cost": (75, W + " Roar", "CONF"),
    # Stance Ravenous Wraith (Module:Stances/data) : combo Block 'Reaping Cyclone'
    "stance_block_pct": (20.0, W + " Ravenous Wraith Block : 2000 % sur 12 coups", "CONF"),
    "stance_block_hits": (12, W + " idem", "CONF"),
    "stance_block_time": (2.4, W + " idem, 2,4 s a vitesse 1,0", "CONF"),
    # Ennemis
    "sp_health_mult": (2.5, W + " The Steel Path : PV et boucliers x2,5 ; armure inchangee", "CONF"),
    "hg_base_level": (8, W + " Module:Enemies/data/grineer Heavy Gunner", "CONF"),
    "hg_health": (300, W + " Heavy Gunner", "CONF"),
    "hg_armor": (500, W + " Heavy Gunner", "CONF"),
    "hg_shot": (8, W + " Heavy Gunner : 8 degats/balle", "CONF"),
    "og_base": (12, W + " Overguard : base 12 (tous Eximus)", "CONF"),
    # Joueur
    "catalyzing_mult": (0.20, W + " Catalyzing Shields : x0,2, gate 1,33 s", "CONF"),
    "gate_time": (1.33, W + " Shield gating", "CONF"),
    # Epitaph Prime (Module:Weapons/data/secondary, tir charge)
    "epi_base": (315.0, W + " Epitaph Prime charge : 126 I / 47,25 P / 141,75 S", "CONF"),
    "epi_cc": (0.50, W + " Epitaph Prime charge", "CONF"),
    "epi_cd": (3.0, W + " Epitaph Prime charge", "CONF"),
    "epi_rate": (1.2, "Hypothese : tirs charges/s (charge 0,36 s + cadence 1,75)", "TEST"),
    "fortifier": (8.0, W + " Secondary Fortifier : x8 contre l'Overguard", "CONF"),
    # Energie
    "orb_energy": (25, W + " Pickups : petit orbe 25", "CONF"),
    "orb_drop": (0.094, W + " Pickups : 9,43 % sur 159 kills (echantillon cite)", "COMM"),
    "energize": (150, W + " Arcane Energize : 60 % -> 150, recharge 15 s", "CONF"),
    # Hypotheses non trouvees
    "cast_time": (0.9, "NON TROUVE : animation moyenne d'un sort (s) avant vitesse de lancer", "TEST"),
    "travel_time": (4.0, "Hypothese : deplacement/visee entre deux packs (s)", "TEST"),
    "pack_size": (15, "Hypothese : ennemis tues par rotation Sow + 2 Reap en Steel Path dense", "TEST"),
    "hits_per_s": (2.0, "Hypothese : coups recus/s par tireur actif a pleine vitesse", "TEST"),
}


def v(k):
    return P[k][0]


# ---------------------------------------------------------------------------
# 1. MODS : (drain de base, rang max, polarite, effets)  Module:Mods/data
# ---------------------------------------------------------------------------
MODS = {
    "Brief Respite": (-2, 5, "Z", {}), "Steel Charge": (-4, 5, "M", {}),
    "Power Drift": (4, 5, "Z", {"str": 0.15}), "Shadow Haze": (6, 3, "Z", {}),
    "Dark Propagation": (6, 3, "Z", {}),
    "Umbral Intensify": (6, 10, "U", {"str": 0.44, "umbral": 1}),
    "Umbral Fiber": (6, 10, "U", {"armor_pct": 1.00, "umbral": 1}),
    "Umbral Vitality": (6, 10, "U", {"health_pct": 1.00, "umbral": 1}),
    "Transient Fortitude": (6, 10, "M", {"str": 0.55, "dur": -0.275}),
    "Precision Intensify": (6, 5, "M", {"str4": 0.90}), "Intensify": (6, 5, "M", {"str": 0.30}),
    "Augur Secrets": (2, 5, "N", {"str": 0.24}), "Catalyzing Shields": (10, 3, "V", {"catalyzing": 1}),
    "Rolling Guard": (2, 10, "V", {}), "Stretch": (4, 5, "N", {"rng": 0.45}),
    "Primed Continuity": (4, 10, "M", {"dur": 0.55}), "Streamline": (4, 5, "N", {"eff": 0.30}),
    "Adaptation": (2, 10, "V", {}), "Preparation": (2, 10, "Z", {}),
    "Primed Flow": (4, 10, "N", {"energy_pct": 1.85}), "Undying Will": (2, 5, "V", {}),
    "Vitality": (2, 10, "V", {"health_pct": 1.00}), "Steel Fiber": (4, 10, "V", {"armor_pct": 1.00}),
    "Fleeting Expertise": (6, 5, "N", {"eff": 0.60, "dur": -0.60}),
    "Cunning Drift": (4, 5, "M", {"rng": 0.15}), "Augur Reach": (2, 5, "N", {"rng": 0.30}),
    "Continuity": (2, 5, "M", {"dur": 0.30}),
    "Overextended": (6, 5, "V", {"rng": 0.90, "str": -0.60}),
    "Overextended R4": (6, 4, "V", {"rng": 0.75, "str": -0.50}),
    "Archon Stretch": (6, 10, "N", {"rng": 0.45}),
    # Melee
    "Primed Pressure Point": (4, 10, "M", {}), "Condition Overload": (10, 5, "M", {}),
    "Blood Rush": (4, 10, "M", {}), "Organ Shatter": (4, 5, "M", {}), "Primed Reach": (4, 10, "M", {}),
    "Weeping Wounds": (4, 5, "M", {}), "Primed Fever Strike": (6, 10, "N", {}), "North Wind": (6, 5, "V", {}),
    "Discipline's Merit": (4, 3, "N", {}), "Life Strike": (4, 3, "V", {}), "Corrupt Charge": (4, 3, "M", {}),
}
UMBRAL_SET = {2: (0.25, 0.30), 3: (0.75, 0.80)}  # Umbral_Set : (Intensify, Fiber/Vitality)


def cost(m):
    b, r, pol, _ = MODS[m]
    return b + r, pol


def slot_cost(c, mpol, spol):
    """Polarity : assortie -> /2 arrondi au-dessus ; differente -> x1,25 arrondi au-dessus."""
    if spol is None:
        return c
    return math.ceil(c / 2) if spol == mpol else math.ceil(c * 1.25)


def aura_bonus(m, spol):
    b, r, pol, _ = MODS[m]
    bonus = abs(b) + r
    if spol in (pol, "ANY"):
        return bonus * 2
    if spol is None:
        return bonus
    return math.floor(bonus * 0.8)


def fit(cfg):
    """Forma minimales (glouton) pour que la config rentre ; l'Aura Forma passe en premier
    car elle rapporte le plus de capacite par Forma."""
    forma, cap = 0, cfg["capacity"]
    aura_pol = None
    if cfg.get("aura"):
        m, innate_aura = cfg["aura"]
        aura_pol = innate_aura
    slots, innate, rest = [], list(cfg["innate"]), []
    for m in sorted(cfg["mods"], key=lambda x: -cost(x)[0]):
        c, pol = cost(m)
        if pol in innate:
            innate.remove(pol)
            slots.append([m, pol])
        else:
            rest.append(m)
    for m in rest:
        slots.append([m, innate.pop(0) if innate else None])
    ex = [cfg["exilus"], None] if cfg.get("exilus") else None

    def capacity():
        return cap + (aura_bonus(cfg["aura"][0], aura_pol) if cfg.get("aura") else 0)

    def total():
        t = sum(slot_cost(cost(m)[0], cost(m)[1], sp) for m, sp in slots)
        if ex:
            t += slot_cost(cost(ex[0])[0], cost(ex[0])[1], ex[1])
        return t

    if cfg.get("aura") and total() > capacity() and aura_pol not in (MODS[cfg["aura"][0]][2], "ANY"):
        aura_pol, forma = "ANY", forma + 1
    while total() > capacity():
        best, gain = None, 0
        for s in slots + ([ex] if ex else []):
            c, pol = cost(s[0])
            if s[1] == pol:
                continue
            g = slot_cost(c, pol, s[1]) - math.ceil(c / 2)
            if g > gain:
                best, gain = s, g
        if not best:
            break
        best[1] = cost(best[0])[1]
        forma += 1
    return {"total": total(), "cap": capacity(), "forma": forma, "slots": slots, "exilus": ex,
            "aura": (cfg["aura"][0], aura_pol, aura_bonus(cfg["aura"][0], aura_pol)) if cfg.get("aura") else None,
            "fits": total() <= capacity()}


def stats(cfg, shards=0.0, molt=0.0, sling=0.0, extra_str=0.0, extra_eff=0.0):
    s = {"str": 1.0, "dur": 1.0, "rng": 1.0, "eff": 1.0, "str4": 0.0, "health_pct": 0.0,
         "armor_pct": 0.0, "energy_pct": 0.0, "umbral": 0, "catalyzing": 0}
    allm = list(cfg["mods"]) + ([cfg["exilus"]] if cfg.get("exilus") else [])
    for m in allm:
        for k, val in MODS[m][3].items():
            s[k] = s.get(k, 0) + val
    if s["umbral"] >= 2:
        bi, bf = UMBRAL_SET[min(s["umbral"], 3)]
        s["str"] += 0.44 * bi if "Umbral Intensify" in allm else 0
        s["armor_pct"] += bf if "Umbral Fiber" in allm else 0
        s["health_pct"] += bf if "Umbral Vitality" in allm else 0
    s["str"] += shards + molt + sling + extra_str
    s["eff"] += extra_eff
    return s


# ---------------------------------------------------------------------------
# 2. BUILDS FINALISTES
# ---------------------------------------------------------------------------
SEVA_INNATE, SHADOW_INNATE, CLAWS_INNATE = ["V", "N", "M"], ["V", "N", "M", "M"], ["M", "M", "M"]
SHARDS = 0.60       # 4 Crimson tauforges +15 % Force (Archon_Shard) ; s'appliquent aussi a l'Ombre (wiki passif)
MOLT = 0.60         # Molt Augmented max (250 kills)
SLING = 0.40        # Madurai Sling Strength (20 s)
CREPUSCULAR = 0.30  # Arcane Crepuscular : +30 % Force si invisible (option)

TOMB_SHADOW = {"capacity": 60, "innate": SHADOW_INNATE, "aura": ("Steel Charge", "M"), "exilus": None,
               "mods": ["Umbral Vitality", "Umbral Fiber", "Umbral Intensify", "Adaptation", "Rolling Guard",
                        "Vitality", "Steel Fiber", "Intensify"]}
TOMB_CLAWS = {"capacity": 70, "innate": CLAWS_INNATE, "aura": None, "exilus": "Discipline's Merit",
              "mods": ["Primed Pressure Point", "Condition Overload", "Blood Rush", "Organ Shatter", "Primed Reach",
                       "Life Strike", "Primed Fever Strike", "North Wind"]}
SHADOW_F2 = {"capacity": 60, "innate": SHADOW_INNATE, "aura": ("Brief Respite", "M"), "exilus": "Power Drift",
             "mods": ["Preparation", "Transient Fortitude", "Umbral Intensify", "Umbral Fiber", "Intensify",
                      "Catalyzing Shields", "Adaptation", "Rolling Guard"]}
CLAWS_F2 = {"capacity": 70, "innate": CLAWS_INNATE, "aura": None, "exilus": "Discipline's Merit",
            "mods": ["Primed Pressure Point", "Condition Overload", "Blood Rush", "Organ Shatter", "Primed Reach",
                     "Weeping Wounds", "Primed Fever Strike", "North Wind"]}

BUILDS = {
    "F1": dict(label="F1 Faucheuse invisible (Reap/Sow/Gloom/Roar en 4, Huras Kubrow)",
               seva={"capacity": 60, "innate": SEVA_INNATE, "aura": ("Brief Respite", None), "exilus": "Power Drift",
                     "mods": ["Shadow Haze", "Dark Propagation", "Umbral Intensify", "Augur Secrets",
                              "Intensify", "Catalyzing Shields", "Primed Continuity", "Streamline"]},
               shadow=TOMB_SHADOW, claws=TOMB_CLAWS, roar_slot=4, gloom=True, exalted=False, viral=False,
               shade=True, seismic=True),  # Huras Kubrow : Stalk (invisibilite) + Seismic Bond (bete)
    "F2": dict(label="F2 Ombre Faucheuse (Reap/Sow/Roar en 3/Exalted Shadow)",
               seva={"capacity": 60, "innate": SEVA_INNATE, "aura": ("Brief Respite", None), "exilus": "Power Drift",
                     "mods": ["Shadow Haze", "Dark Propagation", "Umbral Intensify", "Augur Secrets", "Intensify",
                              "Catalyzing Shields", "Primed Continuity", "Streamline"]},
               shadow=SHADOW_F2, claws=CLAWS_F2, roar_slot=3, gloom=False, exalted=True, viral=False,
               shade=False, seismic=False),
    "F3": dict(label="F3 Sans Helminth (Reap/Sow/Gloom/Exalted Shadow)",
               seva={"capacity": 60, "innate": SEVA_INNATE, "aura": ("Brief Respite", None), "exilus": "Power Drift",
                     "mods": ["Shadow Haze", "Dark Propagation", "Umbral Intensify", "Augur Secrets",
                              "Precision Intensify", "Catalyzing Shields", "Primed Continuity", "Streamline"]},
               shadow=SHADOW_F2, claws=CLAWS_F2, roar_slot=None, gloom=True, exalted=True, viral=True,
               shade=False, seismic=True),
}


def strengths(key, shards=SHARDS, molt=0.0, sling=0.0, crep=0.0):
    b = BUILDS[key]
    st = stats(b["seva"], shards, molt, sling, extra_str=crep)
    S = st["str"]
    S4 = S + st["str4"]
    roar_S = S4 if b["roar_slot"] == 4 else (S if b["roar_slot"] == 3 else None)
    S_sh = stats(b["shadow"], shards)["str"]
    return dict(S=S, S4=S4, roar_S=roar_S, S_sh=S_sh, st=st)


# ---------------------------------------------------------------------------
# 3. SCALING ENNEMI (Enemy_Level_Scaling : courbes a deux bouts + smoothstep)
# ---------------------------------------------------------------------------
def smooth(q, lo, hi):
    t = min(max((q - lo) / (hi - lo), 0.0), 1.0)
    return t * t * (3 - 2 * t)


def two_curve(q, c1, e1, c2, e2, lo, hi):
    q = max(q, 0.0)
    f1, f2 = 1 + c1 * q ** e1, 1 + c2 * q ** e2
    return f1 + (f2 - f1) * smooth(q, lo, hi)


def heavy_gunner(level, eximus=False, sp=True):
    q = level - v("hg_base_level")
    base = v("hg_health")
    if eximus:  # Eximus avec armure : bonus de PV de base (x6 au-dela du niveau 100)
        k = 0.25 * (base + 900)
        f = 6 if level > 100 else 4.5 + 0.03 * (level - 50)
        base = max(base * 1.1, k * f)
    h = base * two_curve(q, 0.015, 2.12, 10.7332, 0.72, 70, 80) * (v("sp_health_mult") if sp else 1)
    a = min(max(v("hg_armor") * two_curve(q, 0.005, 1.75, 0.4, 0.75, 70, 80), 200), 2700)
    og = v("og_base") * two_curve(level - 1, 0.0015, 4, 260, 0.9, 45, 50) if eximus else 0.0
    dmg = two_curve(q, 0.015, 1.75, 0.0075, 1.55, 1, 25)
    return dict(health=h, armor=a, og=og, dmg_mult=dmg)


def armor_dr(a):
    return 0.9 * math.sqrt(min(a, 2700) / 2700)


LEVELS = {"S1 SP175": 175, "S2a 500": 500, "S2b 1000": 1000, "S3 9999": 9999}


# ---------------------------------------------------------------------------
# 4. NUKE : fraction des PV actuels par detonation Reap+Sow
# ---------------------------------------------------------------------------
def viral_mult(n):
    return 1.0 if n <= 0 else 2 + 0.25 * (min(n, 10) - 1)


def roar_mult(S):
    return 1 + v("roar_helminth") * S if S else 1.0


def frac(vuln, roar=1.0, viral=0):
    return v("detonate_pct") * (1 + vuln) * roar * viral_mult(viral)


def threshold_roar4():
    lo, hi = 1.0, 4.0
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if frac(0.5 * mid, roar_mult(mid + 0.9)) >= 1 else (mid, hi)
    return hi


def nuke_report():
    o = ["## M3. Nuke Reap+Sow (fraction des PV actuels retiree ; >= 1,00 = mort, hors Overguard)"]
    o.append(f"Controle des seuils CONF du wiki : S=2,00 + 1 Viral -> {frac(1.0, viral=1):.3f} ; "
             f"S=2,55 + Roar -> {frac(1.275, roar_mult(2.55)):.3f}")
    o.append(f"DED : Roar en slot 4 + Precision Intensify -> seuil ramene a {threshold_roar4()*100:.1f} % de Force")
    o.append("")
    o.append("| Build | etat | Force | Roar | vuln Reap | 1er Reap (sans vuln) | 2e Reap | Gloom slow |")
    o.append("|---|---|---|---|---|---|---|---|")
    for key, b in BUILDS.items():
        for etat, molt, sling, crep in (("debut", 0, 0, 0), ("+Molt", MOLT, 0, 0), ("+Molt+Sling", MOLT, SLING, 0)):
            s = strengths(key, molt=molt, sling=sling, crep=crep)
            r = roar_mult(s["roar_S"])
            vi = 1 if b["viral"] else 0
            slow = min(v("gloom_slow") * s["S"], 0.95) if b["gloom"] else 0
            o.append(f"| {key} | {etat} | {s['S']*100:.0f} % | x{r:.2f} | +{50*s['S']:.0f} % | "
                     f"{frac(0, r, vi):.2f} | {frac(0.5*s['S'], r, vi):.2f} | {slow*100:.0f} % |")
    o.append("(F3 suppose 1 stack Viral pose avant : sans amorce, 2e Reap = "
             f"{frac(0.5*strengths('F3')['S']):.2f})")
    o.append("")
    for key in ("F2", "F3"):
        s = strengths(key)
        r = roar_mult(s["roar_S"])
        f = frac(v("dh_vuln") * s["S_sh"], r, 1 if BUILDS[key]["viral"] else 0)
        o.append(f"Ombre {key} : Force Ombre {s['S_sh']*100:.0f} % -> DH +{50*s['S_sh']:.0f} %, Roar x{r:.2f} -> "
                 f"detonation par mini-Reap sur cible deja sous DH = {f:.2f}")
    return "\n".join(o)


# ---------------------------------------------------------------------------
# 5. EXIMUS : PV / armure / Overguard et facon de le tuer
# ---------------------------------------------------------------------------
def detonations_to_kill(level, f_health, f_og):
    t = heavy_gunner(level, eximus=True)
    h, og, n = t["health"], t["og"], 0
    while n < 12:
        n += 1
        d = f_og * h
        if og > 0:
            if d < og:
                og -= d
                continue
            h -= (d - og) / f_og * f_health
            og = 0
        else:
            h -= f_health * h
        if h <= 0:
            return n
    return 99


def epitaph_shot_vs_og(S_seva, roar):
    """Epitaph Prime charge (Hornet Strike +220 %, Barrel Diffusion +120 % MS, Primed Pistol Gambit +187 % CC,
    Primed Target Cracker +110 % CD, 2 elements 165+90 %) + Shadow Haze + Roar + Secondary Fortifier x8.
    L'OG est neutre : pas d'armure, pas de faction, pas de Viral."""
    base = v("epi_base")
    dmg = 1 + 2.2
    ms = 1 + 1.2
    elem = 1 + 1.65 + 0.90
    cc = v("epi_cc") * (1 + 1.87) + v("haze_cc") * S_seva
    cd = v("epi_cd") * (1 + 1.10)
    crit = 1 + cc * (cd - 1)
    return base * dmg * ms * elem * crit * roar * v("fortifier")


def eximus_report():
    o = ["## M4. Heavy Gunner Eximus (Steel Path) : PV, armure, Overguard"]
    o.append("| Niveau | PV Heavy Gunner | PV Eximus | Armure | Overguard | OG/PV |")
    o.append("|---|---|---|---|---|---|")
    for n, L in LEVELS.items():
        a, e = heavy_gunner(L), heavy_gunner(L, True)
        o.append(f"| {n} | {a['health']:,.0f} | {e['health']:,.0f} | {e['armor']:.0f} | {e['og']:,.0f} | {e['og']/e['health']:.2f} |")
    o.append("")
    o.append("Detonations Reap+Sow pour tuer l'Eximus (T1) : H1a = le True traverse l'OG avec vuln+Roar, "
             "H1b = OG ne prend que Roar, H0 = OG bloque (il faut l'enlever autrement)")
    o.append("| Build | Niveau | H1a | H1b | H0 : tirs Epitaph+Fortifier pour l'OG |")
    o.append("|---|---|---|---|---|")
    for key in ("F1", "F2"):
        s = strengths(key)
        r = roar_mult(s["roar_S"])
        fh = frac(0.5 * s["S"], r)
        for n, L in LEVELS.items():
            og = heavy_gunner(L, True)["og"]
            shots = math.ceil(og / epitaph_shot_vs_og(s["S"], r))
            o.append(f"| {key} | {n} | {detonations_to_kill(L, fh, fh)} | "
                     f"{detonations_to_kill(L, fh, v('detonate_pct')*r)} | {shots} |")
    return "\n".join(o)


# ---------------------------------------------------------------------------
# 6. SHADOW CLAWS PRIME
# ---------------------------------------------------------------------------
def claws_hit(S4, S_seva, S_sh, combo, t, full=True, heavy=False, vuln_og=True, exposure=4, fury=0.0):
    """Pipeline : base (x Force Seva sur la 4e) -> Phoenix Talons (+30 % physique) -> degats additifs
    (Primed Pressure Point, Condition Overload, Arcane Fury) -> elements (Viral 255 %, Corrosif Melee Exposure)
    -> crit (Blood Rush, Shadow Haze, Organ Shatter) -> combo (lourde) -> vuln DH -> faction -> armure -> Viral."""
    base = (v("claws_heavy") if heavy else v("claws_base")) * S4
    phys = base * 1.3
    lvl = 1.0 if full is True else (0.0 if full is False else float(full))   # 1 = statuts empiles, 0 = cible fraiche
    dmg = 1 + 1.65 + 0.80 * (1 + round(4 * lvl)) + fury
    parts = {"I": phys * .3, "P": phys * .2, "S": phys * .5, "V": base * 2.55, "C": base * 0.60 * exposure}
    parts = {k: x * dmg for k, x in parts.items()}
    cc = v("claws_cc") * (1 + 0.40 * max(combo - 1, 0)) + v("haze_cc") * S_seva
    cd = v("claws_cd") * 1.9
    crit = 1 + cc * (cd - 1)
    cm = combo if heavy else 1.0
    vuln = 1 + v("dh_vuln") * S_sh
    raw = sum(parts.values()) * crit * cm
    og = raw * (vuln if vuln_og else 1)
    fac = {"I": 1.5, "P": 1, "S": 1, "V": 1, "C": 1.5}  # Grineer : Impact et Corrosif +50 % (Damage 3.0)
    n = round(10 * lvl)
    arm = t["armor"] * (1 - (0.2 + 0.06 * n if n else 0))  # Corrosif : 26 % puis +6 %/stack, 80 % a 10
    vir = viral_mult(n)
    hp = sum(parts[k] * fac[k] for k in parts) * crit * cm * vuln * (1 - armor_dr(arm)) * vir
    sc = v("claws_sc") * (1 + 0.40 * max(combo - 1, 0))   # Weeping Wounds
    bleed = sc * parts["S"] / sum(parts.values()) * 0.35 * 6 * phys * dmg * crit * cm * vuln * vir
    return og, hp + bleed


FURY = 1.80  # Arcane Fury sur l'Ombre : +180 % degats de melee (CONF : s'applique aux griffes) ; CC > 100 % -> quasi permanent


def claws_ttk(L, S4, S_seva, S_sh, combo, mode="light", **kw):
    kw.setdefault("fury", FURY)
    t = heavy_gunner(L, True)
    per_s = v("stance_block_pct") / v("stance_block_time")
    hits_s = v("stance_block_hits") / v("stance_block_time")
    og_l, hp_l = claws_hit(S4, S_seva, S_sh, combo, t, **kw)
    dog, dhp = og_l * per_s, hp_l * per_s
    if mode == "tennokai":  # Discipline's Merit : opportunite tous les 4 coups, lourde sans consommer le combo
        og_h, hp_h = claws_hit(S4, S_seva, S_sh, combo, t, heavy=True, **kw)
        cyc = 4 / hits_s + 0.9
        lf = (4 / hits_s) / cyc
        dog, dhp = dog * lf + og_h / cyc, dhp * lf + hp_h / cyc
    return t["og"] / dog + t["health"] / dhp, t["og"] / dog, t["health"] / dhp


def claws_report():
    o = ["## M5. Shadow Claws Prime : TTK Heavy Gunner Eximus (OG + sante), cible seule"]
    for key in ("F2", "F3"):
        s = strengths(key)
        o.append(f"{key} debut : base griffes {v('claws_base')*s['S4']:.0f} (Force 4e {s['S4']*100:.0f} %), "
                 f"CC Shadow Haze +{50*s['S']:.0f} %, vuln DH +{50*s['S_sh']:.0f} %")
    o.append("| Build | Niveau | 4x leger | 4x Tennokai | 12x Tennokai | typique (statuts a moitie, 4x Tennokai) | plancher (cible fraiche, 4x, pas de vuln sur OG) |")
    o.append("|---|---|---|---|---|---|---|")
    for key in ("F2", "F3"):
        s = strengths(key)
        for n, L in LEVELS.items():
            a = claws_ttk(L, s["S4"], s["S"], s["S_sh"], 4)[0]
            b = claws_ttk(L, s["S4"], s["S"], s["S_sh"], 4, "tennokai")[0]
            c = claws_ttk(L, s["S4"], s["S"], s["S_sh"], 12, "tennokai")[0]
            d = claws_ttk(L, s["S4"], s["S"], s["S_sh"], 4, "tennokai", full=False, vuln_og=False)[0]
            e = claws_ttk(L, s["S4"], s["S"], s["S_sh"], 4, "tennokai", full=0.5)[0]
            o.append(f"| {key} | {n} | {a:,.2f} s | {b:,.2f} s | {c:,.2f} s | {e:,.2f} s | {d:,.1f} s |")
    s = strengths("F2")
    cc12 = v("claws_cc") * (1 + 0.4 * 11) + v("haze_cc") * s["S"]
    o.append(f"CC a 12x avec Shadow Haze : {cc12*100:.0f} % -> tiers rouges ; Melee Duplicate (crits jaunes) est inutile ici.")
    return "\n".join(o)


# ---------------------------------------------------------------------------
# 7. SURVIE
# ---------------------------------------------------------------------------
def ehp(health, shield, armor, st, catalyzing):
    hp = health * (1 + st["health_pct"])
    sh = shield * (v("catalyzing_mult") if catalyzing else 1)
    ar = armor * (1 + st["armor_pct"])
    dr = ar / (ar + 300)
    return hp / (1 - dr) + sh, dr


def coverage(key):
    """Part du temps ou le tir DIRECT peut toucher. DED (hypotheses TEST) :
    - F1 + Shade (Ghost, CONF) : invisible tant qu'un ennemi est a 24 m et qu'on ne tire pas ; on ne tire
      jamais en S2/S3 -> 5 % residuel (deplacements hors portee, cooldown 7 s apres une rupture).
    - F2/F3 : corps intouchable quand l'Ombre est sortie ; cycle Seva 3 lancers (~3 s) + Ombre 5 s
      (invulnerable) + 2 animations (~1,8 s) ; sur la part exposee, gate Catalyzing ~60 % et Rolling Guard 30 %.
    - F1 sans Shade : gate ~60 %, pas de Rolling Guard."""
    gate, rg = 0.60, 0.30
    if key == "F1":
        return 0.05
    seva, sh, anim = 3.0, 5.0, 1.8
    exposed = (seva + anim) / (seva + sh + anim)
    return exposed * (1 - gate) * (1 - rg)


def survival_report():
    o = ["## M6. Survie"]
    stb = stats(BUILDS["F1"]["seva"], SHARDS)
    sts = stats(SHADOW_F2, SHARDS)
    stt = stats(TOMB_SHADOW, SHARDS)
    eb, drb = ehp(v("seva_health"), v("seva_shield"), v("seva_armor"), stb, True)
    es, drs = ehp(v("sh_health"), v("sh_shield"), v("sh_armor"), sts, True)
    et, drt = ehp(v("sh_health"), v("sh_shield"), v("sh_armor"), stt, True)
    o.append(f"EHP corps Sevagoth : {eb:,.0f} (DR armure {drb*100:.1f} %) ; Ombre F2 : {es:,.0f} (DR {drs*100:.1f} %) ; "
             f"Ombre Tombstone F1 : {et:,.0f} (DR {drt*100:.1f} %)")
    o.append("| Niveau | degats/balle Heavy Gunner | balles -> corps | balles -> Ombre F2 | balles -> Ombre Tombstone |")
    o.append("|---|---|---|---|---|")
    for n, L in LEVELS.items():
        d = v("hg_shot") * heavy_gunner(L)["dmg_mult"]
        o.append(f"| {n} | {d:,.0f} | {eb/d:.2f} | {es/d:.2f} | {et/d:.2f} |")
    o.append("")
    o.append("Indice de risque tir direct (DED) = (tireurs trash x (1-slow) + Eximus) x coups/s x part touchable x 60")
    o.append("| Build | Niveau | slow trash | part touchable | indice (coups/min) | relatif F1 |")
    o.append("|---|---|---|---|---|---|")
    scen = {175: (4, 0.5), 500: (5, 1.0), 1000: (5, 1.5), 9999: (5, 2.0)}  # trash vivants en LoS, Eximus vivants (TEST)
    for n, L in LEVELS.items():
        base = None
        for key, b in BUILDS.items():
            s = strengths(key, molt=MOLT)
            slow = min(v("gloom_slow") * s["S"], 0.95) if b["gloom"] else 0
            ntr, nex = scen[L]
            idx = (ntr * (1 - slow) + nex) * v("hits_per_s") * coverage(key) * 60
            base = idx if key == "F1" else base
            o.append(f"| {key} | {n} | {slow*100:.0f} % | {coverage(key):.2f} | {idx:.1f} | x{idx/base:.1f} |")
    return "\n".join(o)


# ---------------------------------------------------------------------------
# 8. ENERGIE (corps de Sevagoth)
# ---------------------------------------------------------------------------
def energize_rate(orbs_s):
    return 0.0 if orbs_s <= 0 else 1.0 / (15 + 1.0 / (0.6 * orbs_s))


def energy_flow(key, kpm, orb_eff=0.0, seva_share=1.0):
    b = BUILDS[key]
    st = stats(b["seva"], SHARDS)
    eff = st["eff"] + (0.30 if b["seismic"] else 0)       # Seismic Bond (bete) pendant Gloom
    cm = max(2 - eff, 0.25)
    packs = kpm / 60 / v("pack_size") * seva_share
    cost = packs * (v("sow_cost") + 2 * v("reap_cost")) * cm
    if b["roar_slot"]:
        cost += v("roar_cost") * cm / (v("roar_dur") * st["dur"])
    if b["gloom"]:
        cost += v("gloom_drain") * 10 * max(cm / st["dur"], 0.25)
    orbs = kpm / 60 * v("orb_drop") * seva_share           # en Ombre, les orbes vont a l'Ombre
    inc = orbs * v("orb_energy") * (1 + orb_eff) + energize_rate(orbs) * v("energize")
    return cost, inc


def energy_report():
    o = ["## M7. Energie nette du corps (energie/s)"]
    o.append("Couts : Sow + 2 Reap par pack de 15 kills, Roar recast a expiration, Gloom au plafond (10 ennemis).")
    o.append("Revenus : orbes 9,4 %/kill x 25 (option eclat Amber tauforge +75 %), Arcane Energize. F2 : 50 % des kills en Ombre.")
    o.append("| Build | kills/min | cout | revenu | net | net avec Amber orbe |")
    o.append("|---|---|---|---|---|---|")
    for key in BUILDS:
        share = 0.5 if key == "F2" else 1.0
        for kpm in (30, 60, 90, 120):
            c, i = energy_flow(key, kpm, 0, share)
            c2, i2 = energy_flow(key, kpm, 0.75, share)
            o.append(f"| {key} | {kpm} | {c:.2f} | {i:.2f} | {i-c:+.2f} | {i2-c2:+.2f} |")
    o.append("")
    for key in BUILDS:
        share = 0.5 if key == "F2" else 1.0
        st = stats(BUILDS[key]["seva"], SHARDS)
        for orb_eff, lab in ((0, "sans"), (0.75, "avec")):
            k = next((k for k in range(5, 601) if (lambda ci: ci[1] >= ci[0])(energy_flow(key, k, orb_eff, share))), None)
            o.append(f"Seuil {key} ({lab} Amber orbe, eff {st['eff']*100:.0f} %, duree {st['dur']*100:.0f} %) : "
                     f"{'~%d kills/min' % k if k else '> 600 kills/min'}")
    return "\n".join(o)


# ---------------------------------------------------------------------------
# 9. DEATH WELL
# ---------------------------------------------------------------------------
def uptime(kps, nuke_share=0.8, overhead=1.8, seva_min=3.0, D=25.0):
    f = kps * (nuke_share * 10 + (1 - nuke_share) * 5)
    if f <= 0:
        return 0.0
    t_sh = D / v("well_drain")
    return t_sh / (t_sh + max(D / f, seva_min) + overhead)


def well_report():
    o = ["## M8. Death Well (F2/F3)"]
    o.append("| kills/s en Seva | 0 -> 75 % | uptime Ombre (cycles de 25 %) |")
    o.append("|---|---|---|")
    for k in (0.2, 0.5, 1.0, 2.0):
        f = k * (0.8 * 10 + 0.2 * 5)
        o.append(f"| {k} | {75/f:.1f} s | {uptime(k)*100:.0f} % |")
    o.append("Puits a 100 % = 6 invocations d'affilee (100 -> 75) en ne restant que 5 s (invulnerables) a chaque fois.")
    return "\n".join(o)


# ---------------------------------------------------------------------------
# 10. CLEAR : temps par pack (S1)
# ---------------------------------------------------------------------------
def pack_time(key, cs=0.375, eximus=True, h1=True):
    """DED, hypotheses TEST : animation 0,9 s / (1 + vitesse de lancer), deplacement 4 s.
    F1/F2 : Sow + 2 Reap ; F3 : + 1 tir d'amorce Viral (0,8 s).
    Eximus : F1 sous H1 -> inclus ; sous H0 -> 1 tir Epitaph (0,8 s) ; F2/F3 en Ombre : Embrace + DH + griffes,
    l'Embrace regroupe -> taille de pack x1,3 (TEST)."""
    c = v("cast_time") / (1 + cs)
    t = 3 * c + v("travel_time")
    kills = v("pack_size")
    if key == "F3":
        t += 0.8
    if key == "F1" and eximus and not h1:
        t += 0.8
    if key in ("F2", "F3"):
        # moitie des packs en Ombre : 2 lancers + 1 s de griffes + cout d'animation amorti
        t_sh = 2 * c + 1.0 + v("travel_time") + 1.8 / 3
        t = 0.5 * t + 0.5 * t_sh
        kills = 0.5 * kills + 0.5 * kills * 1.3
    return kills / t * 60


def clear_report():
    o = ["## M9. Vitesse de clear S1 (kills/min, modele DED)"]
    o.append("| Build | H1 (nuke traverse l'OG) | H0 (OG a retirer) | relatif F1 (H1) |")
    o.append("|---|---|---|---|")
    base = pack_time("F1")
    for key in BUILDS:
        a, b = pack_time(key), pack_time(key, h1=False)
        o.append(f"| {key} | {a:.0f} | {b:.0f} | x{a/base:.2f} |")
    return "\n".join(o)


# ---------------------------------------------------------------------------
# 11. CAPACITE / FORMA
# ---------------------------------------------------------------------------
def capacity_report():
    o = ["## M2. Capacite et Forma"]
    seen = set()
    for key, b in BUILDS.items():
        for part in ("seva", "shadow", "claws"):
            cfg = b[part]
            if id(cfg) in seen:
                continue
            seen.add(id(cfg))
            r = fit(cfg)
            sl = ", ".join(f"{m}[{sp or '-'}]" for m, sp in r["slots"])
            au = f"{r['aura'][0]}[{r['aura'][1] or '-'}] +{r['aura'][2]}" if r["aura"] else "-"
            ex = f"{r['exilus'][0]}[{r['exilus'][1] or '-'}]" if r["exilus"] else "-"
            o.append(f"{key}/{part} : {r['total']}/{r['cap']} {'OK' if r['fits'] else 'NE RENTRE PAS'}, "
                     f"Forma mini {r['forma']} | aura {au} | exilus {ex}")
            o.append(f"   {sl}")
            if part != "claws":
                st = stats(cfg, SHARDS)
                o.append(f"   avec 4 eclats Force : Force {st['str']*100:.0f} % (+{st['str4']*100:.0f} % sur la 4e), "
                         f"Duree {st['dur']*100:.1f} %, Portee {st['rng']*100:.0f} %, Efficacite {st['eff']*100:.0f} %, "
                         f"PV +{st['health_pct']*100:.0f} %, armure +{st['armor_pct']*100:.0f} %")
    return "\n".join(o)


# ---------------------------------------------------------------------------
# 12. SENSIBILITE
# ---------------------------------------------------------------------------
def sensitivity_report():
    o = ["## M10. Sensibilite"]
    o.append("Marge du nuke (2e Reap, debut de mission, F3 avec 1 Viral) :")
    for key, b in BUILDS.items():
        row = []
        for lab, sh in (("4 eclats", SHARDS), ("2 eclats", 0.30), ("0 eclat", 0.0)):
            s = strengths(key, shards=sh)
            row.append(f"{lab} {frac(0.5*s['S'], roar_mult(s['roar_S']), 1 if b['viral'] else 0):.2f}")
        o.append(f"  {key} : " + " ; ".join(row))
    # F1 : Intensify (+30 % partout) contre Precision Intensify (+90 % sur Roar seulement)
    old_cfg = BUILDS["F1"]["seva"]
    for lab, swap in (("Intensify (build)", None), ("Precision Intensify", "Precision Intensify"), ("ni l'un ni l'autre", "Stretch")):
        cfg = dict(old_cfg)
        if swap:
            cfg["mods"] = [swap if m == "Intensify" else m for m in cfg["mods"]]
        BUILDS["F1"]["seva"] = cfg
        row = []
        for molt in (0.0, MOLT):
            s = strengths("F1", molt=molt)
            row.append(f"Force {s['S']*100:.0f} %, Roar x{roar_mult(s['roar_S']):.2f}, 2e Reap "
                       f"{frac(0.5*s['S'], roar_mult(s['roar_S'])):.2f}, slow {min(0.35*s['S'], 0.95)*100:.0f} %")
        o.append(f"  F1 {lab} : debut [{row[0]}] | Molt [{row[1]}]")
    BUILDS["F1"]["seva"] = old_cfg
    o.append("Griffes F2, lvl 1000, 4x Tennokai :")
    s = strengths("F2")
    ref = claws_ttk(1000, s["S4"], s["S"], s["S_sh"], 4, "tennokai")[0]
    for lab, d in (("+1 eclat Force", dict(S=.15, S4=.15, Sh=.15)), ("sans Shadow Haze", dict(nohaze=True)),
                   ("Precision Intensify au lieu d'Intensify", dict(S=-.30, S4=.60)),
                   ("vuln DH ne s'applique pas a l'OG", dict(novog=True)),
                   ("Melee Exposure a 0 stack", dict(exp0=True))):
        S, S4, Sh = s["S"] + d.get("S", 0), s["S4"] + d.get("S4", 0), s["S_sh"] + d.get("Sh", 0)
        t = claws_ttk(1000, S4, 0 if d.get("nohaze") else S, Sh, 4, "tennokai",
                      vuln_og=not d.get("novog"), exposure=0 if d.get("exp0") else 4)[0]
        o.append(f"  {lab} : {t:.2f} s (reference {ref:.2f} s, x{ref/t:.2f})")
    o.append("Energie F1 a 60 kills/min :")
    for lab, mods in (("build", None), ("Streamline -> Stretch", ("Streamline", "Stretch")),
                      ("Primed Continuity -> Rolling Guard", ("Primed Continuity", "Rolling Guard"))):
        cfg = dict(BUILDS["F1"]["seva"])
        if mods:
            cfg["mods"] = [mods[1] if m == mods[0] else m for m in cfg["mods"]]
        old = BUILDS["F1"]["seva"]
        BUILDS["F1"]["seva"] = cfg
        c, i = energy_flow("F1", 60)
        BUILDS["F1"]["seva"] = old
        o.append(f"  {lab} : net {i-c:+.2f} /s")
    o.append("Taille de pack (energie F1, 60 kills/min) :")
    old = P["pack_size"]
    for ps in (8, 15, 25):
        P["pack_size"] = (ps,) + old[1:]
        c, i = energy_flow("F1", 60)
        o.append(f"  {ps} kills/rotation : net {i-c:+.2f} /s")
    P["pack_size"] = old
    return "\n".join(o)


def summary_report():
    o = ["## M1. Synthese par scenario (base F1 = x1,00)"]
    o.append("| Scenario | Build | clear (kills/min, S1 H1/H0) | Eximus HG : temps typique | indice risque | energie nette (kills/min) |")
    o.append("|---|---|---|---|---|---|")
    kpm = {"S1 SP175": 60, "S2a 500": 90, "S2b 1000": 90, "S3 9999": 45}
    scen = {175: (4, 0.5), 500: (5, 1.0), 1000: (5, 1.5), 9999: (5, 2.0)}
    for n, L in LEVELS.items():
        base_r = None
        for key, b in BUILDS.items():
            s = strengths(key, molt=MOLT)
            slow = min(v("gloom_slow") * s["S"], 0.95) if b["gloom"] else 0
            ntr, nex = scen[L]
            r = (ntr * (1 - slow) + nex) * v("hits_per_s") * coverage(key) * 60
            base_r = r if key == "F1" else base_r
            c, i = energy_flow(key, kpm[n], 0.75, 0.5 if key == "F2" else 1.0)
            if key == "F1":
                og = heavy_gunner(L, True)["og"]
                sh = math.ceil(og / epitaph_shot_vs_og(s["S"], roar_mult(s["roar_S"])))
                ex = f"2 detonations, soit 3 Reap (H1) ou {sh} tir(s) Epitaph (H0)"
            else:
                s0 = strengths(key)
                ex = f"griffes {claws_ttk(L, s0['S4'], s0['S'], s0['S_sh'], 4, 'tennokai', full=0.5)[0]:.2f} s"
            cl = f"{pack_time(key):.0f} / {pack_time(key, h1=False):.0f}" if L == 175 else "-"
            o.append(f"| {n} | {key} | {cl} | {ex} | x{r/base_r:.1f} | {i-c:+.2f}/s ({kpm[n]}) |")
    return "\n".join(o)


# ===========================================================================
# v2 (29/10/2026) : retours d'audit externe
# ===========================================================================
MOLT_PER_KILL = 0.0024   # Molt Augmented R5 : +0,24 % de Force par kill, 250 stacks (CONF)
GLOOM_CAP_STR = 0.95 / 0.35


def f1_frac(S):
    """F1 : Roar en slot 4 sans Precision Intensify -> Roar et vulnerabilite utilisent la meme Force S."""
    return frac(v("reap_vuln") * S, roar_mult(S))


def kills_to(S, target):
    """Kills de Molt Augmented pour que la Force atteigne `target` (None si > 250 stacks)."""
    if S >= target:
        return 0
    k = math.ceil((target - S) / MOLT_PER_KILL - 1e-9)
    return k if k <= 250 else None


def threshold_f1():
    lo, hi = 1.0, 4.0
    for _ in range(80):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if f1_frac(mid) >= 1 else (mid, hi)
    return hi


SHARD_STATES = [  # (libelle, bonus de Force des eclats Crimson, eclat Amber orbe tauforge present)
    ("0 eclat", 0.00, False),
    ("4 Crimson normaux + Amber", 0.40, True),
    ("1 tauforge + 3 normaux + Amber", 0.45, True),
    ("1 tauforge + 4 normaux (5e eclat Crimson, pas d'Amber)", 0.55, False),
    ("2 tauforges + 2 normaux + Amber", 0.50, True),
    ("3 tauforges + 1 normal + Amber", 0.55, True),
    ("4 tauforges + Amber (F1 final)", 0.60, True),
]


def formula_report():
    o = ["## M11. Formule du one-shot F1 (controle de l'audit externe)"]
    o.append("Formule de l'audit : 0,25 x (1 + 0,5 x Force) x (1 + 0,3 x Force). Script : frac(vuln = 0,5 x S, Roar = 1 + 0,3 x S).")
    for S in (2.53, 2.58, 2.73, 3.33):
        audit = 0.25 * (1 + 0.5 * S) * (1 + 0.3 * S)
        o.append(f"  S = {S*100:.0f} % : audit {audit:.4f} | script {f1_frac(S):.4f} | ecart {abs(audit - f1_frac(S)):.1e}")
    o.append(f"Seuil exact (fraction = 1,00) : {threshold_f1()*100:.2f} % de Force ; plafond de Gloom (95 %) : {GLOOM_CAP_STR*100:.1f} %")
    return "\n".join(o)


def shards_report():
    o = ["## M12. Etats d'eclats de F1 (debut de mission, avant Molt)"]
    o.append("| Etat | Force | 2e Reap | one-shot ? | marge | kills Molt -> 1,00 | Gloom slow | kills Molt -> 95 % | energie nette 60 kills/min |")
    o.append("|---|---|---|---|---|---|---|---|---|")
    thr = threshold_f1()
    for lab, bonus, amber in SHARD_STATES:
        S = strengths("F1", shards=bonus)["S"]
        f = f1_frac(S)
        k1, k2 = kills_to(S, thr), kills_to(S, GLOOM_CAP_STR)
        c, i = energy_flow("F1", 60, 0.75 if amber else 0.0)
        o.append(f"| {lab} | {S*100:.0f} % | {f:.3f} | {'oui' if f >= 1 else 'non'} | {f-1:+.3f} | "
                 f"{k1 if k1 is not None else '> 250'} | {min(0.35*S, 0.95)*100:.1f} % | "
                 f"{k2 if k2 is not None else '> 250'} | {i-c:+.2f}/s |")
    return "\n".join(o)


# Sources de Crimson (tables Module:DropTables/data, pages Archon Hunt / Bird 3 / Search Pulse ; CONF)
# Paliers de recompense Archimedea (CONF) : Elite = A, A, B, B, C ; normal (27 pts max) = A, A, B
DA = {"A": (0.0417, 0.1750), "B": (0.0854, 0.1313), "C": (0.1667, 0.0)}   # (tau Crimson, Crimson normal)
TA = {"A": (0.0365, 0.1533), "B": (0.0484, 0.0745), "C": (0.0911, 0.0)}
NETRACELL = (0.0417, 0.1750)
ARCHON_TAU_EFF = 0.3983   # Archon Hunt : taux tauforge effectif avec pitie (Archon_Shard, CONF)


def weekly_crimson(elite=True):
    tiers = ["A", "A", "B", "B", "C"] if elite else ["A", "A", "B"]
    rows = [
        ("Deep Archimedea " + ("Elite" if elite else "normal") + " (2 Search Pulses)",
         sum(DA[t][0] for t in tiers), sum(DA[t][1] for t in tiers)),
        ("Temporal Archimedea " + ("Elite" if elite else "normal") + " (2 Search Pulses)",
         sum(TA[t][0] for t in tiers), sum(TA[t][1] for t in tiers)),
        ("1 Netracell (1 Search Pulse)", NETRACELL[0], NETRACELL[1]),
        ("Archon Hunt (Amar 1 semaine sur 3)", ARCHON_TAU_EFF / 3, (1 - ARCHON_TAU_EFF) / 3),
        ("Bird 3 (Crimson 1 semaine sur 3, 30 000 Cavia)", 0.0, 1 / 3),
    ]
    tau = sum(r[1] for r in rows)
    norm = sum(r[2] for r in rows)
    return rows, tau, norm


def tau_sources_report():
    o = ["## M13. Crimson tauforges : esperance par semaine (5 Search Pulses = DA + TA + 1 Netracell)"]
    for elite in (True, False):
        rows, tau, norm = weekly_crimson(elite)
        o.append(f"### {'Archimedea Elite (37 points)' if elite else 'Archimedea sans Elite (27 points max)'}")
        o.append("| Source | tauforge Crimson / sem | Crimson normal / sem |")
        o.append("|---|---|---|")
        for name, t, n in rows:
            o.append(f"| {name} | {t:.3f} | {n:.3f} |")
        eq = tau + norm / 3
        o.append(f"| **Total** | **{tau:.3f}** | **{norm:.3f}** (Ascent Fusion 3 -> 1 : +{norm/3:.3f}) |")
        o.append(f"Equivalent tauforge par semaine : {eq:.2f} -> 3 tauforges de plus (apres celui de Taubound) en ~{3/eq:.1f} semaines (esperance).")
        o.append("")
    o.append("Calendrier (formules des pages wiki) : Bird 3 vend le Crimson les semaines du 26/10 et du 16/11 ; "
             "Archon Amar (Crimson) les semaines du 09/11 et du 30/11 (reset lundi 00:00 UTC).")
    return "\n".join(o)


def range_report():
    o = ["## M14. Portee : couverture et cout d'un mod de portee (F1, 4 tauforges)"]
    base_cfg = BUILDS["F1"]["seva"]
    opts = [("build actuel", None, None),
            ("Exilus Power Drift -> Cunning Drift", "Power Drift", "Cunning Drift"),
            ("Augur Secrets -> Augur Reach", "Augur Secrets", "Augur Reach"),
            ("Augur Secrets -> Stretch", "Augur Secrets", "Stretch"),
            ("Dark Propagation -> Stretch", "Dark Propagation", "Stretch"),
            ("Streamline -> Stretch", "Streamline", "Stretch"),
            ("Intensify -> Stretch", "Intensify", "Stretch")]
    o.append("Rayons CONF x Portee : Sow 16 m, Gloom 4 -> 16 m, bande de Reap 8 m (mini-Reap idem), Dark Propagation 15 m ; "
             "detection des mini-Reap 30 m fixe. Kills par rotation = min(15 x Portee^2, 30) (TEST).")
    o.append("| Option | Portee | Sow / Gloom | bande Reap | aire Sow | Force debut | 2e Reap debut | kills Molt -> 1,00 | Gloom slow debut | energie 60 kpm | capacite |")
    o.append("|---|---|---|---|---|---|---|---|---|---|---|")
    old_pack = P["pack_size"]
    for lab, out_m, in_m in opts:
        cfg = dict(base_cfg)
        if out_m:
            if out_m == cfg.get("exilus"):
                cfg["exilus"] = in_m
            else:
                cfg["mods"] = [in_m if m == out_m else m for m in cfg["mods"]]
        BUILDS["F1"]["seva"] = cfg
        st = stats(cfg, SHARDS)
        R, S = st["rng"], st["str"]
        P["pack_size"] = (min(15 * R * R, 30),) + old_pack[1:]
        c, i = energy_flow("F1", 60, 0.75)
        P["pack_size"] = old_pack
        k = kills_to(S, threshold_f1())
        r = fit(cfg)
        o.append(f"| {lab} | {R*100:.0f} % | {16*R:.1f} m | {8*R:.1f} m | x{R*R:.2f} | {S*100:.0f} % | {f1_frac(S):.3f} | "
                 f"{k if k is not None else '> 250'} | {min(0.35*S, 0.95)*100:.0f} % | {i-c:+.2f}/s | {r['total']}/{r['cap']} |")
    BUILDS["F1"]["seva"] = base_cfg
    return "\n".join(o)


# Paliers de progression (DED) : chaque palier est une config jouable
_TF = ['Shadow Haze', 'Dark Propagation', 'Umbral Intensify', 'Augur Secrets', 'Intensify', 'Transient Fortitude', 'Catalyzing Shields', 'Streamline']
_PC = ['Shadow Haze', 'Dark Propagation', 'Umbral Intensify', 'Augur Secrets', 'Intensify', 'Primed Continuity', 'Catalyzing Shields', 'Streamline']
TIERS = [
    dict(name="P0 Sans arcanes (reference, deconseille)", shards=0.0, amber=False, molt=False, energize=False, seismic=False, mods=_TF),
    dict(name="P1 Depart : Molt Augmented + Arcane Energize, Shade", shards=0.0, amber=False, molt=True, energize=True, seismic=False, mods=_TF),
    dict(name="P2 + Huras Kubrow (Stalk + Seismic Bond)", shards=0.0, amber=False, molt=True, energize=True, seismic=True, mods=_TF),
    dict(name="P3 + 4 Crimson normaux + Amber normal, Transient -> Primed Continuity", shards=0.40, amber=0.50, molt=True, energize=True, seismic=True, mods=_PC),
    dict(name="P4 + Crimson et Amber tauforges (Taubound)", shards=0.45, amber=0.75, molt=True, energize=True, seismic=True, mods=_PC),
    dict(name="P5 F1 final (4 Crimson tauforges)", shards=0.60, amber=0.75, molt=True, energize=True, seismic=True, mods=_PC),
]


def tier_energy(cfg, kpm, seismic, orb_eff, energize, gloom=1.0):
    """Energie nette du corps ; gloom = part du temps ou Gloom draine (1 = permanent, 0 = a la demande / coupe)."""
    st = stats(cfg, 0)
    eff = st["eff"] + (0.30 if seismic and gloom > 0 else 0)   # Seismic Bond ne joue que pendant une canalisation
    cm = max(2 - eff, 0.25)
    packs = kpm / 60 / v("pack_size")
    cost = packs * (v("sow_cost") + 2 * v("reap_cost")) * cm
    cost += v("roar_cost") * cm / (v("roar_dur") * st["dur"])
    cost += gloom * v("gloom_drain") * 10 * max(cm / st["dur"], 0.25)
    orbs = kpm / 60 * v("orb_drop")
    inc = orbs * v("orb_energy") * (1 + orb_eff) + (energize_rate(orbs) * v("energize") if energize else 0)
    return inc - cost


def tiers_report():
    o = ["## M15. Paliers de progression F1"]
    o.append("| Palier | Force debut / Molt plein | 2e Reap debut / Molt | Gloom debut | Duree | energie 60 kpm (Gloom permanent / a la demande) | seuil kpm (permanent) | capacite |")
    o.append("|---|---|---|---|---|---|---|---|")
    for t in TIERS:
        cfg = dict(BUILDS["F1"]["seva"])
        cfg["mods"] = t["mods"]
        st = stats(cfg, t["shards"])
        S0 = st["str"]
        S1 = S0 + (MOLT if t["molt"] else 0)
        orb = t["amber"] if t["amber"] else 0.0
        n1 = tier_energy(cfg, 60, t["seismic"], orb, t["energize"], 1.0)
        n0 = tier_energy(cfg, 60, t["seismic"], orb, t["energize"], 0.0)
        thr = next((k for k in range(5, 601) if tier_energy(cfg, k, t["seismic"], orb, t["energize"]) >= 0), None)
        r = fit(cfg)
        o.append(f"| {t['name']} | {S0*100:.0f} % / {S1*100:.0f} % | {f1_frac(S0):.3f} / {f1_frac(S1):.3f} | "
                 f"{min(0.35*S0, 0.95)*100:.0f} % | {st['dur']*100:.1f} % | {n1:+.2f} / {n0:+.2f} | "
                 f"{'~%d' % thr if thr else '> 600'} | {r['total']}/{r['cap']} ({r['forma']} Forma) |")
    return "\n".join(o)


def blast_report():
    o = ["## M18. Plan B Overguard : Blast des detonations voisines (DED, T1 etape 7)"]
    o.append("Chaque Heavy Gunner (sans OG) detone dans un rayon de 4 m : 25 % de ses PV x Roar (x vuln si elle s'applique a l'OG).")
    o.append("| Niveau | PV Heavy Gunner | OG Eximus | Blast/voisin (sans vuln sur OG) | voisins pour vider l'OG | avec vuln sur OG | voisins |")
    o.append("|---|---|---|---|---|---|---|")
    s = strengths("F1")
    r = roar_mult(s["roar_S"])
    vuln = 1 + v("reap_vuln") * s["S"]
    for n, L in LEVELS.items():
        h = heavy_gunner(L)["health"]
        og = heavy_gunner(L, True)["og"]
        b0, b1 = v("detonate_pct") * h * r, v("detonate_pct") * h * r * vuln
        o.append(f"| {n} | {h:,.0f} | {og:,.0f} | {b0:,.0f} | {math.ceil(og/b0)} | {b1:,.0f} | {math.ceil(og/b1)} |")
    o.append("Rotation reelle pour un Eximus sous H1 : Reap (vuln) -> Sow -> Reap (1re detonation) -> Reap (2e) ; "
             "ajouter un Sow avant le 3e Reap si T6 montre que Sow est consomme.")
    return "\n".join(o)


def huras_report():
    o = ["## M16. Huras Kubrow : survie (Module:Companions/data, rework des compagnons)"]
    hp0, sh0, ar0 = 560, 490, 300   # CONF (module ; les patch notes du rework annoncaient 200 d'armure)
    builds = [("nu", 0, 0, 0), ("Enhanced Vitality + Metal Fiber", 2.5, 2.5, 0),
              ("+ Calculated Redirection", 2.5, 2.5, 2.5)]
    o.append("| Mods | PV | armure (DR) | boucliers | EHP | balles HG pour le neutraliser (175 / 500 / 1000 / 9999) |")
    o.append("|---|---|---|---|---|---|")
    for lab, h, a, sh in builds:
        hp, ar, shd = hp0 * (1 + h), ar0 * (1 + a), sh0 * (1 + sh)
        dr = ar / (ar + 300)
        e = hp / (1 - dr) + shd
        b = " / ".join(f"{e/(v('hg_shot')*heavy_gunner(L)['dmg_mult']):.1f}" for L in (175, 500, 1000, 9999))
        o.append(f"| {lab} | {hp:,.0f} | {ar:,.0f} ({dr*100:.1f} %) | {shd:,.0f} | {e:,.0f} | {b} |")
    o.append("Neutralisation (CONF) : 60 s de base, retour automatique avec 5 s d'invulnerabilite ; Medi-Pet Kit -15 s, "
             "Momentous Bond -18 s par Eximus tue, Restorative Bond -3 s par orbe de vie, Hard Reset (Parazon) -15 s par Mercy.")
    for lab, base in (("sans mod", 60), ("Medi-Pet Kit", 45)):
        o.append(f"  {lab} : {base} s ; avec 1 Eximus tue / 10 s (Momentous) : ~{max(base / (1 + 18/10), 5):.0f} s (DED, approx.)")
    return "\n".join(o)


TAUBOUND_ITEMS = [  # (objet, Moonflesh, utilite pour F1)
    ("Crimson tauforge (x1)", 375, "+5 % Force : 253 -> 258 %, passe le seuil sans Molt"),
    ("Secondary Fortifier x21 (rang 5)", 21 * 8, "plan B Overguard (Epitaph Prime x8 contre l'OG)"),
    ("Amber tauforge (x1)", 375, "orbes d'energie +75 % au lieu de +50 %"),
    ("Melee Exposure x21 (rang 5)", 21 * 8, "griffes du Tombstone (optionnel)"),
    ("Legendary Core (x1)", 500, "monte Primed Continuity au rang max (optionnel)"),
]


def taubound_report():
    o = ["## M17. Taubound (jusqu'au 17/11/2026) : Moonflesh"]
    total_core = sum(x[1] for x in TAUBOUND_ITEMS[:3])
    total_all = sum(x[1] for x in TAUBOUND_ITEMS)
    for it in TAUBOUND_ITEMS:
        o.append(f"  {it[0]} : {it[1]} Moonflesh - {it[2]}")
    o.append(f"Indispensable (3 premieres lignes) : {total_core} Moonflesh ; avec les options : {total_all}.")
    per_kill = 0.02 * 3   # ~2 % de chance, 3 Moonflesh en Steel Path (CONF, valeur approchee du wiki)
    for kpm in (60, 90, 120):
        rate = per_kill * kpm * 60
        o.append(f"  Kills d'Infestes d'Eris en SP a {kpm} kills/min : ~{rate:.0f} Moonflesh/h (DED) -> "
                 f"{total_core/rate:.1f} h pour l'indispensable, hors alertes (75 chacune en SP)")
    return "\n".join(o)


# ===========================================================================
# v3 (29/10/2026) : guides YouTube (COMM) a recouper
# ===========================================================================
RANGE_V3 = [  # (libelle, remplacements {ancien: nouveau}, exilus)
    ("100 % : F1 actuel", {}, None),
    ("145 % : Augur Secrets -> Stretch (v2, S2)", {"Augur Secrets": "Stretch"}, None),
    ("190 % a : + Cunning Drift (exilus) + Augur Reach a la place de Catalyzing", {"Augur Secrets": "Stretch", "Catalyzing Shields": "Augur Reach"}, "Cunning Drift"),
    ("190 % b : + Cunning Drift + Augur Reach a la place d'Intensify (204 %, comme V1)", {"Augur Secrets": "Stretch", "Intensify": "Augur Reach"}, "Cunning Drift"),
    ("190 % c : + Cunning Drift + Augur Reach a la place de Streamline", {"Augur Secrets": "Stretch", "Streamline": "Augur Reach"}, "Cunning Drift"),
    ("190 % d : variante a + Transient Fortitude a la place de Primed Continuity", {"Augur Secrets": "Stretch", "Catalyzing Shields": "Augur Reach", "Primed Continuity": "Transient Fortitude"}, "Cunning Drift"),
    ("max 280 % : Stretch, Augur Reach, Overextended, Cunning Drift", {"Augur Secrets": "Stretch", "Intensify": "Augur Reach", "Catalyzing Shields": "Overextended"}, "Cunning Drift"),
    ("max 280 % + Transient Fortitude", {"Augur Secrets": "Stretch", "Intensify": "Augur Reach", "Catalyzing Shields": "Overextended", "Primed Continuity": "Transient Fortitude"}, "Cunning Drift"),
    ("250 % facon V3 : Stretch, Augur Reach, Overextended R4, Transient Fortitude, Power Drift garde", {"Augur Secrets": "Stretch", "Intensify": "Augur Reach", "Catalyzing Shields": "Overextended R4", "Primed Continuity": "Transient Fortitude"}, None),
]


def range_v3_report():
    o = ["## M19. Portee 100 % / 190 % / max (F1, 4 Crimson tauforges)"]
    o.append("Dependant de la Portee (CONF, wiki) : bande de Reap 8 m, mini-Reap de Shadow Haze (rayon), Sow 16 m, "
             "Dark Propagation 15 m (Portee de Sevagoth), Gloom 4 -> 16 m. Fixe : explosion de Sow/Reap 4 m (pas d'icone de "
             "Portee sur le wiki), detection des mini-Reap 30 m, Shadow Haze (crit independant de la Portee depuis 33.6.3).")
    o.append("| Option | Portee | Sow / Gloom / DP | bande Reap | Force debut / Molt | 2e Reap debut / Molt | kills Molt -> 1,00 | Gloom debut | Duree | energie 60 kpm (aire / sans aire) | capacite |")
    o.append("|---|---|---|---|---|---|---|---|---|---|---|")
    base = BUILDS["F1"]["seva"]
    old_pack = P["pack_size"]
    for lab, rep, ex in RANGE_V3:
        cfg = dict(base)
        cfg["mods"] = [rep.get(m, m) for m in base["mods"]]
        if ex:
            cfg["exilus"] = ex
        BUILDS["F1"]["seva"] = cfg
        st = stats(cfg, SHARDS)
        R, S = st["rng"], st["str"]
        e_flat = tier_energy(cfg, 60, True, 0.75, True, 1.0)
        P["pack_size"] = (min(15 * R * R, 30),) + old_pack[1:]
        e_area = tier_energy(cfg, 60, True, 0.75, True, 1.0)
        P["pack_size"] = old_pack
        k = kills_to(S, threshold_f1())
        r = fit(cfg)
        o.append(f"| {lab} | {R*100:.0f} % | {16*R:.1f} / {16*R:.1f} / {15*R:.1f} m | {8*R:.1f} m | {S*100:.0f} / {(S+MOLT)*100:.0f} % | "
                 f"{f1_frac(S):.3f} / {f1_frac(S+MOLT):.3f} | {k if k is not None else '> 250'} | {min(0.35*S, 0.95)*100:.0f} % | "
                 f"{st['dur']*100:.1f} % | {e_area:+.2f} / {e_flat:+.2f} | {r['total']}/{r['cap']} ({r['forma']} F) |")
    BUILDS["F1"]["seva"] = base
    o.append("Lecture : les 28 m de V3 correspondent a Sow a 175 % (16 x 1,75 : Stretch + Augur Reach) ou a Dark Propagation a ~187 % "
             "(15 x 1,87), jamais a l'explosion de 4 m, qui ne depend pas de la Portee (DED). Le 190 % b reproduit exactement V1 (204 % / 190 %).")
    return "\n".join(o)


def entropic(level):
    """Proxy Eximus Entropique : PV et OG du Heavy Gunner Eximus, armure de base 50 (CONF wiki Eximus)."""
    t = heavy_gunner(level, eximus=True)
    q = level - v("hg_base_level")
    t["armor"] = min(max(50 * two_curve(q, 0.005, 1.75, 0.4, 0.75, 70, 80), 200), 2700)
    return t


def entropic_report():
    o = ["## M20. Eximus Entropiques (Zariman, U44) : que peut faire Sevagoth ?"]
    o.append("Regles CONF (wiki Eximus#Entropic + patch notes U44) : orbe qui bloque projectiles d'armes et d'Amps ; "
             "immunite aux competences tant que l'orbe tient ; armes primaires/secondaires -90 %, Amp -75 %, glaives/gunblades -90 % ; "
             "les degats de zone et les ondes de slam ne traversent pas l'orbe ; les compagnons ne les ciblent pas ; "
             "armure de base 50. Orbe casse par une attaque de melee sous benediction de l'Iceblade de Narin, ou par un Tauron Strike.")
    o.append("Griffes (config Ombre de F3) contre un Eximus Entropique : ni vulnerabilite DH ni Shadow Haze (competences sans effet).")
    o.append("| Niveau | armure | OG | PV | griffes 4x Tennokai, statuts a moitie | idem 12x | griffes F3 si DH et Haze passaient (v1) |")
    o.append("|---|---|---|---|---|---|---|")
    s = strengths("F3")
    for n, L in LEVELS.items():
        t = entropic(L)

        def tt(combo, sh, sv):
            # remplace la cible par le proxy entropique
            per_s = v("stance_block_pct") / v("stance_block_time")
            hits_s = v("stance_block_hits") / v("stance_block_time")
            og_l, hp_l = claws_hit(s["S4"], sv, sh, combo, t, full=0.5, fury=FURY)
            og_h, hp_h = claws_hit(s["S4"], sv, sh, combo, t, full=0.5, heavy=True, fury=FURY)
            cyc = 4 / hits_s + 0.9
            lf = (4 / hits_s) / cyc
            dog = og_l * per_s * lf + og_h / cyc
            dhp = hp_l * per_s * lf + hp_h / cyc
            return t["og"] / dog + t["health"] / dhp
        o.append(f"| {n} | {t['armor']:.0f} | {t['og']:,.0f} | {t['health']:,.0f} | {tt(4, 0.0, 0.0):.2f} s | {tt(12, 0.0, 0.0):.2f} s | {tt(4, s['S_sh'], s['S']):.2f} s |")
    return "\n".join(o)


def gloom_report():
    o = ["## M21. Gloom : garder ou couper ? (F1 final, 60 kills/min)"]
    cfg = BUILDS["F1"]["seva"]
    on = tier_energy(cfg, 60, True, 0.75, True, 1.0)
    off = tier_energy(cfg, 60, True, 0.75, True, 0.0)
    o.append(f"Energie : Gloom permanent (Seismic Bond actif) {on:+.2f}/s ; Gloom coupe (Seismic inactif) {off:+.2f}/s -> Gloom rapporte {on-off:+.2f}/s.")
    # Archon Stretch : 2 energie/s pendant 5 s, sans cumul ni rafraichissement ; bloque par un drain canalise ; 1 s de pause par lancement
    casts_per_s = 60 / 60 / v("pack_size") * 3 + 1 / (v("roar_dur") * stats(cfg, SHARDS)["dur"])
    a_s = 2.0 * max(1 - casts_per_s * 1.0, 0)
    o.append(f"Archon Stretch (si un compagnon le declenche, CONF : competences Electricite seulement ; bloque tant que Gloom draine) : "
             f"au mieux ~{a_s:.2f}/s Gloom coupe (2/s moins 1 s de pause par lancement, {casts_per_s:.2f} lancement/s).")
    o.append(f"  -> Gloom coupe + Archon Stretch : {off + a_s:+.2f}/s contre Gloom + Seismic : {on:+.2f}/s.")
    s = strengths("F1")
    o.append(f"Vol de vie Gloom : {v('gloom_ls')*s['S']*100:.1f} % des degats ; PV du corps 370 -> utile contre les degats d'usure, nul contre un one-shot.")
    o.append(f"Ralentissement : {min(0.35*s['S'], 0.95)*100:.0f} % dans {16*stats(cfg, SHARDS)['rng']:.0f} m, soit le meme rayon que Sow : "
             "les ennemis ralentis sont deja dans la zone du nuke (DED).")
    return "\n".join(o)


def threshold_v3_report():
    o = ["## M22. Seuil (V1/V2/V3 : 255 %)"]
    o.append(f"Seuil exact {threshold_f1()*100:.2f} % ; a 255 % la fraction vaut {f1_frac(2.55):.4f} (>= 1) : coherent, la communaute arrondit.")
    return "\n".join(o)


def circumvent_report():
    o = ["## M23. Retrait de l'Overguard : Arcane Circumvent contre Epitaph + Secondary Fortifier (Heavy Gunner Eximus, F1)"]
    o.append("Circumvent (CONF, wiki) : une roulade a travers un ennemi a 4 m vole 25 % (rang 0) a 50 % (rang 5) de son armure, "
             "ses boucliers et son OG ; repetable ; 'deux roulades retirent tout au rang max' ; OG gagne par le joueur plafonne a 10 000. "
             "Lecture lineaire (% de l'OG max, celle du wiki) contre lecture geometrique (% de l'OG restant) : T20 tranche.")
    o.append("| Niveau | OG de l'Eximus | roulades R5 (lin. / OG restant apres 2 en geom.) | roulades R0 (lin.) | OG gagne par roulade | tirs Epitaph+Fortifier |")
    o.append("|---|---|---|---|---|---|")
    s = strengths("F1")
    r = roar_mult(s["roar_S"])
    for n, L in LEVELS.items():
        og = heavy_gunner(L, eximus=True)["og"]
        shots = math.ceil(og / epitaph_shot_vs_og(s["S"], r))
        o.append(f"| {n} | {og:,.0f} | {math.ceil(1/0.50)} / {0.5**2*100:.0f} % | {math.ceil(1/0.25)} | {min(0.5*og, 10000):,.0f} | {shots} |")
    o.append("Roulade : pas une attaque d'arme -> ne devrait pas casser Stalk/Ghost (DED depuis la page Ghost, T20). Epitaph : casse l'invisibilite, 7 s.")
    return "\n".join(o)

# ===========================================================================
# v4 (30/10/2026) : video de RubyBlossom5 (A) et tests Ombre/equipement (B), COMM
# ===========================================================================
SWAPPABLE = ["Augur Secrets", "Intensify", "Catalyzing Shields", "Primed Continuity", "Streamline"]
FIXED_F1 = ["Shadow Haze", "Dark Propagation", "Umbral Intensify"]
for _r in range(4):   # Overextended aux rangs 0 a 3 : +15 % de Portee et -10 % de Force par rang (CONF, wiki)
    MODS[f"Overextended R{_r}"] = (6, _r, "V", {"rng": 0.15 * (_r + 1), "str": -0.10 * (_r + 1)})
POOL_V4 = SWAPPABLE + ["Stretch", "Augur Reach", "Transient Fortitude"] + [f"Overextended R{r}" for r in range(5)] + ["Overextended"]
SHADOW_DETECT = 30.0   # m, detection des mini-Reap, fixe (CONF, wiki Shadow Haze)


def range_configs(target):
    """Toutes les configs F1 (4 Crimson tauforges) dont la Portee vaut `target`, triees par Force de depart."""
    out = []
    base = BUILDS["F1"]["seva"]
    for combo in itertools.combinations(POOL_V4, 5):
        if sum(m.startswith("Overextended") for m in combo) > 1:
            continue
        for ex in ("Power Drift", "Cunning Drift"):
            cfg = dict(base)
            cfg["mods"] = FIXED_F1 + list(combo)
            cfg["exilus"] = ex
            st = stats(cfg, SHARDS)
            if abs(st["rng"] - target) > 1e-6:
                continue
            r = fit(cfg)
            if not r["fits"]:
                continue
            out.append((st["str"], cfg, st, r))
    out.sort(key=lambda x: (-x[0], -x[2]["dur"], -x[2]["eff"]))
    return out


def _row(lab, cfg, st, r):
    S, R = st["str"], st["rng"]
    e = tier_energy(cfg, 60, True, 0.75, True, 1.0)
    k = kills_to(S, threshold_f1())
    out = [m for m in SWAPPABLE if m not in cfg["mods"]] + (["Power Drift"] if cfg["exilus"] != "Power Drift" else [])
    inn = [m for m in cfg["mods"] if m not in FIXED_F1 + SWAPPABLE] + (["Cunning Drift"] if cfg["exilus"] == "Cunning Drift" else [])
    return (f"| {lab} | {R*100:.0f} % | {', '.join(inn) or '-'} | {', '.join(out) or '-'} | {S*100:.0f} / {(S+MOLT)*100:.0f} % | "
            f"{f1_frac(S):.3f} | {k if k is not None else '> 250'} | {st['dur']*100:.1f} % | {st['eff']*100:.0f} % | "
            f"{'oui' if st['catalyzing'] else 'non'} | {e:+.2f} | {8*R:.1f} / {16*R:.1f} m | {r['total']}/{r['cap']} ({r['forma']} F) |")


def range_v4_report():
    o = ["## M24. Portee 175 % et 190 % : meilleures configs de Force (F1, 4 Crimson tauforges, P5)"]
    o.append(f"Mini-Reap : rayon 8 m x Portee (CONF) ; detection {SHADOW_DETECT:.0f} m fixe (CONF) ; Sow 16 m x Portee. "
             f"Le rayon de Sow depasse la detection au-dela de {SHADOW_DETECT/16*100:.1f} % (DED).")
    o.append("Toutes les combinaisons des 5 slots echangeables (Augur Secrets, Intensify, Catalyzing, Primed Continuity, Streamline) "
             "avec Stretch, Augur Reach, Transient Fortitude, Overextended (rangs 0 a 5) et l'exilus Power/Cunning Drift ; capacite verifiee. "
             "Ne sont gardees que les configs non dominees (Force, energie, Catalyzing). Energie : 10 stacks de Seismic Bond (cf. M25).")
    o.append("| Config | Portee | Ajoute | Retire | Force debut / Molt | 2e Reap debut | kills Molt -> 1,00 | Duree | Efficacite | Catalyzing | energie 60 kpm (pack constant) | rayon mini-Reap / Sow | capacite |")
    o.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    o.append(_row("100 % : F1 actuel", BUILDS["F1"]["seva"], stats(BUILDS["F1"]["seva"], SHARDS), fit(BUILDS["F1"]["seva"])))
    for tgt in (1.75, 1.90, 2.35):
        rows = [(S, cfg, st, r, tier_energy(cfg, 60, True, 0.75, True, 1.0)) for S, cfg, st, r in range_configs(tgt)]
        front = []
        for x in rows:
            dominated = any(y[0] >= x[0] - 1e-9 and y[4] >= x[4] - 1e-9 and y[2]["catalyzing"] >= x[2]["catalyzing"]
                            and (y[0] > x[0] + 1e-9 or y[4] > x[4] + 1e-9 or y[2]["catalyzing"] > x[2]["catalyzing"]) for y in rows)
            if not dominated and not any(abs(f[0] - x[0]) < 1e-9 and abs(f[4] - x[4]) < 1e-9 and f[2]["catalyzing"] == x[2]["catalyzing"] for f in front):
                front.append(x)
        front = [x for x in front if x[4] > 0]
        for i, (S, cfg, st, r, e) in enumerate(sorted(front, key=lambda x: -x[0])):
            o.append(_row(f"{tgt*100:.0f} % {chr(97+i)}", cfg, st, r))
    return "\n".join(o)


def seismic_energy(cfg, stacks_eff, mode):
    """Energie nette (60 kpm, P5) avec Seismic Bond a `stacks_eff` (0 a 0,30).
    mode 'dyn' : le drain de Gloom suit l'efficacite (CONF, page Gloom) ; 'snap0' : drain fige sans stack ; 'off' : Gloom coupe."""
    st = stats(cfg, 0)
    e_cast = st["eff"] + (stacks_eff if mode != "off" else 0)
    e_drain = st["eff"] + (stacks_eff if mode == "dyn" else 0)
    cm, cd = max(2 - e_cast, 0.25), max(2 - e_drain, 0.25)
    packs = 60 / 60 / v("pack_size")
    cost = packs * (v("sow_cost") + 2 * v("reap_cost")) * cm + v("roar_cost") * cm / (v("roar_dur") * st["dur"])
    if mode != "off":
        cost += v("gloom_drain") * 10 * max(cd / st["dur"], 0.25)
    orbs = 60 / 60 * v("orb_drop")
    return orbs * v("orb_energy") * 1.75 + energize_rate(orbs) * v("energize") - cost


def seismic_report():
    o = ["## M25. Seismic Bond reel : stacks et figeage de Gloom (F1 P5, 60 kills/min)"]
    o.append("CONF (wiki Seismic Bond) : +3 %/stack, 12 s par stack, plafond +30 % ; un stack par degat du compagnon pendant une "
             "competence canalisee ; Gloom ne compte que s'il draine. CONF (wiki Gloom) : le drain de Gloom suit l'efficacite en continu. "
             "v3 supposait +30 % en permanence.")
    cfg = BUILDS["F1"]["seva"]
    off = seismic_energy(cfg, 0, "off")
    o.append("| Stacks | Efficacite sous Gloom | Gloom permanent (drain dynamique, CONF) | Gloom fige sans stack (hypothese) | Gloom coupe |")
    o.append("|---|---|---|---|---|")
    for n in (0, 3, 5, 7, 10):
        e = 0.03 * n
        o.append(f"| {n} | {(stats(cfg)['eff']+e)*100:.0f} % | {seismic_energy(cfg, e, 'dyn'):+.2f} | {seismic_energy(cfg, e, 'snap0'):+.2f} | {off:+.2f} |")
    be = next((n for n in range(11) if seismic_energy(cfg, 0.03 * n, "dyn") >= off), None)
    o.append(f"Seuil : Gloom permanent rapporte plus que Gloom coupe a partir de {be} stacks (DED). "
             f"Fige sans stack, il ne passe jamais devant ({seismic_energy(cfg, 0.30, 'snap0'):+.2f} au mieux) ; "
             "relancer Gloom une fois les stacks montes rend le cas fige identique au cas dynamique.")
    return "\n".join(o)


def ruby_loop_report():
    o = ["## M26. Boucle de RubyBlossom5 (Gloom retire, Ombre gardee) contre F1"]
    o.append("CONF : corps invulnerable et non ciblable pendant l'Ombre ; 5 s d'invulnerabilite a l'invocation ; Reunite casse Stalk "
             "(Sevagoth reste invisible tant que l'Ombre est sortie) ; 7 s de recharge apres toute invisibilite ; "
             "Transference force Reunite ; Death Well : 5 % par ennemi touche par Reap/Sow/DH, sortie a 75 %.")
    o.append("| Duree d'une boucle (s) | Temps visible apres Reunite (7 s) | Part du temps visible (DED) |")
    o.append("|---|---|---|")
    for T in (15, 20, 30, 45):
        o.append(f"| {T} | 7 s | {7/T*100:.0f} % |")
    cfg = BUILDS["F1"]["seva"]
    o.append(f"Energie du corps : la boucle lance les memes Sow/Reap/Roar que F1 sans Gloom, donc au mieux le bilan 'Gloom coupe' "
             f"({seismic_energy(cfg, 0, 'off'):+.2f}/s) ; les sorts de l'Ombre utilisent sa propre reserve (CONF). "
             f"F1 Gloom permanent : {seismic_energy(cfg, 0.30, 'dyn'):+.2f}/s a 10 stacks, {seismic_energy(cfg, 0.0, 'dyn'):+.2f}/s a 0.")
    return "\n".join(o)


def viral_threshold(n, roar=True, first=False):
    """Force minimale pour un one-shot : 2e Reap (vulnerabilite) ou 1re detonation (sans vulnerabilite)."""
    V = viral_mult(n)
    if first:
        return 0.0 if v("detonate_pct") * V >= 1 else None
    lo, hi = 0.0, 6.0
    f = (lambda S: frac(v("reap_vuln") * S, roar_mult(S) if roar else 1.0, n))
    if f(hi) < 1:
        return None
    for _ in range(80):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if f(mid) >= 1 else (mid, hi)
    return hi


def tempest_sim(S, R, dur, r_pos, trials=4000, seed=7):
    """Monte Carlo (DED) : stacks Viral d'un ennemi immobile a r_pos m du centre d'un Tempest Barrage.
    CONF : 4 missiles/s, zone de 10 m (fixe), explosion 5 m x Portee, Viral Tempest R3 : 100 % x Force par missile,
    Viral 6 s par stack. NON TROUVE : repartition des impacts (supposee uniforme dans le disque)."""
    rnd = random.Random(seed)
    T, rexp, dt = 10 * dur, 5 * R, 0.25
    t1, t9 = [], []
    for _ in range(trials):
        stacks, a1, a9, t = [], None, None, 0.0
        while t < T:
            t += dt
            ang, rad = rnd.random() * 2 * math.pi, 10 * math.sqrt(rnd.random())
            x, y = rad * math.cos(ang) - r_pos, rad * math.sin(ang)
            if x * x + y * y <= rexp * rexp:
                k = int(S) + (1 if rnd.random() < S - int(S) else 0)
                stacks += [t] * k
            stacks = [s for s in stacks if t - s < 6.0][-10:]
            if a1 is None and len(stacks) >= 1:
                a1 = t
            if a9 is None and len(stacks) >= 9:
                a9 = t
        t1.append(a1 if a1 is not None else float("inf"))
        t9.append(a9 if a9 is not None else float("inf"))
    med = lambda xs: sorted(xs)[len(xs) // 2]
    return med(t1), med(t9), sum(x < float("inf") for x in t9) / trials


def viral_report():
    o = ["## M27. Viral : seuils et sources compatibles avec l'invisibilite"]
    o.append("CONF (wiki Viral) : degats aux PV x(2 + 0,25 x (n - 1)), 10 stacks max, 6 s chacun ; ne s'applique pas tant que l'Overguard tient. "
             "CONF (wiki Shadow Haze) : 9 stacks suffisent pour que Sow + 1 Reap tuent avant la vulnerabilite.")
    o.append("| Stacks Viral | Multiplicateur | Force mini, 2e Reap, avec Roar | sans Roar | 1re detonation seule (sans vulnerabilite) |")
    o.append("|---|---|---|---|---|")
    for n in (0, 1, 2, 5, 9, 10):
        a, b, c = viral_threshold(n, True), viral_threshold(n, False), viral_threshold(n, first=True)
        o.append(f"| {n} | x{viral_mult(n):.2f} | {a*100:.1f} % | {b*100:.1f} % | {'tue (' + format(v('detonate_pct')*viral_mult(n), '.3f') + ')' if c is not None else 'non (' + format(v('detonate_pct')*viral_mult(n), '.3f') + ')'} |")
    o.append("Tempest Barrage + Viral Tempest (Helminth slot 4 a la place de Roar) : delai median avant 1 et 9 stacks (DED, Monte Carlo).")
    o.append("| Config | Force | Portee | Duree | ennemi au centre : 1 / 9 stacks | a 5 m | a 9 m | part qui atteint 9 stacks (a 9 m) |")
    o.append("|---|---|---|---|---|---|---|---|")
    for lab, S, R, D in (("100 %, Force F1", 2.73, 1.0, 1.55), ("175 %, Force 219 %", 2.19, 1.75, 1.55), ("280 %, Force 144 %", 1.44, 2.80, 1.55)):
        c = [tempest_sim(S, R, D, rp) for rp in (0.0, 5.0, 9.0)]
        o.append(f"| {lab} | {S*100:.0f} % | {R*100:.0f} % | {D*100:.0f} % | {c[0][0]:.2f} / {c[0][1]:.2f} s | {c[1][0]:.2f} / {c[1][1]:.2f} s | "
                 f"{c[2][0]:.2f} / {c[2][1]:.2f} s | {c[2][2]*100:.0f} % |")
    o.append(f"Energie : Tempest 25 par {10*1.55:.1f} s, Roar 75 par {30*1.55:.1f} s -> meme cout par seconde a zone unique (CONF + DED).")
    return "\n".join(o)


def entropic_v4_report():
    o = ["## M28. Eximus Entropiques apres les precisions des patch notes U44"]
    o.append("CONF (U44, precisions) : degats non-melee -90 % (Operateur -75 %), bulle cassee ou non ; la bulle empeche les competences "
             "de blesser l'Eximus, de l'interieur comme de l'exterieur.")
    S = SHARDS + stats(BUILDS["F1"]["seva"])["str"]
    f = f1_frac(S)
    rem = [(1 - 0.10 * f) ** k for k in (1, 3, 10)]
    o.append(f"Nuke F1 sur un Entropique dont la bulle est cassee (DED, si -90 % s'applique au True) : {0.10*f:.4f} des PV actuels par "
             f"detonation -> reste {rem[0]*100:.0f} % apres 1, {rem[1]*100:.0f} % apres 3, {rem[2]*100:.0f} % apres 10 detonations.")
    return "\n".join(o)


# ===========================================================================
# v5 (30/10/2026) : page Overframe et calculateur de RubyBlossom5 (source C, COMM)
# ===========================================================================
RUBY_CALC = {2.53: 0.9960, 2.54: 0.9999, 2.58: 1.0156, 2.73: 1.0755}   # valeurs lues dans son PDF (p. 1)


def gloom_drain(n, eff, dur):
    """CONF (wiki Channeled Abilities / Gloom) : 0,75 x (2 - E) / D par ennemi, 10 ennemis max."""
    return v("gloom_drain") * min(n, 10) * max(2 - eff, 0.25) / dur


def calc_compare_report():
    o = ["## M29. Calculateur de RubyBlossom5 contre ce script"]
    o.append("| Force | Ruby (2e Reap, Roar) | Script f1_frac | Ecart |")
    o.append("|---|---|---|---|")
    for S, r in RUBY_CALC.items():
        o.append(f"| {S*100:.0f} % | {r*100:.2f} % | {f1_frac(S)*100:.2f} % | {(f1_frac(S)-r)*100:+.3f} pt |")
    o.append(f"Force de base (100 %), Reap + Roar : {frac(v('reap_vuln')*1.0, roar_mult(1.0))*100:.2f} % (Ruby : 48,75 %).")
    o.append("Drain de Gloom (Duree 155 %, Efficacite 130 % ; Ruby p. 3 : 0,339 par ennemi, 3,387 a 10) :")
    for n in (1, 5, 10):
        o.append(f"  {n} ennemi(s) : {gloom_drain(n, 1.30, 1.55):.3f}/s sans Seismic Bond, {gloom_drain(n, 1.60, 1.55):.3f}/s a 10 stacks ; "
                 f"641 d'energie durent {641/gloom_drain(n, 1.30, 1.55)/60:.1f} min sans regeneration")
    o.append("Rayon de Gloom : 4 -> 16 m x Portee, vague a 2 m/s x Duree (CONF) -> temps de croissance 6 x Portee / Duree :")
    for lab, R, D in (("F1 100 %", 1.0, 1.55), ("175 % b", 1.75, 1.275), ("Ruby 145 %", 1.45, 1.0), ("Ruby 175 %", 1.75, 1.0)):
        o.append(f"  {lab} : {16*R:.1f} m atteints en {6*R/D:.1f} s")
    o.append("Ralentissement effectif 1 / (1 - ralentissement) (metrique de Ruby) : "
             + ", ".join(f"{S*100:.0f} % -> {min(0.35*S,0.95)*100:.1f} % (x{1/(1-min(0.35*S,0.95)):.2f})" for S in (1.74, 2.34, 2.49, 2.58, 2.74)))
    o.append("Colonne 'Vs Orokin / Anarchs' = bloc Smite (Helminth d'Oberon) : min(35 % x Force, 50 %) x (1 + 0,5 x Force) x 0,5 "
             "(Radiation x0,5 contre Orokin et Anarch, CONF). Egale au True sans Roar seulement quand Smite est plafonne (Force >= 142,9 %) :")
    for S in (0.63, 1.0, 1.43, 2.73):
        smite = min(0.35 * S, 0.50) * (1 + 0.5 * S)
        o.append(f"  {S*100:.0f} % : Smite + vuln {smite*100:.2f} %, vs Orokin/Anarchs {smite*50:.2f} %, True sans Roar {0.25*(1+0.5*S)*100:.2f} %")
    return "\n".join(o)


def ruby_main_report():
    o = ["## M30. Build principale de Ruby (sans Helminth, Gloom + Ombre, Viral a l'arme) contre F1"]
    o.append("COMM (source C) : Force 174 % au depart, 234 % Molt plein ; Portee 145 ou 175 % ; Viral pose a l'arme (Kompressa, Epitaph). "
             "CONF : le Viral ne prend pas sous Overguard ; tirer casse Stalk.")
    o.append("| Build | Force | Roar | Viral | 2e Reap | Ralentissement de Gloom (fige au lancer) |")
    o.append("|---|---|---|---|---|---|")
    rows = [("Ruby, debut", 1.74, False, 1), ("Ruby, debut", 1.74, False, 2), ("Ruby, Molt plein", 2.34, False, 1),
            ("F1 100 %", 2.73, True, 0), ("F1 175 % b", 2.74, True, 0)]
    for lab, S, roar, n in rows:
        f = frac(v("reap_vuln") * S, roar_mult(S) if roar else 1.0, n)
        o.append(f"| {lab} | {S*100:.0f} % | {'oui' if roar else 'non'} | {n} | {f:.3f} | {min(0.35*S,0.95)*100:.1f} % |")
    k = math.ceil((2.00 - 1.74) / MOLT_PER_KILL)
    o.append(f"Ruby atteint 200 % (one-shot a 1 stack) apres {k} kills de Molt ; avant, il faut 2 stacks Viral par cible.")
    o.append("Death Well (COMM C, coherent avec le wiki 5 % par ennemi et par competence) : 10 % par kill marque par Sow et Reap -> "
             "75 % apres 8 kills, donc une sortie d'Ombre possible a chaque pack.")
    return "\n".join(o)


def emerald_report():
    o = ["## M31. Config C (Tempest + Viral Tempest) : eclats Crimson contre Emeraude (source C, DED)"]
    o.append("CONF : Tempest Barrage pose Corrosif a 100 % ; Emeraude tauforge = +15 % de degats de competence sur les ennemis "
             "deja sous Corrosion, multiplicatif avec la Force, cumul additif entre eclats.")
    o.append("| Eclats (4 slots + Amber) | Force | 1 stack Viral, 2e Reap | 9 stacks, 1re detonation | Ralentissement de Gloom | stacks Viral par missile |")
    o.append("|---|---|---|---|---|---|")
    base = stats(BUILDS["F1"]["seva"])["str"]
    for n_em in range(0, 5):
        S = base + 0.15 * (4 - n_em)
        mult = 1 + 0.15 * n_em
        f1 = frac(v("reap_vuln") * S, 1.0, 1) * mult
        f9 = v("detonate_pct") * viral_mult(9) * mult
        o.append(f"| {4-n_em} Crimson tau + {n_em} Emeraude tau | {S*100:.0f} % | {f1:.3f} | {f9:.3f} | {min(0.35*S,0.95)*100:.1f} % | {S:.2f} |")
    o.append("A comparer : F1 (Roar, 4 Crimson tau) 1,075 sans aucun Viral, sur tout le rayon de Sow.")
    return "\n".join(o)


SECTIONS = {"summary": summary_report, "capacity": capacity_report, "nuke": nuke_report, "eximus": eximus_report,
            "claws": claws_report, "survival": survival_report, "energy": energy_report, "well": well_report,
            "clear": clear_report, "sensitivity": sensitivity_report, "formula": formula_report,
            "shards": shards_report, "tau": tau_sources_report, "range": range_report, "tiers": tiers_report,
            "huras": huras_report, "taubound": taubound_report, "blast": blast_report,
            "range3": range_v3_report, "entropic": entropic_report, "gloom": gloom_report, "seuil": threshold_v3_report,
            "circumvent": circumvent_report, "range4": range_v4_report, "seismic": seismic_report,
            "ruby": ruby_loop_report, "viral": viral_report, "entropic4": entropic_v4_report,
            "calc": calc_compare_report, "ruby_main": ruby_main_report, "emerald": emerald_report}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--section", choices=list(SECTIONS))
    ap.add_argument("--params", action="store_true")
    a = ap.parse_args()
    if a.params:
        for k, (val, src, lab) in P.items():
            print(f"{k:18s} {val!s:>8}  [{lab}] {src}")
    elif a.section:
        print(SECTIONS[a.section]())
    else:
        for f in SECTIONS.values():
            print(f())
            print()
