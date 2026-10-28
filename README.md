# Warframe

Guides de theorycrafting endgame (Steel Path, Level Cap).

## Builds

- [Protea Prime — Steel Path & Level Cap (v2.0)](builds/protea-prime-level-cap-endurance.md) · [version web](https://tusrajamaisquichui-ctrl.github.io/Warframe/) — deux configurations sur un seul kit : Grenade Fan / Blaze Artillery / Roar (Helminth, à la place de Dispensary) / Temporal Anchor. Communs aux deux : Arcane Sculptor, 3 Tauforged Crimson Strength + 2 Tauforged Amber Casting Speed, Zenurik, 6 Forma (Update 44, Hotfix 44.1.3).
  - [① Config Steel Path](builds/protea-prime-level-cap-endurance.md#steel-path) — tout le contenu Steel Path : Temporal Artillery (tourelle suiveuse), Primed Continuity, Molt Augmented, Nautilus Prime + Verglas Prime, Torid Viral / Epitaph Corrosive + Encumber / Glaive Viral
  - [② Config Level Cap](builds/protea-prime-level-cap-endurance.md#level-cap) — niveaux 1 000 à 9 999 en solo : Temporal Erosion (armure à zéro), Rolling Guard, Arcane Energize et « règle de l'ancre » pour l'énergie, Panzer Vulpaphyla + Martyr Symbiosis, Torid et Epitaph en Magnetic + Secondary Fortifier
  - [Mécaniques communes](builds/protea-prime-level-cap-endurance.md#mecaniques) — shield gate, satellites posés par paires, Toxin, Temporal Anchor (rembobinage, annulation, protection contre la mort), Roar et passif, énergie, multiplicateurs
  - [Analyse comparative 2026](builds/analyse-comparative-2026.md) — 28 builds de la communauté confrontés au guide ; c'est la base des choix de la v2.0
  - [Audit hostile v2 (sur la v1.3)](builds/audit-protea-prime-v2.md) — contre-expertise : cadre solo (Icebind = 6 joueurs), satellites consommés par paires, Toxin sans réaction possible au cap, shards Crimson Strength > Duration ; ses corrections sont intégrées depuis la v1.4
  - [Audit hostile de la v1.0](builds/audit-protea-prime-v1.md) — 12 défauts relevés et corrigés en v1.1

Rien n'a été mesuré en jeu : la liste des tests à faire est dans les annexes du guide.

## Site web (lecture sur téléphone)

Le guide, l'analyse et les deux audits sont publiés en pages statiques, sombres et pensées pour le mobile : **https://tusrajamaisquichui-ctrl.github.io/Warframe/**

- onglets **Accueil · ① Steel Path · ② Level Cap · Mécaniques · Annexes** (barre en bas de l'écran sur téléphone, en haut sur ordinateur) ;
- sommaire par onglet (bouton « Sommaire » sur téléphone, colonne fixe sur ordinateur) et liens directs vers chaque section (`index.html#s2-5`) ; les anciens liens de la v1.4 (`#bloc-1`, `#bloc-2`, `#bloc-3`) ouvrent l'onglet qui les remplace ;
- tableaux longs affichés en fiches sur téléphone ; renvois du type « (3.4) » cliquables, d'un onglet à l'autre.

### Publication (GitHub Pages)

*Settings → Pages → Build and deployment* : **Source = Deploy from a branch**, branche de travail (ou `main` une fois fusionnée), dossier **`/docs`**. Avec le dossier `/ (root)`, GitHub publie ce README à la place du site.

Le dossier [`docs/`](docs/) contient tout le site : `index.html` (guide), `analyse.html`, `audit-v2.html`, `audit-v1.html`, `assets/` (CSS, JS, icône) et `.nojekyll` (fichiers servis tels quels).

### Mettre le site à jour après une modification du guide

Les fichiers Markdown de `builds/` restent la seule source : `docs/` est généré, on ne le modifie pas à la main.

```sh
python3 -m pip install -r tools/requirements.txt
python3 tools/build_site.py           # régénère docs/
python3 tools/build_site.py --check   # échoue si docs/ n'est plus à jour
```

Puis committer `builds/` et `docs/` ensemble.
