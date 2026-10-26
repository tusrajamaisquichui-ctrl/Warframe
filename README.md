# Warframe

Guides de theorycrafting endgame (Steel Path, Level Cap, Endurance).

## Builds

- [Protea Prime — Solo Level Cap / Endurance (v1.4)](builds/protea-prime-level-cap-endurance.md) · [version web](https://tusrajamaisquichui-ctrl.github.io/Warframe/) — Roar (Helminth), Arcane Sculptor, 2 Tauforged Crimson Strength, Torid Incarnon / Epitaph Prime / Glaive Prime (Update 44.1.3), en 3 blocs étanches :
  - [① Socle commun](builds/protea-prime-level-cap-endurance.md#bloc-1) — mods, shards, stats, économie d'énergie Sculptor + Equilibrium, survie de base (satellites posés par paires, Toxin en prévention)
  - [② Endurance standard](builds/protea-prime-level-cap-endurance.md#bloc-2) — Molt Augmented, Nautilus Prime + Verglas Prime, arsenal Viral
  - [③ Level Cap 9999](builds/protea-prime-level-cap-endurance.md#bloc-3) — Arcane Escapist, Panzer Vulpaphyla + Martyr Symbiosis, Torid Magnetic / Corrosive, Secondary Fortifier, Kuva Nukor, Vazarin, variante « ancre mobile » (Temporal Artillery)
  - [Audit hostile de la v1.0](builds/audit-protea-prime-v1.md) — 12 défauts relevés et corrigés, robustesse 4/10 → 6/10
  - [Audit hostile v2 (sur la v1.3)](builds/audit-protea-prime-v2.md) — contre-expertise : cadre solo (Icebind = 6 joueurs), satellites consommés par paires, Toxin sans réaction possible au cap, Untreatable et Manifold Bond réfutés, shards Crimson Strength > Duration ; robustesse réévaluée à 4/10, 16 tests à mener. Ses corrections sont intégrées dans la v1.4.

## Site web (lecture sur téléphone)

Le guide et ses deux audits sont publiés en pages statiques, sombres et pensées pour le mobile :

- onglets **Accueil · ① Socle · ② Endurance · ③ Level Cap · Annexes** (barre en bas de l'écran sur téléphone, en haut sur ordinateur) ;
- sommaire par onglet (bouton « Sommaire » sur téléphone, colonne fixe sur ordinateur), liens directs vers chaque section (`index.html#s3-12`) ;
- tableaux longs affichés en fiches sur téléphone ; renvois du type « cf. 1.11 » cliquables ; ajouts de la v1.4 signalés par un badge.

Adresse une fois GitHub Pages activé : **https://tusrajamaisquichui-ctrl.github.io/Warframe/**

### Activer la publication (une seule fois)

1. Le dépôt est **privé** : avec un compte GitHub Free, Pages ne publie que les dépôts publics. Il faut soit rendre le dépôt public (*Settings → General → Danger Zone → Change visibility*), soit un abonnement GitHub Pro. Dans les deux cas, le site lui‑même est public.
2. *Settings → Pages → Build and deployment* : **Source = Deploy from a branch**, branche **`main`** (une fois cette branche fusionnée, ou directement la branche de travail), dossier **`/docs`**, puis *Save*.
3. Après une à deux minutes, l'adresse s'affiche en haut de la page *Pages*.

Le dossier [`docs/`](docs/) contient tout le site : `index.html` (guide), `audit-v2.html`, `audit-v1.html`, `assets/` (CSS, JS, icône) et `.nojekyll` (fichiers servis tels quels).

### Mettre le site à jour après une modification du guide

Les fichiers Markdown de `builds/` restent la seule source : `docs/` est généré, on ne le modifie pas à la main.

```sh
python3 -m pip install -r tools/requirements.txt
python3 tools/build_site.py           # régénère docs/
python3 tools/build_site.py --check   # échoue si docs/ n'est plus à jour
```

Puis committer `builds/` et `docs/` ensemble.
