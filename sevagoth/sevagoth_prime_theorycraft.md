# Sevagoth Prime : theorycraft complet et auditable

**Version 1.0 du 29/10/2026.** Patch **Hotfix 44.1.4.1** (« Iceblade of Narin : The Icebind »), en ligne sur PSN depuis le 28/10/2026.
Modèle de calcul : [`sevagoth_model.py`](sevagoth_model.py). Sortie brute : [`model_output.txt`](model_output.txt). Paramètres et sources : [`model_params.txt`](model_params.txt).

Étiquettes : **CONF** = wiki officiel ou patch notes · **COMM** = communauté · **DÉD** = déduit par le modèle · **TEST** = à mesurer en jeu (tests T1 à T14, section 4).

---

## 1. Verdict

1. **Build retenu : F1 « Faucheuse invisible »** = Reap / Sow / Gloom / **Roar infusé à la place d'Exalted Shadow**, 273 % de Force dès le départ (one-shot à 1,08 des PV actuels, Gloom au plafond de 95 %), et un **Huras Kubrow** (invisibilité + Seismic Bond). L'Ombre n'est pas l'option la plus forte : le slot 4 rapporte plus en Roar.
2. **S1, Steel Path ~175 : F1.** F2 « Ombre Faucheuse » (Roar en 3, Ombre gardée) nettoie 7 % plus vite dans le modèle (21 % si le nuke ne traverse pas l'Overguard, test T1), mais elle est 17 fois plus exposée au tir direct. Écart de clear dans la marge d'erreur, donc F1.
3. **S2, endurance 500 puis 1000+ : F1, nettement.** Le nuke retire un pourcentage des PV, donc il ne faiblit pas avec le niveau. L'invisibilité du Huras couvre le tir direct, Gloom ralentit le trash de 95 %, et l'énergie tient dès ~20 kills/min.
4. **S3, level cap 9999 : F1 avec les swaps level cap** (Arcane Escapist, Vazarin, Rolling Guard). Sevagoth y nettoie le trash sans problème. Il reste limité par les Eximus (T1), les Nullifiers et la mort du compagnon. Viable, mais pas une référence de survie.
5. **À éviter :** jouer l'Ombre avec un compagnon d'invisibilité (Reunite casse l'invisibilité, CONF), Melee Duplicate sur les griffes (inutile au-delà de 200 % de chance critique), et Roar en slot 3 sur la même frame que F1 (un sort Helminth occupe le même slot dans toutes les configs, CONF).

---

## 2. Fiches builds prêtes à recopier

Conventions : polarités V = Vazarin, N = Naramon, M = Madurai, Z = Zenurik, U = Umbra, « - » = slot sans polarité. Coûts au rang max. Capacités vérifiées par `fit()` dans le script (section M2).

### F1 « Faucheuse invisible » (build principal, S1 à S3)

**Sevagoth Prime, config A**

| Slot | Mod | Polarité du slot | Coût |
|---|---|---|---|
| Aura | Brief Respite | Aura Forma (universelle) | +14 |
| Exilus | Power Drift | - | 9 |
| 1 | Shadow Haze (augment Reap) | - (Z conseillé) | 9 |
| 2 | Dark Propagation (augment Sow) | - (Z conseillé) | 9 |
| 3 | Umbral Intensify | U (Umbra Forma) | 8 |
| 4 | Augur Secrets | - | 7 |
| 5 | Intensify | - | 11 |
| 6 | Catalyzing Shields | V (innée) | 7 |
| 7 | Primed Continuity | M (innée) | 7 |
| 8 | Streamline | N (innée) | 5 |

- **Capacité : 72/74.** 2 Forma minimum (Aura Forma + Umbra Forma). 4 conseillées : ajouter Z sur les deux augments libère 8 points pour les swaps S3.
- **Helminth : Roar sur Exalted Shadow (slot 4).** Pourquoi : Roar multiplie le pourcentage du nuke sans amorce Viral. Le seuil CONF du wiki (255 % de Force avec Roar) est dépassé dès le départ (273 %). Alternative : garder Gloom + Ombre sans Helminth, c'est F3.
- **Variante Precision Intensify au slot 5** (+90 % sur le slot 4, donc sur Roar seul) : seuil ramené à 216,7 % (DÉD), 2e Reap 1,11 au lieu de 1,08, Roar ×2,00 au lieu de ×1,82 (+10 % sur les armes). Mais la Force générale retombe à 243 % : Gloom à 85 % tant que Molt n'est pas plein. Quasi équivalent ; Intensify est retenu parce qu'il ne dépend ni de Molt ni du test T3.
- **Arcanes :** Molt Augmented + Arcane Energize. En S3, remplacer Molt par Arcane Escapist.
- **Éclats :** 4 × Crimson tauforgé (+15 % Force chacun) + 1 × Amber tauforgé (orbes d'énergie +75 %). Alternative : Amber vitesse de lancement (+37,5 %).
- **Focus : Vazarin** (Protective Sling : 5 s d'invulnérabilité à la demande ; Mending Soul). Madurai n'apporte plus rien d'indispensable (le plafond de Gloom est atteint sans Sling Strength), et Zenurik ne régénère pas pendant Gloom (CONF).
- **Stats finales** (début de mission → Molt plein) : Force **273 % → 333 %**, Durée 155 %, Portée 100 %, Efficacité 130 % (160 % avec Seismic Bond pendant Gloom, donc coûts ×0,40). PV 370, boucliers 74 (Catalyzing), armure 185, énergie 225.
  - Roar ×1,82 → ×2,00, 46,5 s. Vulnérabilité de Reap +136 % → +166 %, 15,5 s. Ralentissement de Gloom **95 % (plafond) dès le départ**. Vol de vie Gloom 14 % → 17 %. Shadow Haze +136 % → +166 % de chance critique fixe.
  - Coûts sous Gloom : Reap 10, Sow 20, Roar 30, Gloom 20 + 1,94 énergie/s à 10 ennemis.
- **Compagnon : Huras Kubrow.** Stalk (invisibilité indéfinie tant qu'un ennemi est à moins de 24 m et qu'on ne tire pas ; le Kubrow peut attaquer sans casser le camouflage, CONF). Seismic Bond (+30 % d'efficacité pendant une compétence canalisée). Assassin Posture (cible les Eximus, +300 % de dégâts contre l'Overguard). Le reste en survie du compagnon (sa mort coupe l'invisibilité, test T4).
- **Armes :** Epitaph Prime (arme signature : +20 % de dégâts headshot pour Sevagoth Prime, CONF) avec Secondary Fortifier (×8 contre l'Overguard). Tir chargé : 1 tir retire l'Overguard d'un Heavy Gunner Eximus jusqu'au niveau 1000, 6 à 7 tirs au niveau 9999 (DÉD). Le tir non chargé (AoE, 50 % de statut) sert d'amorce Viral. En S2/S3, **ne pas tirer** sauf urgence : chaque tir casse l'invisibilité, puis 7 s de recharge (CONF).

**Ombre, config « Tombstone »** (utilisée seulement par le passif à la mort)

| Slot | Mod | Polarité |
|---|---|---|
| Aura | Steel Charge (+60 % mêlée, sert aux lourdes anti-Overguard) | M (innée), +18 |
| Exilus | aucun nécessaire (l'Ombre est déjà immunisée au knockdown, CONF) | - |
| Mods | Umbral Vitality, Umbral Fiber, Umbral Intensify (set de 3), Adaptation, Rolling Guard (effet sur l'Ombre : test T13), Vitality, Steel Fiber, Intensify | 3 Umbra Forma |

- **Capacité 73/78, 3 Forma.** PV +280 %, armure +280 % : **EHP 9 902** (contre 672 pour le corps). Arcanes : Arcane Fury + Arcane Reaper.
- **Variante 0 Forma :** retirer le set Umbral. L'EHP baisse, mais c'est un filet de secours, pas une config de jeu.

**Shadow Claws Prime, config Tombstone** : Primed Pressure Point, Condition Overload, Blood Rush, Organ Shatter, Primed Reach, Life Strike (+20 % de vol de vie sur lourde), Primed Fever Strike, North Wind. Exilus Discipline's Merit, arcane Melee Exposure. 66/70, 3 Forma. Rôle : retirer l'Overguard à la lourde pour pouvoir Consume (Consume ne cible pas l'Overguard, CONF).

**Rotation F1**
1. Entrée de zone : Roar, puis Gloom.
2. Par pack : **Reap → Sow → Reap**. Le premier Reap pose la vulnérabilité, le second déclenche Sow avec vulnérabilité : **1,08** des PV actuels au début, **1,33** avec Molt, soit la mort de tout ce qui n'a pas d'Overguard. Cet ordre ne dépend pas de la question « Sow est-il consommé par la détonation ? » (T6).
3. Les mini-Reap de Shadow Haze (jusqu'à 3, CONF) et la propagation de Sow (15 m) font la chaîne. On ramasse les orbes au passage.
4. Eximus : sous H1 (test T1), les deux mêmes Reap suffisent. Sous H0, 1 tir chargé d'Epitaph (S1/S2), ou on laisse faire l'Assassin Posture du Huras.
5. Roar à relancer toutes les 46,5 s. Gloom reste actif ; son ralentissement est figé au lancement (CONF), mais il est déjà au plafond, donc pas besoin de le relancer.

**Death Well en F1 :** sans objet (Exalted Shadow remplacé). Le passif reste actif (CONF). À la mort : Ombre Tombstone, 5 s d'invulnérabilité, **5 Consume** (gratuits, tuent tout non-boss sans Overguard) en 20 s. Une lourde des griffes sur un Eximus retire son Overguard.

---

### F2 « Ombre Faucheuse » (alternative S1, incompatible avec F1 sur la même frame)

**Sevagoth Prime**
- Helminth : **Roar sur Gloom (slot 3).** Alternative : Silence ou Eclipse (option de Ninjase, COMM).
- Aura Brief Respite (Aura Forma), Exilus Power Drift.
- Mods : Shadow Haze, Dark Propagation, Umbral Intensify [U], Augur Secrets, Intensify, Catalyzing Shields [V], Primed Continuity [M], Streamline [N].
- 72/74, 2 Forma.
- Force **273 % → 333 %**, Durée 155 %, Efficacité 130 %. Roar ×1,82 → ×2,00. 2e Reap : **1,08 → 1,33**.
- Mêmes mods que F1 : Roar en slot 3 ne profiterait de toute façon pas de Precision Intensify.
- Arcanes Molt Augmented + Arcane Energize. Éclats comme F1. Focus Madurai (Phoenix Talons : +30 % de dégâts physiques, s'applique aux armes exaltées, CONF).

**Ombre**
- Aura Brief Respite (Aura Forma), Exilus Power Drift.
- Mods : Preparation [Z], Transient Fortitude [M], Umbral Intensify [U], Umbral Fiber [U], Intensify [M], Catalyzing Shields [V], Adaptation [V], Rolling Guard.
- 70/74, **5 Forma**.
- Force **315 %** (éclats inclus, ils s'appliquent à l'Ombre, CONF) : Death's Harvest +158 %, 7,25 s. Armure 1 092 (DR 78,5 %), EHP 1 754. Énergie pleine à chaque invocation grâce à Preparation : 2 Death's Harvest, ou 1 DH + 3 Embrace.
- Arcanes : Arcane Fury (+180 % de dégâts de mêlée, s'applique aux griffes, CONF) + Arcane Reaper.

**Shadow Claws Prime**
- Primed Pressure Point, Condition Overload, Blood Rush, Organ Shatter, Primed Reach, Weeping Wounds, Primed Fever Strike, North Wind (Viral 255 %).
- Exilus **Discipline's Merit** : une opportunité Tennokai tous les 4 coups, c'est-à-dire une lourde qui ne consomme pas le combo.
- Arcane **Melee Exposure** : +60 % Corrosif par lancement, jusqu'à 240 % ; les sorts de l'Ombre devraient compter (T11).
- 68/70, 3 Forma.
- Base **682 → 832** (250 × Force de Sevagoth figée au lancement d'Exalted Shadow, CONF). Chance critique à 4x de combo : 220 %, à 12x : 342 %. Multiplicateur critique ×4,94. Portée 4,5 m.

**Rotation F2**
1. Corps : Roar → Reap → Sow → Reap. 8 kills « True » remplissent 75 % du puits (10 % par kill, CONF).
2. Exalted Shadow, 5 s d'invulnérabilité : **Embrace** (cône de 20 m, regroupe) → **Death's Harvest** (vulnérabilité + Sow grâce à Dark Propagation) → un coup de griffe sur une cible marquée → les mini-Reap déclenchent la chaîne à **1,17**.
3. Eximus : griffes en lourde Tennokai, environ 0,2 s à 0,7 s de S1 à S2 (« typique » du modèle).
4. Reunite ou mort de l'Ombre (sans pénalité, CONF) → retour au corps.
5. **Ne pas ramasser les orbes d'énergie avec l'Ombre** : elles vont à sa réserve (COMM).

### F3 « Sans Helminth » (config B possible sur la même frame que F1)

Même config Sevagoth que F1, mais Precision Intensify booste Exalted Shadow : griffes en base 832. Ombre et griffes identiques à F2. Compagnon : un fauve avec Seismic Bond (Gloom est canalisé). Amorce Viral obligatoire pour le nuke du corps (tir non chargé d'Epitaph). Sans amorce, le 2e Reap ne fait que **0,55**. F3 est compatible avec F1 parce qu'elle n'a pas d'infusion (CONF : chaque config peut avoir sa propre infusion ou aucune).

---

## 3. Liste de farm priorisée (build F1, puis ce qu'ajoutent F2/F3)

Prix : warframe.market, vendeurs « en jeu », crossplay, relevés le 29/10/2026 (médiane ; R = rang). **Raccourci limité dans le temps :** l'Epoch Operation : Taubound (Eris) tourne **jusqu'au 17/11/2026 et ne reviendra pas** (CONF). Praghasa y vend 1 Crimson, 1 Amber et 1 Azure tauforgés à 375 Moonflesh chacun (limite 1), ainsi que Melee Exposure et Secondary Fortifier à 8 Moonflesh l'unité (168 pour un rang max).

| Priorité | Pièce | Impact sur le build | Où (patch actuel) | Coût approx. | Substitut temporaire et perte |
|---|---|---|---|---|---|
| 1 | **Roar (Helminth)** | Sans lui, plus de one-shot sans amorce Viral | Faire absorber un Rhino par l'Helminth | Rhino + sécrétions | F3 avec amorce Viral : 2e Reap 0,55 sans amorce, 1,11 avec |
| 2 | **4 Crimson tauforgés (Force)** | Sans : 2e Reap 0,85 au début, 0,96 avec 2 éclats ; Gloom sous le plafond | Taubound (1 avant le 17/11), Archon Hunt hebdo (20 % tau avec pitié), Netracells, Deep/Temporal Archimedea, Descendia SP, coffres Icebind. Ascent Fusion : 3 normaux → 1 tau | 375 Moonflesh, ou des semaines | 4 Crimson normaux (+10 % chacun) : 2e Reap à 1,00 au début, au seuil après 5 kills de Molt ; Gloom 89 % |
| 3 | **Intensify** (4e mod de Force) | Sans : 2e Reap 0,96 au début, one-shot après ~46 kills de Molt | Drop de boss (2 %) ou échange | quelques p | Stretch à la place : Portée +45 %, mais pas de one-shot avant Molt |
| 4 | **Huras Kubrow + Seismic Bond + Assassin Posture** | Invisibilité (S2/S3) et +30 % d'efficacité. Sans Seismic : énergie −2,25/s à 60 kills/min (au lieu de +1,69) | Huras : œuf de Kubrow (Terre) + incubation aléatoire. Seismic Bond : Son (Entrati, rang 3, 20 000). Assassin Posture : The Business (Fortuna, 3+3+3 tags Kubrodon) | ~29 p (Seismic) | Shade (Ghost) : même invisibilité, mais pas de Seismic |
| 5 | **Shadow Haze / Dark Propagation** | Chaîne de mini-Reap et +136 à 166 % de chance critique pour les armes / propagation de Sow | Cephalon Suda ou Perrin Sequence, 25 000 standing chacun | ~20–25 p R3 | Aucun : ce sont les augments du kit |
| 6 | **Arcane Energize** | Moitié du revenu d'énergie | Capture de l'Hydrolyst, Orphix Veil Proxima rotation C | **~210 p R5** (le plus cher) | Amber orbe + Equilibrium : le seuil de tenue monte |
| 7 | **Molt Augmented** | +60 % de Force : 2e Reap 1,08 → 1,33 (marge) | Cavalero (Holdfasts rang 5, 10 000), Thrax/Void Angels 6,67 % | ~50 p R5 | Madurai Sling Strength (+40 %, 20 s) |
| 8 | **Catalyzing Shields, Brief Respite, Umbral Intensify, Primed Continuity, Augur Secrets, Power Drift** | Shield gating, Force, Durée | Coffre Derelict 4,17 % / Orphid Specter / Simaris 100 000 (non échangeable) / Baro / Thumpers 12,5 % / test Lua | 38 / 30 / – / **155** / 45 / 20 p | Intensify à la place d'Umbral Intensify (−14 %) ; Continuity simple (−25 % de Durée) |
| 9 | **Forma** | 2 sur Sevagoth (Aura + Umbra), 6 pour Ombre et griffes Tombstone | Aura Forma : Nightwave, plan en Arbitrations, marché ; Umbra Forma : Teshin (150 Steel Essence, toutes les 8 semaines), Nightwave | – | L'Ombre Tombstone en variante 0 Forma |
| 10 | **Epitaph Prime + Secondary Fortifier** | Retire l'Overguard si T1 donne H0 | Epitaph Prime vaulté (set ~37 p). Fortifier : Taubound, Ordis (Drifter), Nightcap, Ascension | ~37 p + ~50 p | Toute arme secondaire avec Fortifier |
| 11 | **Sevagoth Prime** | Frame elle-même | **Vaultée depuis l'U43** (17/06/2026), set ~50 p ; Prime Resurgence (rotation non vérifiée) | ~50 p | Sevagoth de base : stats moindres, mêmes calculs à ±10 % |

**En plus pour F2/F3 (Ombre de jeu et griffes) :** Precision Intensify pour F3 (~17 p, The Fragmented 20 %), Discipline's Merit (**~100 p R3**, Entrati Alchemy 6 %), Melee Exposure (Taubound ou Bird 3, ~70 p), Blood Rush (~94 p R10, Lua Spy 12 %), Primed Pressure Point / Primed Reach / Primed Fever Strike (Baro, 115–120 p), Weeping Wounds (~49 p, primes Necralisk), Condition Overload (~20 p), Transient Fortitude (~89 p), Preparation / Adaptation / Rolling Guard (vendeur Arbitrations, 30/20/20 Vitus), Umbral Fiber (Simaris), Arcane Fury (Hydrolyst), Arcane Reaper (Circuit SP), et 8 Forma de plus.

**Ordre conseillé :** Roar → éclats tauforgés (Taubound d'abord, avant le 17/11) → Huras + Seismic → augments → Energize → Molt → reste.

---

## 4. Chiffres clés, hypothèses, ce qui renverserait le verdict, tests

### Chiffres qui portent le verdict (sortie du script, section M1)

| Scénario | Build | Clear S1 (kills/min, H1/H0) | Eximus Heavy Gunner | Risque tir direct | Énergie nette |
|---|---|---|---|---|---|
| S1 SP175 | **F1** | 151 / 133 (×1,00) | 2 Reap (H1) ou 1 tir Epitaph (H0) | ×1,0 | +3,45/s à 60 kills/min |
| S1 SP175 | F2 | 161 / 161 (×1,07 / ×1,21) | griffes 0,17 s | ×17,6 | +1,57/s |
| S1 SP175 | F3 | 151 / 151 | griffes 0,15 s | ×2,7 | +4,09/s |
| S2b 1000 | **F1** | – | 2 Reap ou 1 tir | ×1,0 | +5,18/s à 90 kills/min |
| S2b 1000 | F2 | – | griffes 0,67 s | ×10,2 | +2,34/s |
| S2b 1000 | F3 | – | griffes 0,59 s | ×2,7 | +5,83/s |
| S3 9999 | **F1** | – | 2 Reap ou 6 tirs | ×1,0 | +2,39/s à 45 kills/min |
| S3 9999 | F2 | – | griffes 3,96 s | ×8,5 | +1,07/s |

Énergie calculée avec l'éclat Amber orbe de F1. L'indice de risque est **relatif** : seul l'ordre de grandeur compte (hypothèses TEST en M6).

**Cinq chiffres à retenir**
- Nuke : 2e Reap = **1,08** des PV actuels au début (F1), **1,33** avec Molt. Seuil CONF 255 % de Force avec Roar, atteint à 273 %.
- Eximus Heavy Gunner SP175 : **1,93 M PV + 324 k Overguard**. Niveau 1000 : 6,9 M + 1,56 M. Niveau 9999 : 36,6 M + 12,4 M (CONF, formules du wiki).
- Une balle de Heavy Gunner : **175** dégâts au niveau 175, **2 655** au niveau 1000, **94 969** au niveau 9999. Une seule balle tue le corps (EHP 672) dès le niveau **415**, et l'Ombre de F2 (EHP 1 754) dès le niveau **767** (CONF formules, DÉD application).
- Énergie F1 : tient dès **~20 kills/min** avec l'éclat Amber orbe, ~27 sans (DÉD, sensible à la taille des packs).
- Uptime de l'Ombre (F2/F3) : **77 % à 84 %** de 0,5 à 1 kill/s ; 8,3 s pour 0 → 75 % à 1 kill/s (DÉD).

### Hypothèses principales
- Taille de pack 15 kills par rotation (TEST). À 8 kills, F1 passe à −0,65/s : relancer Sow moins souvent ou couper Gloom hors combat.
- Animation 0,9 s par sort, NON TROUVÉE. Mesure : chronométrer 10 lancements de Reap en Simulacrum (vidéo, compter les images).
- Orbes : 9,4 % par kill, échantillon de 159 kills cité par le wiki (COMM). Mesure : compter sur 200 kills en SP.
- Tir direct : 4 à 5 tireurs trash et 0,5 à 2 Eximus actifs, 2 coups/s (TEST). Seuls les ratios entre builds sont utilisés.

### Ce qui renverserait le verdict
- **Le Huras (ou Shade) meurt trop vite au niveau 1000+**, ou Stalk ne tient pas avec Sevagoth (T4). F1 perd alors sa couche principale : F3 (Gloom + Ombre) passe devant en S2/S3 (risque ×2,7 seulement, et l'Ombre comme couche active).
- **H0 au test T1 et Epitaph trop lent au level cap** (6 à 7 tirs, invisibilité cassée) : en S3, F2/F3 (griffes) deviennent l'outil anti-Eximus, mais restent beaucoup plus exposés.
- **Gloom ne ralentit pas la cadence de tir** (T5) : l'avantage de F1/F3 sur F2 en S1 se réduit (l'invisibilité de F1 reste).
- **Clear S1 : F2 mesuré à plus de 15 % au-dessus de F1** (T7) : F2 devient le meilleur build S1, sur un Sevagoth séparé à cause de la contrainte de slot Helminth.

### Tests en jeu
| # | Question | Mise en place | Mesure | Confirme / infirme |
|---|---|---|---|---|
| T1 | Le True 25 % traverse-t-il l'Overguard ? | SP, Heavy Gunner Eximus seul ; F1 : Reap → Sow → Reap | Barres OG et PV après chaque Reap, 10 essais | H1 : OG vidée et PV entamés au 2e Reap, mort en ≤ 2. H0 : OG seule touchée, PV intacts |
| T2 | La vulnérabilité de Death's Harvest et de Reap s'applique-t-elle à l'OG ? | Simulacrum, Eximus, griffes sans combo | Chiffres de dégâts sur OG avec et sans DH | ≈×2,6 avec DH : oui. ×1 : non (griffes ×0,60 en M10) |
| T3 | (variante Precision) Precision Intensify booste-t-il Roar en slot 4 ? | Arsenal, puis mission | Valeur du buff Roar dans le HUD | ≈+100 % : la variante tient (1,11). ≈+73 % : rester sur Intensify |
| T4 | Stalk tient-il pendant Reap/Sow/Gloom/Roar, et le Huras survit-il ? | SP niveau 500+, 5 min sans tirer | Ruptures d'invisibilité et morts du Kubrow | 0 rupture : F1 confirmé. Ruptures fréquentes : voir « renverserait » |
| T5 | Gloom à 95 % ralentit-il la cadence de tir ? | Simulacrum, Heavy Gunner, Gloom on/off | Balles par 5 s | Division ≈20 : oui |
| T6 | Sow survit-il à une détonation ? | Sow → Reap → Reap sans relancer Sow | Deux détonations ou une | Deux : Sow → Reap → Reap possible. Une : garder Reap → Sow → Reap |
| T7 | Clear réel F1 contre F2 | Même nœud SP survival, 10 min chacun, 3 fois | kills/min de fin de mission | Écart supérieur à 15 % en faveur de F2 : F2 pour S1 |
| T8 | Tenue d'énergie F1 | SP survival, 20 min, Gloom permanent | Courbe d'énergie toutes les 2 min | Stable ou en hausse au-dessus de 20 kills/min : modèle confirmé |
| T9 | Roar du corps sur les griffes et sur le nuke de l'Ombre | F2, buff Roar actif | Dégâts des griffes avec et sans Roar ; détonation par mini-Reap | COMM : griffes non, nuke oui |
| T10 | Le Tombstone coûte-t-il un revive ? Molt est-il réinitialisé ? | Solo, 5 morts contrôlées | Compteur de revives, stacks de Molt | DE (2023) : pas de revive consommé. À revérifier sur le patch 44 |
| T11 | Melee Exposure se charge-t-il avec les sorts de l'Ombre ? | F2, Embrace et DH | Buff +60 % par lancement | Oui : modèle tel quel. Non : griffes ×0,58 |
| T12 | Precision Intensify (F3) augmente-t-il la base des griffes ? | F3, Arsenal des griffes ou chiffres en mission | Base 832 ou 607 au début | Non : retirer Precision de F3 |
| T13 | Rolling Guard fonctionne-t-il sur l'Ombre ? Un Mercy casse-t-il Stalk (Escapist en S3) ? | Esquive en Ombre ; Mercy sur Eximus | Icône d'invulnérabilité ; état du camouflage | Non : swap Adaptation/Vitality ; Escapist seulement hors invisibilité |
| T14 | Blood Rush et Weeping Wounds s'équipent-ils sur Shadow Claws Prime ? | Arsenal, onglet griffes | Le mod se pose-t-il, et la chance critique monte-t-elle avec le combo ? | Oui (patch 38.5) : build tel quel. Non : Gladiator Might + True Steel à la place, griffes nettement plus faibles |

---

## 5. Étape 0 : état du jeu (vérifié le 29/10/2026)

**Patch actuel :** Hotfix **44.1.4.1** du 28/10/2026, publié sur PSN (page officielle warframe.com/patch-notes/psn, CONF). Update 44 « Iceblade of Narin » le 23/09/2026 sur toutes les plateformes, dont PS5 (CONF). 44.1 « The Icebind » le 07/10/2026. Événement en cours : Epoch Operation : Taubound, du 15/10 au 17/11/2026 (CONF).

**Sevagoth Prime :** sorti le 21/08/2024 (U36.1). **Vaulté avec Epitaph Prime et Nautilus Prime à l'U43** (17/06/2026, CONF).

### Changements depuis août 2024 qui touchent ce build
Aucun rework, buff ou nerf chiffré de Sevagoth depuis sa Prime. L'historique ne contient que des corrections (CONF, wiki Sevagoth/Patch History). Avant la Prime, l'U36 (juin 2024) avait ajouté Dark Propagation et rendu Sow relançable.

| Patch (date) | Changement | Effet sur le build |
|---|---|---|
| 36.1 (21/08/2024) | Sevagoth Prime ; l'Ombre regagne ses 5 s d'invulnérabilité à chaque invocation (correctif) | Base des cycles d'invulnérabilité de F2/F3 |
| 37 (02/10/2024) | Rework des compagnons : **Assassin Posture** +300 % contre l'Overguard ; vulnérabilités de certaines compétences étendues aux boucliers et à l'OG (pas Reap/DH) ; un seul sort Helminth de bonus de dégâts (Roar ou Xata) | Huras anti-OG ; T2 reste ouvert |
| 38 (13/12/2024) | Nouveaux arcanes (Crepuscular, Bellicose, Impetus, Melee Doughty…) | Crepuscular : option +30 % de Force invisible |
| **38.5 (19/03/2025)** | **Armes exaltées :** slot d'arcane, **mods Acolyte/combo (Blood Rush, Weeping Wounds, Body Count…) autorisés**, bonus de set calculés sur l'arme active, la stance donne de la capacité (Zenurik, +10) ; Arcane Escapist ; Hot Shot et Universal Fallout sur les statuts exaltés (38.5.2) | Rend les griffes viables (le Fandom et l'Overframe d'avant 2025 sont périmés sur ce point) |
| 38.6 (21/05/2025) | Retrait d'éclats : sécrétion propre à chaque couleur, 15 % (tau 30 %) | Coût de re-socket |
| 39.0.7 (été 2025) | Power Spike de Naramon corrigé sur les Shadow Claws | Naramon possible pour un build griffes |
| 40 (15/10/2025) | Refonte de l'atténuation de dégâts : proportionnelle aux PV max ; **Acolytes one-shotables** ; 40.0.3 : armure de l'Ombre Prime corrigée | Acolytes : le nuke % peut les toucher (à vérifier) |
| 41 (10/12/2025) | Tauron Strikes (Focus), arcanes Expertise / Persistence / Concentration, Descendia | Concentration : piège avec Sow (voir synergies) |
| 42 (25/03/2026) | Rework des Arctic Eximus (Froid en bulle) ; mods compagnon (Medi-Ray, Guardian…) enfin actifs sur l'Ombre | – |
| 43 (17/06/2026) | Vault de Sevagoth Prime ; **Surge Eximus** ; Steel Path Railjack ; **Molt Augmented se charge enfin pendant les passifs de mort** ; plus de mods compagnon actifs sur l'Ombre | Molt fiable en Tombstone |
| 44 / 44.1 (sept.–oct. 2026) | Entropic Eximus (Zariman), splicing de Rivens ; correctifs Sevagoth (Specter, Ombre absente de l'Arsenal) | Aucun effet chiffré |

Conflit de sources noté : le module `Mods/data` du wiki liste encore Blood Rush comme incompatible avec les armes exaltées (`POWER_WEAPON`). Les patch notes 38.5 l'emportent (règle « patch notes > wiki »), et la page wiki Exalted Weapon les reprend. Vérifier en Arsenal (T14).

---

## 6. Étape 1 : le kit décortiqué

### Sevagoth (valeurs au rang 3, CONF wiki)
| Compétence | Effet | Base | Modifiée par | Figé au lancement |
|---|---|---|---|---|
| **Reap** (25) | Ombre volante (6 s, 8 m de rayon) : 250 Radiation + **vulnérabilité 50 %**, 10 s | 250 / 50 % / 10 s / 8 m | Force (dégâts, vuln), Durée (vol, debuff), Portée | Vuln non rafraîchissable tant qu'elle n'a pas expiré ; une seule fois par cible et par Reap ; partage le debuff avec Death's Harvest |
| **Sow** (50) | Graine : 250 True/s pendant 10 s, falloff jusqu'à 25 % ; **Reap sur cible Sow : 25 % des PV actuels en True, puis vuln, puis 25 % en Blast (4 m) sur les voisins** | 250/s, 16 m | Force (DoT), Durée, Portée | Ne remplace un Sow existant que si la nouvelle durée est plus longue |
| **Gloom** (50 + 0,75/s par ennemi, 10 max) | Aura qui s'étend jusqu'à 16 m : **ralentissement 35 %** (plafond 95 % à 272 %), **vol de vie 5 %** (armes et compétences), puits +0,1 %/s par ennemi | – | Force, Portée, Durée (vitesse d'expansion, drain) | **Ralentissement figé au lancement** ; drain recalculé en continu ; n'affecte pas l'Overguard, les Eidolons, les Archons |
| **Exalted Shadow** (puits ≥ 75 %) | Contrôle de l'Ombre ; corps invulnérable et inciblable ; 1 %/s | 5 s d'invulnérabilité, propulsion de 5 m | Force de Sevagoth → base des griffes | Base des griffes figée à l'invocation |

### L'Ombre
| Compétence | Effet | Base | Modifiée par |
|---|---|---|---|
| **Embrace** (25) | Cône de 80° sur 20 m : ragdoll et regroupement 8 s | 20 m / 8 s | Portée, Durée |
| **Consume** (25) | Ruée sur une cible (14 m) : 2 500 Radiation, soin de 25 % des dégâts initiaux (fixe) | – | Force, Portée ; ne cible pas l'Overguard |
| **Death's Harvest** (75) | Vulnérabilité 50 % sur 12 m pendant 10 s (même debuff que Reap) ; avec Dark Propagation, applique aussi Sow | 50 % / 12 m / 10 s | **Force et Durée de l'Ombre** ; Shadow Haze et la propagation utilisent les stats de Sevagoth |
| **Reunite** | Retour au corps (téléportation illimitée) ; soigne 1 % des PV max par % de puits drainé | – | – |

**Death Well (CONF) :** +5 % par ennemi affecté (Reap, Sow, Death's Harvest) puis tué, **+5 % de plus** si le kill vient du Radiation de Reap ou du True boosté à 100 %, et +0,1 %/s par ennemi vivant dans Gloom. **Il ne se remplit que quand on contrôle Sevagoth.** Il se vide de 1 %/s en Ombre, et Reunite arrête le drain. Vitesse réelle (DÉD, M8) : 0 → 75 % en 8,3 s à 1 kill/s, 41,7 s à 0,2 kill/s. Un puits à 100 % permet 6 invocations d'affilée de 5 s.

**Passif (CONF) :** à la mort, tombeau et Ombre (5 s d'invulnérabilité, puis vulnérable ; immunisée au knockdown). 5 âmes à collecter avec Consume (0 énergie, tue tout non-boss sans Overguard) en 20 s, 34,4 s avec Undying Will. Les kills des griffes ne comptent pas. Mourir en Ombre en solo coupe le bleedout et tue Sevagoth. Ne fonctionne pas en Arbitrations. Pas de revive consommé selon le guide officiel de DE (24/11/2023 ; à revérifier, T10). **Le fiabiliser :** config Ombre Tombstone (EHP 9 902), griffes en lourde contre l'Overguard, Huras Assassin Posture.

**Ce que l'Ombre hérite (CONF) :** les éclats d'Archonte de Sevagoth (et ses griffes), son école de Focus, les Invigorations Helminth, et la Force de Sevagoth (base des griffes, y compris le bonus de Force des Arbitrations). **Ce qu'elle n'hérite pas :** mods, arcanes et armes de Sevagoth ; Roar (COMM). Elle a sa propre config : aura (active seulement en Ombre ou en Tombstone, et elle coupe celle du corps), exilus, 8 mods, 2 arcanes, Reactor préinstallé. Ses sorts ne peuvent pas être remplacés par l'Helminth.

**Ce qui tue l'Ombre :** les balles (EHP 1 754 en F2 : 10 balles au niveau 175, 2 au niveau 500, **one-shot dès le niveau 767**), les bulles de Nullifier (15 % des PV max toutes les 0,5 s, donc environ 3,5 s), le Toxin qui ignore les boucliers.

**Shadow Claws Prime (CONF) :** base 250 (I 30 / P 20 / S 50) × Force de Sevagoth, 38 % de chance critique, ×2,6, 24 % de statut, portée 1,5 m, lourde 1 000, 3 polarités M, stance Ravenous Wraith (le combo Block fait 2 000 % en 12 coups et 2,4 s, c'est le meilleur). Leviers : Steel Charge et Arcane Fury équipés sur l'Ombre (CONF), mods de combo (U38.5), Phoenix Talons, Shadow Haze, vulnérabilité de DH, Condition Overload. Pas de Riven.

### Augments : gain chiffré contre le coût d'un slot
- **Shadow Haze** (9 de capacité) : **+136 % → +166 %** de chance critique fixe pour toutes les armes en F1 (Force 273 → 333 %), plus 3 mini-Reap qui relancent la chaîne. Griffes sans lui : TTK ×2,27 (M10). **Indispensable.**
- **Dark Propagation** (9) : propage Sow sur 15 m à la mort, et **Death's Harvest pose Sow**. En F2/F3, sans lui il n'y a pas de nuke en phase Ombre. En F1, il évite des relances de Sow (20 d'énergie) ; gain non chiffré (DÉD). **Indispensable en F2/F3, swap possible en F1 S3** (contre Rolling Guard).

### Synergies et anti-synergies non évidentes
- **Precision Intensify booste n'importe quel sort du slot 4** (CONF, astuce Gloom du wiki) : avec Roar en 4, le seuil passe de 255 % à 216,7 % (DÉD). C'est un faux gain face à Intensify : 1,11 contre 1,08 au 2e Reap, mais Gloom perd 10 points de ralentissement sans Molt.
- **Un sort Helminth occupe le même slot dans toutes les configs** (CONF) : F1 (Roar en 4) et F2 (Roar en 3) ne peuvent pas coexister sur un même Sevagoth Prime. F3 (sans infusion) peut être la config B de F1.
- **Reunite casse l'invisibilité de Shade et du Huras**, les attaques des griffes aussi (CONF), puis 7 s de recharge : l'invisibilité ne sert qu'à un Sevagoth sans Ombre (F1).
- **Le Huras peut attaquer sans casser le camouflage** (CONF) : c'est ce qui permet d'avoir à la fois l'invisibilité et Seismic Bond.
- **Melee Duplicate ne double que les crits jaunes** (CONF) : avec Shadow Haze, les griffes dépassent 200 % de chance critique, donc l'arcane est inutile.
- **Le Death Well ne se remplit pas en Ombre** (CONF), et les orbes ramassées par l'Ombre vont à sa réserve (COMM).
- **Molt Augmented sur l'Ombre se perd à sa mort** (CONF) : le mettre sur Sevagoth uniquement.
- **Reap et Death's Harvest partagent le même debuff** (CONF) : en F2, ne pas superposer les deux sur un même groupe.
- **Arcane Concentration est un piège pour Sow** (CONF) : un Sow lancé sous Concentration bloque les relances suivantes plus courtes.
- **Le Blast de la détonation** (25 % des PV avant détonation × vuln × Roar, sans armure sur l'OG) entame l'Overguard des Eximus voisins (DÉD).
- **Zenurik ne régénère pas pendant une compétence canalisée** (CONF) : Energy Pulse et Wellspring sont inutiles avec Gloom.
- **Un Nullifier qui touche le corps coupe Exalted Shadow**, et la bulle détruit l'Ombre de Reap (CONF).

---

## 7. Étape 2 : scénarios (fixés pour toutes les comparaisons)
- **S1 :** Steel Path standard, ennemis niveau ~175 (+100 de SP inclus). Factions mixtes. Référence : Grineer (Heavy Gunner, armure 500 → 2 700 plafonnée), et Corpus / Infesté pour vérifier.
- **S2 :** endurance SP, niveaux 500 puis 1 000+.
- **S3 :** level cap 9 999. Le nuke en pourcentage y fonctionne ; c'est la survie qui décide.
- **Métriques :** vitesse de clear (kills/min, M9), TTK sur Heavy Gunner et Heavy Gunner Eximus (M4, M5), EHP réel et indice de risque au tir direct (M6), énergie nette par seconde (M7), uptime de l'Ombre (M8). La base ×1,00 est F1.

---

## 8. Étape 3 : archétypes

| Archétype | Source | Verdict |
|---|---|---|
| **A. Nuke Roar sur le 4 (Reap/Sow/Gloom/Roar)** | COMM : Ninjase « Gloom Reaper », 1 531 votes, et variante invisible (vidéo de mai 2026, contenu non vérifié) | **Finaliste → F1** (+ Huras/Seismic, DÉD) |
| **B. Ombre nukeuse avec Roar sur Gloom** | COMM : Ninjase « Shadow Realm » (536 votes), RubyBlossom5 « Ravenous Alliance » (19 votes) | **Finaliste → F2** |
| **C. Sans Helminth, Gloom + Ombre** | COMM : RubyBlossom5 « The Reaper's Bible », 98 votes, mise à jour le 22/10/2026 | **Finaliste → F3** |
| D. Griffes pures (Ombre en mêlée permanente) | – | Éliminé : un seul cible à 4,5 m, battu au clear par tout nuke ; reste un outil anti-Eximus de F2/F3 |
| E. Gloom tank / plateforme d'armes | – | Éliminé : le nuke en pourcentage fait mieux à tout niveau ; Gloom est une couche, pas un archétype |
| F. Helminth Nourish / Silence / Eclipse / Jade Stars | COMM (Ninjase) | Éliminé : Nourish ne pose pas de Viral via les compétences ; Silence et Eclipse ne lèvent pas le seuil ; Jade Stars demande la ligne de vue (U43) |
| G. Sevagoth donneur de Gloom | – | Hors sujet (une ligne à la fin) |

Comparaison ×1,00 sur S1/S2/S3 : section 4 (tableau M1). F2 gagne 7 à 21 % au clear S1 ; F1 gagne la survie partout (×8 à ×18 contre F2, ×2,7 contre F3) et l'énergie contre F2. F3 n'a l'avantage nulle part sauf l'absence d'Helminth.

---

## 9. Étape 5 : modélisation (résumé, détail dans `model_output.txt`)

- **Pipeline du nuke :** 0,25 × (1 + vuln posée avant le coup) × Roar × Viral (×2 à ×4,25). Il reproduit exactement les seuils CONF du wiki : 200 % de Force avec 1 Viral → 1,000 ; 255 % avec Roar → 1,004.
- **Pipeline des griffes :** base × Force → Phoenix Talons → dégâts additifs (Primed Pressure Point, Condition Overload, Arcane Fury) → éléments (Viral 255 %, Corrosif Exposure) → crit (Blood Rush, Shadow Haze, Organ Shatter) → combo (lourde) → vuln DH → faction (Grineer : Impact et Corrosif +50 %) → armure (0,9 × √(A/2700), Corrosif −80 %) → Viral → Slash (35 % × 6 ticks, ignore l'armure).
  - Plancher : cible fraîche, pas de vuln sur l'OG. Typique : statuts à moitié. Plafond : tout empilé.
  - S1 : plancher 1,9 s, typique 0,17 s, plafond 0,02 s.
- **Ennemis :** formules exactes du wiki (deux courbes et smoothstep, ×2,5 PV en SP, armure plafonnée à 2 700, Overguard 12 × courbe).
- **Survie :** EHP = PV / (1 − A / (A + 300)) + boucliers ; dégâts Grineer à double courbe ; indice de risque = tireurs × (1 − ralentissement) × coups/s × part touchable.
- **Énergie :** coûts × max(2 − efficacité, 0,25), drain de Gloom × max((2 − eff) / durée, 0,25) (CONF) ; Energize modélisé en processus de Poisson.
- **Sensibilité (M10) :**
  - Le levier n°1 du nuke F1 est le **4e mod de Force** : Intensify ou Precision donnent 1,08 à 1,11, contre 0,96 sans. Viennent ensuite les éclats (+0,06 par éclat).
  - Pour les griffes : Shadow Haze (×2,27), Melee Exposure chargé (×1,7), vuln de DH sur l'OG (×1,67).
  - Pour l'énergie F1 : Streamline (+3,9/s) et la taille des packs.
  - **L'hypothèse qui renverse le plus : la survie du compagnon (T4).**

---

## 10. Audit hostile : les 5 points les plus fragiles, revérifiés

1. **« Blood Rush et Weeping Wounds marchent sur les griffes. »** Le Fandom, des guides de 2024 et le module `Mods/data` disent non. Revérifié : patch notes 38.5 (wiki Update 38 et page Exalted Weapon) : **autorisés**. Verdict maintenu, données du module signalées comme périmées, contrôle en Arsenal ajouté.
2. **« 255 % de Force avec Roar = one-shot. »** Revérifié (wiki Reap) : la vulnérabilité est posée **après** le True du même coup, donc le premier Reap ne fait que 0,50. **Corrigé :** rotation Reap → Sow → Reap, qui ne dépend plus de la persistance de Sow (T6) ; le one-shot se compte sur le 2e Reap (1,08 pour F1).
3. **« Shade = invisibilité gratuite pour toutes les variantes. »** Revérifié (page Ghost) : Reunite et les attaques des griffes cassent l'invisibilité. **Corrigé :** l'invisibilité est réservée à F1, et le compagnon passe de Shade à **Huras** (Stalk identique, il attaque sans casser le camouflage, et comme c'est un fauve il porte Seismic Bond). Énergie F1 : −2,25/s → **+1,69/s** à 60 kills/min.
4. **« On peut avoir F1 et F2 sur la même frame. »** Revérifié (page Helminth) : une capacité infusée occupe **le même slot dans toutes les configs**. **Corrigé :** F1 et F2 sont exclusives ; F3 devient la config B compatible.
5. **« Precision Intensify est le meilleur levier du nuke F1 (seuil 216,7 %). »** Revérifié en recalculant le substitut : **Intensify** (+30 % sur toutes les compétences) donne 1,08 au début au lieu de 1,11, et Gloom au plafond de 95 % dès le départ (85 % avec Precision). Le gain de Precision ne valait que 0,03 de marge. **Corrigé :** F1 passe sur Intensify (273 % de Force), Precision devient une variante, Focus Vazarin au lieu de Madurai.

Autres corrections du premier jet : le corps de F2 était à 243 % de Force (0,96, pas de one-shot au début) → Intensify ajouté (273 %, 1,08). L'énergie était négative pour les 3 builds (packs de 10, sans efficacité) → efficacité ajoutée, Rolling Guard du corps F2 remplacé par Streamline. Le TTK des griffes était présenté au plafond seulement → plancher et typique ajoutés.

---

## Sources (consultées le 29/10/2026 sauf mention)
- Wiki officiel : [Sevagoth/Prime](https://wiki.warframe.com/w/Sevagoth/Prime), [Sevagoth/Abilities](https://wiki.warframe.com/w/Sevagoth/Abilities), [Sevagoth/Patch History](https://wiki.warframe.com/w/Sevagoth/Patch_History), [Reap](https://wiki.warframe.com/w/Reap), [Sow](https://wiki.warframe.com/w/Sow), [Gloom](https://wiki.warframe.com/w/Gloom), [Exalted Shadow](https://wiki.warframe.com/w/Exalted_Shadow), [Death's Harvest](https://wiki.warframe.com/w/Death%27s_Harvest), [Shadow Haze](https://wiki.warframe.com/w/Shadow_Haze), [Dark Propagation](https://wiki.warframe.com/w/Dark_Propagation), [Shadow Claws](https://wiki.warframe.com/w/Shadow_Claws), [Exalted Weapon](https://wiki.warframe.com/w/Exalted_Weapon), [Enemy Level Scaling](https://wiki.warframe.com/w/Enemy_Level_Scaling), [The Steel Path](https://wiki.warframe.com/w/The_Steel_Path), [Overguard](https://wiki.warframe.com/w/Overguard), [Armor](https://wiki.warframe.com/w/Armor), [Archon Shard](https://wiki.warframe.com/w/Archon_Shard), [Helminth](https://wiki.warframe.com/w/Helminth), [Roar](https://wiki.warframe.com/w/Roar), [Ghost](https://wiki.warframe.com/w/Ghost), [Stalk](https://wiki.warframe.com/w/Stalk), [Blood Rush](https://wiki.warframe.com/w/Blood_Rush), [Melee Combo](https://wiki.warframe.com/w/Melee_Combo), [Damage Reduction](https://wiki.warframe.com/w/Damage_Reduction), [Update 38](https://wiki.warframe.com/w/Update_38) à [Update 44](https://wiki.warframe.com/w/Update_44), [Epoch Operation : Taubound](https://wiki.warframe.com/w/Epoch_Operation:_Taubound), modules Lua `Warframes/data`, `Weapons/data`, `Mods/data`, `Arcane/data`, `Stances/data`, `Enemies/data`, `DropTables/data`, `Version/data`.
- Patch notes officielles : [warframe.com, PSN](https://www.warframe.com/patch-notes/psn) (Hotfix 44.1.4 + 4.1, 28/10/2026) ; [RPG Site, sortie d'Iceblade of Narin sur toutes les plateformes](https://www.rpgsite.net/news/21459-warframe-iceblade-of-narin-update-download-free-login-bonus) ; [DE, How to Play Sevagoth](https://www.warframe.com/en/news/how-to-play-sevagoth) (24/11/2023).
- Communauté : [Ninjase, Gloom Reaper Sevagoth](https://overframe.gg/build/717054/sevagoth-prime/gloom-reaper-sevagoth-sp-general-use-nuke-crit-buff-slow-shadow/) (1 531 votes, mise à jour il y a ~10 mois) ; [copie de « Shadow Realm Sevagoth »](https://overframe.gg/build/885203/sevagoth-prime/shadow-realm-sevagoth-pure-nuke-oneshot-levelcap-variant/) (original : 536 votes) ; [RubyBlossom5, The Reaper's Bible](https://overframe.gg/build/874263/sevagoth-prime/go-to-sevagoth-shadow-claws-blossoming-death-in-depth-build/) (98 votes, 22/10/2026) ; [RubyBlossom5, A Ravenous Alliance](https://overframe.gg/build/874330/sevagoth-prime/a-ravenous-alliance-sevagoth-shadow-nuke-partners-roar-build-guide-and-variants/) (19 votes, ~2 mois) ; [gameplay.tips](https://gameplay.tips/guides/warframe-the-ultimate-sevagoth-guide.html) (29/09/2026) ; [togame.io](https://togame.io/a/warframe-sevagoth-prime-best-build-2026/) (non daté, faible confiance). Les vidéos YouTube citées n'ont pas été vues.
- Prix : [warframe.market](https://warframe.market) API v2, vendeurs en jeu, 29/10/2026.

*Hors sujet, une ligne :* un Sevagoth non-Prime peut porter F2 (Roar en 3) sans toucher au Roar en 4 de ton Prime.
