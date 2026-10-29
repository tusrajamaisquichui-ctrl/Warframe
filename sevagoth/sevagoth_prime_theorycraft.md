# Sevagoth Prime : theorycraft complet et auditable

**Version 2.0 du 29/10/2026.** Patch **Hotfix 44.1.4.1** (« Iceblade of Narin : The Icebind »), en ligne sur PSN depuis le 28/10/2026.
Build acté : **F1 « Faucheuse invisible »**. Modèle de calcul : [`sevagoth_model.py`](sevagoth_model.py) (sections M1 à M18). Sortie brute : [`model_output.txt`](model_output.txt). Paramètres et sources : [`model_params.txt`](model_params.txt).

Étiquettes : **CONF** = wiki officiel ou patch notes · **COMM** = communauté · **DÉD** = déduit par le modèle · **TEST** = à mesurer en jeu · **NON TROUVÉ** = aucune source.

---

## Changelog v1 → v2

Les quatre retours de l'audit externe ont été vérifiés : **aucun n'est faux**.

| # | Changement | Pourquoi | Étiquette |
|---|---|---|---|
| 1 | **Formule du one-shot confirmée** : 0,25 × (1 + 0,5 × Force) × (1 + 0,3 × Force), écart nul avec le script. Seuil exact **254,0 %** (v1 : arrondi à 255 %) | Retour d'audit 1 | DÉD (contrôle M11) |
| 2 | **Éclats réalistes :** Taubound vend un seul Crimson tauforgé. Nouveau tableau à 7 états (M12) : 4 Crimson normaux = **0,996** (raté, 5 kills de Molt) ; 1 tauforgé + 3 normaux = **1,016** (passe) | Retour 1 confirmé | CONF (boutique) + DÉD |
| 3 | **Sources de Crimson tauforgés chiffrées** : environ **1,45 équivalent tauforgé par semaine** en Archimedea Elite, **0,99** sans Elite. Les 3 tauforgés manquants prennent **2 à 3 semaines** en espérance | Retour 1 | CONF (tables de drop) + DÉD |
| 4 | **Overguard :** l'interaction avec le % de Sow+Reap est **non documentée**. T1 est réécrit pour le Simulacrum PS5, et un plan B est classé | Retour 2 | NON TROUVÉ → TEST |
| 5 | **Correction v1 :** « Eximus = 2 Reap » était faux. Il faut **2 détonations, soit 3 Reap** (Reap → Sow → Reap → Reap, plus un Sow si T6 montre qu'il est consommé) | Relecture du modèle | DÉD |
| 6 | **Portée :** 100 % suffit en S1 et S3. En endurance (S2), échanger Augur Secrets contre Stretch (+45 %) double l'aire de Sow et Gloom (×2,1) pour un coût négligeable (Molt rattrape la marge en 21 kills) | Retour 3 | CONF (rayons) + DÉD |
| 7 | **Huras Kubrow :** un compagnon ne meurt plus. À 0 PV, il est neutralisé 60 s, puis revient avec 5 s d'invulnérabilité. Mods de survie listés, T4 réécrit | Retour 4 | CONF |
| 8 | **Énergie :** sans Arcane Energize, F1 n'est pas viable (−4,73 énergie/s même Gloom coupé). Energize et Molt passent en tête de farm, Seismic Bond juste après | Nouveau modèle de paliers (M15) | DÉD |
| 9 | Plan de progression P0 → P5, ordre des Forma, calendrier Taubound (**918 Moonflesh** nécessaires) | Demande v2 | DÉD |
| 10 | F2 et F3 archivées (annexe A), le choix F1 étant acté | Demande v2 | – |
| 11 | Script : sections M11 à M18 ajoutées ; libellé Eximus de M1 corrigé ; Cunning Drift, Augur Reach et Continuity ajoutés aux mods | – | – |

Conflit de sources relevé : la page wiki « Effects Scaling With Enemy Stats » parle de « 25 % des PV **max** ». Les pages Reap et Sow, plus détaillées (processus en 4 étapes), disent « PV **actuels** ». La v2 garde « actuels » ; T1 tranche au passage.

---

## 1. Verdict

1. **Build : F1 « Faucheuse invisible »** = Reap / Sow / Gloom / **Roar à la place d'Exalted Shadow**, avec un Huras Kubrow (invisibilité et Seismic Bond).
2. **Cible :** 4 Crimson tauforgés, 273 % de Force, 2e Reap à **1,075** des PV actuels. **Le one-shot existe dès « 1 tauforgé + 3 normaux »** (258 %, 1,016), et même sans éclat avec Transient Fortitude (palier P1).
3. **Pièces vraiment bloquantes : l'énergie, pas la Force.** Arcane Energize, puis Seismic Bond (Huras), puis Primed Continuity ; elles passent avant les éclats tauforgés.
4. **S1 et S3 :** portée 100 %. **S2 endurance :** Augur Secrets → Stretch.
5. **Overguard :** comportement inconnu (T1). Le plan B sans casser l'invisibilité repose sur le Blast des détonations voisines et l'Assassin Posture du Huras. Epitaph Prime + Secondary Fortifier en dernier recours (casse l'invisibilité 7 s).

---

## 2. Fiche finale F1 (à recopier en jeu)

**Sevagoth Prime**
- **Helminth :** Roar infusé en **slot 4** (remplace Exalted Shadow ; le passif Tombstone reste actif, CONF).
- **Aura :** Brief Respite (Aura Forma). **Exilus :** Power Drift.
- **Mods :** Shadow Haze · Dark Propagation · Umbral Intensify [U] · Augur Secrets · Intensify · Catalyzing Shields [V] · Primed Continuity [M] · Streamline [N].
  - Capacité 72/74, 2 Forma (Aura + Umbra).
- **Swaps selon le contenu :**
  - S2 endurance : Augur Secrets → **Stretch** (Forma Naramon sur ce slot : 70/74).
  - S3 level cap : Molt Augmented → **Arcane Escapist** ; garder Augur Secrets.
- **Arcanes :** Molt Augmented + Arcane Energize.
- **Éclats :** 4 × Crimson tauforgé (Force) + 1 × Amber tauforgé (orbes d'énergie +75 %).
- **Focus :** Vazarin. **Parazon :** Hard Reset (−15 s de neutralisation du compagnon par Mercy, CONF).
- **Stats :**
  - Force 273 % → 333 % (Molt plein), Durée 155 %, Portée 100 %, Efficacité 130 % (160 % sous Gloom avec Seismic Bond).
  - 2e Reap **1,075 → 1,332**. Roar ×1,82 → ×2,00 (46,5 s). Gloom **95 % dès le départ**. Énergie +3,45/s à 60 kills/min ; tient dès ~20 kills/min.

**Ombre (config Tombstone, sert seulement à la mort)**
- **Aura :** Steel Charge (M, +18).
- **Mods :** Umbral Vitality · Umbral Fiber · Umbral Intensify · Adaptation · Rolling Guard · Vitality · Steel Fiber · Intensify.
- **Arcanes :** Arcane Fury + Arcane Reaper. 73/78, 3 Forma. EHP 9 902.

**Shadow Claws Prime (Tombstone)**
- **Mods :** Primed Pressure Point · Condition Overload · Blood Rush · Organ Shatter · Primed Reach · Life Strike · Primed Fever Strike · North Wind.
- **Exilus :** Discipline's Merit. **Arcane :** Melee Exposure. 66/70, 3 Forma. Rôle : une lourde pour retirer l'Overguard avant de Consume.

**Huras Kubrow** (détails en section 7)
- **Précepte :** Stalk (+ Hunt).
- **Mods :** Seismic Bond · Enhanced Vitality · Metal Fiber · Medi-Pet Kit · Momentous Bond (+ Calculated Redirection avec 2 Forma Vazarin).
- **Arme du Kubrow :** Assassin Posture en posture.

**Arme :** Epitaph Prime + Secondary Fortifier (urgence anti-Overguard, amorce).

**Rotation**
1. Roar → Gloom.
2. Par pack : **Reap → Sow → Reap**. Eximus : **+1 Reap** (et Sow avant si T6 dit « consommé »).
3. Roar toutes les 46,5 s. Ramasser les orbes.
4. **Aucun tir en S2/S3** (l'invisibilité casse, puis 7 s de recharge).

---

## 3. Plan de progression (paliers P0 → P5)

Chaque palier est une config complète qui rentre en capacité (M15, DÉD). « Gloom permanent » = drain à 10 ennemis en continu ; « à la demande » = Gloom coupé hors des pics.

| Palier | Ce qui change | Force (début / Molt) | 2e Reap (début / Molt) | Gloom | Durée | Énergie à 60 kills/min (permanent / à la demande) | Tient jusqu'à (DÉD) |
|---|---|---|---|---|---|---|---|
| P0 | Référence sans arcanes (déconseillé) | 268 % / 268 % | 1,055 / 1,055 | 94 % | 72,5 % | **−11,97 / −4,73** | Rien d'endurant : l'énergie s'effondre |
| **P1** | Départ : Molt + Arcane Energize, Shade | 268 % / 328 % | 1,055 / 1,309 | 94 % | 72,5 % | −7,39 / **−0,15** | S1 avec Gloom à la demande |
| **P2** | + Huras Kubrow (Stalk + Seismic Bond) | 268 % / 328 % | 1,055 / 1,309 | 94 % | 72,5 % | −1,25 / −0,15 | S1, S2a court (Gloom permanent tenable au-dessus de ~112 kills/min) |
| **P3** | + 4 Crimson normaux + Amber normal ; Transient Fortitude → Primed Continuity | 253 % / 313 % | **0,996** / 1,243 | 89 % | 155 % | **+2,86** / +2,31 | S2 (500 et 1000+), dès ~21 kills/min |
| **P4** | + Crimson et Amber tauforgés (Taubound) | 258 % / 318 % | **1,016** / 1,265 | 90 % | 155 % | +3,45 / +2,90 | S2 et S3 (avec les swaps) |
| **P5** | F1 final : 4 Crimson tauforgés | 273 % / 333 % | 1,075 / 1,332 | **95 %** | 155 % | +3,45 / +2,90 | Tout, marge dès la 1re seconde |

### Fiche par palier
- **P1 — Départ.**
  - Mods de la fiche finale, mais **Transient Fortitude à la place de Primed Continuity** (même polarité M). C'est lui qui donne le one-shot sans éclat (268 %).
  - Arcanes Molt + Energize. Compagnon Shade (Ghost, CONF : invisibilité identique à Stalk). 0 éclat.
  - Manque : Seismic Bond, éclats, Primed Continuity.
  - **Prochaine pièce, Seismic Bond (via le Huras) : +6,14 énergie/s** avec Gloom permanent (DÉD).
- **P2 — Huras Kubrow.** Même fiche, Shade remplacé par le Huras avec Seismic Bond.
  - Manque : la durée (Transient Fortitude coûte −27,5 %, donc Gloom draine fort).
  - **Prochaines pièces, 4 Crimson normaux + Amber normal :** ils permettent Transient → Primed Continuity sans perdre le one-shot (0,996, 5 kills de Molt). Gain : **+2,94/s** (Durée 155 %) **+ 1,18/s** (Amber +50 %) → +2,86/s net avec Gloom permanent.
- **P3 — Fiche finale avec éclats normaux.**
  - Manque : les tauforgés.
  - **Prochaine pièce, le Crimson tauforgé de Taubound :** 0,996 → **1,016**, one-shot sans attendre Molt. L'Amber tauforgé ajoute +0,58/s.
  - Variante utile : un **5e Crimson à la place de l'Amber** (1 tauforgé + 4 normaux) donne **268 %, soit 1,055**, pour −1,76/s d'énergie (DÉD, M12).
- **P4 — Taubound.**
  - Manque : 3 Crimson tauforgés.
  - **Gain des 3 suivants :** 1,016 → 1,075, et Gloom au plafond dès le départ (90 % → 95 %, au lieu d'attendre 56 kills de Molt).
- **P5 — Final.** Plus rien à farmer pour Sevagoth : la suite concerne l'Ombre et les griffes Tombstone, plus des Forma de confort.

### Ordre des Forma (aucune à regretter)
1. **Aura Forma** sur l'aura (Brief Respite) : +7 de capacité. Elle sert à tous les paliers.
2. **Umbra Forma** sur le slot d'Umbral Intensify. Avec ces deux-là, P1 à P5 rentrent (73/74 puis 72/74).
3. Confort, dans cet ordre :
   - Zenurik sur Shadow Haze, Zenurik sur Dark Propagation, Zenurik sur l'exilus (Power Drift) ;
   - **Naramon** sur Augur Secrets (le même slot accueille Stretch pour le swap S2) ;
   - Madurai sur Intensify.
   Tous ces mods restent dans F1 final.
4. **À ne jamais faire :** poser une polarité pour Transient Fortitude (il utilise le M inné, que Primed Continuity reprend ensuite) ou pour un mod de passage.
5. **Ensuite seulement :** Ombre Tombstone (3 Umbra) et griffes Tombstone (3 Forma). Le Kubrow n'en a pas besoin, sauf 2 Vazarin si tu ajoutes Calculated Redirection.

### Calendrier Taubound (aujourd'hui → **17/11/2026**, l'événement ne reviendra pas, CONF)

| Achat | Moonflesh | Pour F1 |
|---|---|---|
| 1. **Crimson tauforgé** (limite 1) | 375 | Passe le seuil sans Molt (0,996 → 1,016) |
| 2. **Secondary Fortifier ×21** (rang 5) | 168 | Plan B Overguard, quel que soit le résultat de T1 |
| 3. **Amber tauforgé** (limite 1) | 375 | Orbes +75 % au lieu de +50 % (+0,58/s) |
| **Total indispensable** | **918** | |
| Options : Melee Exposure ×21 (griffes Tombstone) 168 ; Legendary Core (monte Primed Continuity au max) 500 | +668 | |

- **Meilleure méthode** (DÉD à partir de valeurs CONF) : un nœud Survival ou Defense d'Eris en **Steel Path**, avec F1.
  - Chaque Infesté tué a environ 2 % de chance de donner 3 Moonflesh, soit ~0,06 par kill. Cela fait **~216 à 432 Moonflesh/h** entre 60 et 120 kills/min.
  - On enchaîne les alertes Taubound d'Eris dès qu'elles apparaissent : 75 Moonflesh chacune en SP, jusqu'à 3 actives, nouvelles toutes les 30 min.
  - Les 918 Moonflesh prennent **2 à 4,5 h**. Ces sessions servent aussi de phase B pour T4 et de T8.
- **Ordre :** Crimson tauforgé dès que tu as 375, puis Secondary Fortifier, puis Amber.
- **À ne pas oublier cette semaine :** Bird 3 vend le **Crimson normal** jusqu'au lundi 02/11 00:00 UTC (30 000 standing Cavia, rang 5), puis de nouveau la semaine du 16/11.
- **Archon Hunt :** Amar (Crimson) les semaines du **09/11** et du **30/11** (formules de rotation du wiki, CONF).

---

## 4. Éclats d'Archonte : états, sources, délai

**États de F1** (début de mission, avant Molt ; M12, DÉD) :

| État | Force | 2e Reap | One-shot ? | Kills de Molt pour 1,00 | Gloom | Kills de Molt pour 95 % |
|---|---|---|---|---|---|---|
| 0 éclat | 213 % | 0,846 | non | 171 | 74,5 % | 244 |
| **4 Crimson normaux** + Amber | **253 %** | **0,996** | non (−0,4 %) | **5** | 88,5 % | 77 |
| **1 tauforgé + 3 normaux** + Amber | **258 %** | **1,016** | oui (+1,6 %) | 0 | 90,3 % | 56 |
| 1 tauforgé + 4 normaux (sans Amber) | 268 % | 1,055 | oui | 0 | 93,8 % | 15 |
| 2 tauforgés + 2 normaux + Amber | 263 % | 1,035 | oui | 0 | 92,0 % | 36 |
| 3 tauforgés + 1 normal + Amber | 268 % | 1,055 | oui | 0 | 93,8 % | 15 |
| **4 tauforgés** + Amber | **273 %** | **1,075** | oui (+7,5 %) | 0 | 95,0 % | 0 |

- Molt donne +0,24 % de Force par kill (CONF).
- À 4 Crimson normaux, le 2e Reap laisse 0,4 % des PV. Un 3e Reap, le Blast ou le Sow finissent la cible, donc le « non » ne coûte presque rien en pratique (DÉD).

**Obtenir d'autres Crimson tauforgés** (patch actuel ; taux CONF des tables de drop du wiki, espérance DÉD) :
- **Search Pulses : 5 par semaine** (CONF). Meilleur usage : Deep Archimedea (2) + Temporal Archimedea (2) + 1 Netracell.
- **Deep Archimedea Elite** (paliers A, A, B, B, C) : 0,421 tauforgé Crimson et 0,613 Crimson normal par semaine.
  - Taux : 4,17 % (pool A), 8,54 % (B), 16,67 % (C).
- **Temporal Archimedea Elite** : 0,261 tauforgé et 0,456 normal.
- **Netracell** : 4,17 % tauforgé, 17,5 % normal.
- **Archon Hunt** : Crimson une semaine sur trois (Amar). Le tauforgé tombe à 20 % de base, avec une pitié de +20 % par échec, soit **39,83 % effectifs** (CONF).
- **Bird 3** : 1 Crimson normal toutes les 3 semaines.
- **Ascent Fusion** : 3 normaux de la même couleur → 1 tauforgé, pour 100 Stela (CONF).
- **Sans taux trouvé** (NON TROUVÉ) :
  - Descendia SP palier 21 : un Crimson possible parmi d'autres lots.
  - Coffres Icebind : Crimson normal à 11,67 % (coffre « Crested ») ou 3,33 % (coffre ordinaire), mais le nombre de Cryobells obtenables n'est pas documenté.
- **Total :** **1,45 équivalent tauforgé par semaine en Elite** (0,86 tauforgé + 1,78 normal fusionné), **0,99 sans Elite**. Les 3 tauforgés qui manquent après Taubound prennent **~2,1 semaines (Elite)** ou **~3 semaines** en espérance (DÉD ; forte variance). Avant le 17/11, c'est possible mais pas probable : l'audit avait raison.

---

## 5. Overguard : ce qui est documenté, et le plan B

**Ce qui est documenté (CONF) :**
- L'Overguard « doit être retiré avant de pouvoir toucher les PV et boucliers » (texte d'introduction de l'U31).
- Il est neutre à tous les types de dégâts, insensible à l'armure, et le Viral ne s'y applique pas (correctif U31).
- La vulnérabilité aux dégâts s'y applique « normalement » d'après la page Overguard. Mais Reap et Death's Harvest ne figurent pas dans la liste U37 des vulnérabilités étendues à l'OG.
- Le vol de vie fonctionne sur les dégâts infligés à l'OG (U31).

**Ce qui ne l'est pas : NON TROUVÉ.** Aucune source ne dit si le % de PV actuels de Sow+Reap entame l'Overguard, ni s'il déborde sur les PV. Sources cherchées :
- wiki : Overguard, Reap, Sow, Eximus, Damage Vulnerability, Effects Scaling With Enemy Stats ;
- patch notes U31 à U44 ;
- Overframe, forums et Steam.

L'astuce du wiki selon laquelle « Sow + Reap descend les Eximus jusqu'au seuil de Mercy » ne précise pas si l'OG était déjà retiré. → **T1** (section 8).

**Plan B si le nuke ne traverse pas l'OG**, classé du moins au plus coûteux en invisibilité :

| Rang | Moyen | Casse l'invisibilité ? | Efficacité | Coût pour le build |
|---|---|---|---|---|
| 1 | **Blast des détonations voisines** : 25 % des PV du voisin × Roar (× vuln si elle touche l'OG) dans 4 m | Non | Il faut **3 Heavy Gunners** à 4 m de l'Eximus de SP175 à 1000, 5 au 9999 ; seulement 1 à 2 si la vulnérabilité touche l'OG (DÉD, M18) | Aucun ; dépend de la densité (F1 ne regroupe pas) |
| 2 | **Assassin Posture du Huras** : cible les Eximus, +300 % contre l'OG | Non (le Huras attaque sans casser Stalk, CONF) | NON TROUVÉ : dégâts du compagnon au niveau visé (T4) | Aucun |
| 3 | **Amp de l'Opérateur** : l'OG prend +50 % de dégâts Void | Non (attaquer en Opérateur ne casse pas le camouflage, CONF) | Faible à haut niveau (DÉD) | Aucun |
| 4 | **Nidri Tauron Strike + Rift Waters** (Vazarin) : vortex de 20 m pendant 20 s, OG −25 %/s (CONF) ; nœud marqué Opérateur, invulnérable pendant le lancement | À TESTER | Retire tout l'OG en 4 s, quel que soit le niveau. Mais la charge ne vient que de 0,02 % par kill (+10 % par lentille) et de 20 % par orbe de Convergence : quelques fois par heure (DÉD) | The Old Peace + Tektolyst Artifact Vazarin (150 Lyroic Bridge, Ren Hypercore et Ascaris Prime) + nœuds |
| 5 | **Epitaph Prime + Secondary Fortifier** (×8 contre l'OG) | **Oui**, 7 s de recharge (CONF) | 1 tir chargé jusqu'au niveau 1000, 6 à 7 au 9999 (DÉD) | Aucun (déjà dans le build) ; risque des 7 s visibles |

**Lecture :**
- **H0 en S1/S2 :** le rang 5 suffit (le corps encaisse 7 s avec gating et ralentissement).
- **H0 en S3 :** rangs 1, 2 et 4 d'abord, le rang 5 seulement dans une fenêtre sûre.
- Dans ce cas S3 devient nettement plus dur pour F1 (cf. « ce qui renverserait » v1).

---

## 6. Portée

Rayons CONF multipliés par la Portée : Sow 16 m, Gloom de 4 à 16 m, bande de Reap 8 m (mini-Reap pareil), Dark Propagation 15 m. La détection des mini-Reap est fixe à 30 m. Le vol de Reap couvre 93 m en tap (10 m/s × 9,3 s) et 186 m en maintien.

| Option (4 tauforgés) | Portée | Sow / Gloom | Bande de Reap | Aire de Sow | 2e Reap début | Kills de Molt pour 1,00 | Gloom début | Énergie 60 kpm* |
|---|---|---|---|---|---|---|---|---|
| Build actuel | 100 % | 16,0 m | 8,0 m | ×1,00 | 1,075 | 0 | 95 % | +3,45 |
| Exilus Power Drift → Cunning Drift | 115 % | 18,4 m | 9,2 m | ×1,32 | 1,016 | 0 | 90 % | +4,10 |
| **Augur Secrets → Stretch** | 145 % | 23,2 m | 11,6 m | **×2,10** | 0,981 | **21** | 87 % (95 % après 94 kills) | +4,78 |
| Dark Propagation → Stretch | 145 % | 23,2 m | 11,6 m | ×2,10 | 1,075 | 0 | 95 % | +4,78 |
| Streamline → Stretch | 145 % | 23,2 m | 11,6 m | ×2,10 | 1,075 | 0 | 95 % | **+1,85** |
| Intensify → Stretch | 145 % | 23,2 m | 11,6 m | ×2,10 | 0,957 | 46 | 85 % | +4,78 |

\* Énergie : on suppose que les kills par rotation suivent l'aire (15 × Portée², plafonné à 30). C'est une hypothèse TEST, d'où T15.

- **L'invisibilité change la donne (DÉD) :** les ennemis ne convergent pas vers un Sevagoth invisible. La portée compte donc plus qu'en jeu visible. Distance d'engagement typique : NON TROUVÉE (T15).
- **S1 :** 100 % suffit. Les packs sont denses et le vol de Reap couvre la distance.
- **S2 endurance : Augur Secrets → Stretch.**
  - Le 0,981 de départ ne coûte rien : une endurance commence à bas niveau, et Molt rattrape le seuil en **21 kills** et le plafond de Gloom en **94**.
  - Capacité 74/74 (70/74 avec une Naramon).
  - **Seulement à partir de P5.** À P3 (Crimson normaux), le même swap tombe à 0,905 et demande 105 kills de Molt.
- **S3 level cap :** garder Augur Secrets, car le niveau est maximal dès la 1re seconde.
- **Dark Propagation → Stretch :** ne coûte ni Force ni énergie, mais on perd la propagation de Sow (non chiffrée). À trancher par T15.

---

## 7. Huras Kubrow : survie (T4)

**CONF (rework des compagnons et Module:Companions/data) :**
- Les compagnons sont **immortels**. À 0 PV, ils sont **neutralisés 60 s**, puis reviennent seuls avec **5 s d'invulnérabilité** ; un Kubrow peut aussi être relevé à la main.
- **Pendant la neutralisation, Stalk ne fonctionne pas.** C'est le vrai risque de F1.
- Huras : 560 PV, 490 boucliers, **300 d'armure** (le module donne 300, les patch notes du rework annonçaient 200 ; le module est plus récent), polarités Penjaga / Madurai / Penjaga.
- Le Huras est lui aussi camouflé. Il ne prend donc pas le tir ciblé, mais il prend les **zones** (auras et ondes des Eximus, explosions, statuts).

**Mods du Huras**, par priorité (valeurs CONF, capacité DÉD) :
1. **Stalk** (précepte, indispensable).
2. **Seismic Bond** (+30 % d'efficacité sous Gloom, l'énergie de F1).
3. **Enhanced Vitality** (+250 % de PV) et **Metal Fiber** (+250 % d'armure) : EHP de 1 610 à **9 310**.
4. **Medi-Pet Kit** : +12 PV/s et **−15 s** de neutralisation.
5. **Momentous Bond** : **−18 s** de neutralisation par Eximus tué.
6. Calculated Redirection : +250 % de boucliers, EHP 10 535 ; demande 2 Forma Vazarin.
7. Arme du Kubrow : **Assassin Posture** en posture (+300 % contre l'OG).

Hors du Kubrow : Hard Reset sur le Parazon (−15 s par Mercy) et Restorative Bond (−3 s par orbe de vie) si tu as la place. Sans Forma, la liste 1 à 5 + Hunt entre dans environ 55 de capacité (DÉD ; capacité exacte du Kubrow NON TROUVÉE ici, à lire en Arsenal).

| Mods | EHP | Balles de Heavy Gunner pour le neutraliser (niv. 175 / 500 / 1000 / 9999) |
|---|---|---|
| Aucun | 1 610 | 9,2 / 1,8 / 0,6 / 0,0 |
| Enhanced Vitality + Metal Fiber | 9 310 | 53 / 10 / 3,5 / 0,1 |
| + Calculated Redirection | 10 535 | 60 / 12 / 4,0 / 0,1 |

Temps de neutralisation (DÉD, approximation continue) : 45 s avec Medi-Pet Kit ; ~16 s si un Eximus meurt toutes les 10 s (Momentous Bond).

---

## 8. Tests en jeu (T1 et T4 réécrits ; T15 nouveau)

### T1 : le % de PV actuels de Sow+Reap traverse-t-il l'Overguard ? (protocole PS5)
**Préparation**
- **Lieu :** Simulacrum, de préférence le Sanctum Simulacrum, qui autorise +25 niveaux (CONF).
- **Console :**
  - niveau ennemi **au maximum** (5 × Mastery Rank + 30, +25 au Sanctum ; environ 205 à MR30, CONF) ;
  - **Steel Path ON** (dans le Simulacrum, PV, armure et boucliers ×3,5, CONF U33.5) ;
  - **Pause AI ON** ; invincibilité du joueur ON.
- **Compagnon retiré** (l'Assassin Posture fausserait la mesure). Armes rangées.
- **Cible :** **1 Heavy Gunner Eximus** (il faut l'avoir scanné au Codex). Sinon, n'importe quel Eximus Grineer à armure : noter son nom exact.
- **Build :** F1, noter la Force affichée. Activer la capture vidéo (bouton Créer) pour relire image par image.

**Séquence** (10 répétitions, « Kill all » entre chaque) :
1. Spawn de l'Eximus. Noter les barres d'Overguard (au-dessus de la vie) et de PV.
2. Roar.
3. Reap, attendre la fin du vol. Noter OG et PV (seul le Radiation de 250 × Force doit marquer).
4. Sow.
5. Reap. Noter OG et PV **juste après la détonation**.
6. Reap (précédé d'un Sow si T6 a montré que Sow est consommé). Noter OG et PV.
7. **Variante Blast :** 1 Eximus + 4 Heavy Gunners collés au même point de spawn, puis Sow et Reap. Noter l'OG de l'Eximus après la mort des 4 voisins.

**Contrôles**
- **C1 :** même séquence sur un Heavy Gunner sans Eximus. Il doit mourir à l'étape 5. Sinon c'est le modèle du nuke qui est faux, avant même l'OG.
- **C2 :** Eximus dont l'OG a d'abord été vidé à l'Epitaph + Fortifier. Il doit mourir à l'étape 5.

**Lecture**
| Observation à l'étape 5 | Hypothèse | Conséquence |
|---|---|---|
| OG vide et PV fortement entamés (≈ 90 % des PV au niveau de S1, DÉD) ; mort à l'étape 6 | H1a : le True traverse, vulnérabilité comprise | Rotation Eximus = 3 Reap ; aucun plan B nécessaire |
| OG vide, PV moins entamés ; mort à l'étape 6 ou 7 | H1b : la vulnérabilité ne s'applique pas à l'OG | Idem, un Reap de plus parfois |
| OG vide, PV **intacts** | Pas de débordement | 3 à 4 Reap par Eximus |
| OG presque intact | **H0** | Plan B (section 5). L'étape 7 dit si le Blast voisin suffit |

### T4 : survie du Huras Kubrow et tenue de Stalk
**Phase A : Simulacrum, reproductible**
- **Console :** niveau max, Steel Path ON, invincibilité **joueur ON, compagnon OFF**, Pause AI **OFF**.
- **Vague :** 4 Heavy Gunners, 2 Arson Eximus, 2 Blitz Eximus et 2 Bombards (ennemis à dégâts de zone ; noter les noms exacts de la console). On la relance à chaque fois qu'elle meurt.
- **Jeu :** 5 minutes de rotation F1 **sans tirer**, 3 fois pour chaque config :
  - (a) Huras avec Enhanced Vitality, Metal Fiber, Medi-Pet Kit et Momentous Bond ;
  - (b) Huras sans mods de survie ;
  - (c) Shade en référence.
- **Mesures :**
  - nombre de messages « compagnon neutralisé » ;
  - nombre de ruptures d'invisibilité (icône du HUD) ;
  - durée de chaque neutralisation, chronométrée sur la vidéo.

**Phase B : vraie endurance**
- **Où :** Survival Steel Path d'Eris (Infestés), ce qui compte aussi pour le farm de Moonflesh. 60 minutes au minimum.
- **Relevés :**
  - noter le chrono de mission à chaque neutralisation ;
  - à chaque neutralisation (on est déjà visible) ou toutes les 10 min, scanner un ennemi au Codex Scanner pour relever son niveau. Le scanner compte comme une arme et casse l'invisibilité (CONF), d'où ces moments-là.

**Critères**
- **Confirme F1 :** au plus 1 neutralisation par 10 min au niveau visé, et invisibilité au moins 90 % du temps.
- **Infirme :** plus de 2 neutralisations par 10 min dès le niveau 500. Ajouter alors Calculated Redirection (2 Forma Vazarin), ou comparer avec la phase A (c) :
  - le Shade est une sentinelle : avec Primed Regen, sa neutralisation baisse de 35 s et il revient avec 10 s d'invulnérabilité (CONF) ;
  - mais pas de Seismic Bond, soit −6,14/s d'énergie sous Gloom permanent.
- Si même le Shade ne tient pas, F3 (Gloom + Ombre) redevient l'option S2/S3 (cf. v1).

### Autres tests (repris de la v1 ; ceux propres à F2/F3 sont abandonnés)
| # | Question | Mise en place | Mesure | Confirme / infirme |
|---|---|---|---|---|
| T2 | La vulnérabilité de Reap s'applique-t-elle à l'OG ? | Simulacrum, Eximus, Pause AI ; tir chargé d'Epitaph avant et après un Reap | Chiffre de dégâts sur l'OG | ≈×2,36 : oui (plan B rang 1 à 1–2 voisins). ×1 : non (3 voisins) |
| T3 | (variante) Precision Intensify booste-t-il Roar en slot 4 ? | Arsenal, puis mission | Buff Roar dans le HUD | Optionnel : Intensify reste le choix par défaut |
| T5 | Gloom à 95 % ralentit-il la cadence de tir ? | Simulacrum, Heavy Gunner, Gloom on/off | Balles par 5 s | Division par ≈20 : oui |
| T6 | Sow survit-il à une détonation ? | Sow → Reap → Reap sans relancer Sow | Une ou deux détonations | Une : ajouter un Sow avant le 3e Reap sur les Eximus |
| T8 | Tenue d'énergie | SP survival, 20 min, Gloom permanent, palier en cours | Énergie toutes les 2 min | Conforme au tableau des paliers à ±1/s |
| T10 | Le Tombstone coûte-t-il un revive ? Molt est-il réinitialisé ? | Solo, 5 morts contrôlées | Compteur de revives, stacks de Molt | DE (2023) : pas de revive consommé |
| T13 | Un Mercy casse-t-il Stalk ? (Escapist, Hard Reset) | Mercy sur un Eximus affaibli | État du camouflage | Oui : en S3, Escapist seulement dans une fenêtre sûre |
| T14 | Blood Rush se pose-t-il sur Shadow Claws Prime ? (griffes Tombstone) | Arsenal | Le mod s'équipe-t-il ? | Non : True Steel à la place |
| T7, T9, T11, T12 | Abandonnés (F2/F3 non retenues) | – | – | – |
| **T15** | Portée en endurance | Même nœud SP survival, 15 min × 3 configs : build, Augur Secrets → Stretch, Dark Propagation → Stretch | Kills/min de fin de mission, courbe d'énergie | Plus de 10 % de kills/min pour une config Stretch : l'adopter en S2 |

---

## 9. Chiffres clés et ce qui renverserait le verdict

- **Nuke F1** (M11/M12) : seuil 254,0 % de Force. 1,075 à P5, 1,016 à P4, 0,996 à P3 (5 kills de Molt), 1,055 à P1/P2 grâce à Transient Fortitude.
- **Eximus Heavy Gunner** (M4) : 1,93 M PV et 324 k OG au niveau 175 ; 6,9 M et 1,56 M au 1000 ; 36,6 M et 12,4 M au 9999. Une balle tue le corps dès le niveau **415** (M6).
- **Énergie** (M15) : P5 tient dès ~20 kills/min. Sans Energize (P0), −4,73/s même Gloom coupé.
- **Crimson tauforgés** (M13) : 1,45 équivalent par semaine en Elite, 0,99 sans.
- **Taubound** (M17) : 918 Moonflesh, ~2 à 4,5 h de farm.

**Ce qui renverserait le verdict :**
- **Le Huras est neutralisé plus de 2 fois par 10 min dès le niveau 500 (T4)** et le Shade ne fait pas mieux : F1 perd sa couche principale en S2/S3.
- **H0 au T1 et Blast voisin insuffisant (étape 7)** : en S3, les Eximus imposent l'Epitaph, donc des fenêtres visibles. F1 reste le meilleur build, mais S3 passe de « viable » à « difficile ».
- **Packs de moins de 8 kills par rotation (T8)** : l'énergie de P5 passe à −0,65/s. Couper Gloom hors des pics, ou passer à la portée (section 6).

---

## 10. Liste de farm priorisée (v2)

Prix : warframe.market, vendeurs en jeu, crossplay, 29/10/2026. Les sources et substituts de la v1 restent valables ; seul l'ordre change.

| Priorité | Pièce | Palier | Impact (DÉD) | Où | Coût |
|---|---|---|---|---|---|
| 1 | **Arcane Energize** | P1 | +4,58/s : sans lui, F1 n'est pas viable | Capture de l'Hydrolyst ; Orphix Veil Proxima rotation C | ~210 p |
| 1 | **Molt Augmented** | P1 | +60 % de Force après 250 kills | Cavalero (Holdfasts rang 5) ; Thrax/Void Angels 6,67 % | ~50 p |
| 2 | Roar (Helminth), Shadow Haze, Dark Propagation, Umbral Intensify, Transient Fortitude, Catalyzing Shields, Brief Respite, Augur Secrets, Power Drift, Streamline, Shade | P1 | Base du one-shot (268 %) et du gating | Helminth / Suda ou Perrin / Simaris / coffre de Deimos / Derelict / Orphid / Thumpers / test Lua / Junction / Marché | voir v1 |
| 3 | **Huras Kubrow + Seismic Bond** (+ mods de survie, Assassin Posture) | P2 | +6,14/s sous Gloom permanent | Œuf de Kubrow, incubation aléatoire (taux NON TROUVÉ) ; Son (Entrati rang 3) ; The Business | ~29 p (Seismic) |
| 4 | **Taubound** : Crimson tau, Secondary Fortifier, Amber tau | P4 | 0,996 → 1,016 ; plan B OG ; +0,58/s | Praghasa, Eris, **avant le 17/11** | 918 Moonflesh |
| 5 | **4 Crimson normaux + 1 Amber normal**, **Primed Continuity** | P3 | Permet Transient → Primed Continuity : +2,94/s (+1,18 avec l'Amber) | Bird 3 cette semaine, Archon Hunt, Netracells, Archimedea, Icebind ; Primed Continuity chez Baro | ~155 p (Primed Continuity R10) |
| 6 | **3 Crimson tauforgés de plus** | P5 | 1,016 → 1,075, Gloom 95 % dès le départ | Section 4 (2 à 3 semaines) | – |
| 7 | Forma de confort ; Ombre et griffes Tombstone | – | Filet de secours à la mort | v1 | – |

---

## Annexes (v1, inchangées sauf mention)

## A. Fiches détaillées v1 (F1 détaillée ; F2 et F3 archivées en v2)

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
- **Compagnon : Huras Kubrow.** Stalk (invisibilité indéfinie tant qu'un ennemi est à moins de 24 m et qu'on ne tire pas ; le Kubrow peut attaquer sans casser le camouflage, CONF). Seismic Bond (+30 % d'efficacité pendant une compétence canalisée). Assassin Posture (cible les Eximus, +300 % de dégâts contre l'Overguard). Le reste en survie du compagnon (sa neutralisation coupe l'invisibilité ; mods et T4 en sections 7 et 8).
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
4. Eximus : sous H1 (test T1), il faut **2 détonations, soit un 3e Reap** (correction v2). Sous H0 : plan B de la section 5.
5. Roar à relancer toutes les 46,5 s. Gloom reste actif ; son ralentissement est figé au lancement (CONF), mais il est déjà au plafond, donc pas besoin de le relancer.

**Death Well en F1 :** sans objet (Exalted Shadow remplacé). Le passif reste actif (CONF). À la mort : Ombre Tombstone, 5 s d'invulnérabilité, **5 Consume** (gratuits, tuent tout non-boss sans Overguard) en 20 s. Une lourde des griffes sur un Eximus retire son Overguard.

### F2 « Ombre Faucheuse » (archivée en v2 ; incompatible avec F1 sur la même frame)

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

### F3 « Sans Helminth » (archivée en v2 ; config B possible sur la même frame que F1)

Même config Sevagoth que F1, mais Precision Intensify booste Exalted Shadow : griffes en base 832. Ombre et griffes identiques à F2. Compagnon : un fauve avec Seismic Bond (Gloom est canalisé). Amorce Viral obligatoire pour le nuke du corps (tir non chargé d'Epitaph). Sans amorce, le 2e Reap ne fait que **0,55**. F3 est compatible avec F1 parce qu'elle n'a pas d'infusion (CONF : chaque config peut avoir sa propre infusion ou aucune).

## B. Étape 0 : état du jeu (vérifié le 29/10/2026)

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

Conflit de sources noté : le module `Mods/data` du wiki liste encore Blood Rush comme incompatible avec les armes exaltées (`POWER_WEAPON`). Les patch notes 38.5 l'emportent (règle « patch notes > wiki »), et la page wiki Exalted Weapon les reprend. Vérifier en Arsenal (T14, section 8).

## C. Étape 1 : le kit décortiqué

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

## D. Étape 2 : scénarios (fixés pour toutes les comparaisons)
- **S1 :** Steel Path standard, ennemis niveau ~175 (+100 de SP inclus). Factions mixtes. Référence : Grineer (Heavy Gunner, armure 500 → 2 700 plafonnée), et Corpus / Infesté pour vérifier.
- **S2 :** endurance SP, niveaux 500 puis 1 000+.
- **S3 :** level cap 9 999. Le nuke en pourcentage y fonctionne ; c'est la survie qui décide.
- **Métriques :** vitesse de clear (kills/min, M9), TTK sur Heavy Gunner et Heavy Gunner Eximus (M4, M5), EHP réel et indice de risque au tir direct (M6), énergie nette par seconde (M7), uptime de l'Ombre (M8). La base ×1,00 est F1.

## E. Étape 3 : archétypes

| Archétype | Source | Verdict |
|---|---|---|
| **A. Nuke Roar sur le 4 (Reap/Sow/Gloom/Roar)** | COMM : Ninjase « Gloom Reaper », 1 531 votes, et variante invisible (vidéo de mai 2026, contenu non vérifié) | **Finaliste → F1** (+ Huras/Seismic, DÉD) |
| **B. Ombre nukeuse avec Roar sur Gloom** | COMM : Ninjase « Shadow Realm » (536 votes), RubyBlossom5 « Ravenous Alliance » (19 votes) | **Finaliste → F2** |
| **C. Sans Helminth, Gloom + Ombre** | COMM : RubyBlossom5 « The Reaper's Bible », 98 votes, mise à jour le 22/10/2026 | **Finaliste → F3** |
| D. Griffes pures (Ombre en mêlée permanente) | – | Éliminé : un seul cible à 4,5 m, battu au clear par tout nuke ; reste un outil anti-Eximus de F2/F3 |
| E. Gloom tank / plateforme d'armes | – | Éliminé : le nuke en pourcentage fait mieux à tout niveau ; Gloom est une couche, pas un archétype |
| F. Helminth Nourish / Silence / Eclipse / Jade Stars | COMM (Ninjase) | Éliminé : Nourish ne pose pas de Viral via les compétences ; Silence et Eclipse ne lèvent pas le seuil ; Jade Stars demande la ligne de vue (U43) |
| G. Sevagoth donneur de Gloom | – | Hors sujet (une ligne à la fin) |

Comparaison ×1,00 sur S1/S2/S3 : annexe I (tableau M1). F2 gagne 7 à 21 % au clear S1 ; F1 gagne la survie partout (×8 à ×18 contre F2, ×2,7 contre F3) et l'énergie contre F2. F3 n'a l'avantage nulle part sauf l'absence d'Helminth.

## F. Étape 5 : modélisation v1 (résumé, détail dans `model_output.txt`)

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

## G. Audit hostile v1 : les 5 points les plus fragiles, revérifiés

1. **« Blood Rush et Weeping Wounds marchent sur les griffes. »** Le Fandom, des guides de 2024 et le module `Mods/data` disent non. Revérifié : patch notes 38.5 (wiki Update 38 et page Exalted Weapon) : **autorisés**. Verdict maintenu, données du module signalées comme périmées, contrôle en Arsenal ajouté.
2. **« 255 % de Force avec Roar = one-shot. »** Revérifié (wiki Reap) : la vulnérabilité est posée **après** le True du même coup, donc le premier Reap ne fait que 0,50. **Corrigé :** rotation Reap → Sow → Reap, qui ne dépend plus de la persistance de Sow (T6) ; le one-shot se compte sur le 2e Reap (1,08 pour F1).
3. **« Shade = invisibilité gratuite pour toutes les variantes. »** Revérifié (page Ghost) : Reunite et les attaques des griffes cassent l'invisibilité. **Corrigé :** l'invisibilité est réservée à F1, et le compagnon passe de Shade à **Huras** (Stalk identique, il attaque sans casser le camouflage, et comme c'est un fauve il porte Seismic Bond). Énergie F1 : −2,25/s → **+1,69/s** à 60 kills/min.
4. **« On peut avoir F1 et F2 sur la même frame. »** Revérifié (page Helminth) : une capacité infusée occupe **le même slot dans toutes les configs**. **Corrigé :** F1 et F2 sont exclusives ; F3 devient la config B compatible.
5. **« Precision Intensify est le meilleur levier du nuke F1 (seuil 216,7 %). »** Revérifié en recalculant le substitut : **Intensify** (+30 % sur toutes les compétences) donne 1,08 au début au lieu de 1,11, et Gloom au plafond de 95 % dès le départ (85 % avec Precision). Le gain de Precision ne valait que 0,03 de marge. **Corrigé :** F1 passe sur Intensify (273 % de Force), Precision devient une variante, Focus Vazarin au lieu de Madurai.

Autres corrections du premier jet : le corps de F2 était à 243 % de Force (0,96, pas de one-shot au début) → Intensify ajouté (273 %, 1,08). L'énergie était négative pour les 3 builds (packs de 10, sans efficacité) → efficacité ajoutée, Rolling Guard du corps F2 remplacé par Streamline. Le TTK des griffes était présenté au plafond seulement → plancher et typique ajoutés.

## H. Liste de farm v1 (sources et substituts détaillés ; ordre remplacé par la section 10)

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

## I. Chiffres v1 et hypothèses (tests remplacés par la section 8)

### Chiffres qui portent le verdict (sortie du script, section M1)

| Scénario | Build | Clear S1 (kills/min, H1/H0) | Eximus Heavy Gunner | Risque tir direct | Énergie nette |
|---|---|---|---|---|---|
| S1 SP175 | **F1** | 151 / 133 (×1,00) | 2 détonations, soit 3 Reap (H1), ou 1 tir Epitaph (H0) | ×1,0 | +3,45/s à 60 kills/min |
| S1 SP175 | F2 | 161 / 161 (×1,07 / ×1,21) | griffes 0,17 s | ×17,6 | +1,57/s |
| S1 SP175 | F3 | 151 / 151 | griffes 0,15 s | ×2,7 | +4,09/s |
| S2b 1000 | **F1** | – | 3 Reap ou 1 tir | ×1,0 | +5,18/s à 90 kills/min |
| S2b 1000 | F2 | – | griffes 0,67 s | ×10,2 | +2,34/s |
| S2b 1000 | F3 | – | griffes 0,59 s | ×2,7 | +5,83/s |
| S3 9999 | **F1** | – | 3 Reap ou 6 tirs | ×1,0 | +2,39/s à 45 kills/min |
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
- **Le Huras (ou Shade) est neutralisé trop souvent au niveau 1000+** (v2 : les compagnons ne meurent plus), ou Stalk ne tient pas avec Sevagoth (T4). F1 perd alors sa couche principale : F3 (Gloom + Ombre) passe devant en S2/S3 (risque ×2,7 seulement, et l'Ombre comme couche active).
- **H0 au test T1 et Epitaph trop lent au level cap** (6 à 7 tirs, invisibilité cassée) : en S3, F2/F3 (griffes) deviennent l'outil anti-Eximus, mais restent beaucoup plus exposés.
- **Gloom ne ralentit pas la cadence de tir** (T5) : l'avantage de F1/F3 sur F2 en S1 se réduit (l'invisibilité de F1 reste).
- **Clear S1 : F2 mesuré à plus de 15 % au-dessus de F1** (T7) : F2 devient le meilleur build S1, sur un Sevagoth séparé à cause de la contrainte de slot Helminth.

---

## Sources (consultées le 29/10/2026 sauf mention)
- **Ajouts v2 :** wiki [Archon Hunt](https://wiki.warframe.com/w/Archon_Hunt), [Netracells](https://wiki.warframe.com/w/Netracells), [Deep Archimedea](https://wiki.warframe.com/w/Deep_Archimedea), [Temporal Archimedea](https://wiki.warframe.com/w/Temporal_Archimedea), [Search Pulse](https://wiki.warframe.com/w/Search_Pulse), [Bird 3](https://wiki.warframe.com/w/Bird_3), [The Icebind](https://wiki.warframe.com/w/The_Icebind), [The Descendia](https://wiki.warframe.com/w/The_Descendia), [Simulacrum](https://wiki.warframe.com/w/Simulacrum), [Companion](https://wiki.warframe.com/w/Companion), [Huras Kubrow](https://wiki.warframe.com/w/Huras_Kubrow), [Tauron Strike](https://wiki.warframe.com/w/Tauron_Strike), [Focus/Vazarin](https://wiki.warframe.com/w/Focus/Vazarin), [Effects Scaling With Enemy Stats](https://wiki.warframe.com/w/Effects_Scaling_With_Enemy_Stats), [Update 31](https://wiki.warframe.com/w/Update_31) (introduction de l'Overguard), modules `Companions/data` et `DropTables/data`. Recherches sans résultat sur l'interaction % PV / Overguard : [vortexgaming.io](https://vortexgaming.io/en/postdetail/696494), [Steam](https://steamcommunity.com/app/230410/discussions/0/3826414483635039170), [forums Warframe](https://forums.warframe.com/topic/1450429-bad-game-design-overguard/).
- Wiki officiel : [Sevagoth/Prime](https://wiki.warframe.com/w/Sevagoth/Prime), [Sevagoth/Abilities](https://wiki.warframe.com/w/Sevagoth/Abilities), [Sevagoth/Patch History](https://wiki.warframe.com/w/Sevagoth/Patch_History), [Reap](https://wiki.warframe.com/w/Reap), [Sow](https://wiki.warframe.com/w/Sow), [Gloom](https://wiki.warframe.com/w/Gloom), [Exalted Shadow](https://wiki.warframe.com/w/Exalted_Shadow), [Death's Harvest](https://wiki.warframe.com/w/Death%27s_Harvest), [Shadow Haze](https://wiki.warframe.com/w/Shadow_Haze), [Dark Propagation](https://wiki.warframe.com/w/Dark_Propagation), [Shadow Claws](https://wiki.warframe.com/w/Shadow_Claws), [Exalted Weapon](https://wiki.warframe.com/w/Exalted_Weapon), [Enemy Level Scaling](https://wiki.warframe.com/w/Enemy_Level_Scaling), [The Steel Path](https://wiki.warframe.com/w/The_Steel_Path), [Overguard](https://wiki.warframe.com/w/Overguard), [Armor](https://wiki.warframe.com/w/Armor), [Archon Shard](https://wiki.warframe.com/w/Archon_Shard), [Helminth](https://wiki.warframe.com/w/Helminth), [Roar](https://wiki.warframe.com/w/Roar), [Ghost](https://wiki.warframe.com/w/Ghost), [Stalk](https://wiki.warframe.com/w/Stalk), [Blood Rush](https://wiki.warframe.com/w/Blood_Rush), [Melee Combo](https://wiki.warframe.com/w/Melee_Combo), [Damage Reduction](https://wiki.warframe.com/w/Damage_Reduction), [Update 38](https://wiki.warframe.com/w/Update_38) à [Update 44](https://wiki.warframe.com/w/Update_44), [Epoch Operation : Taubound](https://wiki.warframe.com/w/Epoch_Operation:_Taubound), modules Lua `Warframes/data`, `Weapons/data`, `Mods/data`, `Arcane/data`, `Stances/data`, `Enemies/data`, `DropTables/data`, `Version/data`.
- Patch notes officielles : [warframe.com, PSN](https://www.warframe.com/patch-notes/psn) (Hotfix 44.1.4 + 4.1, 28/10/2026) ; [RPG Site, sortie d'Iceblade of Narin sur toutes les plateformes](https://www.rpgsite.net/news/21459-warframe-iceblade-of-narin-update-download-free-login-bonus) ; [DE, How to Play Sevagoth](https://www.warframe.com/en/news/how-to-play-sevagoth) (24/11/2023).
- Communauté : [Ninjase, Gloom Reaper Sevagoth](https://overframe.gg/build/717054/sevagoth-prime/gloom-reaper-sevagoth-sp-general-use-nuke-crit-buff-slow-shadow/) (1 531 votes, mise à jour il y a ~10 mois) ; [copie de « Shadow Realm Sevagoth »](https://overframe.gg/build/885203/sevagoth-prime/shadow-realm-sevagoth-pure-nuke-oneshot-levelcap-variant/) (original : 536 votes) ; [RubyBlossom5, The Reaper's Bible](https://overframe.gg/build/874263/sevagoth-prime/go-to-sevagoth-shadow-claws-blossoming-death-in-depth-build/) (98 votes, 22/10/2026) ; [RubyBlossom5, A Ravenous Alliance](https://overframe.gg/build/874330/sevagoth-prime/a-ravenous-alliance-sevagoth-shadow-nuke-partners-roar-build-guide-and-variants/) (19 votes, ~2 mois) ; [gameplay.tips](https://gameplay.tips/guides/warframe-the-ultimate-sevagoth-guide.html) (29/09/2026) ; [togame.io](https://togame.io/a/warframe-sevagoth-prime-best-build-2026/) (non daté, faible confiance). Les vidéos YouTube citées n'ont pas été vues.
- Prix : [warframe.market](https://warframe.market) API v2, vendeurs en jeu, 29/10/2026.

*Hors sujet, une ligne :* un Sevagoth non-Prime peut porter F2 (Roar en 3) sans toucher au Roar en 4 de ton Prime.
