# Audit hostile — Protea Prime Solo Level Cap / Endurance (guide v1.0)

> **Cible :** `builds/protea-prime-level-cap-endurance.md`, version 1.0 (commit `0c8c172`).
> **Méthode :** re-vérification de chaque affirmation critique contre le wiki officiel (descriptions in‑game, modules de données, patch notes U43–U44.1.3), recalcul des chiffres, recherche des contradictions internes.
> **Légende :** 🔴 erreur ou risque de mort · 🟠 surestimation ou angle mort · 🟡 imprécision.
> Les corrections sont appliquées dans la **v1.1** du guide (dernière section).

---

## Synthèse

Le guide v1.0 est **chiffré, mais vendu plus solide qu'il ne l'est**. Les faiblesses sont les suivantes :

- Sa promesse de survie centrale (gate de 5 s avec satellite) repose sur une page wiki que **la description in‑game ne confirme pas**.
- Il contient **deux erreurs de mécanique** : le Slash « qui traverse les shields », et l'absence d'anti‑mort.
- Il présente des **valeurs de dégâts « stacks pleins » comme des garanties** au niveau cap, précisément là où ces stacks s'effondrent.
- Il ignore **toutes les pénalités de mission**, alors que le mode endgame actuel (The Icebind, niveau 999+) **réduit le Shield Gate de 50 % par défaut**.

---

## 1. Durabilité et Shield Gating

### 🔴 1.1 La promesse « 5 s de gate avec satellite » n'est pas démontrée

- **Ce que dit le guide :** satellite accroché = gate **doublé**, 2,5 s → **5 s**.
- **Ce que disent les sources :**
  - Description **in‑game** de Grenade Fan : *« When Shields break, a Satellite is destroyed to double **minimum** Shield Gate invincibility time. »*
  - Champ technique du wiki : *« 2x s (minimum shield gate extension) »*.
  - Seule la page *Shield* du wiki affirme « 0,66 – 5 s ». C'est une interprétation éditoriale, sans patch note ni test cité.
- **Les deux lectures possibles :**
  - **A** : toute la courbe est doublée (0,66–5 s).
  - **B** : seul le plancher de 0,33 s passe à 0,66 s. Avec 1 230 shields, le gate reste alors à **2,5 s** et le satellite n'ajoute **rien**.
- **Conséquence :** le protocole v1.0 dit « n'entre dans le satellite suivant qu'à ~4 s ». **Si la lecture B est la bonne, tu passes 1,5 s à 0 shield au niveau 9999 = mort.** C'est l'instruction la plus dangereuse du guide.
- **Verdict :** seule la durée de **2,5 s** est garantie. Le doublement doit être **mesuré** (Simulacrum, ennemi niveau 9999, chrono de la barre de vie grise avec et sans satellite) avant de bâtir un timing dessus.

### 🔴 1.2 Les 3 Tauforged Azure ignorent les pénalités de mission

Le calcul est **juste** en conditions nominales (555 + 675 = 1 230 > 1 150 → 2,5 s). Il est **robuste aux variations de mods**, parce que la courbe est plate près du seuil :

| Strength (recharge satellite) | Gate obtenu |
|---|---|
| 243 % (1 215) | 2,50 s |
| 229 % (fallback Intensify : 1 145) | 2,49 s |
| 200 % (1 000) | 2,31 s |
| 150 % (750) | 1,97 s |

Il est en revanche **fragile aux pénalités de mission**, que la v1.0 ne mentionne pas :

| Pénalité (source) | Shields | Gate réel | Satellite (si lecture A) |
|---|---|---|---|
| Nominal | 1 230 | 2,50 s | 5,00 s |
| **Stunted Shields** (Icebind, **trait standard**, niveau 999+) | 1 230 | **1,25 s** | 2,50 s |
| Cryogenic Leakage (−50 %, appliqué au total) | 615 | 1,78 s | 3,55 s |
| Anemic Shields (Archimedea, plafond 500) | 500 | 1,59 s | 3,19 s |
| Flankable (Icebind, −75 %) | 308 | 1,25 s | 2,51 s |
| Flankable + Stunted | 308 | **0,63 s** | 1,25 s |
| **Bruised Shields** (Icebind : shields restaurés **uniquement** par la mêlée) | — | Satellites **inopérants** | — |
| **Untreatable** (Icebind : Health Orbs impossibles à ramasser) | — | Le moteur d'énergie meurt (cf. 2.1) | — |
| Decaying Dragon Key | — | 0,33 s fixe | — |

L'ordre d'application de Cryogenic Leakage par rapport aux shards plats n'est **pas documenté** (si la pénalité s'applique avant les shards : 952 shields, 2,25 s).

### 🔴 1.3 La micro‑fenêtre mortelle existe, et le guide l'aggrave

- **Latence réseau :** non pertinente en solo (tu es l'hôte).
- **Le vrai délai** se décompose ainsi :
  1. Animation **corps entier** de Grenade Fan, avec saut forcé de 1 m. Elle n'est accélérée par **aucun** Casting Speed dans le build, et la v1.0 a écarté l'Amber Casting Speed comme « inutile ».
  2. Vol des grenades, rebonds jusqu'à une surface horizontale, puis déploiement du satellite.
  3. Accroche quand tu es dans le rayon de 3,95 m.

  Ce délai n'est **pas mesuré** dans le guide. Pendant ce temps, à 0 shield au niveau 9999, n'importe quel tir touche la santé.
- **Contradiction interne :** la section 1.6 dit de lancer les satellites **à 4–6 m** pour éviter qu'ils s'accrochent en chaîne. La procédure d'urgence (5.4) dit de les viser **à tes pieds**. Le wiki confirme le problème : *« heavy fire can cause a single ally to acquire and lose a series of shield satellites very quickly »*. Viser à tes pieds sous un feu nourri, c'est **brûler les 4 satellites en une fraction de seconde**.
- **Verdict :** au niveau cap, le satellite **réactif** ne marche pas. La seule méthode viable est **proactive** : un satellite toujours accroché, et les casts de Grenade Fan faits **pendant** un gate ou une Rolling Guard.

### 🔴 1.4 Erreur de mécanique : le Slash ne traverse PAS les shields

- **Ce que dit le guide** (sections 1.6, 1.8 et 4.4) : *« Bleed = dégâts True (ignore armure et shields) »*.
- **Ce qui est vrai** (wiki, refonte des dégâts) : *« Toxin bypasses Shields (but not Armor) whereas Slash Status bypasses Armor but not Shields »*. Le Bleed inflige des dégâts **Cinematic** : il ignore l'**armure**, pas les shields.
- **Conséquences réelles :**
  - La seule menace qui ignore réellement les shields est le **Toxin** (plus les drains de santé type Leech).
  - Les DoT ennemis (Slash, Heat) **frappent tes shields** à chaque tick. Un tick qui casse des shields fraîchement restaurés **déclenche un gate et consomme un satellite**.
  - Rolling Guard ne sert donc pas à « sauver la santé » contre le Slash : elle sert à **empêcher les DoT de manger tes satellites**.

### 🟠 1.5 Infested = « meilleure faction » ? Pour les dégâts, oui. Pour survivre, c'est la pire

- La Heat fait ×1,5 contre les Infested, d'où l'étiquette de la v1.0.
- Mais leurs dégâts sont saturés de **Toxin** : Toxic Ancient, nuages de Mutalist Osprey, aura de 3,5 m des Septic/Venomous Eximus. Le Toxin ignore les shields **et donc le Shield Gating**. Avec 740 PV, c'est un one‑shot au cap.
- Le guide a fusionné « faction où l'on tue le plus vite » et « faction la plus sûre » : c'est faux.

### 🔴 1.6 Zéro anti‑mort, alors qu'une option existe

- **Ce que dit le guide :** « tu n'as plus aucune protection anti‑mort », avec Sacrifice comme seul filet partiel.
- **C'est faux. Arcane Escapist existe** :
  - Chaque Mercy kill donne 1 stack (maximum 9, conservés indéfiniment).
  - Sur un dégât fatal, il consomme 3 stacks : **12 s d'invulnérabilité** au R5, et +1 revive dès le R3.
  - Seuil de Mercy au cap : 10 % minimum sur les unités lourdes au‑delà du niveau ~300. Chaque proc **Impact** ajoute +8 % au seuil (jusqu'à 80 %).
  - Synergie directe : le Glaive Prime (Impact forcé sur la détonation) et l'Epitaph Prime (Impact forcé sur le tir direct) font monter le seuil tout seuls.
  - Tu es invulnérable pendant l'animation de Mercy.
- **Le bon échange n'est pas « Sculptor ou Escapist »**, mais **Molt Augmented → Arcane Escapist** au niveau cap :
  - Molt donne +60 % de Strength, ce qui fait passer Roar de +80 % à +98 %. C'est du DPS.
  - Il n'apporte rien à la survie : le seuil de recharge des satellites (1 150) est déjà atteint à 243 %.
- **Coût réel :** R5 = 21 exemplaires. En achat hebdomadaire chez Kaya Velasco (5 Pix Chip, 1 par semaine), c'est **21 semaines**. Pour aller plus vite : Temporal Archimedea ou échange (MR 11). Le R3 (10 exemplaires) donne déjà 8 s d'invulnérabilité et +1 revive.

---

## 2. Économie et stacking

### 🟢 2.1 Arcane Sculptor : le choix est confirmé, et c'est l'autre arcane qui est mal choisi

Comparaison avec Molt Efficiency (+6 % de Duration par seconde tant que les shields sont actifs, plafond +36 %) :

| Pire situation d'endurance | Avec Sculptor | Sans Sculptor (Efficiency 45 %) |
|---|---|---|
| Nominal | +32,2 énergie/s | +4,3/s (aucune marge réelle) |
| **Untreatable** (Health Orbs non ramassables) | **+1,1/s** | **−26,8/s : 250 d'énergie vidés en 9,3 s** |
| **Constricted** (énergie max −75 % → 62,5) | Cast max à 18,75 : jouable | **Dispensary et Roar (116,25) incastables** |
| Energy Exhaustion (−2/s par ennemi à 10 m, 10 ennemis) | +12,2/s | −15,8/s |

- Molt Efficiency ne produit **pas un seul point d'énergie**. Au niveau cap, ses shields sont cassés en permanence, donc son uptime est proche de **0**. Il est inférieur à Sculptor dans **toutes** les pires situations.
- **Le vrai défaut du duo d'arcanes v1.0 :** les deux arcanes sont DPS/économie. **Aucun n'est défensif**, dans un guide qui annonce « survie prioritaire ». Correction en 1.6 : remplacer Molt Augmented par Arcane Escapist.
- **Défaut secondaire de Sculptor :** un objet n'est « valide » qu'une fois posé (le wiki prend l'exemple de Brightbonnet). Les grenades de Grenade Fan déclenchent donc Sculptor **à l'atterrissage**, pas au cast. L'ouverture v1.0 « Grenade Fan, puis Dispensary immédiatement » peut **payer le Dispensary plein tarif** (116,25).

### 🟠 2.2 Roar : le « dead time » est réel, mais pas là où on le pense

- **Ce n'est pas le passif qui se « maintient » :** c'est un compteur (3 barres sur le HUD). Avec 27,3 casts/min, un 4e cast tombe toutes les **8,8 s**, soit **9,7 procs par cycle de Roar de 85 s**.
- **1 seul de ces procs** va sur Roar. Les ~8,7 autres tombent surtout sur des tourelles (rendement en √k) ou sur des satellites (aucun gain : le seuil est déjà atteint). **Environ 90 % des procs du passif sont du rendement marginal.**
- **Le vrai danger** est le **gel volontaire des casts** :
  - Pour aligner le passif, une fois les 3 barres chargées, tu ne dois **plus rien lancer** avant l'expiration de Roar.
  - Pendant cette fenêtre (jusqu'à 5 s selon la v1.0), **lancer un satellite d'urgence consomme le passif**, et Roar repart à +80 % au lieu de +110 %, **verrouillé pendant 85 s** (pas de relance possible).
  - La v1.0 ne dit pas quoi prioriser. **Règle manquante : la survie passe avant le passif, toujours.** Un Roar à +80 % ne tue personne ; un satellite manqué, si.
- **Autres frictions :**
  - « Abbreviated Abilities » (Icebind, −50 % de durée) : Roar dure 42,6 s.
  - Un Nullifier dissipe Roar. C'est en fait une **opportunité** de le réaligner.
- **🟡 Affirmation non sourcée :** « le passif s'applique aux compétences Helminth ». La page du passif dit « every 4th ability cast » sans mentionner l'Helminth. C'est **à vérifier en jeu** (valeur affichée dans le buff de Roar : 110 % attendu au lieu de 80 %).

---

## 3. Loadout et armes

### 🔴 3.1 Torid Incarnon : le Viral par défaut est un choix de facilité, et les chiffres sont des chiffres de papier

- **Précision :** le build v1.0 est **Viral/Crit, sans Slash** (pas de Hunter Munitions).
- **Choix de facilité avoué contre les Grineer.** La section 4.2 garde le Viral contre les Grineer **parce que** passer en High Voltage coûtait 61/60 de capacité. L'élément a été choisi par **contrainte de capacité**, pas par optimisation.
  - Solution simple, que la v1.0 n'a pas vue : **Primed Cryo Rounds → Rifle Elementalist** (slot Vazarin, 5) et **Malignant Force → High Voltage**. On obtient **Corrosive** (Electricity + Toxin innée), à **57/60** de capacité.
  - Avec 93,6 % de Status à 6,4 ticks/s, la Torid applique les **10 stacks de Corrosive en ~2 s** sur sa cible : **×5,98** de dégâts contre une armure au plafond. Ça rend l'arme autonome au lieu de dépendre de l'Epitaph.
- **Dépendance en chaîne.** Contre une armure de 2 700, la Torid en Viral inflige **×0,1** tant que l'Epitaph n'a pas posé sa Corrosive (fenêtre de 15,2 s). Rate le primer, et la Torid ne fait plus rien.
- **Overguard (Eximus).** Le Viral ne touche **pas** l'Overguard. Or les Eximus sont plus fréquents à haut niveau (Icebind : « Increased chance of Eximus » ; tactical bind « Bolstered Belligerents » = Overguard égal à 50 % de la santé max sur **tous** les ennemis). Au cap, le **Magnetic** (configuration Corpus) devrait être la configuration **par défaut**, et le Viral la configuration Corrupted.
- **🔴 L'effondrement des stacks.** Merciless (12 stacks, −1 stack toutes les 4 s sans kill), Galvanized Aptitude (×2), Galvanized Chamber (×5) et Molt Augmented dépendent **tous** des kills.
  - Bucket de base : **9,45** à stacks pleins contre **2,65** à 0 stack (×3,57).
  - Multishot : 3,3 contre 1,8 (×1,83).
  - **Total : ×6,5 d'écart.** Au cap, où les TTK s'allongent, l'arme se dégrade en spirale. Les chiffres de la v1.0 sont des **plafonds**, présentés comme des valeurs de travail.
- **Arcane :** Primary Merciless était imposé par la demande. Au cap, c'est l'arcane le plus sensible au rythme de kills.

### 🟠 3.2 Glaive Prime : « combo ×6 garanti » est faux

- 110 de combo initial suppose **4 stacks de Galvanized Reflex**, soit 4 kills en mêlée dans les 20 s.
- **Le plancher réel est Corrupt Charge seul : 30 de combo = ×2.** La v1.0 surestime donc la détonation d'un facteur **×3** dès que les kills ralentissent.
- Seule l'**option B** (Tandem Bond : +6 combo par coup de griffe) maintient le combo sans kills. **Avec l'option A, le Glaive s'effondre au cap.**
- Les 2,4 M par explosion sont un chiffre « stacks pleins + Roar + Tenacious ».

### 🟠 3.3 Verglas Prime / Tenacious Bond : le riven n'est pas le vrai problème, la mortalité de la sentinelle l'est

- **Sans le riven** (≥ +57,2 % de CC), Tenacious Bond est un **slot mort**. On perd ×1,29 sur le Glaive et ×1,185 sur la Torid.
  - Le build ne s'effondre **pas** pour autant (le fallback Contagious Bond est fourni), mais l'option A perd environ 20–30 % de dégâts critiques.
  - Point de contexte (H44.1.3) : les dispositions de riven ont été supprimées (toutes à l'équivalent 1.2) et l'échange de rivens est rétabli. Un riven Verglas Prime avec +57 % de CC est **facile à obtenir**. C'est un coût en Kuva et en temps, pas un mur.
- **La vraie faille :** Nautilus Prime a 560 PV et 350 shields (1 225 avec Calculated Redirection). Au 9999, c'est **un coup = une sentinelle à terre**.
  - À terre, il n'y a **plus de Cordon, d'Assault Mode** (Verglas ne tire plus, Growing Power retombe sur l'Epitaph seul) **ni de Sacrifice** (le seul « filet » vanté par la v1.0 disparaît au moment où tu en as besoin).
  - Le comportement de Tenacious Bond quand le compagnon est à terre n'est **pas documenté**.
  - Seul Vacuum continue de fonctionner.
- **Verdict : l'option A est une option d'Endurance moyenne, pas de level cap.** L'option B (Panzer Devolution : jamais hors combat, Tenacious Bond gratuit) est le seul compagnon viable au 9999. La v1.0 le laissait seulement entendre dans un tableau.

---

## 4. Verdict de robustesse

### Note de tolérance à l'erreur : **4/10** (v1.0)

Le build est un **glass cannon technique** déguisé en build de survie. Il exige en permanence, et à la main :

1. le placement et le timing d'entrée des satellites, sur un timing **non vérifié** ;
2. une Rolling Guard en < 1 s sur chaque proc Toxin ou Magnetic ;
3. un primer Epitaph toutes les ≤ 6 s (Growing Power + Corrosive) ;
4. l'alignement du passif sur Roar ;
5. la présence physique au Dispensary pour l'énergie ;
6. un rythme de kills soutenu pour 5 mécaniques à stacks.

Une erreur sur le point 1 ou 2 au cap = mort, **sans aucun filet**.

**Après corrections (v1.1) : 6/10.** Arcane Escapist apporte un filet, les satellites deviennent proactifs, le timing est sécurisé sur 2,5 s, et le compagnon B est imposé au cap. Le build reste exigeant : il ne pardonne pas le Toxin.

### Les 3 plus gros risques de mort en mission réelle

1. **Les dégâts Toxin** (Septic/Venomous Eximus, Toxic Ancients, nuages Infested). Ils ignorent les shields, donc le gate, les satellites et toute la couche défensive. 740 PV = one‑shot au cap. Seules réponses : tuer à distance, Rolling Guard en réflexe, et désormais Arcane Escapist.
2. **Le trou à 0 shield entre deux gates.** Le satellite réactif a une latence d'animation et de vol non mesurée. Sous le feu, les satellites dans le rayon s'accrochent et se détruisent en chaîne. Et si le doublement à 5 s est faux, le protocole v1.0 « entrer à 4 s » laisse **1,5 s à découvert**.
3. **Les modificateurs de mission qui désactivent le moteur du build** :
   - Stunted Shields (standard en Icebind, gate à 1,25 s) ;
   - Bruised Shields (satellites inutiles) ;
   - Untreatable (plus d'énergie Dispensary) ;
   - Miasmic Militia (immunité Toxin/Gas/Viral/Corrosive : tout le plan de statuts tombe) ;
   - Archaic Armor (pas de retrait d'armure) ;
   - Inferno (la Heat des tourelles alimente la menace).

   Le guide v1.0 n'en dit **pas un mot**.

---

## Corrections appliquées dans le guide v1.1

| # | Défaut v1.0 | Correction v1.1 |
|---|---|---|
| 1 | Gate de 5 s présenté comme acquis | 2,5 s garantis, ×2 « non confirmé » avec protocole de test ; entrée dans le satellite suivant à **~2 s** |
| 2 | Slash « traverse les shields » | Corrigé : Toxin = traverse les shields ; Slash = ignore l'armure ; les DoT ennemis mangent les satellites |
| 3 | Aucun anti‑mort | **Arcane Escapist** remplace Molt Augmented en level cap (Molt reste pour l'Endurance hors cap) |
| 4 | Urgence « satellites à tes pieds » | Remplacé par la séquence RG → satellites à 4–6 m → entrée ; « à tes pieds » seulement si la RG est en recharge |
| 5 | Viral par défaut contre les Grineer, par contrainte de capacité | Ajout de la configuration Torid **Corrosive** (57/60) ; Magnetic recommandé par défaut au cap |
| 6 | « Combo ×6 garanti » | Plancher ×2 annoncé, ×6 conditionnel ; Tandem Bond indispensable pour le Glaive au cap |
| 7 | Infested « meilleure faction » | « Meilleure en dégâts, pire en survie (Toxin) » |
| 8 | Passif sur l'Helminth affirmé | Marqué « à vérifier en jeu » ; règle survie > passif ajoutée |
| 9 | Pénalités de mission absentes | Nouvelle section avec le tableau des modificateurs et les réponses |
| 10 | Ouverture Sculptor | Attendre l'atterrissage des grenades avant le cast suivant |
| 11 | Option A présentée comme équivalente au cap | Option A = Endurance ; **option B imposée au 9999** |
| 12 | Amber Casting Speed jugée inutile | Variante level cap : 1 Tauforged Amber Casting Speed à la place d'1 Tauforged Crimson Duration |

---

## Sources ajoutées

[Grenade Fan (description in‑game)](https://wiki.warframe.com/w/Grenade_Fan) · [Shield](https://wiki.warframe.com/w/Shield) · [Arcane Escapist](https://wiki.warframe.com/w/Arcane_Escapist) · [Mercy](https://wiki.warframe.com/w/Mercy) · [Slash Damage](https://wiki.warframe.com/w/Damage/Slash_Damage) · [Toxin Damage](https://wiki.warframe.com/w/Damage/Toxin_Damage) · [Magnetic Damage](https://wiki.warframe.com/w/Damage/Magnetic_Damage) · [Protea Passive](https://wiki.warframe.com/w/Protea/Abilities/Passive) · [Arcane Sculptor](https://wiki.warframe.com/w/Arcane_Sculptor) · [Deep Archimedea](https://wiki.warframe.com/w/Deep_Archimedea) · [Update 44 (The Icebind)](https://wiki.warframe.com/w/Update_44) · [Martyr Symbiosis](https://wiki.warframe.com/w/Martyr_Symbiosis)
