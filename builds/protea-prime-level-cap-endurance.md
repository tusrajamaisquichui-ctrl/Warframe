# Protea Prime — Solo Level Cap / Endurance (build BiS)

> **Version 1.2** : croisement avec deux vidéos d'octobre 2026 (SyrexLeon Gaming, RexChamp Sean) : variante « ancre mobile » avec Temporal Artillery (1.11), couches de survie Secondary Fortifier + Vazarin (1.12), arsenal alternatif (2.4). La v1.1 intégrait les 12 corrections de l'audit hostile [`audit-protea-prime-v1.md`](audit-protea-prime-v1.md). Journal en fin de document.
> **Patch de référence : Update 44 « Iceblade of Narin » / Hotfix 44.1.3 (22/10/2026).**
> Toutes les valeurs ci‑dessous (compétences, mods, arcanes, shards, armes) ont été vérifiées sur le wiki officiel (`wiki.warframe.com`) au 25/10/2026, y compris les modules de données (mods, armes, compagnons). Les calculs sont faits à partir de ces valeurs brutes.
> Changements récents qui impactent ce build : **Arcane Sculptor** (U43), **retrait des dispositions de Riven** (toutes à l'équivalent 1.2, H44.1.3), **cap d'Ammo Efficiency à 75 %** (H44.1.3), conversion « On Headshot » → « On Weak Point » (U44).
> **Limite de la v1.2** : les deux vidéos n'ont pas pu être visionnées depuis l'environnement de rédaction (accès YouTube bloqué). Les choix évalués sont ceux qu'elles mettent en avant (Temporal Artillery, Phantasma Prime, Kuva Nukor, Hate, Secondary Fortifier, Vazarin), et chaque mécanique a été revérifiée sur le wiki. Leurs listes de mods exactes ne sont pas reprises.

---

## 0. Fiche récap (à garder sous les yeux)

| Élément | Choix |
|---|---|
| Warframe | **Protea Prime** (Protea standard : build identique, +1 Forma) |
| Helminth | **Roar** à la place de Temporal Anchor — **variante C** (level cap) : Roar à la place de **Dispensary**, Temporal Anchor + **Temporal Artillery** (cf. 1.11) |
| Aura / Exilus | **Growing Power** / **Primed Sure Footed** |
| 8 mods | Archon Vitality, Blind Rage, Umbral Intensify, Primed Continuity, Narrow Minded, Stretch, Rolling Guard, Equilibrium |
| Arcanes | **Arcane Sculptor** + **Arcane Escapist** (level cap 9999) / **Molt Augmented** (Endurance hors cap) |
| Archon Shards | 3× Tauforged Azure (Shield Capacity) + 2× Tauforged Crimson (Ability Duration) — variante cap : 1 Crimson → 1 Tauforged Amber (Casting Speed) |
| Stats (Arsenal) | Strength **243 %** · Duration **284 %** · Range **79 %** · Efficiency **45 %** (verrouillée à **175 %** en mission par Sculptor) |
| Survie | Shields **1 230** (gate **2,5 s garanti**) · Health **740** · Armor 185 · Energy 250 |
| Primary | **Torid Incarnon** — Primary Merciless — Evo : Final Fusillade / Swift Deliverance / Commodore's Fortune |
| Secondary | **Epitaph Prime** (primer Corrosive) — Secondary Encumber (Endurance) / **Secondary Fortifier** (level cap, cf. 1.12) |
| Melee | **Glaive Prime** (heavy detonation, Viral) — Melee Duplicate |
| Compagnon | **A :** Nautilus Prime + Verglas Prime (Endurance, contrôle) · **B :** Panzer Vulpaphyla (**obligatoire au 9999**) |
| Focus | **Vazarin** (Protective Sling, Mending Soul) — ne jamais lancer Guardian Shell (cf. 1.12) |
| Arsenal alternatif | **B :** Phantasma Prime (primer) + Kuva Nukor (Secondary Fortifier) + Glaive Prime ; Hate Incarnon en mêlée de confort (cf. 2.4) |

---

## 1. ARCHITECTURE DU BUILD PROTEA PRIME (Survie & Level Cap)

### 1.1 Investissement en ressources

| Ressource | Quantité | Détail |
|---|---|---|
| Orokin Reactor | 1 | Capacité 30 → 60 |
| Exilus Warframe Adapter | 1 | Pour Primed Sure Footed |
| Forma | **5** (dont 1 Umbra Forma) | 3× Vazarin (Archon Vitality, Narrow Minded, **slot Exilus**), 1× Madurai (Primed Continuity), 1× **Umbra** (Umbral Intensify) |
| Helminth | 1 Rhino (rang 30) subsumé | Débloque Roar |
| Archon Shards | 3 Tauforged Azure + 2 Tauforged Crimson | Voir 1.10 |
| Arcanes | Arcane Sculptor R5 + Arcane Escapist (R3 = 10 exemplaires minimum, R5 = 21) ; Molt Augmented R5 pour l'Endurance hors cap | 21 exemplaires pour un R5 |

**Polarités finales (Protea Prime : innées Madurai / Naramon / Naramon, Aura universelle « Any », Exilus vierge)**

| Slot | Polarité | Mod | Coût |
|---|---|---|---|
| Aura | Universelle (innée) | Growing Power | **+14** capacité |
| Exilus | Vazarin (Forma) | Primed Sure Footed | 8 |
| 1 | Madurai (innée) | Blind Rage | 8 |
| 2 | Naramon (innée) | Stretch | 5 |
| 3 | Naramon (innée) | Equilibrium | 7 |
| 4 | Vazarin (Forma) | Archon Vitality | 8 |
| 5 | Umbra (Forma) | Umbral Intensify | 8 |
| 6 | Madurai (Forma) | Primed Continuity | 7 |
| 7 | Vazarin (Forma) | Narrow Minded | 8 |
| 8 | Vierge | Rolling Guard | 12 |
| **Total** | | | **71 / 74** |

- **Sans Umbra Forma** : remplace Umbral Intensify (+44 %) par **Intensify** (+30 %) → **4 Forma**, 74/74, Strength 229 % au lieu de 243 %.
- **Protea non‑Prime** (une seule Naramon innée) : même build, **6 Forma** (Rolling Guard passe en Vazarin, Stretch en slot vierge). Protea Prime apporte aussi Armor 185 (vs 135) et Energy 250 (vs 225).

### 1.2 Cibles de stats

| Stat | Arsenal | En mission | Pourquoi ce chiffre |
|---|---|---|---|
| **Strength** | 243 % | 268 % (Growing Power) → **328 %** (Molt Augmented 250 kills) → **428 %** sur le 4e cast (passif) | ≥ 230 % garantit qu'**un satellite recharge ≥ 1 150 shields** (500 × 2,43 = 1 215) = shield gate complet réarmé. Roar 80–128 %. |
| **Duration** | **284 %** | 284 % | Stat n°1 de Blaze Artillery : les dégâts d'une tourelle ∝ Strength × Duration² (multiplicateur cumulatif par tir). Tourelle 8,52 s, Dispensary 71 s, Roar 85 s. |
| **Range** | 79 % | 79 % | Tourelle 23,7 m (assez en couloir), rayon de capture satellite 3,95 m. Un **petit** rayon est un avantage : tu contrôles quand un satellite libre s'accroche (voir 1.6). |
| **Efficiency** | 45 % | **175 % (verrouillée)** | Arcane Sculptor verrouille l'efficacité à 175 % pendant 12 s à chaque création d'objet (Grenade Fan, Blaze Artillery, Dispensary). Le malus de Blind Rage ne s'applique qu'au tout premier cast. |

### 1.3 Valeurs réelles des compétences (avec ce build)

| Compétence | Coût (1er cast / Sculptor) | Valeurs clés |
|---|---|---|
| **Grenade Fan** (1) — *tap* : Shrapnel Vortex ×3 · *hold* : Shield Satellites ×4 | 38,75 / **6,25** | Satellite : **+1 340 shields** à l'accroche (1 215 en Arsenal, 1 640 avec Molt, 2 140 sur le 4e cast) puis +134/s, plafonné à la limite d'Overshield (1 200). Durée **fixe 13 s**. Rayon 3,95 m. Vortex : 1 340 Slash/s, **100 % de chance de stagger par tick**. |
| **Blaze Artillery** (2) | 77,5 / **12,5** | 1 340 Heat par tir (1 215 Arsenal), **+100 % de dégâts par ennemi touché** (cumulatif, sans plafond hors augment), 3 tirs/s, **8,52 s** (≈25 tirs), 23,7 m, cône 130°, 3 tourelles max, perforation infinie des corps, 100 % de chance de statut Heat. |
| **Dispensary** (3) | 116,25 / **18,75** | **71 s**, 1 pickup toutes les 2 s (Empowered Health Orb 100 PV → Universal Ammo Pack → Energy Orb 25), chance de doublon **67 %** (82 % avec Molt, **100 %** sur le 4e cast avec Molt). |
| **Roar** (4, Helminth) | 116,25 / **18,75** | 30 % × Strength : **+80,4 %** (GP), **+98,4 %** (Molt), **+110,4 % / +128,4 %** sur le 4e cast. 85 s. Non relançable tant qu'il est actif. |

### 1.4 Compromis Helminth : Roar à la place de Temporal Anchor

**Ce que tu perds (Temporal Anchor avec ces stats) :**

- Ancre de **22,7 s** (8 s × 2,84), **3 s d'invulnérabilité** à chaque cast (≈ 13 % d'uptime d'invulnérabilité si recasté en boucle).
- **Death gate** : un coup létal pendant l'ancre te rembobine (5 % PV, ragdoll forcé que **aucun mod n'empêche**, mais tu peux relancer l'ancre pendant le ragdoll).
- Rembobinage : énergie/shields/santé/munitions restaurés, statuts purgés.
- Implosion : **67 %** (25 % × 2,68) des dégâts enregistrés, en Blast, 11,85 m, knockdown + aspiration.

**Ce que tu gagnes (Roar) :**

- **×1,80 → ×2,28** sur *tout* (armes, compétences, compagnon) : c'est un bonus de faction, multiplicatif avec tout le reste.
- **Double application sur les DoT** (Heat des tourelles, Slash, Toxin, Gas) : ×(1+Roar)² → **×3,25 → ×5,22** sur chaque tick de Heat.
- Sur les armes (Glaive, Torid) : gain **linéaire** (×2,1 à ×2,28).
- Sur les tourelles, rendements décroissants (le wiki le confirme) : les dégâts d'une tourelle croissent ≈ en n² (n = nombre de tirs), donc multiplier les dégâts par k réduit le TTK d'un facteur 1/√k → Roar ×2,1 = **−31 % de TTK direct**, ×4,4 sur la Heat = **−52 % de TTK** sur la partie DoT.

**Verdict.** Pour ton objectif (Endurance stable + nettoyage rapide), **Roar est le bon choix**. La survie de ce build repose sur les satellites et Rolling Guard, pas sur l'ancre, et le ×2,1–2,28 permanent sur armes et compagnon raccourcit chaque engagement.

Le prix à payer : la perte du death gate de l'ancre. **Arcane Escapist** le remplace (v1.1). Chaque Mercy kill donne 1 stack ; sur un coup fatal, 3 stacks sont consommés pour **12 s d'invulnérabilité** (R5). Ça fait jusqu'à 3 sauvetages (9 stacks), et il prend la place de Molt Augmented au niveau cap.

Le seul cas où Temporal Anchor redevient BiS : une tentative de record où tu restes à 9999 pendant des heures sans chercher à tuer vite. **Sacrifice** (option A) n'est **pas** un filet fiable au cap : la sentinelle est à terre au moment où tu en as besoin.

**v1.2 : le choix n'est pas binaire.** Roar peut remplacer **Dispensary** au lieu de Temporal Anchor. Tu gardes alors Roar **et** l'ancre (death gate, 3 s d'invulnérabilité), et tu débloques Temporal Artillery. Le prix : le moteur d'énergie du Dispensary. C'est la variante C, détaillée en 1.11.

### 1.5 Gestion de l'énergie

**Coûts réels (Efficiency 45 % sans Sculptor, 175 % avec) :**

| Cast | Sans Sculptor | Avec Sculptor |
|---|---|---|
| Grenade Fan | 38,75 | 6,25 |
| Blaze Artillery | 77,5 | 12,5 |
| Dispensary | 116,25 | 18,75 |
| Roar | 116,25 | 18,75 |

**Rythme de cast réel :** 3 tourelles de 8,52 s = 21,1 casts/min ; satellites toutes les ~13 s = 4,6/min ; Dispensary 0,85/min ; Roar 0,7/min.

| Budget | Consommation | Production Dispensary + Equilibrium |
|---|---|---|
| **Avec Sculptor** | **322 énergie/min (5,4/s)** | **≈ 2 664 énergie par Dispensary = 37,5/s** (12 Empowered Health Orbs × 1,67 × 110 + 11 Energy Orbs × 1,67 × 25) |
| Sans Sculptor | 1 996 énergie/min (33,3/s) | idem, **37,5/s** : zéro marge, chaque orbe ratée = déficit |

- **Equilibrium** est le cœur de l'économie : chaque Empowered Health Orb (base 100) rapporte **110 énergie**, et le mod permet de ramasser une orbe de vie même à pleine santé si l'énergie n'est pas pleine. Ramasse **tout** : un type de pickup non ramassé bloque la réapparition suivante de ce type.
- **Pourquoi pas Arcane Energize :** 150 énergie à 60 %, cooldown 15 s → **≤ 10 énergie/s**. Sculptor fait économiser **≈ 28 énergie/s** sur ce rythme de cast et libère Blind Rage. Sculptor > Energize d'un facteur ~3.
- **Pourquoi pas Primed Flow / Archon Flow :** la jauge n'est jamais le facteur limitant (cast max 18,75 sous Sculptor, 250 de réserve) ; +185 % d'énergie max ne produit rien.
- **Amber Shards énergie : inutiles ici** : leur bonus d'efficacité des orbes **n'affecte pas** la conversion d'Equilibrium (le wiki le confirme).
- **Ouverture de mission** : le premier cast se paie plein tarif (Sculptor ne réduit pas le cast qui le déclenche). Ouvre **toujours** sur Grenade Fan (38,75), jamais sur Roar ou Dispensary (116,25).

### 1.6 Survie Level Cap

**Mécanique du Shield Gate (valeurs actuelles) :**
`t = (Shield_max / 350)^0,65 + 1/3` pour 53–1 150 shields, **plafond 2,5 s au‑delà de 1 150**. La durée dépend des shields **regénérés depuis le dernier gate**.

| Shields max | Gate normal (**garanti**) | Satellite accroché : lecture A (×2) / lecture B (seul le minimum doublé) |
|---|---|---|
| 555 (Protea Prime nue) | 1,68 s | 3,37 s / 1,68 s |
| 1 005 (3 Azure normales) | 2,32 s | 4,64 s / 2,32 s |
| **1 230 (3 Tauforged Azure)** | **2,50 s** | **5,00 s / 2,50 s** |

- **⚠️ Le doublement à 5 s n'est PAS confirmé.**
  - La description in‑game dit : *« a Satellite is destroyed to double **minimum** Shield Gate invincibility time »*. Seule la page *Shield* du wiki annonce « 0,66 – 5 s ».
  - **Construis ton timing sur 2,5 s.** Pour trancher : Simulacrum, ennemi niveau 9999, chrono de la barre de vie grise avec et sans satellite accroché.
- **Shield Satellites** : avec ≥ 230 % de Strength, chaque satellite recharge > 1 150 shields, donc **chaque satellite réarme un gate complet** (2,5 s garantis). 4 satellites pour 6,25 énergie.
- **Le piège** : *toute* restauration de shields pendant le gate le **termine immédiatement**.
  - Un satellite libre dans tes 3,95 m s'accroche dès que tu n'en portes plus et coupe ton gate.
  - Sous un feu nourri, plusieurs satellites dans le rayon s'accrochent et sont détruits **en chaîne** (le wiki le confirme).
  - Lance donc tes satellites à **4–6 m** : ce sont des « stations de recharge ». Marche dedans à **~2 s** de gate (avant la fin garantie à 2,5 s) pour récupérer shields pleins + un gate réarmé. Si ton test confirme les 5 s, tu peux attendre ~4,5 s.
- **Le compagnon peut voler un satellite** (les compagnons sont des cibles éligibles). Place tes satellites hors de sa trajectoire.
- **Interdits absolus** (ils restaurent des shields pendant le gate et le raccourcissent) : Brief Respite, set Augur, précepte **Guardian**, **Fast Deflection** (avec −45 % de délai, la recharge naturelle démarre à 2,2 s et coupe ton gate de 2,5 s), Catalyzing Shields (1,33 s fixe = pire que tes 2,5 s), Decaying Dragon Key (gate plafonné à 0,33 s), **Guardian Shell** de Vazarin (sa rupture déclenche Guardian Break : −80 % de délai de regen pendant 12 s, cf. 1.12).
- **Rolling Guard** : 3 s d'invulnérabilité + **purge de tous les statuts** + immunité au knockdown, puis 7 s de recharge (cycle de 10 s). Ses usages :
  - **Toxin** : la **seule** menace qui traverse les shields, et donc le gate.
  - **Magnetic** : amplifie les dégâts sur shields, réduit la régénération naturelle et draine l'énergie.
  - **DoT ennemis (Slash, Heat)** : ils **frappent tes shields** à chaque tick. Un tick sur des shields fraîchement restaurés déclenche un gate et **consomme un satellite**.
  - Attention : le Slash ignore l'**armure**, **pas** les shields.
- **Health 740** (370 × 2 via Archon Vitality) : c'est ton seul tampon face au Toxin tant que les ennemis ne one‑shot pas encore. Au 9999, n'importe quel dégât sur la santé est mortel : la règle est **ne jamais encaisser sur la santé**, d'où la purge immédiate via Rolling Guard et le filet Arcane Escapist.
- **Primed Sure Footed** : 100 % de résistance au knockdown/stagger, **y compris l'auto‑stagger** de l'explosion d'Epitaph Prime (non chargé) et de la détonation du Glaive Prime. Sans lui, ce loadout s'auto‑stagger en boucle.
- **Armor 185** : inutile au cap (l'armure ne protège pas les shields). Ne mets **aucun** mod d'armure.
- **Conseil d'options** : inverse Tap/Hold de Grenade Fan (option du jeu) pour que le **tap** lance les satellites : tu gagnes le temps de maintien aux moments critiques.

### 1.7 Gestion du passif (+100 % Strength additif au 4e cast)

- Le passif s'applique au **4e cast, quel qu'il soit**. Tu ne peux pas le « sauter ».
- **⚠️ Non documenté** : le wiki ne précise pas si le passif s'applique aux compétences Helminth. Vérifie en jeu : le buff de Roar doit afficher **~110 %** au 4e cast, contre ~80 % sinon.
- **Règle absolue : la survie passe avant le passif.** Si tu as besoin d'un satellite pendant que les 3 barres sont chargées, lance‑le. Un Roar à +80 % ne tue personne ; un satellite manqué, si.
- **Cible n°1 : Roar.** 30 % × (2,68 + 1,00) = **+110,4 %** (avant Molt) → **+128,4 %** (Molt max) pendant 85 s, sur tout et en double sur les DoT. Aucune autre cible ne vaut ça.
- **Contrainte** : Roar ne peut pas être relancé tant qu'il est actif. Procédure d'alignement :
  1. Quand il reste < 5 s à Roar, regarde le compteur du passif.
  2. Compteur à 3 → lance Roar à l'expiration.
  3. Compteur à 0–2 → complète avec des casts utiles (tourelle à 12,5, ou Grenade Fan *tap* à 6,25) jusqu'à 3, puis Roar.
  4. Coût de l'alignement : 0 à 3 casts, soit ≤ 37,5 énergie par cycle de 85 s.
- **Snapshot** : Growing Power (6 s, déclenché par un statut d'**arme**) et les stacks Molt doivent être actifs **au moment du cast** de Roar. Tire une balle d'Epitaph juste avant.
- **Cibles secondaires** (les ~8 autres procs par cycle de Roar tombent naturellement) : Dispensary (doublons garantis à 100 % avec Molt), puis Satellites (2 140 shields à l'accroche), puis Blaze Artillery (base ×2, mais rendement décroissant).
- **Blaze Artillery** : le passif double la base de *ce* tir de tourelle (1 340 → 1 840/2 140), mais l'effet est dilué par le multiplicateur cumulatif. Ne force pas l'alignement dessus.

### 1.8 Les 10 mods (exacts)

| # | Mod | Rang | Effet | Rôle |
|---|---|---|---|---|
| Aura | **Growing Power** | 5 | +25 % Strength pendant 6 s sur statut infligé par une **arme** (compagnon inclus, compétences exclues) | Uptime 100 % via Epitaph/Verglas/griffes |
| Exilus | **Primed Sure Footed** | 10 | +100 % résistance knockdown/stagger | Anti‑CC + anti auto‑stagger |
| 1 | **Archon Vitality** | 10 | +100 % Health ; les statuts Heat des compétences sont appliqués **deux fois** | Double la Heat de Blaze Artillery |
| 2 | **Blind Rage** | 10 | +99 % Strength / −55 % Efficiency | Malus annulé par Sculptor |
| 3 | **Umbral Intensify** | 10 | +44 % Strength (+11 % résistance Tau) | Strength sans malus |
| 4 | **Primed Continuity** | 10 | +55 % Duration | Durée tourelles / Roar / Dispensary |
| 5 | **Narrow Minded** | 10 | +99 % Duration / −66 % Range | Le plus gros levier de dégâts de tourelle (Duration²) |
| 6 | **Stretch** | 5 | +45 % Range | Ramène la Range à 79 % (Archon Stretch = même +45 % pour 16 au lieu de 9, effet secondaire mort sur Protea, cf. 5.1) |
| 7 | **Rolling Guard** | 10 | Roulade : 3 s d'invulnérabilité + purge des statuts, recharge 7 s | Purge le Toxin (traverse les shields) et les DoT qui mangent les satellites |
| 8 | **Equilibrium** | 10 | Health pickups → +110 % énergie ; Energy pickups → +110 % santé | Moteur d'énergie avec Dispensary |

### 1.9 Les 2 Arcanes

| Arcane | Effet (R5) | Justification |
|---|---|---|
| **Molt Augmented** | +0,24 % Strength par kill, 250 stacks = **+60 %**, conservé jusqu'à la mort | Kills de toutes sources (tourelles, compagnon) ; plein en < 2 min d'Endurance. Roar +80 % → +98 % ; satellites 1 340 → 1 640. |
| **Arcane Sculptor** | À la création d'un objet par une compétence : Efficiency **verrouillée à 175 %** pendant 12 s | Grenade Fan, Blaze Artillery et Dispensary sont des objets valides (liste officielle). Avec une tourelle toutes les ~2,8 s, l'uptime est permanent : tous les casts coûtent 25 %. Remplace Arcane Energize (cf. 1.5). Achat : Hunhow (Pontis Tower, Uranus Proxima) 10 Emerald Talent + 10 Crimson Talent, ou récompense des missions Railjack Scoria's Angel / The Kuva Wytch. |

**Configuration level cap 9999 (v1.1) : Molt Augmented → Arcane Escapist.**

- **Effet** : chaque Mercy kill donne 1 stack (max 9, conservés indéfiniment). Sur un coup fatal, 3 stacks sont consommés : **12 s d'invulnérabilité** au R5 (8 s au R3), +1 revive dès le R3.
- **Seuil de Mercy** : 10 % minimum sur les unités lourdes au‑delà du niveau ~300. Chaque proc **Impact** ajoute +8 % (jusqu'à 80 %). La détonation du Glaive et le tir direct de l'Epitaph ont un Impact **forcé**. Tu es invulnérable pendant l'animation.
- **Ce que tu perds** : +60 % de Strength. Roar redescend à +80/+110 % et les satellites à 1 340 shields. Ce n'est que du DPS : le seuil de 1 150 shields reste atteint.
- **Acquisition** : Kaya Velasco (Höllvania Central Mall), 5 Pix Chip, 1 exemplaire par semaine ; Temporal Archimedea ; échange (MR 11).

> Si tu n'as pas encore Sculptor : **Arcane Energize** en intérim, et remplace **Stretch** par **Streamline**. Garde Blind Rage : sans elle, un satellite ne recharge plus 1 150 shields. Résultat : Efficiency 75 %, consommation **26,8/s** contre 37,5/s produits (+ ~10/s d'Energize), Range 34 % (tourelles 10,2 m, satellites 1,7 m).

### 1.10 Les 5 Archon Shards

| Shard | Bonus | Effet |
|---|---|---|
| Tauforged Azure | +225 Shield Capacity | |
| Tauforged Azure | +225 Shield Capacity | 555 + 675 = **1 230** > 1 150 → gate **2,5 s** (plafond) |
| Tauforged Azure | +225 Shield Capacity | |
| Tauforged Crimson | +15 % Ability Duration | Duration 254 % → **284 %** |
| Tauforged Crimson | +15 % Ability Duration | |

**Justification mathématique :**

- **Shields** : sans shards, gate 1,68 s. Les 3 Tauforged amènent au plafond de 2,5 s : **+49 % de durée d'invulnérabilité par gate**, quelle que soit la lecture du doublement satellite. C'est le meilleur gain de survie disponible pour 3 slots.
- **Limite** : ce plafond est **nominal**. Plusieurs modificateurs de mission le cassent (Stunted Shields, standard en Icebind : 1,25 s). Voir 4.5.
- **Duration plutôt que Strength** : dégâts d'une tourelle ∝ Str × Dur². +15 % de Strength sur 268 % = **×1,056** ; +15 % de Duration sur 254 % = **×1,122**. Duration rapporte ×2,2 plus. Sur Roar, +15 % de Strength ne vaut que ×1,024 de dégâts totaux.
- **Pourquoi pas d'Amber en Endurance** : l'efficacité des orbes n'affecte pas Equilibrium, et l'énergie initiale est inutile avec Sculptor.
- **Variante level cap 9999 (v1.1)** : remplace **1 Tauforged Crimson Duration par 1 Tauforged Amber Casting Speed (+37,5 %)**. L'animation de cast est ta fenêtre d'exposition : Grenade Fan est une animation corps entier avec saut forcé. La Casting Speed raccourcit cette animation, mais pas le vol des grenades. Coût : Duration 284 % → 269 %, soit ≈ −10 % de dégâts de tourelle.
- **Normal vs Tauforged** : avec des shards normaux (+150), il en faut **4 Azure** (555 + 600 = 1 155 ≥ 1 150) + 1 Crimson Duration (+10 %). Avec 3 Azure normales, on plafonne à 1 005 (gate 2,32 s, −7 %).

### 1.11 Variante C — « ancre mobile » avec Temporal Artillery (ajout v1.2)

**Ce que fait l'augment (description in‑game et notes du wiki) :**

- *« When Temporal Anchor is activated, one existing Artillery unit will attach to Protea, halting its duration countdown. Max combo count is 20x. »*
- À l'activation de **Temporal Anchor**, la tourelle active **la plus proche** s'attache à Protea et la suit. Son compte à rebours est **suspendu** tant que l'ancre est active.
- Elle perd son cône frontal de 130° et vise **tous les ennemis à portée** (23,7 m avec ce build), donc à 360°. Sans cible, elle tire là où tu vises.
- Contrepartie : son multiplicateur de combo est **plafonné à 20×** (14× au R0, non modifiable par les mods). Si elle dépassait 20× au moment de l'attache, elle redescend à 20×.
- À la fin de l'ancre, elle redevient une tourelle fixe normale (cône de 130°, combo non plafonné) et son compte à rebours reprend.
- Les 2 autres tourelles restent fixes. Un cast au‑delà de 3 remplace une tourelle fixe, jamais la suiveuse.
- Polarité Zenurik, coût 9 au R3. Achat : Arbiters of Hexis (rang Maxim) ou The Perrin Sequence (rang Partner), 25 000 standing.

**⚠️ Inutilisable dans la configuration A (v1.1).** L'augment exige Temporal Anchor actif, et la v1.1 remplace justement Temporal Anchor par Roar. L'intégrer impose de réorganiser le kit :

| Config | Kit (1 / 2 / 3 / 4) | Roar | Death gate de l'ancre | Tourelle suiveuse | Énergie | Verdict |
|---|---|---|---|---|---|---|
| **A — v1.1** | Grenade Fan / Blaze / Dispensary / **Roar** | ✔ | ✘ (Arcane Escapist seul) | ✘ | Dispensary + Equilibrium : **+37,5/s** | Défaut Endurance ; défaut au cap tant que C n'est pas validée |
| **B — kit natif** | Grenade Fan / Blaze / Dispensary / Temporal Anchor | ✘ | ✔ | ✔ | Dispensary + remboursement au rembobinage | Confort maximal, mais sans Roar : **−44 à −56 %** de dégâts directs, **−69 à −81 %** sur la Heat. Non retenue |
| **C — ancre mobile** | Grenade Fan / Blaze / **Roar** / Temporal Anchor | ✔ | ✔ | ✔ | Remboursement au rembobinage : **−25 net par ancre** | **Candidate au 9999** (3 tests ci‑dessous) |

**Mods de la variante C** (Equilibrium → Temporal Artillery, 1 Forma Zenurik sur le slot 3) :

| Slot | Polarité | Mod | Coût |
|---|---|---|---|
| Aura | Universelle (innée) | Growing Power | **+14** capacité |
| Exilus | Vazarin (Forma) | Primed Sure Footed | 8 |
| 1 | Madurai (innée) | Blind Rage | 8 |
| 2 | Naramon (innée) | Stretch | 5 |
| 3 | **Zenurik (Forma)** | **Temporal Artillery** (R3) | 5 |
| 4 | Vazarin (Forma) | Archon Vitality | 8 |
| 5 | Umbra (Forma) | Umbral Intensify | 8 |
| 6 | Madurai (Forma) | Primed Continuity | 7 |
| 7 | Vazarin (Forma) | Narrow Minded | 8 |
| 8 | Vierge | Rolling Guard | 12 |
| **Total** | | | **69 / 74** |

- **6 Forma** au total. Sans la Forma Zenurik, l'augment coûte 11–12 en slot Naramon et le build passe à 75–76/74.
- **Pourquoi Equilibrium sort** : sans Dispensary, il ne convertit plus que les orbes d'Eximus et de Synth Deconstruct, et le rembobinage efface l'énergie ramassée pendant l'ancre (voir l'économie ci‑dessous).
- **Stats inchangées** : 243 % / 284 % / 79 % / 45 % (175 % sous Sculptor). Arcanes, shards et compagnon B identiques.

**Valeurs propres à la variante C :**

| Élément | Valeur |
|---|---|
| **Temporal Anchor** (4) | 155 au 1er cast / **25** sous Sculptor · **22,7 s** · 3 s d'invulnérabilité au cast · death gate · au rembobinage : purge de tous les statuts, énergie / shields / santé / munitions / combo ramenés à la valeur enregistrée |
| **Implosion** | **67 %** des dégâts enregistrés (92 % sur le 4e cast), Blast, 11,85 m, knockdown + aspiration. Les tourelles (DoT compris) et les Shrapnel Vortex alimentent l'enregistrement |
| **Tourelle suiveuse** | 360°, 23,7 m, **20 × 1 340 = 26 800 Heat par tir** au plafond (×2 stacks de Heat via Archon Vitality, ×Roar), sans expiration tant que l'ancre tient |
| **Roar** (3, Helminth) | Inchangé : 116,25 / 18,75, +80 % à +128 %, 85 s |

**Suiveuse (plafond 20×) contre tourelle fixe (non plafonnée).** Le multiplicateur d'un tir vaut 1 + k × (nombre de tirs précédents), avec k = ennemis touchés par tir. Sur les 25 tirs d'une tourelle fixe (8,52 s) :

| Ennemis touchés par tir (k) | Tourelle fixe (multiplicateur moyen) | Suiveuse |
|---|---|---|
| 1 | 13× | **20×** (atteint au 20e tir, puis conservé) |
| 2 | 25× | 20× |
| 3 | 37× | 20× |
| 5 | 61× | 20× |

- **Seuil ≈ 1,6 ennemi par tir.** En dessous (cibles éparses, contournements, ennemis dans ton dos), la suiveuse fait mieux qu'une tourelle fixe. Au‑dessus (couloir dense, Cordon), elle tombe au **tiers** d'une tourelle fixe.
- En couloir dense, C perd donc jusqu'à **~22 %** des dégâts de tourelles (1 tourelle sur 3 au tiers) ; l'implosion périodique compense en partie. En contenu mobile, C gagne.

**Économie d'énergie.** Selon le wiki, le rembobinage rembourse tout ce qui a été dépensé pendant l'ancre, sauf le coût de l'ancre elle‑même :

| Poste (par ancre de 22,7 s, sous Sculptor) | Énergie |
|---|---|
| 2 tourelles fixes (~5,3 casts × 12,5) | 66 (remboursés) |
| Satellites (~1,75 cast × 6,25) | 11 (remboursés) |
| Roar (~0,27 cast × 18,75) | 5 (remboursé) |
| Temporal Anchor | **25 (non remboursé)** |
| **Net** | **−25 par ancre (−1,1/s)**, contre +37,5/s en A |

- Réserve de 250 : **~10 ancres (~3,8 min) sans aucun apport**. Il faut ≈ 110 d'énergie au moment de poser l'ancre pour couvrir la fenêtre.
- **Piège** : le rembobinage **ramène** l'énergie à la valeur enregistrée. Une orbe ramassée pendant l'ancre est donc perdue. Deux parades :
  - ramasse les orbes (Eximus : Large Energy Orb de 50) **entre** le rembobinage et la pose de l'ancre suivante ;
  - si ta jauge dépasse la valeur enregistrée juste avant l'expiration, **maintiens 4** (destruction de l'ancre sans rembobinage), puis repose‑la.
- Même logique pour les munitions : l'Epitaph (40 max) et la Torid reviennent à la valeur enregistrée. La charge Incarnon n'est pas restaurée.
- **Nullifier** : une bulle dissipe l'ancre **sans rembobinage**, donc sans remboursement de la fenêtre en cours.

**Ce que C gagne en survie** (par rapport à A) :

- **Death gate** : un coup fatal pendant l'ancre te ramène à l'ancre avec 5 % de PV (ragdoll) ; relance l'ancre aussitôt pour ses 3 s d'invulnérabilité.
- **3 s d'invulnérabilité à chaque ancre** (≈ 13 % d'uptime).
- **Purge de tous les statuts** au rembobinage, Toxin compris.
- **Insensible à Untreatable** : plus aucune dépendance aux Health Orbs du Dispensary (cf. 4.5).

**Ce que C coûte :**

- Dispensary (plus d'Empowered Health Orbs : sans effet au 9999, mais tampon de santé perdu en Endurance) et Equilibrium.
- Le rembobinage te **téléporte** à l'ancre toutes les 22,7 s : pose‑la à un endroit sûr. Pour te déplacer, maintiens 4 et repose‑la plus loin, mais tu perds le remboursement de la fenêtre.
- Une Forma de plus et un augment à acheter.

**Ouverture C :** Epitaph → Grenade Fan, satellites (38,75) → attends l'atterrissage (Sculptor) → Blaze ×2 → **Roar (4e cast, +110 %)** → 3e Blaze **près de toi** (elle sera la plus proche) → Temporal Anchor (la suiveuse s'attache).

**Tests à faire en Simulacrum avant d'adopter C au 9999 :**

1. Le rembobinage rend‑il bien l'énergie dépensée en tourelles ? Une orbe ramassée pendant l'ancre est‑elle effacée ?
2. Après un rembobinage puis une nouvelle ancre, la même tourelle se rattache‑t‑elle, avec son combo à 20× ?
3. Coup fatal pendant l'ancre avec Arcane Escapist chargé : lequel se déclenche en premier, et Escapist consomme‑t‑il ses stacks ?

**Verdict.** C garde Roar **et** récupère le death gate que la v1.1 avait sacrifié : sur le papier, c'est la configuration level cap la plus sûre, à dégâts comparables. En échange, elle remplace un moteur d'énergie excédentaire (+37,5/s) par une boucle de remboursement à **−1,1/s** qui demande de la gestion. **A reste le défaut en Endurance** (couloirs denses, Dispensary utile). **C devient la référence au 9999 si les tests 1 et 2 passent.** Bonus : C rend aussi accessible **Temporal Erosion** (l'autre augment de l'ancre : Grenade Fan et Blaze Artillery retirent de l'armure pendant l'ancre), mais il faut lui trouver un slot (piste non chiffrée).

### 1.12 Couches de survie complémentaires : Secondary Fortifier et Vazarin (ajout v1.2)

**Ce ne sont pas des alternatives à Arcane Escapist.** Escapist occupe un slot d'arcane de Warframe ; Secondary Fortifier, le slot d'arcane de l'arme secondaire (à la place de Secondary Encumber) ; Vazarin est une école de Focus (le guide n'en imposait aucune). Les trois s'empilent sans rien retirer au build de la Warframe. **Escapist reste en place.**

**Secondary Fortifier (sur l'Epitaph Prime, au level cap)**

- Texte (R5) : *« Gain 1 Overguard for every 100 Damage dealt to an enemy's Overguard. Deals x8 Extra Damage to Overguard. »* Plafond : **15 000 Overguard**.
- **Pourquoi c'est fort ici** : sur un joueur, l'Overguard est neutre à tous les types de dégâts sauf Void, **annule tous les statuts** (Toxin et Magnetic compris) et ouvre un **gate de 0,5 s** à sa rupture, sans débordement sur les shields. C'est la seule couche du build qui arrête un tir **Toxin**, la menace n°1 de l'audit.
- **Bonus offensif** : ×8 sur l'Overguard des Eximus, principale résistance au cap (le Viral ne le touche pas, cf. 4.3). L'AoE de 14,4 m de l'Epitaph touche plusieurs Eximus à la fois.
- **Limites :**
  - Il ne se recharge **que** sur un ennemi doté d'Overguard (Eximus). Sans Eximus, l'arcane ne fait rien.
  - 15 000 = **un coup** au 9999, plus 0,5 s. Ce n'est pas un mur, c'est un gate de plus.
  - **Non documenté** : un gain d'Overguard pendant un shield gate le coupe‑t‑il, comme une recharge de shields ? À tester. En attendant, ne tire pas sur un Eximus pendant ton gate.
- **Ce que tu perds** : Secondary Encumber (+24 % de chance d'un second statut aléatoire), soit en moyenne moins d'un type de statut en plus sur la cible. Coût faible au cap, où ce sont les tourelles qui tuent. **Garde Encumber en Endurance.**
- **Usage** : avant de tuer un Eximus, **remplis ton Overguard sur lui**. Au 9999, son Overguard est en général assez gros pour te recharger plusieurs fois.

**École de Focus : Vazarin**

- **Protective Sling** : un allié touché par ton Void Sling est **invulnérable 5 s** et soigné de 60 % sur 5 s, **ta propre Warframe comprise**. Coût : 10 énergie, aucun temps de recharge indiqué.
  - Procédure : Transference (ta Warframe est en règle générale invulnérable tant que l'Operator est sorti) → Void Sling **à travers ta Warframe** → retour. Le wiki indique que l'invulnérabilité est conservée au retour (sauf Excalibur Umbra).
  - **Risque** : au 9999, l'Operator meurt en un coup. Tu reviens alors dans la Warframe **shields vides**, avec un stack de Transference Static (−20 % de santé max ; au 4e stack, bleedout immédiat). Fais‑le vite, hors de la ligne de tir.
  - C'est un bouton **proactif**. Escapist (et, en variante C, le death gate de l'ancre) restent les seuls filets **automatiques** sur coup fatal.
- **Mending Soul** (passif) : les **4 premières réanimations sont instantanées**, soit 4 relevés immédiats par mission une fois à terre (non rechargeables).
- **Nidri Tauron Strike / Deathless Currents** (ultime) : 20 s de vortex qui réanime instantanément dans sa zone, même là où l'auto‑réanimation est désactivée.
- **⚠️ Piège : Guardian Shell.** Sa rupture déclenche **Guardian Break** (+150 % de régénération de shields, **−80 % de délai** pendant 12 s). Pour la même raison que Fast Deflection (cf. 1.6), la recharge naturelle démarrerait pendant ton gate et le couperait. **Ne lance jamais Guardian Shell.**

**Pile de filets au 9999 (v1.2) :**

| # | Couche | Couverture | Déclenchement | Source |
|---|---|---|---|---|
| 1 | Overguard (≤ 15 000) | 1 coup de tout type + 0,5 s, statuts annulés | Automatique, s'il est chargé | Secondary Fortifier |
| 2 | Shield gate (+ satellite) | 2,5 s | Automatique | Shields 1 230 / Grenade Fan |
| 3 | Rolling Guard | 3 s + purge des statuts | Roulade, recharge 7 s | Mod |
| 4 | Protective Sling | 5 s | Manuel (Operator) | Vazarin |
| 5 | Death gate de l'ancre | Retour à l'ancre, 5 % de PV | Coup fatal, ancre active | Variante C uniquement |
| 6 | Arcane Escapist | 12 s | Coup fatal, 3 stacks | Arcane |
| 7 | Mending Soul | Réanimation instantanée | À terre (×4 par mission) | Vazarin |

Seul l'ordre Martyr Symbiosis → Escapist est documenté (cf. 3). L'ordre entre le death gate de l'ancre et Escapist est à tester (test 3 de 1.11).

---

## 2. LOADOUT COMPLET DES ARMES

### 2.1 Arme principale : Torid Incarnon

**Investissement :** Torid Incarnon Genesis (Steel Path Circuit, rotation hebdomadaire, ou Cavalero 120 platinum, achat unique) + installation (20 Pathos Clamp, 60 Rune Marrow, 20 Maw Fang) · Orokin Catalyst · **6 Forma** (3 Madurai, 2 Vazarin, 1 Naramon) · Exilus Weapon Adapter (Exilus déjà Naramon) · Primary Arcane Adapter (Teshin, 15 Steel Essence).

| Slot | Polarité | Mod | Coût |
|---|---|---|---|
| 1 | Madurai | Serration (+165 % dégâts) | 7 |
| 2 | Vazarin | **Primed Cryo Rounds** (+165 % Cold) | 8 |
| 3 | Vierge | **Malignant Force** (+60 % Toxin / +60 % Status) | 7 |
| 4 | Vazarin | Galvanized Aptitude (+80 % Status ; +40 % dégâts directs par type de statut, ×2) | 6 |
| 5 | Naramon | Critical Delay (+200 % CC / −20 % Fire Rate) | 5 |
| 6 | Vierge | Vital Sense (+120 % CD) | 7 |
| 7 | Madurai | Galvanized Chamber (+80 % Multishot ; +30 % par kill ×5) | 8 |
| 8 | Madurai | Primed Firestorm (+44 % rayon : zone d'impact du rayon 2,3 → 3,3 m, nuage 3 → 4,3 m) | 8 |
| Exilus | Naramon | Ammo Drum (+90 % munitions max : 60 → 114) | 4 |
| Arcane | — | **Primary Merciless** (+30 % dégâts par kill pendant 4 s, ×12 = +360 %, +30 % Reload) | — |
| | | **Total** | **60 / 60** |

**Éléments** : Cold (Primed Cryo Rounds) + Toxin (Malignant Force et Toxin innée fusionnée) = **Viral pur**. Ce sont les deux seuls éléments, donc l'ordre des slots n'a pas d'importance.

**Évolutions Incarnon** : la Torid Incarnon Genesis a **4 paliers (Évo I à IV)**. Il **n'existe pas d'Évolution V** sur cet adaptateur. Les 4 paliers :

| Palier | Choix | Effet | Pourquoi |
|---|---|---|---|
| **Évo I** | Incarnon Form (fixe) | 5 tirs directs remplissent la jauge (34 munitions par charge, max 170) ; Alt Fire → **rayon Toxin continu** 37 m qui **chaîne sur 5 ennemis à 7 m** (75 % par saut) + zone de 2,3 m à l'impact | Arme de nettoyage de couloir |
| **Évo II** | **Final Fusillade** | +51 dégâts de base (51 → **102** en forme Incarnon, **×2**) ; +3 Multishot sur la dernière balle du chargeur | Double la base sans vider les munitions (Plentiful Mayhem draine le chargeur Incarnon) |
| **Évo III** | **Swift Deliverance** | +50 % vitesse de projectile (40 → 60 m/s) | Fiabilise les 5 tirs directs nécessaires pour recharger l'Incarnon |
| **Évo IV** | **Commodore's Fortune** | +20 % CC de base (29 → **49 %**) | 49 % × 3,0 = **147 % CC** : orange garantis à 47 %, CD 6,82 (+1,2 final via Tenacious Bond = ×1,185) |

**Profil forme Incarnon** : 102 de base (Viral ×3,25), CC 147 %, CD 6,82, Status 93,6 %, 6,4 ticks/s, Multishot 1,8 → 3,3 (Galvanized Chamber 5 stacks). Rôle : nettoyer le menu fretin, poser du Viral en masse, empiler Merciless et Galvanized. Au 9999, ce sont les tourelles qui tuent ; la Torid applique les statuts et achève.

**⚠️ Arme à stacks.** Merciless (−1 stack toutes les 4 s sans kill), Galvanized Aptitude et Galvanized Chamber dépendent des kills : **×6,5 d'écart** entre stacks pleins (bucket de base 9,45, Multishot 3,3) et 0 stack (2,65 et 1,8). Au cap, quand le rythme de kills chute, l'arme se dégrade en spirale. Les chiffres ci‑dessus sont des **plafonds**.

**Configurations alternatives (même polarités, sans Forma supplémentaire) :**

| Config | Changements | Éléments | Capacité | Quand |
|---|---|---|---|---|
| **Viral** (ci‑dessus) | — | Viral | 60/60 | Corrupted, Endurance standard |
| **Corrosive** | Primed Cryo Rounds → **Rifle Elementalist** (slot Vazarin) ; Malignant Force → **High Voltage** | Electricity + Toxin innée = **Corrosive** | 57/60 | Grineer / Kuva : 10 stacks en ~2 s sur la cible = **×5,98** contre une armure au plafond, sans dépendre de l'Epitaph |
| **Magnetic** | Malignant Force → **High Voltage** | Cold + Electricity = **Magnetic** + Toxin innée séparée | 60/60 | **Défaut au cap 9999** (Eximus/Overguard fréquents, le Viral ne touche pas l'Overguard), Corpus |

### 2.2 Arme secondaire : Epitaph Prime (primer)

**Investissement :** Orokin Catalyst · **3 Forma** (1 Vazarin, 2 Naramon) · Exilus Weapon Adapter (Exilus déjà Naramon) · Secondary Arcane Adapter.
**Mode de tir : NON chargé uniquement** (50 % Status de base, explosion de 10 m, proc Cold forcé sur l'AoE, Impact forcé sur l'impact direct). Le tir chargé est un tir crit, il ne sert pas ici.

| Slot | Polarité | Mod | Coût |
|---|---|---|---|
| 1 | Madurai | **Pistol Pestilence** (+60 % Toxin / +60 % Status) | 4 |
| 2 | Madurai | Primed Fulmination (+44 % rayon : **10 → 14,4 m**) | 8 |
| 3 | Vazarin | Galvanized Shot (+80 % Status ; +40 % dégâts directs par type de statut, ×3) | 6 |
| 4 | Vierge | **Jolt** (+60 % Electricity / +60 % Status) | 7 |
| 5 | Vierge | Augur Seeker (+90 % Status Duration : Corrosive 8 → **15,2 s**) | 7 |
| 6 | Naramon | Stunning Speed (+40 % Reload / +30 % Status) | 5 |
| 7 | Naramon | Primed Quickdraw (+88 % Reload) | 6 |
| 8 | Vierge | Pistol Elementalist (+90 % Status Damage / +60 % Reload) | 9 |
| Exilus | Naramon | Primed Pistol Ammo Mutation (seulement 40 munitions max) | 5 |
| Arcane | — | **Secondary Encumber** (+24 % de chance de déclencher un second statut aléatoire parmi 13) — au level cap : **Secondary Fortifier** (cf. 1.12) | — |
| | | **Total** | **57 / 60** |

- **Éléments** : Toxin + Electricity = **Corrosive** (seuls éléments, ordre indifférent). L'AoE garde son Blast natif.
- **Chiffres** : Status **165 %** par impact et par explosion (calculés séparément) ; reload 0,6 → **0,21 s** (chargeur de 1 : le reload *est* ta cadence).
- **Statuts posés par tir** : Corrosive, Blast, Cold (forcé), Impact/Puncture/Slash (impact direct), plus Encumber au hasard (Viral, Magnetic, Gas, Radiation, Heat…). Combiné à la Heat des tourelles et au Viral de la Torid/du compagnon, ça fait **6 à 8 types** : Galvanized Aptitude/Shot au maximum, Cull the Weak (griffes) au maximum.
- **Limite d'Encumber** : 1 proc bonus par instant et par cible. L'AoE ne multiplie pas Encumber, elle étend les statuts de base.

### 2.3 Arme de mêlée : Glaive Prime (heavy detonation)

**Investissement :** Orokin Catalyst · **2 Forma** (1 Umbra pour Sacrificial Steel, 1 Madurai) **ou 3 Madurai** sans Umbra (67/70) · Stance **Gleaming Talon** (Naramon assortie : +10 capacité) · Melee Arcane Adapter.
**Mécanique** : maintenir Mêlée = lancer chargé ; **Heavy Attack pendant le vol = explosion de 4,8 m** (Charged Throw Recall Explosion : **1 184 Blast**, sans falloff, Impact + Slash forcés, CC 26 %, CD 2,4×, Status 34 %), qui consomme le combo et applique le multiplicateur de Heavy. **Condition Overload n'affecte pas l'explosion** : c'est pour ça qu'il n'y en a pas.

| Slot | Polarité | Mod | Coût |
|---|---|---|---|
| Stance | Naramon | Gleaming Talon | +10 |
| 1 | Madurai | Primed Pressure Point (+165 % Melee Damage) | 7 |
| 2 | Naramon | **Primed Fever Strike** (+165 % Toxin) | 8 |
| 3 | Vierge | Killing Blow (+120 % dégâts sur Heavy / +60 % Wind Up) | 11 |
| 4 | Umbra | Sacrificial Steel (+220 % CC, **×2 sur Heavy** = +440 %) | 8 |
| 5 | Vierge | Amalgam Organ Shatter (+85 % CD / +60 % Wind Up) | 11 |
| 6 | Madurai | Galvanized Reflex (+50 % Heavy Attack Efficiency ; +20 Initial Combo par kill ×4) | 6 |
| 7 | Vierge | Corrupt Charge (+30 Initial Combo / −50 % Combo Duration) | 7 |
| 8 | Vierge | **North Wind** (+90 % Cold) | 11 |
| Arcane | — | **Melee Duplicate** (crit jaune → seconde instance de dégâts, 100 % au R5) | — |
| | | **Total** | **69 / 70** |

**Chiffres de la détonation :**

- **Éléments** : Toxin (165 %) + Cold (90 %) = **Viral +255 %** (seuls éléments : ordre indifférent), en plus du Blast natif.
- **Crit** : CC 26 % × 5,4 = **140,4 %**, CD 2,4 × 1,85 = **4,44**. Le CC optimal pour Melee Duplicate est `(3·CD − 4)/(2·CD − 2)` = **135,5 %** (139 % avec Tenacious Bond) : on est **pile dessus**. Duplicate = **×1,60** (60 % de crits jaunes dupliqués).
- **Combo** : 30 (Corrupt Charge) + 80 (Galvanized Reflex ×4) = 110 de combo initial = **×6, à condition de faire 4 kills en mêlée en moins de 20 s**. **Plancher réel : ×2** (Corrupt Charge seul, 30). Sans Tandem Bond (option B), la détonation perd un facteur **×3** dès que les kills ralentissent. Heavy Attack Efficiency : 50 %.
- **Wind Up** : +120 %, soit 1,2 s → ~0,55 s de charge.
- **Ordre de grandeur** (avant armure/Viral) : 1 184 × 3,85 × 3,55 × 6 × 7,51 (crit + Tenacious) × 1,6 × 2,1 (Roar) ≈ **2,4 millions par explosion**, en AoE de 4,8 m. C'est un plafond : avec un combo à ×2, sans Tenacious ni Roar, on tombe à ≈ 0,3 M (÷8).
- **Alternative niveau cap pur** : *Melee Assimilation* (sur rupture de shields : +150 % dégâts Heavy, et les kills Heavy rendent 30 % des shields max). Elle réarme le gate par les kills, mais **coupe** les gates des satellites en cours. Duplicate reste le BiS burst.

### 2.4 Arsenal alternatif (ajout v1.2)

Les deux vidéos construisent l'arsenal autrement. Le **primer passe en arme principale** (Phantasma Prime), la secondaire devient une arme d'Overguard et de dégâts (Kuva Nukor), et la mêlée est une faux (Hate). Valeurs : wiki, au 25/10/2026.

**Phantasma Prime (primer principal, à la place de la Torid Incarnon)**

| Stat | Valeur |
|---|---|
| Faisceau | 6 rayons × 15 (5 Impact + 10 Radiation), **12 ticks/s**, hitscan, 25 m |
| Statut | 22,2 % par rayon (≈ 1,33 proc par tick sans mods) |
| Crit | 11 % / 1,9× |
| Perforation | **Infinie à travers les corps** (pas les surfaces) |
| Munitions | 0,5 par tick (6/s) ; 330 max ≈ 55 s de tir continu ; chargeur 11, reload 0,5 s |
| Polarités | Madurai, Madurai, Naramon (Exilus Madurai). **Vaultée** : reliques en stock, échange ou Prime Resurgence |

- **Pourquoi c'est pertinent** : au cap, ce sont les tourelles qui tuent, et la Torid n'est plus qu'un applicateur de statuts dont les dégâts s'effondrent avec ses stacks (×6,5, cf. 2.1). Phantasma Prime fait ce travail **sans dépendre des kills**.
  - Avec +200 % de statut (Galvanized Savvy + deux mods doubles 60/60), un rayon atteint 66,6 % : ≈ **4 procs par tick, ~48 par seconde**, sur **toute une ligne** d'ennemis.
  - C'est la même géométrie que les tourelles (perforation infinie des corps).
- **Éléments** : Toxic Barrage + Frigid Blast = **Viral** (+ Radiation innée, séparée) ; Toxic Barrage + Shell Shock = **Corrosive** (+ Radiation). La Radiation est résistée par les Corrupted, mais son statut (confusion) est un vrai contrôle au cap.
- **Synergie Escapist** : l'Impact représente 1/3 des dégâts de base, donc beaucoup de procs Impact, qui relèvent le seuil de Mercy (+8 % par proc).
- **Arcane** : **Primary Crux** (sur Weak Point : +30 % de statut et +6 % d'Ammo Efficiency par stack, 10 s, jusqu'à 10 stacks = +300 %). Primary Merciless n'a pas de sens sur un primer, et Primary Debilitate est moins efficace sur les faisceaux (wiki).
- **Contre** : 25 m (contre 37 m pour le rayon Incarnon de la Torid), crit faible, arme vaultée, munitions à surveiller (cap d'Ammo Efficiency à 75 %).
- **Verdict** : **meilleur primer de ligne que l'Epitaph**, mais sans l'AoE de 14,4 m ni le Cold forcé. Son vrai intérêt : il libère le slot secondaire pour le Kuva Nukor (arsenal B). Liste de mods complète et capacité non chiffrées ici.

**Kuva Nukor (secondaire, à la place de l'Epitaph Prime)**

| Stat | Valeur |
|---|---|
| Faisceau | 21 Radiation (+25 à 60 % d'élément Kuva selon le progéniteur), **10 ticks/s**, hitscan, 29 m |
| Chaînage | 2 ennemis à 9 m, 50 % des dégâts (les cadavres servent de relais) |
| Crit | 7 % / **5,0×** (multiplicateur le plus élevé du jeu) |
| Statut | 50 % ; inflige **Microwave** (statut invisible, compté comme un type distinct par Galvanized) |
| Munitions | Chargeur 77, reload 2 s, 210 max |
| Polarités | Aucune (Exilus Madurai) : Forma à prévoir. Obtention : Kuva Lich |

- **Pourquoi c'est pertinent** : la cadence de 10/s et le chaînage en font l'arme qui exploite le mieux **Secondary Fortifier** (vol d'Overguard continu sur plusieurs Eximus, au‑dessus du seuil de 2 tirs/s cité par le wiki).
  - En **Magnetic** (Frostbite + Jolt, + Radiation innée), il amplifie les dégâts sur l'Overguard (jusqu'à +325 % à 10 stacks) en plus du ×8 de Fortifier.
  - Le multiplicateur de 5× en fait aussi une vraie arme de dégâts. Le wiki conseille les bonus de crit plat (Secondary Enervate), mais ce slot d'arcane est pris par Fortifier : Primed Pistol Gambit fait monter le CC à ~20 %.
- **Ce que tu perds par rapport à l'Epitaph** : l'AoE de 14,4 m, le Cold et l'**Impact forcés** (seuil de Mercy pour Escapist), le Corrosive de 15,2 s. Le Nukor ne prime qu'une cible + 2.
- **Verdict** : l'Epitaph reste le primer par défaut de l'arsenal A. Le Nukor devient la bonne secondaire **dès que le primer passe en principale** (arsenal B).

**Hate Incarnon (mêlée, à la place du Glaive Prime)**

| Stat | Valeur |
|---|---|
| Base | 230 (161 Slash, 34,5 Impact, 34,5 Puncture), crit 30 % / 2,5×, statut 20 %, portée 2,8 m, 0,917 attaque/s |
| Heavy | Heavy Attack 1 380 ; Heavy Slam 690 Blast sur 9 m (Lifted forcé) |
| Incarnon (Évo I) | Combo 6× puis Heavy Attack : 180 s, conservé au bleedout. Les combos avant/neutre lancent une lame spectrale (60 m/s) qui explose en **Heat sur 3 m** après 0,4 s, sans auto‑stagger |
| Évolutions | II : Swordsman's Flourish / Stalker's Legacy (+30 de base) · III : Orokin Reach / Swift Break (+60 % de Wind Up) / Resolute Force · IV : Absolute Valor / Absolute Dominion / Subtle Force |
| Obtention | Plan sur le Stalker ; Incarnon Genesis : Circuit Steel Path, 120 platinum chez Cavalero |

- **Pour** : arme Slash (le Bleed ignore l'armure, utile sous Archaic Armor), Incarnon persistant, pas de micro lancer/rappel, lames à distance sans auto‑stagger.
- **Contre :**
  - Les lames spectrales **ne profitent pas** du +30 de base, du +100 % de l'Incarnon ni des mods de dégâts de mêlée (Pressure Point) : elles scalent mal au 9999.
  - Le reste du kit (Heavy, Slam) se joue **au contact**, là où le Glaive détone à distance.
  - L'attaque normale n'a pas d'Impact forcé (seul le Slam en a) : moins de Mercy pour Escapist.
- **Verdict** : le **Glaive Prime reste le BiS** de ce build (détonation à distance de 4,8 m, Impact + Slash forcés, crit calé sur Melee Duplicate). Hate Incarnon est une alternative de confort si tu ne veux pas gérer le lancer/rappel, ou contre l'armure non retirable.

**Arsenal B (primer en principale)**

| Slot | Arsenal A (défaut) | Arsenal B (inspiré des vidéos) |
|---|---|---|
| Principale | Torid Incarnon (nettoyage + Viral) — Primary Merciless | **Phantasma Prime** (primer de ligne) — **Primary Crux** |
| Secondaire | Epitaph Prime (primer AoE) — Encumber / Fortifier | **Kuva Nukor** (Magnetic, moteur d'Overguard) — **Secondary Fortifier** |
| Mêlée | Glaive Prime — Melee Duplicate | Glaive Prime (ou Hate Incarnon) |

- **B est plus fort contre les Eximus** (Magnetic + ×8 sur l'Overguard, Overguard du joueur entretenu en continu) et ne s'effondre pas quand le rythme de kills chute.
- **A garde l'avantage** en AoE de priming (Epitaph, 14,4 m), en Mercy (Impact forcé) et en accessibilité (Phantasma Prime est vaultée, le Nukor exige une Kuva Lich).
- Growing Power reste à 100 % d'uptime dans les deux cas (statuts d'arme en continu).

---

## 3. COMPAGNON & ARMEMENT

> Règles communes : **Synth Deconstruct** (25 % d'orbe de vie sur les ennemis blessés par le compagnon, donc +27 énergie via Equilibrium), **Tenacious Bond** (si le CC du compagnon est ≥ 50 % : **+1,2× Critical Damage final** sur *tes* armes : Glaive ×1,29, Torid ×1,185). **Jamais Guardian** (casse les gates). Le compagnon est éligible aux satellites : un Redirection côté compagnon les rentabilise.

### Option A — Nautilus Prime + Verglas Prime (contrôle / regroupement)

**Pourquoi :** **Cordon** regroupe les ennemis dans un rayon de 30 m autour de la cible (recharge 15 s). Les dégâts d'une tourelle montent de +100 % **par ennemi touché par tir** : regrouper k ennemis sur la trajectoire multiplie le gain par k. C'est la synergie Blaze Artillery la plus forte du jeu (le wiki la cite). **Sacrifice** compense en partie la perte de Temporal Anchor.

**Investissement :** Orokin Reactor · **2 Forma Vazarin** (polarités innées Penjaga ×4, Vazarin ×1) — **58/60**.

| # | Mod | Polarité / coût | Rôle |
|---|---|---|---|
| 1 | **Cordon** | Penjaga / 4 | Regroupement toutes les 15 s (moins avec Manifold) |
| 2 | **Assault Mode** | vierge / 5 | Verglas tire en continu : Growing Power à 100 % + Viral |
| 3 | **Vacuum** | Penjaga / 4 | Ramassage à 13,5 m : orbes du Dispensary et des Eximus |
| 4 | **Synth Deconstruct** | vierge / 9 | Orbes de vie → énergie |
| 5 | **Tenacious Bond** | vierge / 7 | +1,2× CD final (**exige le riven**, voir arme) |
| 6 | **Manifold Bond** | Vazarin (Forma) / 5 | Cordon applique les statuts de Verglas ; −3 s de recharge par kill d'un ennemi à ≥ 3 statuts (tourelles + Viral + Corrosive) |
| 7 | **Primed Regen** | Penjaga / 7 | −35 s de recharge du compagnon, 10 s d'invulnérabilité à la réapparition |
| 8 | **Sacrifice** | Penjaga / 5 | Te relève à 100 % santé + shields en 4 s quand tu tombes à terre (filet solo) |
| 9 | **Calculated Redirection** | Vazarin / 7 | +250 % shields du compagnon (shield gate du compagnon + satellites) |
| 10 | **Restorative Bond** | Vazarin (Forma) / 5 | Orbes de vie : +60 PV et −3 s de recharge du compagnon (Dispensary toutes les 6 s) |

**Verglas Prime** (Cold 32, CC 14 %, CD 2,2, Status 36 %, rayon 12/s, 24 m) — Orokin Catalyst · **4 Forma** (2 Madurai, 2 Vazarin ; Naramon innée) — **58/60** :

| Slot | Mod | Note |
|---|---|---|
| 1 (Naramon) | Critical Delay (+200 % CC) | |
| 2 (Madurai) | **Riven** avec **≥ +57,2 % CC** | 14 % × (1 + 2,0 + 0,572) = **50 %** → Tenacious Bond actif. Sans riven, plafond à 42 % : Tenacious impossible |
| 3 (Vazarin) | **Primed Cryo Rounds** (+165 % Cold) | **Ordre des éléments : 1er élément = Cold** (absorbe le Cold inné)… |
| 4 (vierge) | **Malignant Force** (+60 % Toxin / +60 % Status) | …**2e = Toxin → Viral** |
| 5 (Vazarin) | Galvanized Aptitude (+80 % Status) | Status 36 % × 2,4 = **86,4 % par tick à 12 ticks/s** |
| 6 (Madurai) | Serration (+165 %) | |
| 7 (vierge) | Vital Sense (+120 % CD) | |
| 8 (vierge) | Split Chamber (+90 % Multishot) | |

> **Sans riven** : retire Critical Delay et le Riven pour Galvanized Chamber + Rifle Elementalist, et remplace Tenacious Bond par **Contagious Bond**.

### Option B — Panzer Vulpaphyla (viral / immortalité)

**Pourquoi :** **Viral Quills** (6 épines à 20 m, 60 Viral, 40 % Status, spores qui propagent le Viral, recharge 4 s) met du Viral sur **toute** la map, ce qui amplifie chaque tick de Heat des tourelles de ×2 à ×4,25. **Panzer Devolution** : à terre, le Panzer passe en forme larvaire qui continue de tirer des épines Viral (60) pendant 30 s, puis reprend sa forme normale ; il ne quitte jamais le combat. **Tenacious Bond sans riven** grâce à Bite. **Tandem Bond** alimente le combo du Glaive.

**Investissement :** Gilding obligatoire avant toute Forma (Son, Necralisk : rang Acquaintance chez les Entrati, Vulpaphyla rang 30, 10 Son Token + 5 000 crédits) · Orokin Reactor · **3 Forma** (1 Vazarin, 2 Madurai ; 1 Penjaga innée) — **59/60**.

| # | Mod | Polarité / coût | Rôle |
|---|---|---|---|
| 1 | **Viral Quills** | vierge / 3 | Viral de masse |
| 2 | **Panzer Devolution** | vierge / 3 | Compagnon « immortel » |
| 3 | **Tenacious Bond** | vierge / 7 | CC griffes 107,5 % ≥ 50 % → **+1,2× CD final** |
| 4 | **Tandem Bond** | vierge / 7 | Chaque coup de griffe = **+6 combo** pour ton Glaive ; tes Heavy donnent +30 % × multiplicateur de combo aux dégâts de mêlée du compagnon pendant 30 s |
| 5 | **Synth Deconstruct** | Madurai (Forma) / 5 | Orbes → énergie |
| 6 | **Vicious Bond** | Madurai (Forma) / 5 | Les coups de griffe retirent 15 % d'armure ; les ennemis récemment touchés par une compétence (tourelles) propagent l'effet à 9 m |
| 7 | **Contagious Bond** | vierge / 9 | Kill du compagnon sur cible sous statut → 50 % des statuts propagés à 9 m |
| 8 | **Fetch** | Penjaga / 4 | Ramassage à 13,5 m |
| 9 | **Restorative Bond** | vierge / 9 | Synergie Dispensary |
| 10 | **Link Redirection** | Vazarin (Forma) / 7 | +125 % des shields de Protea (+1 537) : le gate du compagnon et les satellites deviennent utiles |

**Panzer Claws** (Slash 45 + Toxin 45, CC 25 %, CD 2,0, Status 12,5 %) — Orokin Catalyst · **3 Forma Madurai** (calculé sans polarité innée) · posture Penjaga (+10) — **66/70** :

| Slot | Mod | Note |
|---|---|---|
| Posture | **Protector Posture** | Cible les ennemis à ≤ 15 m de toi (reste dans ta zone Dispensary/tourelles) ; +4 statuts Puncture |
| 1 | **Bite** (+330 % CC / +220 % CD) | CC **107,5 %**, CD 6,4 → Tenacious Bond actif |
| 2 | Maul (+330 % Melee Damage) | |
| 3 | Precision Conditioning (+385 % Melee Damage, physique converti en Slash) | Le Bleed ignore l'armure |
| 4 | **Sepsis Claws** (+330 % Toxin / +330 % Status) | Même élément que la Toxin innée : aucune perte à la conversion. Toxin = ignore les shields Corpus |
| 5 | Venom Teeth (+60 % Toxin / +60 % Status) | Status 12,5 % × 4,9 = **61 %** |
| 6 | Cull the Weak (+60 % par type de statut ; +240 % sur coup non critique) | |
| 7 | Immunity Resistance (+50 % Status Damage) | |
| 8 | Bloodthirst (100 PV volés par coup et par stack de Slash) | Tient le compagnon en vie |

### Verdict comparatif

| Critère | A — Nautilus Prime | B — Panzer Vulpaphyla |
|---|---|---|
| Dégâts des tourelles | **★★★** (Cordon = k ennemis par tir) | ★★ (Viral ×2 → ×4,25 sur la Heat) |
| Tenacious Bond | Riven obligatoire | **Gratuit** (Bite) |
| Survie du joueur | **Sacrifice** (relève) | Aucune relève |
| Présence au 9999 | Sentinelle souvent détruite (Primed Regen) | **Jamais hors combat** (Devolution) |
| Synergie Glaive | — | **Tandem Bond** (combo) |
| **Quand le prendre** | Endurance en couloirs (Survival, Defense, Mirror Defense, Disruption) **tant que la sentinelle survit** | **Obligatoire au 9999** ; aussi sans riven, ou avec un loadout centré sur le Glaive |

**Correction v1.1 : l'option A n'est pas une option level cap.** Nautilus Prime a 560 PV et 350 shields (1 225 avec Calculated Redirection) : au 9999, un coup suffit à la mettre à terre. À terre, il n'y a plus de Cordon, plus d'Assault Mode (Growing Power ne repose plus que sur l'Epitaph) et plus de Sacrifice ; seul Vacuum continue de fonctionner. Le comportement de Tenacious Bond quand le compagnon est à terre n'est pas documenté.

**Option B, ajout possible :** **Martyr Symbiosis** (précepte Vulpaphyla, coût 3) à la place de Restorative Bond. Il stocke de la santé sur les cadavres et se sacrifie pour te soigner sous 10 % de santé (1 s d'invulnérabilité), et le wiki indique qu'il se déclenche **avant** Arcane Escapist sans consommer ses stacks. Son comportement face à un one‑shot depuis la santé pleine n'est pas documenté. **En variante C** (sans Dispensary), Restorative Bond perd sa synergie : Martyr Symbiosis y devient le choix par défaut.

---

## 4. VARIANTES D'ENNEMIS & HIÉRARCHIE DES DÉGÂTS

### 4.1 Faiblesses (Update 36+ : vulnérable = ×1,5, résistant = ×0,5)

| Faction | Vulnérable | Résistant | Impact sur ce build |
|---|---|---|---|
| Grineer | Impact, **Corrosive** | — | Corrosive via Epitaph |
| Kuva Grineer | Impact, **Corrosive** | **Heat** | **Tourelles ×0,5** : la mêlée et Roar prennent le relais |
| Corpus | Puncture, **Magnetic** | — | Shields : Toxin les ignore, Viral non |
| Corpus Amalgam | Electricity, **Magnetic** | **Blast** | Détonation du Glaive ×0,5 |
| Infested | Slash, **Heat** | — | Tourelles ×1,5 : **la meilleure en dégâts, la pire en survie** (Toxin partout : Toxic Ancient, Mutalist Osprey, Septic Eximus) |
| Infested (Deimos) | **Blast**, **Gas** | **Viral** | Retire le Viral |
| Corrupted (Orokin) | Puncture, **Viral** | Radiation | **Loadout par défaut = optimal** |

### 4.2 Swaps par faction (coûts de capacité vérifiés, sans Forma supplémentaire)

| Faction | Torid Incarnon | Epitaph Prime | Glaive Prime |
|---|---|---|---|
| Corrupted | Défaut (Viral) | Défaut (Corrosive) | Défaut (Viral) |
| Grineer / Kuva | Config **Corrosive** (cf. 2.1 : Rifle Elementalist + High Voltage, 57/60) | Défaut (Corrosive, prime **en priorité**) | North Wind → **Voltaic Strike** = **Corrosive** (×1,5) |
| **Level cap 9999 (toutes factions)** | Config **Magnetic** (Overguard des Eximus) | Défaut | Défaut, ou Magnetic (ligne Corpus) contre l'Overguard |
| Corpus / Amalgam | Malignant Force → **High Voltage** = **Magnetic** + Toxin innée séparée (ignore les shields) | Pistol Pestilence → **Frostbite** = **Magnetic** | Primed Fever Strike → **Voltaic Strike** (+1 capacité, 70/70) = **Magnetic** |
| Infested (Deimos) | Malignant Force → **Thermite Rounds** = **Blast** + Toxin innée | Défaut | North Wind → **Volcanic Edge** = **Gas** (Blast natif ×1,5 aussi) |

Menaces de faction prioritaires :

- **Corpus Nullifier** : les tourelles **ne visent pas** les ennemis dans la bulle, et entrer dans la bulle dissipe tes buffs. Éclate‑la au rayon de la Torid ou à l'explosion du Glaive avant d'avancer.
- **Toxic Ancient** : −80 % de dégâts Toxin pour les alliés dans son aura, et Toxin = dégâts sur la santé.
- **Ancient Disruptor** : draine l'énergie et pose du Magnetic. **Kill immédiat.**

### 4.3 Unités Eximus

- **Overguard** : immunisé aux CC, **le Viral ne touche pas l'Overguard**. Le **Magnetic** amplifie les dégâts sur l'Overguard (+100 % au 1er stack → +325 % à 10 stacks) et inflige des dégâts Electricity à sa rupture. Le Cold fonctionne jusqu'à 4 stacks.
  - Swap anti‑Eximus = le swap Corpus (Magnetic). Encumber pose aussi du Magnetic au hasard.
  - **v1.2 : Secondary Fortifier** (cf. 1.12) multiplie par ×8 les dégâts de la secondaire sur l'Overguard, et chaque tranche de 100 dégâts sur l'Overguard ennemi te rend 1 Overguard (plafond 15 000). Au cap, c'est la meilleure réponse aux Eximus, et elle te protège en même temps.
- **Ordre de kill au cap** :
  1. **Septic / Venomous** : aura Toxin de 3,5 m avec proc Toxin garanti, qui ignore les shields. Tue‑les **à distance**, jamais au contact.
  2. **Energy Leech / Parasitic** : zone qui s'effondre en 3 s avec dégâts **Magnetic** et proc garanti (shields détruits, énergie drainée). Sors de la zone, et Rolling Guard si tu prends le proc.
  3. **Leech / Sanguine** : zone de 3 m qui draine 5 % de la santé max par tick. Sors‑en.
  4. **Blitz** : onde de choc → Primed Sure Footed la neutralise.
  5. **Arctic** : bulle de glace → les nuages de la Torid (mode normal) la traversent.
  6. **Entropic** (U44) : bulle quasi impénétrable → entre dedans et détone le Glaive à l'intérieur.
- **Bonus** : chaque Eximus lâche **1 Large Energy Orb (50) + 2 Health Orbs garantis**, soit ≈ **+104 énergie** avec Equilibrium (50 + 2 × 27).

### 4.4 Hiérarchie des multiplicateurs (au niveau cap)

Formule simplifiée : `Dégâts = Base × (1+Σ%Base) × Multishot × (1+Σ%Élém) × Crit × (1+Faction) × Armure × Viral [× Combo × Duplicate en mêlée]`. Chaque parenthèse est un **bucket multiplicatif** : investis dans le bucket le moins rempli.

1. **Réduction d'armure** (contre les ennemis blindés, armure plafonnée à 2 700). Réduction des dégâts ennemie = `90 % × √(Armure/2700)`.
   - Heat seule (tourelles, −50 %) : **×3,64**.
   - Corrosive ×10 (Epitaph, −80 %) : **×5,98**.
   - Corrosive + Heat : **≈ ×7,15**.
   - Armure retirée à 100 % : ×10.
   - **Priorité n°1 contre Grineer et Corrupted.**
2. **Faction (Roar)** : ×1,80 → ×2,28 sur le direct, **×3,25 → ×5,22 sur les DoT** (double application).
3. **Viral** : ×2,00 (1 stack) → **×4,25** (10 stacks) sur la santé. Inutile sur shields et Overguard.
4. **Critical Damage / palier de crit** : Tenacious Bond (+1,2 final) = ×1,29 Glaive, ×1,185 Torid ; Melee Duplicate ×1,60.
5. **Éléments** : bucket additif. Important pour *choisir* le type (faiblesses), moins pour empiler.
6. **Dégâts directs (base %)** : le bucket **le plus saturé** (Serration 165 + Merciless 360 + Galvanized : +40 % par type de statut et par stack). +165 % dessus ne vaut que ×1,2–1,3.
7. **Slash** : le Bleed (dégâts Cinematic) **ignore l'armure mais pas les shields** (correction v1.1 : c'est le Toxin qui traverse les shields). Son intérêt est **inversement proportionnel** à ton retrait d'armure : roi tant que l'armure est pleine, marginal une fois à −80/−100 %. Les procs Slash forcés du Glaive et les griffes en Slash servent de filet de sécurité contre les Grineer et Corrupted blindés.

### 4.5 Modificateurs de mission qui cassent le build (ajout v1.1)

| Modificateur (source) | Effet sur ce build | Réponse |
|---|---|---|
| **Stunted Shields** (Icebind, **trait standard**, niveau 999+) | Gate 2,5 → **1,25 s** | Entrer dans le satellite suivant à ~1 s ; Arcane Escapist obligatoire |
| **Cryogenic Leakage** (aléa d'environnement, −50 % de shields) | 615 shields → gate 1,78 s (2,25 s si appliqué avant les shards) | Sortir de la zone, timing satellites à ~1,5 s |
| **Anemic Shields** (Archimedea, plafond 500) | Gate 1,59 s | Idem |
| **Flankable** (Icebind, −75 % de shields) | Gate 1,25 s (0,63 s avec Stunted) | Reste face aux ennemis (bouclier Volt frontal) ; build à éviter |
| **Bruised Shields** (Icebind : shields restaurés uniquement par la mêlée) | **Satellites inopérants** | Melee Assimilation sur le Glaive (les kills Heavy rendent 30 % des shields) ; l'Overguard de Secondary Fortifier n'est pas un shield et devrait rester utilisable (à tester) ; sinon, autre Warframe |
| **Untreatable** (Icebind : Health Orbs non ramassables) | Énergie Dispensary : 37,5 → **6,5/s** | Sculptor garde le build à +1,1/s ; zéro marge. **Variante C** (1.11) : non concernée, elle ne dépend pas des Health Orbs |
| **Constricted** (Icebind : énergie max −75 %) | Max 62,5 | Jouable **uniquement** avec Sculptor (cast max 18,75) |
| **Framecurse Syndrome** (Icebind / Archimedea : 50 PV + 150 shields par cast) | ~27 casts/min : −1 350 PV/min | Réduire les recasts de tourelles ; build à éviter |
| **Abbreviated Abilities** (Icebind : −50 % de durée) | Tourelles 4,3 s, Roar 42,6 s, Dispensary 35,5 s | Variante Duration impossible à compenser ; accepter |
| **Miasmic Militia** (Icebind : ennemis immunisés Toxin/Gas/Viral/Corrosive) | Tout le plan de statuts tombe | Torid Magnetic, Glaive Magnetic |
| **Archaic Armor** (Icebind : armure non retirable) | Corrosive et Heat ne retirent plus d'armure | Slash (ignore l'armure) |
| **Inferno** (Icebind : la Heat nourrit l'Inferno) | **La Heat des tourelles est une menace** | Build à éviter |
| **Decaying Dragon Key** | Gate à 0,33 s | Ne jamais l'équiper |

---

## 5. MÉCANIQUES CLÉS & GAMEPLAY LOOP

### 5.1 Pourquoi Archon Stretch ne se déclenche pas sur les tourelles

- **Condition exacte** : une **compétence** (de Warframe ou de compagnon) doit infliger des dégâts **Electricity**, ou un statut Electricity (y compris celui forcé par le Magnetic). Effet : +2 énergie/s pendant 5 s (10 au total), **non cumulable, non rafraîchissable**, et **chaque cast coupe la régénération pendant 1 s**.
- **Blaze Artillery** inflige **uniquement de la Heat** (100 % de statut Heat). Grenade Fan inflige du Slash, Temporal Anchor du Blast, Dispensary et Roar rien. **Protea n'a aucune source native d'Electricity** : l'effet ne se déclenche **jamais** par ses compétences.
- **Même déclenché**, il vaudrait 10 énergie par fenêtre, amputés par tes recasts de tourelle toutes les ~2,8 s, contre **110 énergie par Empowered Health Orb** avec Equilibrium. Valeur nulle.
- **Seules façons de le déclencher sur Protea** (toutes externes) : Panzer Vulpaphyla Viral Quills avec **Shocking Claws**, Dethcube Vaporize avec une arme de compagnon moddée Electricity, Manifold Bond avec une arme Electricity, le mod Retribution.
- **Conclusion** : Stretch (coût 9) à la place d'Archon Stretch (coût 16) pour le même +45 %.

### 5.2 Comportement réel d'Archon Vitality sur Blaze Artillery

- Texte exact : *« Status Effects from abilities that deal Heat Damage will be applied twice »*. **Chaque application** de statut Heat par la compétence ajoute **1 stack supplémentaire aux mêmes dégâts**.
- Blaze Artillery a **100 % de chance de statut** : **2 stacks de Heat par tir et par ennemi touché**, sur toute la ligne (perforation infinie) + l'AoE de 2 m. Une tourelle = 3 tirs/s, donc **6 stacks/s** par ennemi dans sa ligne.
- Chaque stack inflige ses ticks (1 s de délai puis 1 tick/s pendant 6 s) **à partir des dégâts du tir qui l'a posé**, multiplicateur de tourelle inclus. Les stacks posés en fin de vie de la tourelle sont énormes, et doublés par AV.
- **Ce qu'AV ne fait pas :**
  - Le retrait d'armure de la Heat reste **plafonné à 50 %** (rampe 15/30/40/50 % sur 2 s), quel que soit le nombre de stacks.
  - Le stack bonus ne génère pas de stacks de Cascadia Flare ni d'Arcane Hot Shot.
- **Avec Roar** : chaque tick est multiplié par (1+Roar)², soit ×5,22 au maximum. AV double un DoT déjà élevé au carré : **c'est le cœur des dégâts du build.**
- L'effet secondaire d'AV est indépendant du rang. On garde quand même R10 pour le +100 % de Health (370 → 740).

### 5.3 Séquence de combat en Endurance (pas à pas)

**Phase 0 — Ouverture (0–10 s)**

1. **Epitaph** (non chargé) sur le premier groupe → Growing Power actif (6 s) + Corrosive.
2. **Grenade Fan, satellites** → 38,75 énergie (le seul cast plein tarif). Passif : 1. **Attends que les grenades aient atterri et que les satellites apparaissent** : un objet ne déclenche Sculptor qu'une fois posé.
3. **Dispensary** (18,75 une fois Sculptor actif, 116,25 si tu le lances trop tôt) près de ta position d'ancrage. Passif : 2.
4. **Blaze Artillery** face à la voie d'arrivée principale (12,5). Passif : 3.
5. **Roar** (18,75) → **4e cast = +110 %** (+128 % une fois Molt plein, configuration Endurance). 85 s.

**Phase 1 — Montée (0 → 250 kills, Molt)**

- Complète les **3 tourelles** sur **3 voies qui ne se chevauchent pas** (le wiki : empiler 3 tourelles au même endroit ne fait que ×2 de DPS, pas ×3).
- Place‑les **bas, au niveau des ennemis**, alignées sur l'axe d'un couloir (perforation infinie des corps).
- Pose des **Shrapnel Vortex** (*hold* ou *tap* selon ton réglage) aux étranglements : stagger à 100 % par tick, ils « canalisent » les ennemis dans les lignes de tir.

**Phase 2 — Boucle stable**

| Action | Fréquence | Détail |
|---|---|---|
| Recast de la tourelle la plus ancienne | toutes les ~2,8 s | Garde 3 tourelles actives ; garantit aussi Sculptor |
| Satellites | toutes les 10–13 s, ou dès qu'un gate consomme le tien | Lance‑les à 4–6 m : « stations de recharge » |
| Tir d'Epitaph | toutes les ≤ 6 s | Growing Power permanent + Corrosive (15,2 s) |
| Détonation du Glaive | sur chaque groupe à ≤ 5 m | Les kills alimentent Galvanized Reflex (combo ×6 si 4 kills en 20 s, plancher ×2 ; Tandem Bond le maintient) |
| Torid Incarnon | trash / couloirs | 5 grenades directes pour recharger |
| Dispensary | toutes les 71 s | Reste dans l'anneau d'apparition ; ramasse l'**Ammo Pack avec l'arme qui en a besoin équipée** (il ne recharge que l'arme en main) |
| Roar | toutes les 85 s | Alignement du passif (cf. 1.7) |

**Phase 3 — Protocole Level Cap (dès qu'une rafale vide tes 1 230 shields d'un coup, jusqu'au 9999)**

1. **Jamais à 0 shield sans satellite accroché.** Avant chaque engagement, vérifie le buff satellite. Le satellite est **proactif**, jamais réactif : le cast + le vol des grenades laissent une fenêtre non couverte.
2. **Gate déclenché** (barre de vie grise, **2,5 s garantis**) : repositionne‑toi et relance pendant le gate. **Entre dans un satellite libre à ~2 s** (~1 s sous Stunted Shields). Si ton test confirme les 5 s, tu peux attendre ~4,5 s.
3. **Rolling Guard** sur tout proc **Toxin** (traverse les shields) ou **Magnetic**, et sur les DoT Slash/Heat qui mangent tes satellites. Pour couvrir un trou, enchaîne gate (2,5 s) → RG (3 s) → satellite. Ne superpose **jamais** RG et un gate (gaspillage).
4. **Casts à animation lourde** (Grenade Fan = animation corps entier avec saut forcé de 1 m) : lance‑les **pendant** un gate ou une RG.
5. **Stacks d'Arcane Escapist** : fais un Mercy kill dès que l'invite apparaît sur une unité lourde (seuil relevé par les Impact du Glaive et de l'Epitaph). Vise 9 stacks avant de pousser le niveau.
6. **Overguard (Secondary Fortifier, v1.2)** : sur chaque Eximus, remplis ton Overguard **avant** de le tuer. Tant qu'il tient, un tir Toxin ne passe pas. Évite de le recharger pendant un shield gate (interaction non documentée, cf. 1.12).
7. **Ordre de kill** : Septic/Venomous Eximus → Energy Leech Eximus → Toxic Ancient / Ancient Disruptor → Nullifier → unités à knockdown de zone.

### 5.4 Moments critiques

| Situation | Réponse immédiate |
|---|---|
| **0 shield, aucun satellite, RG disponible** | **RG d'abord** (3 s), puis pendant la RG : satellites à 4–6 m, et entre dans l'un d'eux avant la fin de la RG |
| **0 shield, aucun satellite, RG en recharge** | **Protective Sling** si tu as une seconde à couvert : Transference → Void Sling à travers ta Warframe → retour = 5 s d'invulnérabilité pour reposer des satellites à 4–6 m. Sinon, dernier recours : satellites **à tes pieds**. Sous un feu nourri, les 4 s'accrocheront et seront détruits en chaîne : prévois **2 casts** et compte sur Arcane Escapist |
| **Variante C : rembobinage imminent dans une zone dangereuse** | Maintiens 4 (destruction de l'ancre sans rembobinage) et repose‑la ici. Tu perds le remboursement de la fenêtre, pas ta position |
| **Sculptor retombé** (aucun objet créé depuis 12 s, ex. long trajet entre objectifs) | 1er cast = **Grenade Fan** (le moins cher), *jamais* Roar ni Dispensary plein tarif (116,25) |
| **Énergie basse** | Marche sur le Dispensary : 1 Empowered Health Orb = 110 énergie. Chaque Eximus tué ≈ +104 |
| **Proc Magnetic** (Corpus, Energy Leech) | **RG immédiate** : le Magnetic réduit la régénération naturelle, amplifie les dégâts sur shields et draine l'énergie |
| **Kuva Grineer** (Heat résistée) | Primer Corrosive à fond (ou Torid en config Corrosive), la détonation du Glaive devient ta source de dégâts n°1, Roar au passif impératif |
| **Nullifier qui avance** | Éclate la bulle **avant** qu'elle touche tes tourelles ou toi (elle dissipe Roar) |
| **Compagnon qui vole tes satellites** | Lance tes satellites du côté opposé au compagnon |

### 5.5 Erreurs qui tuent ce build

- Jouer Brief Respite, le set Augur, Guardian, Fast Deflection ou Catalyzing Shields (ils raccourcissent tes gates).
- Superposer les 3 tourelles au même endroit.
- Ouvrir une mission (ou relancer après un trajet) avec un cast à 116,25.
- Lancer Roar sans Growing Power actif (−7,5 points de Roar) ou hors du 4e cast (−30 points).
- Rester dans le rayon de 3,95 m d'un satellite libre pendant un gate.
- Bâtir un timing sur un gate de 5 s non vérifié (erreur de la v1.0).
- Jouer au cap avec l'option A (sentinelle) ou sans Arcane Escapist.
- Considérer les Infested comme une faction « facile » : leur Toxin ignore toute ta couche défensive.
- Lire les chiffres de dégâts du guide comme des valeurs de travail : ce sont des plafonds à stacks pleins.
- Équiper Temporal Artillery dans la configuration A : sans Temporal Anchor dans le kit, l'augment ne fait rien.
- Lancer Guardian Shell (Vazarin) : Guardian Break coupe tes gates.
- En variante C, ramasser des orbes pendant l'ancre en croyant les garder : le rembobinage les efface.

---

## Sources (wiki officiel, consulté le 25/10/2026)

- Compétences : [Grenade Fan](https://wiki.warframe.com/w/Grenade_Fan) · [Blaze Artillery](https://wiki.warframe.com/w/Blaze_Artillery) · [Dispensary](https://wiki.warframe.com/w/Dispensary) · [Temporal Anchor](https://wiki.warframe.com/w/Temporal_Anchor) · [Temporal Artillery](https://wiki.warframe.com/w/Temporal_Artillery) · [Roar](https://wiki.warframe.com/w/Roar) · [Protea Prime](https://wiki.warframe.com/w/Protea/Prime)
- Survie : [Shield (Shield Gating)](https://wiki.warframe.com/w/Shield) · [Rolling Guard](https://wiki.warframe.com/w/Rolling_Guard) · [Primed Sure Footed](https://wiki.warframe.com/w/Primed_Sure_Footed) · [Overguard](https://wiki.warframe.com/w/Overguard) · [Armor](https://wiki.warframe.com/w/Armor) · [Enemy Level Scaling](https://wiki.warframe.com/w/Enemy_Level_Scaling)
- Mods / arcanes / shards : [Archon Vitality](https://wiki.warframe.com/w/Archon_Vitality) · [Archon Stretch](https://wiki.warframe.com/w/Archon_Stretch) · [Equilibrium](https://wiki.warframe.com/w/Equilibrium) · [Growing Power](https://wiki.warframe.com/w/Growing_Power) · [Arcane Sculptor](https://wiki.warframe.com/w/Arcane_Sculptor) · [Molt Augmented](https://wiki.warframe.com/w/Molt_Augmented) · [Arcane Energize](https://wiki.warframe.com/w/Arcane_Energize) · [Archon Shard](https://wiki.warframe.com/w/Archon_Shard) · [Module:Mods/data](https://wiki.warframe.com/w/Module:Mods/data)
- Armes : [Torid Incarnon Genesis](https://wiki.warframe.com/w/Torid_Incarnon_Genesis) · [Epitaph](https://wiki.warframe.com/w/Epitaph) · [Glaive Prime](https://wiki.warframe.com/w/Glaive_Prime) · [Heavy Attack](https://wiki.warframe.com/w/Heavy_Attack) · [Melee Duplicate](https://wiki.warframe.com/w/Melee_Duplicate) · [Melee Assimilation](https://wiki.warframe.com/w/Melee_Assimilation) · [Primary Merciless](https://wiki.warframe.com/w/Primary_Merciless) · [Secondary Encumber](https://wiki.warframe.com/w/Secondary_Encumber)
- Compagnons : [Panzer Vulpaphyla](https://wiki.warframe.com/w/Panzer_Vulpaphyla) · [Verglas Prime](https://wiki.warframe.com/w/Verglas_Prime) · [Tenacious Bond](https://wiki.warframe.com/w/Tenacious_Bond) · [Bond Mods](https://wiki.warframe.com/w/Bond_Mods)
- Factions / Eximus : [Damage/Overview Table](https://wiki.warframe.com/w/Damage/Overview_Table) · [Eximus](https://wiki.warframe.com/w/Eximus)
- Patchs : [Update 43](https://wiki.warframe.com/w/Update_43) · [Update 44](https://wiki.warframe.com/w/Update_44)
- Ajouts v1.1 : [Arcane Escapist](https://wiki.warframe.com/w/Arcane_Escapist) · [Mercy](https://wiki.warframe.com/w/Mercy) · [Slash Damage](https://wiki.warframe.com/w/Damage/Slash_Damage) · [Toxin Damage](https://wiki.warframe.com/w/Damage/Toxin_Damage) · [Magnetic Damage](https://wiki.warframe.com/w/Damage/Magnetic_Damage) · [Protea Passive](https://wiki.warframe.com/w/Protea/Abilities/Passive) · [Deep Archimedea](https://wiki.warframe.com/w/Deep_Archimedea) · [Martyr Symbiosis](https://wiki.warframe.com/w/Martyr_Symbiosis)
- Ajouts v1.2 (wiki) : [Temporal Artillery](https://wiki.warframe.com/w/Temporal_Artillery) · [Temporal Anchor](https://wiki.warframe.com/w/Temporal_Anchor) · [Blaze Artillery](https://wiki.warframe.com/w/Blaze_Artillery) · [Secondary Fortifier](https://wiki.warframe.com/w/Secondary_Fortifier) · [Overguard](https://wiki.warframe.com/w/Overguard) · [Vazarin](https://wiki.warframe.com/w/Vazarin) · [Protective Sling](https://wiki.warframe.com/w/Protective_Sling) · [Transference](https://wiki.warframe.com/w/Transference) · [Phantasma Prime](https://wiki.warframe.com/w/Phantasma_Prime) · [Phantasma](https://wiki.warframe.com/w/Phantasma) · [Primary Crux](https://wiki.warframe.com/w/Primary_Crux) · [Primary Debilitate](https://wiki.warframe.com/w/Primary_Debilitate) · [Kuva Nukor](https://wiki.warframe.com/w/Kuva_Nukor) · [Hate](https://wiki.warframe.com/w/Hate) · [Arcane Enhancement](https://wiki.warframe.com/w/Arcane_Enhancement)
- Vidéos croisées en v1.2 (non visionnées, cf. en‑tête) : [« [WARFRAME] PROTEA PRIME vs Level 9999 – You Can Make Tea While Playing »](https://youtu.be/RmMHVDMDNG4) (SyrexLeon Gaming) · [« Why Protea NEVER Leaves S-Tier »](https://youtu.be/fJbfRbPUTW8) (RexChamp Sean)

---

## Journal des versions

**v1.2 (25/10/2026)** — croisement avec deux vidéos (SyrexLeon Gaming, RexChamp Sean) :

1. Temporal Artillery : inutilisable dans la configuration A (pas de Temporal Anchor). Nouvelle **variante C** : Roar à la place de Dispensary, Temporal Anchor + Temporal Artillery à la place d'Equilibrium (69/74, 6 Forma). Candidate au 9999 sous réserve de 3 tests (1.11).
2. Comparatif tourelle suiveuse (plafond 20×) / tourelle fixe : seuil à ~1,6 ennemi par tir ; jusqu'à −22 % de dégâts de tourelles en couloir dense.
3. Économie d'énergie de la variante C chiffrée (remboursement au rembobinage, −1,1/s net), avec ses pièges (orbes effacées, Nullifier).
4. **Secondary Fortifier** sur l'Epitaph au level cap (Overguard jusqu'à 15 000 : arrête le Toxin, ×8 sur l'Overguard des Eximus) ; Secondary Encumber conservé en Endurance.
5. École de Focus **Vazarin** ajoutée (Protective Sling 5 s, Mending Soul ×4) ; **Guardian Shell** ajouté aux interdits.
6. **Arcane Escapist conservé** : Fortifier et Vazarin s'ajoutent sans le remplacer. Pile de filets ordonnée (1.12), protocole level cap et moments critiques mis à jour.
7. Arsenal alternatif évalué (2.4) : Phantasma Prime (primer de ligne, Primary Crux), Kuva Nukor (Fortifier, Magnetic), Hate Incarnon. Arsenal B défini ; l'arsenal A reste le défaut.
8. Limite : vidéos non visionnées depuis l'environnement de rédaction ; leurs listes de mods exactes ne sont pas reprises.

**v1.1 (25/10/2026)** — corrections issues de [l'audit hostile](audit-protea-prime-v1.md) :

1. Gate de satellite : 2,5 s garantis, doublement à 5 s marqué non confirmé (description in‑game : « double minimum »), timing d'entrée ramené à ~2 s.
2. Slash : ignore l'armure, pas les shields (seul le Toxin traverse les shields). Les DoT ennemis mangent les satellites.
3. Ajout d'Arcane Escapist (anti‑mort) à la place de Molt Augmented au cap.
4. Procédure d'urgence satellite réécrite (RG d'abord ; « à tes pieds » en dernier recours seulement).
5. Torid : configurations Corrosive (Grineer) et Magnetic (défaut au cap) ; avertissement sur l'effondrement des stacks (×6,5).
6. Glaive : plancher de combo ×2 annoncé, ×6 conditionnel.
7. Infested : meilleure faction en dégâts, pire en survie.
8. Passif sur l'Helminth : à vérifier en jeu ; règle survie > passif.
9. Nouvelle section 4.5 : modificateurs de mission.
10. Ouverture : attendre l'atterrissage des grenades avant le cast suivant (Sculptor).
11. Option A limitée à l'Endurance ; option B obligatoire au 9999 ; Martyr Symbiosis en option.
12. Variante Amber Casting Speed pour le cap.

**v1.0 (25/10/2026)** — version initiale.
