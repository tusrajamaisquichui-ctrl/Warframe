# Audit hostile v2 — Protea Prime Solo Level Cap / Endurance (guide v1.3)

> **Cible :** [`protea-prime-level-cap-endurance.md`](protea-prime-level-cap-endurance.md) version 1.3 (commit `4836929`, branche `ccr-43e41b64-c6rz56`) et l'audit précédent [`audit-protea-prime-v1.md`](audit-protea-prime-v1.md).
> **Patch de référence :** Update 44.1 « Iceblade of Narin: The Icebind » / Hotfix 44.1.3 (22/10/2026), dernier correctif listé par le wiki au 26/10/2026. La version du guide (1.3) n'est pas une version du jeu.
> **Méthode :**
> - lecture intégrale des trois fichiers du dépôt et des cinq versions successives du guide (v1.0 `0c8c172` → v1.3 `4836929`) ;
> - relecture du wikitexte brut **et** du rendu d'environ 150 pages de [wiki.warframe.com](https://wiki.warframe.com/) le 26/10/2026, y compris les notes de patch officielles qu'elles reproduisent ;
> - recalcul par script de tous les chiffres structurants : gate, géométrie des satellites, tourelles avec Heat Inherit, temps de mise à mort au niveau 9999, énergie, capacités de mods (annexe B).
>
> **Limites :**
> - **aucun test en jeu n'a été réalisé** : je n'ai pas accès au jeu, et aucune mesure n'est simulée ici ;
> - les deux vidéos citées par la v1.2 n'ont pas été visionnées ;
> - plusieurs pages du wiki se contredisent : ces points sont marqués CONTESTÉ.
>
> Aucune valeur n'a été inventée : une donnée absente est marquée NON VÉRIFIÉ.

**Statuts de preuve :**
- **VÉRIFIÉ** : texte ou donnée explicite du wiki ou d'une note de patch.
- **CALCULÉ** : résultat d'une formule explicite appliquée à des données vérifiées.
- **DÉDUIT** : conclusion logique à prémisses identifiées.
- **NON VÉRIFIÉ** : hypothèse à tester.
- **RÉFUTÉ** : contredit par les preuves.
- **CONTESTÉ** : sources contradictoires.

**Gravité :** critique · élevée · moyenne · faible. **Confiance :** élevée · moyenne · faible.

---

## 1. Verdict exécutif

**Ce qui tient.** Le socle mécanique est juste sur presque tout ce qui est chiffrable :
- valeurs des compétences, coûts d'énergie, formule du shield gate ;
- les **9 totaux de capacité** des loadouts ;
- polarités et statistiques de Protea Prime ;
- Arcane Sculptor (objets valides, verrouillage à 175 %) ;
- Dispensary + Equilibrium (orbe renforcée = 110 énergie) ;
- Rolling Guard, Overguard, Arcane Escapist, Temporal Anchor et Temporal Artillery.

Roar est le bon choix Helminth : il vaut même davantage que ce que le guide annonce.

**Ce qui ne tient pas.** Six problèmes dépassent la simple imprécision.

1. **Le cadre de jeu est faux.**
   - Les modificateurs « niveau 999+ » viennent de The Icebind, **un mode réservé aux escouades de six joueurs**, sans solo ni escouade réduite.
   - Archimedea plafonne entre le niveau 250 et le niveau 500.
   - Le Simulacrum ne dépasse pas « 5 × Mastery Rank + 30 (+25) ».
   - En solo, le niveau 9999 ne s'atteint qu'après **plus de 8 heures** de mission sans fin.

   La table 3.12 n'est donc pas le bon modèle de risque pour un guide solo, et les protocoles de test « Simulacrum, ennemi niveau 9999 » (guide et audit v1) sont irréalisables.
2. **Les « stations de recharge » à 4–6 m n'existent pas.**
   - L'éventail fixe de Grenade Fan (−45° / −25° / +25° / +45°) pose les satellites **par paires espacées de 1,4 à 2,1 m**, à l'intérieur du rayon de capture de 3,95 m.
   - Sous feu nourri, chaque paire se consomme en chaîne : la couverture par cast est environ divisée par deux.
3. **Aucune réaction n'est possible contre le Toxin au cap.**
   - Un tick d'aura Septic tue Protea à travers ses shields dès le niveau 140 environ, et le coup de fléau du Toxic Ancient dès les niveaux du Steel Path.
   - Les consignes « Rolling Guard sur tout proc Toxin » et « purge immédiate » ne protègent de rien : seules la distance, une invulnérabilité déjà active ou l'Overguard protègent.
4. **La pile de filets est surévaluée en solo.**
   - Mending Soul ne relève pas un joueur seul.
   - Le Panzer en forme larvaire n'a plus de griffes, donc plus de Tenacious, Tandem ni Vicious Bond, et ses spores sont supprimées à chaque mort et à chaque retour en forme adulte.
   - Escapist offre 3 sauvetages pratiquement non renouvelables au cap.
5. **Deux affirmations sont réfutées par des notes officielles.**
   - Untreatable **ne tue pas** le moteur d'énergie : les notes de l'Update 36.0 précisent qu'Equilibrium convertit toujours les orbes de vie.
   - Cordon **ne transmet pas** les statuts via Manifold Bond.

   Deux menaces décrites par le guide n'existent plus depuis l'Update 38.0 : les auras du Toxic Ancient et de l'Ancient Disruptor.
6. **Le calcul qui justifie les shards est faux.**
   - « Dégâts ∝ Str × Dur², Duration rapporte ×2,2 plus » est vrai par cast, mais faux en DPS soutenu (3 tourelles maximum, recast à l'expiration).
   - En DPS soutenu, Strength et Duration se valent à ±1 %. À travers Roar, **2 Crimson Strength battent 2 Crimson Duration** : +5 % sur les dégâts directs et les armes, +10 % sur la Heat.

**Ce que le guide sous-estime.** Son modèle de Heat ignore Heat Inherit (chaque proc rafraîchit tous les stacks). Avec ce mécanisme :
- une seule voie de tourelle tue un Heavy Gunner Steel Path de niveau 9999 (6,1 M PV) en **≈ 14 s**, ou ≈ 10 s avec la Corrosive de l'Epitaph ;
- les tourelles restent donc létales au cap ;
- Roar y réduit le temps de mise à mort d'**≈ 44 %**, et non de 31 % (CALCULÉ, hypothèse en annexe B).

**Variante C (ancre mobile).**
- Elle **garde Roar**, qui y remplace le Dispensary : la question « la perte de Roar est‑elle compensée ? » ne concerne que le kit natif (§6.3).
- Sur le papier, c'est la plus robuste : death gate à chaque fenêtre, et l'implosion rend 67 % des dégâts enregistrés à chaque ennemi de la zone.
- Mais son économie d'énergie (−25 par ancre, aucun revenu hors orbes d'Eximus ramassées entre deux ancres) ne tient pas une montée de 8 heures.
- La Warframe y devient **vulnérable en Transference** (Protective Sling compromis).
- Son avantage « insensible à Untreatable » n'existe pas.

**Verdict.** Excellent build d'Endurance tant que les shields ne sont pas traversés d'un coup (environ niveau 110 à 450 selon l'arme ennemie et les overshields, §6.1) ; build de level cap **jouable mais nettement plus fragile que ne le dit le guide**. Il faut conserver le socle, corriger le modèle de risque, le protocole des satellites, la pile de filets et les shards, puis passer les 16 tests de la section 11 (T1 à T5 en priorité) avant toute tentative longue. La robustesse de 6/10 attribuée par l'audit v1 était optimiste.

---

## 2. Tableau des affirmations

### 2.1 Survie

| # | Affirmation du guide (section) | Statut | Preuve | Conséquence |
|---|---|---|---|---|
| 1 | `t = (S/350)^0,65 + 1/3`, plafond 2,5 s au‑delà de 1 150 shields (1.11) | **VÉRIFIÉ** | [Shield § Shield Gating](https://wiki.warframe.com/w/Shield#Shield_Gating) (formule approchée) ; notes U34 reproduites sur la page | — |
| 2 | 555 + 3 × 225 = 1 230 → 2,5 s ; 1,68 s sans shards ; 2,32 s avec 3 Azure normales (1.5) | **CALCULÉ ✔** | [Protea Prime](https://wiki.warframe.com/w/Protea/Prime) (555), [Archon Shard](https://wiki.warframe.com/w/Archon_Shard) (+225 à plat) | — |
| 3 | La durée dépend des shields régénérés depuis le dernier gate (1.11) | **VÉRIFIÉ** | Shield : « maximum shields replenished since the last shield gate » ; U34 : « amount of Shields you had upon Shield Break » | Les deux formulations divergent, mais pas au cap (coups qui vident tout) |
| 4 | Implicite : les 3 Azure sont nécessaires au gate de 2,5 s | **NON VÉRIFIÉ** | Aucune source ne dit si les **overshields** comptent | Si oui, un satellite (1 340) donne 2,5 s même à 555 shields max : les Azure ne servent qu'aux gates de régénération naturelle. Test T2 |
| 5 | Satellite = « double **minimum** », doublement à 5 s non confirmé (1.11) | **VÉRIFIÉ** (texte) / **CONTESTÉ** (effet) | [Grenade Fan](https://wiki.warframe.com/w/Grenade_Fan) (description et infobox) vs page Shield (« 0.66 – 5 s ») | La lecture prudente du guide (2,5 s) est la bonne |
| 6 | Toute restauration de shields termine le gate (1.11) | **VÉRIFIÉ** | Shield ; astuces de Grenade Fan | — |
| 7 | Satellite : 500 × Str à l'accroche, 50 × Str /s, plafond overshield 1 200, vie fixe 13 s, rayon 5 m × Range (1.7) | **VÉRIFIÉ** | Grenade Fan (wikitexte : « 13 » souligné = fixe) ; Shield (plafond 1 200) | — |
| 8 | Grenade Fan « durée fixe 13 s » (1.7) | **Partiellement RÉFUTÉ** | Wikitexte : le Shrapnel Vortex porte le marqueur *Ability Duration* | Vortex = 13 × 2,84 = **36,9 s** ; seul le satellite est fixe |
| 9 | Satellites lancés à 4–6 m = stations, « tu contrôles quand un satellite s'accroche » (1.6, 1.11) | **RÉFUTÉ (CALCULÉ)** | Angles −45/−25/+25/+45° (Grenade Fan) → paires à 1,39–2,08 m < 3,95 m | Voir C2 |
| 10 | Destruction en chaîne sous feu nourri (1.11) | **VÉRIFIÉ** | Astuces de Grenade Fan | — |
| 11 | Fast Deflection : recharge à 2,2 s qui coupe le gate (1.11) | **Partiellement VÉRIFIÉ** | Shield : recharge 4 s « after the **last hit** taken during Shield Gate » | Sous feu continu, aucune coupure ; l'interdiction reste sans coût |
| 12 | Rolling Guard : 3 s, purge, 7 s de recharge **après** l'invulnérabilité, anti‑knockdown (1.11) | **VÉRIFIÉ** | [Rolling Guard](https://wiki.warframe.com/w/Rolling_Guard) | — |
| 13 | Rolling Guard en réaction à un proc Toxin, « purge immédiate » (3.10, 3.13) | **RÉFUTÉ au cap (CALCULÉ)** | [Enemy Level Scaling](https://wiki.warframe.com/w/Enemy_Level_Scaling), [Eximus](https://wiki.warframe.com/w/Eximus), [Toxic Ancient](https://wiki.warframe.com/w/Toxic_Ancient) | Le coup est létal avant toute réaction (C3) |
| 14 | Toxin = « la seule menace qui traverse les shields » (1.11) | **Partiellement RÉFUTÉ** | Eximus (Leech : 5 % des PV max par coup) ; Icebind (Framecurse : 50 dégâts directs sur la santé) | — |
| 15 | Slash : ignore l'armure, pas les shields (1.11, 1.16) | **VÉRIFIÉ** | [Toxin Damage](https://wiki.warframe.com/w/Damage/Toxin_Damage) : « Toxin bypasses Shields … Slash Status bypasses Armor but not Shields » | Correction v1 validée |
| 16 | Implicite : le gate est une invulnérabilité qui bloque les statuts | **CONTESTÉ** | Shield (« gain Invulnerability ») vs [Invulnerability](https://wiki.warframe.com/w/Invulnerability) : le Shield Gating « is not the same as invulnerability as a mechanic », alors que la vraie invulnérabilité bloque tout nouveau statut | Voir C5 |
| 17 | Primed Sure Footed bloque l'auto‑stagger de l'Epitaph et du Glaive (1.11) | **VÉRIFIÉ** | [Primed Sure Footed](https://wiki.warframe.com/w/Primed_Sure_Footed) | — |
| 18 | Overguard joueur : neutre sauf Void, annule tous les statuts, gate de 0,5 s, arrête le Toxin (3.10) | **VÉRIFIÉ** | [Overguard](https://wiki.warframe.com/w/Overguard) ; Toxin : « ignores … Shields, but not Overguard » | Il immunise aussi contre Energy Exhaustion (non dit) |
| 19 | Fortifier : 1 Overguard par tranche de 100 dégâts, ×8, plafond 15 000 (3.10) | **VÉRIFIÉ** | [Secondary Fortifier](https://wiki.warframe.com/w/Secondary_Fortifier) | — |
| 20 | « 15 000 = un coup + 0,5 s, ce n'est pas un mur » (3.10) | **INCOMPLET** | Fortifier : « any secondary with a firing rate >2.0 can maintain functional immortality » | Un seul point d'Overguard absorbe un coup entier (M14) |
| 21 | Escapist : 12 s au R5, 3 stacks par déclenchement, 9 max, permanents, +1 revive dès le R3 (3.2) | **VÉRIFIÉ** | [Arcane Escapist](https://wiki.warframe.com/w/Arcane_Escapist) | — |
| 22 | Martyr Symbiosis se déclenche avant Escapist sans le consommer (3.4) | **VÉRIFIÉ** | Arcane Escapist (astuces) | — |
| 23 | Mercy : seuil plancher de 10 %, +8 % par Impact jusqu'à 80 % au cap (3.2) | **CONTESTÉ** | [Parazon](https://wiki.warframe.com/w/Parazon), [Impact](https://wiki.warframe.com/w/Damage/Impact_Damage) : l'ordre plancher/Impact n'est pas précisé ; « you cannot Mercy Kill enemies with Overguard active » | Au 9999, l'Impact peut ne rien ajouter (M15) |
| 24 | Mending Soul = 4 relevés instantanés « une fois à terre » (3.10) | **RÉFUTÉ en solo (DÉDUIT)** | [Vazarin](https://wiki.warframe.com/w/Focus/Vazarin) : une charge est consommée quand **un joueur interagit avec un joueur à terre** | Couche n° 7 vide en solo |
| 25 | Protective Sling : 5 s d'invulnérabilité, ta Warframe comprise, 10 énergie (3.10) | **VÉRIFIÉ** | Vazarin | — |
| 26 | Warframe invulnérable en Transference « en règle générale » (3.10) | **VÉRIFIÉ, exception omise** | [Operator/Gameplay](https://wiki.warframe.com/w/Operator/Gameplay) : Temporal Anchor → « Vulnerable until the ability's duration ends » | La Sling devient dangereuse en variante C |
| 27 | Mort de l'Operator : retour shields vides, Transference Static (3.10) | **VÉRIFIÉ + précision** | Operator/Gameplay : « depletes all Warframe shields (which also does **not** kick in shieldgating) » ; Static 80 / 50 / 20 %, puis bleedout | Aucun gate au retour |

### 2.2 Compétences et dégâts

| # | Affirmation (section) | Statut | Preuve | Conséquence |
|---|---|---|---|---|
| 28 | Blaze : 500 × Str Heat, 3 s × Dur, 3 tirs/s, 30 m × Range, 130°, 3 tourelles, +100 % par touche cumulatif, 100 % Heat, AoE 2 m, perforation des corps (1.7) | **VÉRIFIÉ** | [Blaze Artillery](https://wiki.warframe.com/w/Blaze_Artillery) (cadence, cône et bonus soulignés = fixes) ; ligne de vue requise | — |
| 29 | Tourelle ∝ Str × Dur², « Duration rapporte ×2,2 plus » (1.5, 1.6, 1.3 NM) | **RÉFUTÉ (CALCULÉ)** | Modèle 7.3 | Vrai par cast, faux en DPS soutenu (M1) |
| 30 | Roar ×2,1 = −31 % de TTK, rendement en 1/√k (1.8) | **RÉFUTÉ au cap (CALCULÉ)** | Modèle 7.4 | Cible qui survit à une tourelle : gain quasi linéaire, −44 % (M2) |
| 31 | Archon Vitality : un stack Heat de plus, identique, par application (1.17) | **VÉRIFIÉ** | [Archon Vitality](https://wiki.warframe.com/w/Archon_Vitality) | — |
| 32 | Chaque stack fait 6 ticks à partir de son tir (1.17) | **RÉFUTÉ** | [Heat Damage](https://wiki.warframe.com/w/Damage/Heat_Damage) : chaque proc « refreshes the duration of **all** currently active heat stacks » (Heat Inherit) | Le DoT est sous‑estimé (M2) |
| 33 | Retrait d'armure Heat plafonné à 50 %, rampe 15/30/40/50 % sur 2 s (1.17) | **VÉRIFIÉ** | Heat Damage | — |
| 34 | Heat × Corrosive multiplicatifs → ×7,15 (1.16) | **VÉRIFIÉ / CALCULÉ ✔** | Heat Damage (formule multiplicative), [Armor](https://wiki.warframe.com/w/Armor) | — |
| 35 | Roar : bonus de faction compté deux fois sur les DoT, multiplicatif avec le reste, non relançable, appliqué aux compagnons (1.8) | **VÉRIFIÉ** | [Roar](https://wiki.warframe.com/w/Roar) | — |
| 36 | Roar Helminth = 30 % × Str → +80,4 % / +110,4 % (1.7) | **CALCULÉ ✔** ; passif sur l'Helminth **NON VÉRIFIÉ** | Roar ; [Passif](https://wiki.warframe.com/w/Protea/Abilities/Passive) muet sur l'Helminth ; aucune seconde source trouvée | — |
| 37 | « ×1,80 → ×2,28 » et « ×3,25 → ×5,22 » dans le **socle** (1.8, 1.16, 1.17) | **RÉFUTÉ (incohérence interne)** | Sans Molt (configuration ③) : plafond ×2,10 en direct, ×4,43 sur DoT | Les valeurs avec Molt contaminent le socle (M3) |
| 38 | Growing Power : +25 % pendant 6 s, statut d'**arme** (compagnon inclus) (1.3) | **VÉRIFIÉ** | [Growing Power](https://wiki.warframe.com/w/Growing_Power) | — |
| 39 | Passif : +100 % additif au 4e cast, combinaison libre (1.10) | **VÉRIFIÉ** (Helminth : NON VÉRIFIÉ) | Passif | — |
| 40 | Temporal Anchor : 22,7 s, 3 s d'invulnérabilité, death gate (5 % PV, ragdoll), rembobinage énergie/shields/santé/munitions/combo, coût d'activation non rendu (1.8, 3.14) | **VÉRIFIÉ** | [Temporal Anchor](https://wiki.warframe.com/w/Temporal_Anchor) | L'implosion frappe **chaque** ennemi de la zone avec 67 % du total enregistré (sous‑exploité, §6.3) |
| 41 | Temporal Artillery : tourelle la plus proche, 360°, plafond 20× au R3, durée suspendue (3.14) | **VÉRIFIÉ** | [Temporal Artillery](https://wiki.warframe.com/w/Temporal_Artillery) | — |
| 42 | Seuil suiveuse / fixe ≈ 1,6 ennemi par tir ; −22 % en couloir dense (3.14) | **CALCULÉ ✔** | Modèle 7.7 : 1,58 et −23 % à k = 5 | — |

### 2.3 Énergie

| # | Affirmation (section) | Statut | Preuve | Conséquence |
|---|---|---|---|---|
| 43 | Sculptor : efficacité **verrouillée** à 175 % pendant 12 s, rafraîchissable, objets valides Grenade Fan / Blaze / Dispensary, sans effet sur le cast déclencheur, actif une fois l'objet posé (1.4, 1.9, 1.12) | **VÉRIFIÉ** | [Arcane Sculptor](https://wiki.warframe.com/w/Arcane_Sculptor) (Temporal Anchor n'est **pas** un objet valide) | Acquisition : Hunhow + bonus de complétion d'Uranus Proxima ; les noms « Scoria's Angel / Kuva Wytch » ne figurent pas sur la page |
| 44 | Coûts 38,75 / 77,5 / 116,25 à 45 % et 6,25 / 12,5 / 18,75 sous Sculptor ; 322/min contre 1 996/min (1.9) | **CALCULÉ ✔** | Coûts de base 25/50/75/75 (pages des compétences) | — |
| 45 | Dispensary : 1 pickup toutes les 2 s, orbe renforcée de 100 PV, doublon 25 % × Str, spawn sauté si non ramassé ; 2 664 énergie = 37,5/s (1.9) | **VÉRIFIÉ / CALCULÉ ✔** | [Dispensary](https://wiki.warframe.com/w/Dispensary), [Equilibrium](https://wiki.warframe.com/w/Equilibrium) | Plafond théorique : il faut tout ramasser |
| 46 | Equilibrium 110 %, ramassage à pleine santé, ignore Amber et Restorative Bond (1.9) | **VÉRIFIÉ** | Equilibrium, Archon Shard | — |
| 47 | Untreatable : 37,5 → **6,5** énergie/s (3.12) | **RÉFUTÉ** | [Deep Archimedea](https://wiki.warframe.com/w/Deep_Archimedea), notes U36.0 : « Equilibrium Mod: Energy can now be gained when picking up Health Orbs » ; [The Icebind](https://wiki.warframe.com/w/The_Icebind) : même note | Moteur intact, seule la guérison est perdue (M4) |
| 48 | Eximus = 1 *Large* Energy Orb (50) + 2 orbes de vie ≈ +104 (1.9) | **NON VÉRIFIÉ, probablement surestimé** | Eximus : « one Energy Orb, two Health Orbs » | ≈ +79 avec une orbe standard de 25 |
| 49 | Ouverture en 5 casts, le seul plein tarif étant Grenade Fan (1.12) | **INCOMPLET (CALCULÉ)** | Protea Prime : énergie de départ **75** | 75 − 38,75 − 18,75 − 12,5 = 5 < 18,75 : Roar est impossible sans ramasser la 1re orbe (M9) |
| 50 | Arcane Energize ≤ 10/s (1.9) | **VÉRIFIÉ** | [Arcane Energize](https://wiki.warframe.com/w/Arcane_Energize) (150 à 60 %, recharge 15 s) | — |

### 2.4 Armes et compagnons

| # | Affirmation (section) | Statut | Preuve | Conséquence |
|---|---|---|---|---|
| 51 | Torid Incarnon : 51 Toxin, CC 29 %, CD 3,1, 8/s, statut 39 % ; profil moddé 102 / 147 % / 6,82 / 93,6 % / 6,4/s (1.14, 2.4) | **VÉRIFIÉ / CALCULÉ ✔** | [Torid](https://wiki.warframe.com/w/Torid), [Torid Incarnon Genesis](https://wiki.warframe.com/w/Torid_Incarnon_Genesis) | L'achat à 120 pl inclut déjà les ressources d'installation |
| 52 | Capacités : Torid 60/60/57, Epitaph 57, Glaive 69, Verglas 49 + riven, Nautilus 58, Panzer 59, griffes 66 | **CALCULÉ ✔ (9/9)** | Infobox de chaque mod (coût de base + rang, ½ si polarité assortie) | — |
| 53 | Merciless : −1 stack toutes les 4 s sans kill (3.5) | **VÉRIFIÉ** | [Primary Merciless](https://wiki.warframe.com/w/Primary_Merciless) : seuls les kills **de l'arme** comptent | Au cap, ce sont les tourelles qui tuent : la Torid reste presque à 0 stack |
| 54 | Epitaph Prime : direct 100 (Impact forcé, 50 %), AoE 30 Blast sur 10 m (Cold forcé), chargeur 1, reload 0,6 → 0,21 s (1.14, 2.5) | **VÉRIFIÉ / CALCULÉ ✔** | [Epitaph Prime](https://wiki.warframe.com/w/Epitaph_Prime) | **Vaultée** (non dit) ; cadence réelle à mesurer (≥ 2/s pour la chaîne Fortifier ?) |
| 55 | Glaive Prime : détonation de 1 184 Blast sur 4,8 m sans atténuation, Impact + Slash forcés, CC 26 %, CD 2,4, Condition Overload sans effet (1.14) | **VÉRIFIÉ** | [Glaive Prime](https://wiki.warframe.com/w/Glaive_Prime) | **Vaulté** (non dit) |
| 56 | Détonation ≈ 2,4 M au plafond, ≈ 0,3 M au plancher (2.6) | **CALCULÉ ✔** (2,45 / 0,30) | Modèle 7.8 | Le multiplicateur Heavy des Glaives (2× / 3×, [Melee](https://wiki.warframe.com/w/Melee#Heavy_Attack)) n'est pas inclus : **NON VÉRIFIÉ**, sous‑estimation possible |
| 57 | Melee Duplicate : CC optimal (3·CD − 4)/(2·CD − 2) = 135,5 % (139 % avec Tenacious), ×1,60 (2.6) | **VÉRIFIÉ / CALCULÉ ✔** | [Melee Duplicate](https://wiki.warframe.com/w/Melee_Duplicate) : le second coup **relance** le palier critique | — |
| 58 | Tenacious Bond : CC ≥ 50 %, +1,2 additif (×1,29 Glaive, ×1,185 Torid) (1.13) | **VÉRIFIÉ / CALCULÉ ✔** | [Tenacious Bond](https://wiki.warframe.com/w/Tenacious_Bond) : `1 + tier × (CD − 1 + final)` | — |
| 59 | Manifold Bond : « Cordon applique les statuts de Verglas » (2.3) | **RÉFUTÉ** | [Cordon](https://wiki.warframe.com/w/Cordon) : « Does **not** apply status effects through Manifold Bond » | Il ne reste que −3 s de recharge par kill (M5) |
| 60 | Viral Quills : 40 % de statut (3.4) | **RÉFUTÉ** | [Viral Quills](https://wiki.warframe.com/w/Viral_Quills) : 2,2 % réels ; les spores ne demandent pas de proc | — |
| 61 | Devolution : le Panzer « ne quitte jamais le combat » (3.4) | **VÉRIFIÉ (présence) / INCOMPLET (fonction)** | [Panzer Devolution](https://wiki.warframe.com/w/Panzer_Devolution) : larve à 3 épines toutes les 5 s, 30 s non accélérables, spores supprimées à la mort ; Viral Quills : spores supprimées au retour en forme adulte | C4 |
| 62 | Tenacious, Tandem et Vicious Bond actifs au 9999 (3.4, 3.7) | **NON VÉRIFIÉ (DÉDUIT : dépendent des coups de griffe de la forme adulte)** | [Tandem Bond](https://wiki.warframe.com/w/Tandem_Bond), [Vicious Bond](https://wiki.warframe.com/w/Vicious_Bond) | Test T11 |
| 63 | Sepsis Claws ne détruit pas le Viral des épines | **DÉDUIT ✔** | [Sepsis Claws](https://wiki.warframe.com/w/Sepsis_Claws) : « Only converts **primary** elemental damage » | — |
| 64 | Cull the Weak : +240 % sur coup non critique (3.4) | **VÉRIFIÉ, sans effet** | CC des griffes 107,5 % : aucun coup non critique | La partie +60 % par statut reste utile |
| 65 | Restorative Bond (Panzer) : « synergie Dispensary » (3.4) | **QUASI NUL au cap (DÉDUIT)** | Panzer Devolution : la transformation « cannot be sped up » ; +60 PV par orbe inutiles au cap | Slot à recycler (Martyr Symbiosis) |
| 66 | Gilding : 10 Son Token + 5 000 **crédits** (3.4) | **RÉFUTÉ** | [Vulpaphyla](https://wiki.warframe.com/w/Vulpaphyla) : 5 000 de **standing** ; le Gilding offre une polarité | — |
| 67 | Nautilus Prime : 560 PV, 350 shields (2.3) | **VÉRIFIÉ** | [Nautilus Prime](https://wiki.warframe.com/w/Nautilus/Prime) | — |

### 2.5 Ennemis et modes

| # | Affirmation (section) | Statut | Preuve | Conséquence |
|---|---|---|---|---|
| 68 | Faiblesses U36 (×1,5 / ×0,5) pour 7 factions (1.15) | **VÉRIFIÉ** | [Damage/Overview Table](https://wiki.warframe.com/w/Damage/Overview_Table) | **Omet** The Murmur (résiste au Viral), Scaldra, Techrot et Narmer (résiste au Magnetic) : ce sont les factions de Deep Archimedea, Temporal Archimedea et The Icebind |
| 69 | Toxic Ancient : aura −80 % de Toxin pour ses alliés (1.15) | **RÉFUTÉ (périmé)** | Toxic Ancient : aura retirée en **U38.0 (13/12/2024)** | La vraie menace est son fléau de 450 Toxin sur 7 m |
| 70 | Ancient Disruptor : aura de drain d'énergie (1.15) | **PÉRIMÉ** | [Ancient Disruptor](https://wiki.warframe.com/w/Ancient_Disruptor) : aura retirée en U38.0 ; Magnetic sur l'attaque lourde | — |
| 71 | Nullifier : tourelles aveugles dans la bulle, buffs dissipés (1.15) | **VÉRIFIÉ** | Blaze Artillery ; [Nullifier Crewman](https://wiki.warframe.com/w/Nullifier_Crewman) | — |
| 72 | Arctic : les nuages de la Torid traversent la bulle (3.11) | **RÉFUTÉ (DÉDUIT)** | Eximus : la barrière « protects all units inside from ranged attacks **and area of effects** » ; 10 000 PV non scalés | Il faut tirer sur la barrière |
| 73 | Entropic : entrer dans l'orbe et y détoner le Glaive (3.11) | **RÉFUTÉ** | Eximus : « All ranged melee attacks from **Glaives** and Gunblades are reduced by 90% » ; les attaques radiales ne traversent pas l'orbe | Seule la mêlée normale fonctionne |
| 74 | Septic/Venomous, Energy Leech, Leech, Blitz (3.11) | **VÉRIFIÉ** | Eximus | Blitz : PSF annule le knockdown, **pas** les dégâts |
| 75 | Icebind : niveau 999+, Stunted Shields en trait standard (3.12) | **VÉRIFIÉ, mais mode à 6 joueurs** | The Icebind : « playing with fewer than six players is not currently available » ; [Update 44](https://wiki.warframe.com/w/Update_44) (44.1) : « Six player squads » | C1 |
| 76 | Formulations des modificateurs cités (Stunted, Flankable, Bruised, Untreatable, Constricted, Energy Exhaustion, Miasmic Militia, Archaic Armor, Inferno, Abbreviated, Framecurse, Anemic, Cryogenic) | **VÉRIFIÉ** (texte), sauf l'effet d'Untreatable | The Icebind ; Deep Archimedea ; [Temporal Archimedea](https://wiki.warframe.com/w/Temporal_Archimedea) ; Shield | §8.4 |
| 77 | Archimedea = mission de niveau 999+ (mode d'emploi) | **RÉFUTÉ** | Deep Archimedea : 250–275 / 375–400 ; Temporal Archimedea : 350–375 / 475–500 | — |
| 78 | Tests « Simulacrum, ennemi niveau 9999 » (1.11, 3.14, audit v1) | **RÉFUTÉ (irréalisable)** | [Simulacrum](https://wiki.warframe.com/w/Simulacrum) : niveau maximal « 5x their Mastery Rank plus 30 », +25 sur certaines cartes | Protocoles à réécrire (§11) |
| 79 | Patch U44.1.3 du 22/10/2026 (en‑tête) | **VÉRIFIÉ** | Update 44 | — |

---

## 3. Erreurs critiques (mort ou invalidation du build)

### C1 — Le modèle de risque du cap décrit un mode qui ne se joue pas en solo
- **Gravité :** critique (cadre). **Confiance :** élevée.
- **Preuves :**
  - The Icebind exige six joueurs, et « Public matchmaking and playing with fewer than six players is not currently available » ([The Icebind](https://wiki.warframe.com/w/The_Icebind), [Update 44.1](https://wiki.warframe.com/w/Update_44) : « Six player squads », niveau 999+, missions de 10–15 min).
  - Deep et Temporal Archimedea : niveaux 250 à 500.
  - Simulacrum : niveau maximal de 5 × MR + 30 (+25 sur certaines cartes).
  - En solo, le niveau 9999 n'est atteint qu'après **8 heures et plus** de mission sans fin ([Enemy Level Scaling](https://wiki.warframe.com/w/Enemy_Level_Scaling)).
- **Impact réel :**
  - La table 3.12 vise un contenu d'escouade de 10–15 minutes, alors que le vrai défi solo est une montée de 8 heures, du niveau 100 au niveau 9999, sans aucune erreur.
  - Dans ce cadre, les ressources finies (3 sauvetages Escapist, réserve d'énergie de la variante C) et la fatigue d'exécution pèsent bien plus lourd que les Binds.
  - Les protocoles « Simulacrum 9999 » sont impossibles.
  - Plusieurs modificateurs d'Archimedea, jouables en solo, frappent directement ce build et ne sont pas cités :
    - *Elemental Potency* : +85 % de résistance élémentaire, ce qui ramène la Heat des tourelles à environ ×0,15 ;
    - *Adaptive Aberrations* ;
    - *Myopic Munitions*.
- **Correction :** séparer trois contextes :
  1. Endurance solo (Steel Path sans fin, jusqu'au seuil des one‑shots, environ niveau 110–450 selon l'arme ennemie) ;
  2. montée solo au 9999 (8 h+, mêmes mécaniques, ressources finies) ;
  3. Archimedea et Icebind, contenus d'escouade ou de niveau 250–999 dont les modificateurs propres sont traités à part.

  Réécrire les tests avec des conditions atteignables (section 11).
- **Gain attendu :** un modèle de risque aligné sur ce que le joueur affrontera réellement.
- **Limite :** il n'existe pas de banc d'essai au 9999 ; les tests se feront au plus haut niveau atteignable (Simulacrum avec Steel Path, ou mission sans fin).

### C2 — Les « stations de recharge » à 4–6 m se consomment par paires
- **Gravité :** critique. **Confiance :** moyenne (géométrie : élevée ; effet en jeu : à mesurer).
- **Preuves :** angles fixes −45°, −25°, +25° et +45° ; attache « au premier allié le plus proche **sans satellite attaché** » dans un rayon de 5 m × Range ; restauration qui termine le gate ([Grenade Fan](https://wiki.warframe.com/w/Grenade_Fan), [Shield](https://wiki.warframe.com/w/Shield#Shield_Gating)).
- **Calcul :** à 5 m, la paire −45°/−25° est espacée de **1,74 m** (1,39 m à 4 m ; 2,08 m à 6 m), pour un rayon de capture de 3,95 m. Une paire ne devient séparable qu'à partir de **11,4 m** de lancer (tableau 7.2).
- **Mécanisme :**
  1. Tu entres dans A : le gate se termine et les shields sont rechargés.
  2. Le coup suivant déclenche un gate, et A se détruit.
  3. B, déjà dans le rayon, s'accroche aussitôt, recharge les shields et **coupe ce nouveau gate**.

  Sous feu dense, une paire vaut donc un seul gate de 2,5 s au lieu de deux. Le Panzer en larve, qui flotte à côté de toi, est aussi une cible éligible (DÉDUIT, NON VÉRIFIÉ).
- **Impact réel :**
  - Couverture par cast : environ 5 s au lieu de 10 s (2,5 s au lieu de 5 s sous Stunted Shields).
  - Avec Rolling Guard (3 s toutes les 10 s), la cadence de satellites prévue par le guide (10–13 s) laisse des trous sous feu continu.
- **Correction :**
  - Compter **une paire = une station** et relancer toutes les ≤ 5 s sous feu dense, toujours pendant un gate ou une RG.
  - Pour obtenir quatre stations distinctes : lancer à ≥ 11–12 m, ou entrer par l'extérieur de l'arc (bande d'environ 1,7 m où un seul satellite est à portée).
  - Test T3.
- **Gain attendu :** suppression des trous de couverture involontaires.
- **Limites :** rebonds, surface d'atterrissage et hauteur de flottement des satellites ne sont pas modélisés. Une Range plus faible (sans Stretch : rayon de 1,7 m) ne séparerait les paires qu'au‑delà d'environ 5 m de lancer, et réduirait la portée des tourelles à 10,2 m.

### C3 — Toxin : aucune réaction possible au cap, seulement de la prévention
- **Gravité :** critique. **Confiance :** élevée (calcul) / moyenne (application du ×3 Infested aux auras).
- **Preuves :**
  - Dégâts ennemis = `1 + 0,015 × Δniveau^1,55`, ×3 pour les Infested.
  - Aura Septic : 10 Toxin scalés, proc garanti.
  - Fléau du Toxic Ancient : 450 Toxin sur 7 m.
  - Le Toxin ignore les shields, mais pas l'armure ni l'Overguard ([Enemy Level Scaling](https://wiki.warframe.com/w/Enemy_Level_Scaling), [Eximus](https://wiki.warframe.com/w/Eximus), [Toxic Ancient](https://wiki.warframe.com/w/Toxic_Ancient), [Toxin](https://wiki.warframe.com/w/Damage/Toxin_Damage)).
- **Calcul :**
  - Santé effective de Protea face au Toxin : 740 PV avec 185 d'armure, soit **968**.
  - Un tick d'aura Septic tue en un coup dès le niveau ≈ **138** (si le ×3 s'applique) ou ≈ 285 (sinon).
  - Le fléau du Toxic Ancient est létal à **tout niveau du Steel Path**.
  - Au 9999, un tick d'aura vaut environ 238 k (713 k avec le ×3).
- **Impact réel :** les consignes « Rolling Guard sur tout proc Toxin », « purge immédiate » et « ne jamais encaisser sur la santé » (3.10, 3.13) ne protègent de rien : il n'y a plus de Protea à purger.
- **Correction :** réécrire la règle en défense préventive :
  1. Distance ≥ 3,5 m des Septic/Venomous et ≥ 7 m d'un Toxic Ancient qui frappe (3e coup de sa séquence).
  2. Overguard chargé (Fortifier) avant tout contact Infested.
  3. N'entrer au contact que pendant une RG.
  4. Escapist, Martyr Symbiosis ou le death gate comme dernier recours.
- **Gain :** supprime une fausse sécurité.
- **Limite :** sous Miasmic Militia face aux Infested, seuls des Venomous Eximus apparaissent : c'est un mode à éviter.

### C4 — La pile de filets compte des couches vides ou intermittentes
- **Gravité :** élevée. **Confiance :** moyenne à élevée.
- **Preuves et impact, couche par couche :**

| Couche (guide 3.10) | Réalité en solo | Preuve |
|---|---|---|
| 1. Overguard (Fortifier) | ✔ conditionnelle (Eximus requis) ; **enchaînable** au‑delà de 2 tirs/s | Secondary Fortifier |
| 2. Gate + satellite | ✔ 2,5 s (1,25 s en Icebind) ; consommation par paires (C2) | Shield, Grenade Fan |
| 3. Rolling Guard | ✔ 3 s toutes les 10 s, soit 30 % du temps | Rolling Guard |
| 4. Protective Sling | ✔ 5 s, mais Operator tué d'un coup au cap, retour **sans gate** ; Warframe vulnérable si Temporal Anchor est actif | Vazarin, Operator/Gameplay |
| 5. Death gate de l'ancre (variante C) | ✔ limité par l'énergie (−25 par ancre) | Temporal Anchor |
| 6. Escapist | ✔ 3 × 12 s, **quasi non renouvelable** au cap (Mercy à 10 %, Overguard bloque le Mercy) | Arcane Escapist, Parazon |
| 7. Mending Soul | ✘ **vide en solo** | Vazarin |
| *(absente)* Martyr Symbiosis | ✔ 1 s + soin, se déclenche avant Escapist sans le consommer | Martyr Symbiosis, Escapist |

  Le **Panzer**, présenté comme obligatoire, perd au cap l'essentiel de sa valeur :
  - forme adulte : 680 PV et 370 + 1 537 shields, tuée en deux coups au 9999 ;
  - larve : 30 s non accélérables, sans griffes, donc sans Tenacious, Tandem ni Vicious Bond (DÉDUIT) ;
  - spores supprimées à chaque transition ;
  - Restorative Bond inutile.
- **Correction :**
  - Retirer Mending Soul de la pile et ajouter Martyr Symbiosis à la place de Restorative Bond (P1).
  - Présenter Escapist comme **3 vies pour toute la montée**, à charger avant le niveau 150 (seuil de Mercy à 40 %).
  - Ne pas compter Tenacious et Tandem Bond au cap tant que le test T11 n'est pas passé.
- **Gain :** une estimation honnête du nombre d'erreurs tolérées.
- **Limite :** l'ordre d'exécution entre le death gate de l'ancre et Escapist reste inconnu (T13).

### C5 — Statuts reçus pendant un gate : point contesté qui peut rendre le protocole létal
- **Gravité :** élevée. **Confiance :** faible (sources contradictoires).
- **Preuves :** la page [Shield](https://wiki.warframe.com/w/Shield#Shield_Gating) parle d'« Invulnerability ». La page [Invulnerability](https://wiki.warframe.com/w/Invulnerability) classe le Shield Gating parmi les effets « similar to invulnerability … not the same as invulnerability as a mechanic » et précise que la vraie invulnérabilité empêche tout nouveau statut.
- **Impact si les statuts passent pendant le gate (DÉDUIT) :**
  - Un proc Toxin reçu pendant le gate tique sur la **santé** dès la fin du gate, car le Toxin ignore les shields rendus par un satellite : « entrer dans un satellite à ~2 s » devient alors mortel.
  - La règle « ne superpose jamais RG et gate » devient fausse : la RG pendant le gate est la seule purge possible avant l'échéance.
  - Les DoT Slash/Heat/Electricity reçus pendant le gate détruisent le satellite suivant, ce que le guide décrit déjà.
- **Correction :** règle conditionnelle :
  - si une icône de statut apparaît pendant un gate, **RG avant la fin du gate et aucun satellite avant la purge** ;
  - sinon, garder l'enchaînement gate → RG → satellite.

  Test T5.
- **Limite :** tant que T5 n'est pas fait, la règle prudente coûte des RG.

### C6 — La variante C est présentée comme « la plus sûre » sans budget viable sur une montée longue
- **Gravité :** élevée (pour la variante C). **Confiance :** élevée (mécanique) / moyenne (impact).
- **Preuves :**
  - Le rembobinage rend l'énergie dépensée, mais efface celle ramassée pendant la fenêtre ; le coût d'activation n'est pas rendu ([Temporal Anchor](https://wiki.warframe.com/w/Temporal_Anchor)).
  - La Warframe est vulnérable en Transference pendant l'ancre ([Operator/Gameplay](https://wiki.warframe.com/w/Operator/Gameplay)).
  - Untreatable ne coupe pas Equilibrium (U36.0).
- **Impact :**
  - Coût de 25 par ancre, soit −1,1/s : 10 ancres, environ **3,8 min** d'autonomie.
  - Revenu : seulement les orbes d'énergie d'Eximus (25) ramassées **entre** deux ancres, car Equilibrium est retiré et les orbes de vie ne rapportent plus rien.
  - Chaque death gate coûte une ancre de plus et l'implosion de la fenêtre.
  - Sur 8 heures, la variante perd son death gate dès que la réserve tombe sous 25.
  - Son argument « insensible à Untreatable » est caduc.
- **Correction :** la réserver aux fenêtres courtes à haut risque, ou aux missions où les Energy Restores sont autorisés. Ne jamais lancer Protective Sling sous l'ancre. Ramasser les orbes juste après chaque rembobinage. Garder 2 Crimson **Duration** dans cette variante (ancre de 22,7 s contre 20,3 s).
- **Limite :** les tests 1 à 3 du guide restent nécessaires.

---

## 4. Erreurs de calcul et de mécanique

| # | Erreur | Gravité | Confiance | Preuve | Correction |
|---|---|---|---|---|---|
| **M1** | « Dégâts ∝ Str × Dur² ; Duration rapporte ×2,2 plus » (1.5, 1.6 ; Narrow Minded « Duration² ») | moyenne | élevée | Cadence fixe de 3 tirs/s et plafond de 3 tourelles ([Blaze Artillery](https://wiki.warframe.com/w/Blaze_Artillery)) : DPS soutenu ∝ Str × Dur, et Strength alimente aussi Roar (7.3) | 2 Crimson **Strength** (+5 % en direct et sur les armes, +10 % sur la Heat) ; l'option Amber coûte −5 % et non −10 % |
| **M2** | Modèle de DoT sans Heat Inherit ; TTK en 1/√k | moyenne | élevée (mécanisme) / moyenne (ampleur) | [Heat Damage](https://wiki.warframe.com/w/Damage/Heat_Damage) ; modèle 7.4 | Le DoT se cumule tant que la cible est touchée toutes les ≤ 6 s : Roar = −44 % de TTK au cap, garder les cibles dans les voies |
| **M3** | Valeurs avec Molt (×2,28, ×5,22, −56 %, −81 %) dans le socle et dans la comparaison des kits de la variante C | faible | élevée | Interne (v1.3 annonce pourtant la séparation) | Socle : ×1,80 → ×2,10 en direct, ×3,25 → ×4,43 sur DoT |
| **M4** | Untreatable tue le moteur d'énergie (guide 3.12, audit v1 2.1) | moyenne | élevée | Notes U36.0 (Deep Archimedea) ; note identique sur l'Untreatable de l'Icebind | Moteur intact (≈ 37,5/s théoriques) ; seule la guérison disparaît |
| **M5** | Cordon applique les statuts de Verglas via Manifold Bond | moyenne (②) | élevée | [Cordon](https://wiki.warframe.com/w/Cordon) | Garder Manifold Bond pour son seul effet réel (−3 s de recharge par kill d'un ennemi à ≥ 3 statuts) |
| **M6** | Auras du Toxic Ancient et de l'Ancient Disruptor | faible | élevée | Retirées en U38.0 (pages ennemies) | Remplacer par : fléau Toxin de 7 m (Toxic Ancient) et Magnetic de l'attaque lourde (Disruptor) |
| **M7** | Arctic (nuages qui traversent) et Entropic (détonation du Glaive dans l'orbe) | moyenne | moyenne / élevée | [Eximus](https://wiki.warframe.com/w/Eximus) | Arctic : tirer sur la barrière (10 000 PV, ni crit ni scaling). Entropic : mêlée normale uniquement, Glaive à distance −90 % |
| **M8** | Option Amber Casting Speed : « raccourcit l'animation de Grenade Fan », coût −10 % | faible | moyenne | Casting Speed est confirmé pour Blaze, Dispensary et Anchor, rien pour Grenade Fan ; coût réel −5,1 % (7.3) | NON VÉRIFIÉ jusqu'au test T4 |
| **M9** | Ouverture : Roar impossible avec 75 d'énergie de départ | faible | moyenne | [Protea Prime](https://wiki.warframe.com/w/Protea/Prime) (Starting Energy 75) | Ramasser la 1re orbe renforcée (t + 2 s après le Dispensary, +110) avant Roar |
| **M10** | « Large Energy Orb (50) » sur chaque Eximus | faible | moyenne | Eximus : « one Energy Orb » | +79 (25 + 2 × 27) et non +104 |
| **M11** | Gilding en crédits ; Glaive Prime et Epitaph Prime non signalés comme vaultés | faible | élevée | Vulpaphyla, pages des armes | 5 000 de standing ; signaler le statut « Vaulted » |
| **M12** | Viral Quills à 40 % ; Cull the Weak « +240 % non critique » | faible | élevée | Viral Quills ; CC des griffes 107,5 % | 2,2 % réels ; bonus non critique inactif |
| **M13** | « Durée fixe 13 s » appliquée au Vortex | faible | élevée | Wikitexte de Grenade Fan | Vortex 36,9 s (33 s avec 2 Crimson Strength) |
| **M14** | Fortifier sous‑estimé, avec une incohérence entre 3.8 (« seuil de 2 tirs/s ») et 3.10 (« un coup + 0,5 s ») | moyenne | moyenne | [Secondary Fortifier](https://wiki.warframe.com/w/Secondary_Fortifier) | 1 point d'Overguard absorbe un coup entier ; à > 2 tirs/s sur un Eximus, les gates de 0,5 s s'enchaînent (Kuva Nukor 10/s ; cadence réelle de l'Epitaph à mesurer) |
| **M15** | Seuil de Mercy relevé par l'Impact au cap | élevée (renouvellement d'Escapist) | faible | [Parazon](https://wiki.warframe.com/w/Parazon) : ordre non précisé ; Overguard bloque le Mercy | Charger les 9 stacks avant le niveau 150 ; au cap, considérer qu'ils ne se renouvellent pas |
| **M16** | Archimedea classée en « niveau 999+ » | faible | élevée | Pages Archimedea | 250–500 |
| **M17** | Factions omises (Murmur, Scaldra, Techrot, Narmer) | moyenne | élevée | [Overview Table](https://wiki.warframe.com/w/Damage/Overview_Table) | Murmur : résiste au Viral, faible à Electricity et Radiation ; Techrot : faible à Gas et Magnetic, résiste au Cold ; Scaldra : faible à Impact et Corrosive, résiste au Gas ; Narmer : résiste au Magnetic |
| **M18** | Modificateurs anti‑spam de compétences absents | élevée (Archimedea/Icebind) | élevée | Icebind et Archimedea | Static Siphon, Antimatter Foes / Dark Antimatter, Entropic Overload, Thin Boundary, Ability Overload, Myopic Munitions, Elemental Potency, Adaptive Aberrations, Hypersensitive, Dropped Guard (Overguard −75 %) |
| **M19** | Archaic Armor : « seul le Slash répond » | faible | élevée | Icebind : « Each hit they take reduces their maximum armor by 1% » | Les armes à cadence élevée (tourelles 3/s, faisceau de la Torid 6,4/s, Nukor 10/s) érodent aussi l'armure |
| **M20** | Link Redirection présenté comme un atout pour les satellites | faible | moyenne | Grenade Fan (compagnons éligibles) | Il rend seulement le vol de satellites moins inutile ; ces satellites ne protègent pas Protea |
| **M21** | Glaive : multiplicateur Heavy (2× / 3×) absent du calcul | faible | faible | [Melee § Heavy Attack](https://wiki.warframe.com/w/Melee#Heavy_Attack) | NON VÉRIFIÉ ; possible sous‑estimation d'un facteur 2 (T12) |
| **M22** | Aucune mention de la vulnérabilité en Transference sous l'ancre | moyenne (C) | élevée | Operator/Gameplay | Pas de Protective Sling sous l'ancre |

---

## 5. Analyse slot par slot

| Slot | Choix du guide | Verdict | Justification |
|---|---|---|---|
| Helminth (4) | Roar | **Conserver** | ×1,80 → ×2,10 sur tout, ×3,25 → ×4,43 sur DoT (VÉRIFIÉ) ; au cap, TTK d'une voie 14 s contre 25 s sans Roar (CALCULÉ) |
| Aura | Growing Power | **Conserver** | Tourelles : ×1,10 sur Strength et ×1,04 via Roar, soit ≈ +15 % en direct et +20 % sur DoT. Corrosive Projection ne gagne (+16,5 %) que contre une armure sans Corrosive (CALCULÉ) |
| Exilus | Primed Sure Footed | **Conserver** | Auto‑stagger de l'Epitaph et du Glaive (VÉRIFIÉ) |
| 1 | Blind Rage | **Conserver** | Satellite ≥ 1 150 dès 230 % ; Roar |
| 2 | Stretch | **Conserver** | Range 79 % (tourelles 23,7 m) ; c'est aussi la cause du rayon de 3,95 m qui crée les paires (C2) |
| 3 | Equilibrium | **Conserver** | Moteur d'énergie, qui fonctionne aussi sous Untreatable (U36.0) |
| 4 | Archon Vitality | **Conserver** | Double stack Heat (VÉRIFIÉ) ; les +370 PV sont inutiles au cap |
| 5 | Umbral Intensify | **Conserver** | +44 % sans malus ; repli Intensify validé (gate de 2,49 s en Arsenal, 2,5 s avec Growing Power) |
| 6 | Primed Continuity | **Conserver** | Duration linéaire |
| 7 | Narrow Minded | **Conserver, pour la bonne raison** | ×1,54 de DPS soutenu avec les shards du guide, ×1,64 avec 2 Crimson Strength (linéaire, pas Duration²). [Transient Fortitude](https://wiki.warframe.com/w/Transient_Fortitude) (+55 % / −27,5 %) à la place : ×0,67, soit ×0,73 en direct et ×0,80 sur la Heat avec Roar (CALCULÉ) |
| 8 | Rolling Guard | **Conserver** | Seule invulnérabilité à la demande (30 % du temps) |
| Arcane 1 | Sculptor | **Conserver** | −27,9 énergie/s par rapport à 45 % d'efficacité (CALCULÉ) |
| Arcane 2 (②) | Molt Augmented | **Conserver** | Kills de toutes sources, compagnon compris ; conservé jusqu'à la mort |
| Arcane 2 (③) | Escapist | **Conserver** | Seul anti‑mort d'arcane ; compter 3 vies par montée (C4) |
| Shards | 3 Tauforged Azure | **Conserver jusqu'au test T2** | Si les overshields comptent, ils ne servent plus qu'aux gates de régénération naturelle |
| Shards | 2 Tauforged Crimson Duration | **Remplacer par 2 Crimson Strength** (②, ③) ; **garder Duration en variante C** | +5 % en direct et sur les armes, +10 % sur la Heat (7.3) ; en C, Duration allonge la fenêtre d'ancre |
| Option ③ | 1 Amber Casting Speed | **Non recommandé avant T4** | Effet sur Grenade Fan non démontré ; coût −5 % |
| Torid Incarnon | Viral (②) / Magnetic ou Corrosive (③) | **Conserver** | Profil correct ; au cap, simple applicateur de statuts (Merciless ne compte que ses propres kills) |
| Epitaph Prime | Encumber (②) / Fortifier (③) | **Conserver** | Corrosive en zone de 14,4 m : ×1,97 sur les tourelles contre l'armure (CALCULÉ) ; arme vaultée |
| Glaive Prime | Melee Duplicate | **Conserver** | Optimum de CC confirmé ; arme vaultée ; inutile contre Entropic |
| Nautilus Prime (②) | Cordon … Manifold Bond | **Conserver, corriger le texte** | Cordon multiplie k (gain linéaire sur les tourelles) ; Manifold Bond = recharge seulement |
| Panzer (③) | Restorative Bond | **Remplacer par Martyr Symbiosis** | Restorative Bond est quasi nul (larve non accélérable) ; Martyr Symbiosis protège Escapist (VÉRIFIÉ) ; 53/60 |
| Focus | Vazarin | **Conserver pour Protective Sling** | Mending Soul ne compte pas en solo |

---

## 6. Analyse des loadouts

### 6.1 Configuration A — Endurance standard (Molt, Nautilus, Viral)
- **Avantages :**
  - meilleure configuration de dégâts soutenus avant le cap ;
  - Cordon multiplie le nombre d'ennemis touchés par tir, et la moyenne du multiplicateur de tourelle croît linéairement avec k (7.3) ;
  - Molt +60 %, Roar jusqu'à +128 %, énergie très excédentaire.
- **Faiblesses :**
  - la sentinelle meurt dès que les coups deviennent lourds ;
  - Manifold Bond surévalué (M5) ;
  - Infested : auras Toxin létales à travers les shields dès le niveau 140 environ (C3).
- **Échec :** un tir traverse 1 230 shields d'un coup. Selon l'arme ennemie, cela arrive vers le **niveau 112–286** (base de 100 à 25 dégâts, Grineer/Corpus), et vers 179–447 avec les overshields pleins (CALCULÉ). La « frontière » du guide existe donc, mais elle arrive tôt contre les armes lourdes.
- **Modification minimale :** 2 Crimson Strength ; corriger Manifold Bond, Toxic Ancient et Disruptor ; ouverture énergie.

### 6.2 Configuration B — Level Cap 9999 (Escapist, Panzer, Magnetic/Corrosive, Fortifier, Vazarin)
- **Avantages :**
  - Escapist donne 3 vies ;
  - l'Overguard de Fortifier est la seule couche passive qui arrête le Toxin, et elle s'enchaîne sur les Eximus ;
  - Magnetic multiplie jusqu'à ×4,25 **tous** les dégâts infligés à l'Overguard, tourelles comprises ;
  - les tourelles restent létales (14 s par Heavy Gunner et par voie).
- **Faiblesses :**
  - protocole des satellites (C2) ;
  - prévention du Toxin (C3) ;
  - pile surévaluée (C4) ;
  - Panzer intermittent ;
  - Escapist non renouvelable ;
  - armes à stacks inertes.
- **Échecs typiques :**
  1. Feu dense, RG en recharge, paire de satellites consommée en chaîne : trou de couverture, puis Escapist.
  2. Contact avec un Venomous ou un Toxic Ancient : mort instantanée.
  3. Overguard vidé hors d'Eximus, puis un coup unique.
  4. Après 3 Escapist, plus aucun filet automatique.
- **Modifications minimales :** C2 à C5, Martyr Symbiosis, 2 Crimson Strength, retrait de Mending Soul.

### 6.3 Configuration C — Variante « ancre mobile » (Temporal Artillery)
On présente souvent cette variante comme un renoncement à Roar. Dans le guide, **C garde Roar** : il remplace le Dispensary, et Temporal Anchor revient. La perte de Roar ne concerne que le kit natif. Deux kits sont donc à évaluer.

| | Ancre mobile (C, guide) | Kit natif (sans Roar) |
|---|---|---|
| Roar | ✔ | ✘ (−44,6 % en direct, −69 % sur DoT ; TTK d'une voie 25 s contre 14 s) |
| Death gate | ✔ par fenêtre de 22,7 s | ✔ |
| Énergie | −25 par ancre, sans revenu hors orbes d'Eximus ramassées entre deux ancres | Dispensary + Equilibrium, mais orbes effacées si ramassées **pendant** l'ancre (placer l'ancre au Dispensary) |
| Implosion | 67 % du total enregistré, rendus **à chaque ennemi** dans 11,85 m (VÉRIFIÉ, texte) ; perdue sur un death gate | idem, sans le bonus de Roar |
| Transference | Warframe **vulnérable** pendant l'ancre | idem |

- **Compensation offensive :** l'implosion est potentiellement la plus grosse source de dégâts de zone du kit, car Heat Inherit fait grimper le total enregistré. Sa valeur exacte est **NON VÉRIFIÉE** : on ignore si l'enregistrement se fait avant ou après réduction, et s'il compte l'overkill. Elle ne remplace pas le ×3,25 à ×4,43 de Roar sur tous les DoT de la carte.
- **Compensation défensive :** oui, nettement. Roar n'a aucune valeur défensive, alors que l'ancre apporte le death gate, 3 s d'invulnérabilité par ancre et une purge à chaque rembobinage.
- **Verdict sur C :** c'est le meilleur kit de survie **à court terme** (fenêtres de moins de 4 min), à dégâts égaux ou supérieurs grâce à l'implosion. En revanche, ce n'est pas un kit de montée de 8 heures sans source d'énergie, et il ne devient pas « la référence au 9999 » du seul fait de réussir les tests 1 et 2 : il faut aussi valider le budget d'énergie et le test 3.

---

## 7. Calculs de dégâts et d'énergie

Toutes les valeurs ci‑dessous sont **CALCULÉES** à partir de données VÉRIFIÉES. Les hypothèses sont listées en annexe B.

### 7.1 Shield gate
| Shields au break | Gate | Sous Stunted (×0,5) |
|---|---|---|
| 555 (sans shards) | 1,68 s | 0,84 s |
| 1 005 (3 Azure normales) | 2,32 s | 1,16 s |
| ≥ 1 150 (1 230, satellite à 1 215 ou plus) | 2,50 s | 1,25 s |
| 1 145 (satellite Intensify en Arsenal) | 2,49 s | 1,25 s |
| 615 / 952 (Cryogenic, après / avant shards) | 1,78 / 2,25 s | 0,89 / 1,13 s |
| 500 (Anemic) | 1,59 s | 0,80 s |
| 307,5 (Flankable) | 1,25 s | 0,63 s |

### 7.2 Géométrie des satellites (angles −45/−25/+25/+45°, rayon 3,95 m)
| Distance de lancer | Écart dans une paire | Écart entre paires | Paire dans le rayon ? |
|---|---|---|---|
| 4 m | 1,39 m | 3,38 m | **oui** |
| 5 m | 1,74 m | 4,23 m | **oui** |
| 6 m | 2,08 m | 5,07 m | **oui** |
| 10 m | 3,47 m | 8,45 m | **oui** |
| 11,4 m | 3,96 m | 9,64 m | non |
| 15 m | 5,21 m | 12,68 m | non |

### 7.3 Strength contre Duration (3 tourelles, recast à l'expiration)
| Shards (Str / Dur en mission) | Dégâts par cast | DPS de base | Direct avec Roar | Heat (Roar²) | Armes | Roar (4e cast) |
|---|---|---|---|---|---|---|
| **Guide : 2 Crimson Duration** (268 / 284 %) | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 | +80,4 % (+110,4 %) |
| 2 Crimson Strength (298 / 254 %) | 0,893 | 0,999 | **1,049** | **1,101** | **1,050** | +89,4 % (+119,4 %) |
| 1 + 1 (283 / 269 %) | 0,949 | 1,002 | 1,027 | 1,053 | 1,025 | +84,9 % (+114,9 %) |
| Option Amber (268 / 269 %) | 0,899 | 0,949 | 0,949 | 0,949 | 1,000 | +80,4 % |

*k = 1 ennemi par tir ; à k = 3, les écarts sont identiques à ±1 point. Contrepartie des 2 Crimson Strength : tourelles 7,62 s, Roar 76 s, Dispensary 63,5 s, Vortex 33 s, soit +0,5 énergie/s.*

### 7.4 Heat Inherit et temps de mise à mort au 9999 (une voie, une tourelle relancée à l'expiration)
Cible : Heavy Gunner Steel Path, niveau 9999, **6,10 M PV**, armure plafonnée à 2 700 ([Enemy Level Scaling](https://wiki.warframe.com/w/Enemy_Level_Scaling)).

| Armure | Modèle du guide (6 ticks par stack) | Heat Inherit | Heat Inherit, 1 tir sur 3 touche |
|---|---|---|---|
| Pleine (Archaic Armor) | 56 s | **27 s** | 46 s |
| Retrait Heat (−50 %) | 18,6 s | **14 s** | 24 s |
| Heat + Corrosive ×10 | 11,6 s | **10 s** | 17 s |
| Retrait Heat, **sans Roar** | — | 25 s | — |
| Kuva Grineer (Heat ×0,5) | 33 s | 20 s | — |

Sur 30 s, trois tourelles sur une cible infligent ≈ 7,7 M en direct contre ≈ 174 M de DoT (valeurs avant armure et faction) : **le DoT pèse environ 20 fois le direct**. Dans ce régime, multiplier les dégâts réduit le TTK de façon presque linéaire. Roar ×1,80 donne −44 %, et non −31 % comme le dit le guide.

### 7.5 Niveau 9999 : ordres de grandeur
| Grandeur | Valeur |
|---|---|
| Multiplicateur de dégâts ennemi | ×23 767 (Grineer/Corpus : ×23 768 avec leur ×2 ; Infested : ×71 301 avec leur ×3) |
| Multiplicateur de santé | Grineer ×8 138 · Infested ×12 212 · Corpus ×2 127 |
| Overguard d'un Eximus | ≈ 12,4 M |
| Protea | Shields 2 460 effectifs (4 860 avec overshields) ; santé 968 effective : **tout coup est létal** |
| Aura Septic, fléau Toxic Ancient, zone Energy Leech, onde Blitz | ≈ 238 k / 10,7 M / 1,19 M / 2,38 M (avant le ×3 éventuel des Infested) |

### 7.6 Énergie, y compris les pires fenêtres
| Situation | Socle (Sculptor actif) | Sans Sculptor |
|---|---|---|
| Consommation nominale | 322/min = 5,4/s (5,9/s avec 2 Crimson Strength) | 1 996/min = 33,3/s |
| Production théorique (tout ramasser) | 2 664 par Dispensary = 37,5/s (40,1/s avec 2 Crimson Strength) | idem |
| Ouverture (75 d'énergie) | Grenade Fan → Dispensary → Blaze : **il reste 5** → ramasser une orbe avant Roar | 75 < 77,5 : Grenade Fan seul |
| Sculptor retombé (> 12 s sans objet) | 1er cast : Grenade Fan 38,75, puis Dispensary 18,75 → **57,5 pour relancer le moteur** | — |
| Réserve seule (aucune orbe) | 250 / 5,4 = 46 s | 7,5 s |
| Proc Magnetic | −120 sur 3 s (texte ; 90 selon l'historique), soit 48 % de la réserve ; la purge RG arrête le drain | — |
| Constricted (max 62,5) | Jouable ; après retombée de Sculptor, **seul Grenade Fan** est lançable (Blaze à 77,5 > 62,5) | Injouable |
| Energy Exhaustion (10 ennemis à 10 m) | −20/s : il faut ≥ 25,4/s d'apport ; l'Overguard en immunise | — |
| Untreatable | **Inchangé** (U36.0) : plus de soins, l'énergie reste | — |
| Moteur à l'arrêt (0 énergie, Dispensary expiré, Sculptor retombé) | Redémarrage = 1 Eximus (≈ 79) ou des orbes de Synth Deconstruct (27) → Grenade Fan → Dispensary | — |
| Variante C | −25 par ancre (22,7 s) : 10 ancres ≈ 3,8 min sans revenu | — |

### 7.7 Tourelle suiveuse (plafond 20×) contre tourelle fixe (8,52 s)
| k ennemis par tir | Multiplicateur moyen fixe | Suiveuse / fixe | 2 fixes + 1 suiveuse, rapporté à 3 fixes |
|---|---|---|---|
| 1 | ×13,3 | 1,51 | 1,17 |
| 1,58 | ×20,4 | 0,98 | 0,99 |
| 3 | ×37,8 | 0,53 | 0,84 |
| 5 | ×62,4 | 0,32 | **0,77** |

### 7.8 Détonation du Glaive Prime (avant armure et Viral)
| Cas | Dégâts |
|---|---|
| Plafond du guide : combo ×6, Tenacious, Roar 2,10, Duplicate | 2,45 M |
| Combo ×6, sans Tenacious (larve) | 1,90 M |
| Combo ×2, Tenacious, Roar | 0,82 M |
| Plancher du guide : ×2, sans Tenacious ni Roar | 0,30 M |

*Si le multiplicateur Heavy 2× des Glaives s'applique à la détonation, toutes ces valeurs doublent (NON VÉRIFIÉ, test T12).*

---

## 8. Scénarios d'échec et limites de survie

### 8.1 Décomposition de la séquence de protection
| Étape | Durée | Statut |
|---|---|---|
| 1. Perte de protection (shields vidés) | instantanée au cap | CALCULÉ (7.5) |
| 2. Rolling Guard | animation de roulade (cabriole aérienne propre à Protea, plus de distance) puis 3 s d'invulnérabilité | durée de l'animation **NON VÉRIFIÉE** |
| 3. Animation de Grenade Fan | corps entier, saut forcé de 1 m | durée **NON VÉRIFIÉE** ; effet de Casting Speed **NON VÉRIFIÉ** |
| 4. Trajectoire et rebonds | jusqu'à une surface horizontale | **NON VÉRIFIÉ** |
| 5. Déploiement | satellite flottant « plusieurs mètres » au‑dessus de son ancrage | hauteur **NON VÉRIFIÉE** (réduit le rayon horizontal réel) |
| 6. Accrochage | instantané dans 3,95 m, mais **le premier allié** à portée (compagnon possible) | VÉRIFIÉ / DÉDUIT |
| 7. Restauration et fin du gate | 1 340 immédiats (1 490 avec 2 Crimson Strength) ; termine le gate | VÉRIFIÉ |

Intervalles où Protea peut subir des dégâts :
- les étapes 3 à 6 si elles débordent la RG ou le gate ;
- tout moment entre la fin d'un gate et l'accroche suivante ;
- toute la période où la RG est en recharge sans gate ni Overguard.

La procédure d'urgence 1.18 (RG, puis Grenade Fan, atterrissage, puis marche jusqu'au satellite en moins de 3 s) est **plausible, mais jamais mesurée**. C'est le maillon le plus fragile : test T4.

### 8.2 Couverture sous feu continu (CALCULÉ, hypothèses en annexe B)
| Source | Couverture |
|---|---|
| Rolling Guard | 3 s toutes les 10 s, soit 30 % |
| Satellites espacés (lancer ≥ 11,4 m) | ≤ 4 × 2,5 = 10 s par cast (5 s en Icebind) |
| Satellites par paires (lancer à 4–6 m) | ≈ 2 × 2,5 = **5 s par cast** (2,5 s en Icebind) |
| Overguard enchaîné (Fortifier > 2 tirs/s sur un Eximus) | continu tant que l'on tire sur un Eximus, sans autre action possible (Glaive, Grenade Fan) |

Conclusion : sous feu continu, il faut un Grenade Fan toutes les ≤ 5 s, par paires, et chaque cast est une animation corps entier à faire pendant une invulnérabilité. Sinon, Escapist finit par se déclencher. Trois Escapist couvrent 36 s de trous **sur toute la montée**.

### 8.3 Menaces simultanées
| Scénario | Résultat probable | Réponse |
|---|---|---|
| RG en recharge, aucun satellite, feu continu | Mort ou Escapist | Satellites à tes pieds (ils brûlent en chaîne, une seule fenêtre de 2,5 s) ; Protective Sling seulement si l'Operator peut sortir à couvert |
| Septic ou Toxic Ancient au contact | Mort ou Escapist, quels que soient les shields | Prévention (C3) |
| Energy Leech et Magnetic pendant un gate | Drain de 120 ; statut éventuellement appliqué (C5) | Sortir de la zone ; RG avant le satellite si une icône apparaît |
| Nullifier sur une tourelle ou sur toi | Roar dissipé, tourelles aveugles ; le satellite accroché, effet de compétence, est probablement dissipé lui aussi (NON VÉRIFIÉ) ; Rolling Guard, effet de mod, n'est pas concernée | Crever la bulle au Torid avant d'y entrer ; une dissipation de Roar est aussi l'occasion de le réaligner sur le passif |
| Entropic, puis Arctic | Glaive à −90 % ; nuages de la Torid bloqués | Mêlée normale ; tirer sur la barrière |
| Constricted, puis retombée de Sculptor | Seul Grenade Fan est lançable | Ne jamais rester 12 s sans poser d'objet |

### 8.4 Modificateurs demandés : fonctionnement, boucle touchée, contournement
| Modificateur (source, formulation vérifiée) | Build fonctionnel ? | Boucle ou ressource touchée | Contournement |
|---|---|---|---|
| Stunted Shields (Icebind, 6 joueurs : « Full Shield Gate immunity duration reduced by 50% ») | Oui, mais très tendu | Gate de 1,25 s ; un Grenade Fan toutes les ≤ 2,5 s par paires | Satellites espacés, Overguard, RG |
| Flankable (Icebind, personnel : shields max −75 %, bouclier électrique frontal) | Difficilement | Gate de 1,25 s (0,63 s avec Stunted) ; si les overshields comptent (T2), les satellites rendent 2,5 s | Rester face aux ennemis ; à éviter |
| Bruised Shields (Icebind, tactique : « Shields can only be restored via melee attacks ») | Couche satellites perdue (DÉDUIT) | Gates de satellite | Melee Assimilation (restauration par kill de Heavy : compte comme « via melee » ? NON VÉRIFIÉ), Overguard, RG |
| Untreatable (Icebind et Archimedea, personnel) | **Oui** | Guérison seulement ; l'énergie via Equilibrium reste (U36.0) | Aucun |
| Constricted (Icebind et Archimedea : énergie max −75 %) | Oui avec Sculptor | 62,5 max ; seul Grenade Fan après une retombée | Recaster un objet toutes les < 12 s |
| Energy Exhaustion (Icebind et Archimedea : −2/s par ennemi à 10 m) | Oui | −20/s à 10 ennemis | Overguard (immunité VÉRIFIÉE) ; garder la distance |
| Miasmic Militia (Icebind, mission : immunité Toxin/Gas/Viral/Corrosive, nuage de Gas à la mort) | Partiellement | Viral, Corrosive et le plan Panzer tombent ; seuls des Venomous apparaissent face aux Infested | Magnetic partout ; Heat et Slash restent ; éviter la combinaison avec les Infested |
| Archaic Armor (Icebind, tactique : armure non retirable, −1 % d'armure max par coup reçu) | Oui | Retrait Heat et Corrosive inopérants | Cadence de coups (tourelles, faisceau, Nukor) et Slash |
| Inferno (Icebind, mission : la Heat des joueurs **et** des ennemis nourrit l'Inferno) | **Non** | Toute la boucle de dégâts est en Heat | Autre Warframe |

---

## 9. Corrections recommandées, par priorité

| Priorité | Correction | Section du guide | Gain | Limite |
|---|---|---|---|---|
| **P0** | Réécrire le cadre : Icebind = 6 joueurs ; Archimedea = 250–500 ; montée solo au 9999 = 8 h+ ; tests réalisables | Mode d'emploi, 3.12, 1.11, 3.14 | Modèle de risque juste | — |
| **P0** | Satellites par paires : une station = une paire, relance toutes les ≤ 5 s sous feu dense, ou lancer à ≥ 11,4 m | 1.6, 1.11, 1.12, 1.18, 3.13 | Supprime les trous involontaires | À valider (T3) |
| **P0** | Toxin = prévention seulement (distances, Overguard, contact pendant une RG) | 1.11, 1.15, 3.10, 3.13 | Supprime une fausse sécurité | — |
| **P0** | Règle conditionnelle « statut pendant le gate → RG avant tout satellite » | 1.11, 3.13 | Évite la mort différée par un Toxin actif | Coûte des RG tant que T5 n'est pas fait |
| **P1** | Pile de filets : retirer Mending Soul, ajouter Martyr Symbiosis, Escapist = 3 vies par montée | 3.10, 3.4 | Estimation honnête | — |
| **P1** | Panzer : Restorative Bond → Martyr Symbiosis (53/60) ; Tenacious et Tandem au cap = NON VÉRIFIÉ | 3.4, 3.7 | +1 couche anti‑mort | T11, T13 |
| **P1** | Shards : 2 Crimson Strength en ② et ③ (Duration seulement en C) ; réécrire 1.5 | 1.1, 1.5, 1.6, 2.x, 3.1, 3.3 | +5 % en direct et sur les armes, +10 % sur la Heat | — |
| **P1** | Untreatable : moteur intact ; retirer l'argument de la variante C | 3.12, 3.14 | Décisions justes | — |
| **P1** | Fortifier : enchaînement d'Overguard (> 2 tirs/s), cohérence entre 3.8 et 3.10 | 3.10 | Couche principale contre les Eximus | Cadence réelle de l'Epitaph (T9) |
| **P1** | Variante C : budget d'énergie, Transference vulnérable, réserve aux fenêtres courtes | 3.14 | Évite une panne d'ancre en cours de montée | — |
| **P2** | Heat Inherit, Roar −44 %, Duration linéaire (Narrow Minded) | 1.8, 1.16, 1.17 | Modèle de dégâts juste | Hypothèse T8 |
| **P2** | Socle : retirer les valeurs avec Molt (×2,28, ×5,22) | 1.8, 1.16, 1.17, 3.14 | Cohérence de la v1.3 | — |
| **P2** | Menaces : Toxic Ancient, Disruptor, Arctic, Entropic ; factions Murmur, Techrot, Scaldra, Narmer | 1.15, 3.11 | Données à jour | — |
| **P2** | Modificateurs absents (Static Siphon, Antimatter, Entropic Overload, Thin Boundary, Myopic, Elemental Potency, Adaptive Aberrations, Dropped Guard) | 3.12 | Couverture complète | — |
| **P2** | Ouverture : ramasser la 1re orbe avant Roar ; orbe d'Eximus ≈ +79 | 1.9, 1.12, 1.18 | Ouverture sans blocage | — |
| **P2** | Petites erreurs : Gilding en standing, armes vaultées, Viral Quills 2,2 %, Cull the Weak, Vortex 36,9 s, Archaic Armor | divers | Exactitude | — |

---

## 10. Build final recommandé et variantes

### 10.1 Build recommandé : variante V1 « socle corrigé »

**Level cap solo (montée longue)**
| Élément | Choix | Justification |
|---|---|---|
| Warframe | Protea Prime, kit Grenade Fan / Blaze Artillery / Dispensary / **Roar** | Inchangé (§5) |
| Mods | Inchangés : Growing Power · Primed Sure Footed · Blind Rage · Stretch · Equilibrium · Archon Vitality · Umbral Intensify · Primed Continuity · Narrow Minded · Rolling Guard (71/74) | Tous vérifiés |
| Arcanes | Arcane Sculptor + Arcane Escapist (9 stacks avant le niveau 150) | Seuil de Mercy à 40 % avant le niveau 150 |
| Shards | 3 Tauforged Azure (Shield) + **2 Tauforged Crimson Ability Strength** | 7.3 ; Azure à réévaluer après T2 |
| Stats | Strength 273 % (Arsenal), 298 % (Growing Power), 398 % (4e cast) · Duration 254 % · Range 79 % · Efficiency 45 % → 175 % | — |
| Valeurs clés | Tourelle 1 490 par tir, 7,62 s · satellite 1 490 (1 990 au 4e cast), 13 s, 3,95 m · Dispensary 63,5 s, doublon 74,5 % · Roar +89,4 % / +119,4 %, 76 s · Vortex 33 s | — |
| Primaire | Torid Incarnon Magnetic (Corrosive contre Grineer, Kuva et Scaldra) + Primary Merciless | Applicateur de statuts au cap |
| Secondaire | Epitaph Prime Corrosive + Secondary Fortifier (Kuva Nukor Magnetic + Fortifier si Eximus en masse : V2) | ×1,97 sur les tourelles contre l'armure ; Overguard |
| Mêlée | Glaive Prime Viral + Melee Duplicate (swaps Magnetic et Corrosive du guide) | — |
| Compagnon | Panzer Vulpaphyla, **Martyr Symbiosis à la place de Restorative Bond** (53/60) | C4 |
| Focus | Vazarin (Protective Sling, hors ancre et hors ligne de tir) | Mending Soul n'est pas compté |
| Procédures | Satellites par paires (≤ 5 s) ou espacés (≥ 11,4 m) ; Grenade Fan seulement en invulnérabilité ; prévention Toxin ; « statut pendant le gate → RG d'abord » ; enchaînement d'Overguard sur les Eximus ; 1re orbe avant Roar | §3 |

**Endurance (avant le cap) :** configuration ② du guide, avec 2 Crimson Strength, Manifold Bond gardé pour sa seule recharge, ouverture corrigée.

### 10.2 Les trois variantes

**V1 — Socle corrigé (identité du build).** Détaillée ci‑dessus.
- **Modifications :** 2 Crimson Duration → 2 Crimson Strength ; Restorative Bond → Martyr Symbiosis ; procédures C2 à C5.
- **Gains :** +4,9 % de dégâts directs de tourelle, +10,1 % de Heat, +5 % sur les armes ; une couche anti‑mort de plus ; fin des trous de couverture involontaires.
- **Pertes :** −10,7 % de dégâts par cast (sans effet sous Sculptor) ; Roar, Dispensary et Vortex plus courts (+0,5 énergie/s de consommation).
- **Supérieure :** partout où le build du guide est jouable.
- **Preuves :** §7.3, Grenade Fan, Martyr Symbiosis.
- **Incertitudes :** T2 (Azure), T3 (paires), T5 (statuts).

**V2 — Dégâts soutenables (cap, indépendants des kills).**
- **Modifications :**
  - Secondaire : Epitaph → **Kuva Nukor Magnetic** (Frostbite + Jolt) + Fortifier.
  - Torid Incarnon en **Corrosive** à plein temps (57/60), qui reprend le retrait d'armure.
  - Le reste comme V1.
- **Gains :**
  - Overguard volé à 10 ticks/s, au‑dessus du seuil de 2 tirs/s : enchaînement continu sur les Eximus ;
  - stacks Magnetic à 10/s : jusqu'à ×4,25 sur **tous** les dégâts infligés à l'Overguard, tourelles comprises ;
  - aucun stack de kill sur la secondaire ;
  - Corrosive appliquée par le faisceau (10 stacks en ≈ 2 s sur la cible, chaînage sur 5 ennemis).
- **Pertes :**
  - la Corrosive en zone de 14,4 m de l'Epitaph disparaît : sur une cible blindée non amorcée par la Torid, les tourelles passent de ×0,715 à ×0,364, **soit −49 %** ;
  - plus d'Impact ni de Cold forcés ;
  - le Nukor ne touche que 3 cibles ;
  - il faut une Kuva Lich ;
  - la Radiation innée est résistée par les Corrupted et les Anarchs.
- **Supérieure :** Eximus en masse (Bolstered Belligerents : Overguard sur tous les ennemis ; Eximus Reinforcements), Corpus, longs combats contre des cibles isolées.
- **Inférieure :** couloirs denses de Grineer ou de Corrupted blindés, où l'Epitaph amorce toute la ligne.
- **Preuves :** Secondary Fortifier, Magnetic Damage, Kuva Nukor, §7.4.
- **Incertitudes :** test T9 ; le guide lui‑même ne chiffre pas la liste de mods du Nukor.

**V3 — Robustesse maximale au cap (fenêtres courtes).**
- **Modifications :** ancre mobile du guide (Grenade Fan / Blaze / **Roar** / Temporal Anchor ; Equilibrium → Temporal Artillery ; 69/74), avec 2 Crimson **Duration**, Martyr Symbiosis, Fortifier.
- **Règles :** pas de Protective Sling sous l'ancre ; orbes ramassées juste après chaque rembobinage ; relance immédiate de l'ancre après un death gate (25 d'énergie, Sculptor actif).
- **Gains :**
  - un death gate par fenêtre de 22,7 s, soit potentiellement des dizaines de sauvetages contre 3 pour Escapist ;
  - 3 s d'invulnérabilité par ancre ;
  - purge toutes les 22,7 s ;
  - implosion à 67 % sur chaque ennemi de la zone ;
  - tourelle suiveuse à 360° (×1,17 de dégâts de tourelle si k = 1).
- **Pertes :**
  - Dispensary et Equilibrium ;
  - −25 par ancre, soit environ 3,8 min d'autonomie sans revenu ;
  - retour forcé à l'ancre ;
  - −23 % de dégâts de tourelle en couloir dense (k = 5) ;
  - 1 Forma et un augment de plus.
- **Supérieure :** pics de niveau courts (quelques minutes), missions avec Energy Restores ou flux régulier d'Eximus.
- **Inférieure :** montée de 8 h sans revenu d'énergie.
- **Preuves :** Temporal Anchor, Temporal Artillery, Operator/Gameplay, §7.6–7.7.
- **Incertitudes :** tests 1 à 3 du guide (T13 à T15), valeur réelle de l'implosion.

---

## 11. Tests en jeu encore nécessaires

Conditions atteignables :
- **Simulacrum** : niveau maximal 5 × MR + 30 (+25 sur certaines cartes) ; option Steel Path ; « Pause AI » désactivé ; invincibilité désactivée.
- Pour les tests qui exigent des coups létaux : une mission sans fin du Steel Path au‑delà du niveau 300.

Enregistrer en vidéo et compter les images (60 i/s).

| # | Question | Protocole | Critère |
|---|---|---|---|
| T1 | Doublement du gate par satellite | Shields pleins, satellite accroché, laisser un ennemi lourd vider les shields ; chronométrer la barre grise, avec et sans satellite | ≈ 5 s → lecture A ; ≈ 2,5 s → lecture B |
| T2 | Les overshields comptent‑ils dans le gate ? | Retirer les Azure (555 shields max) ; vider les shields, accrocher un satellite à 0 shield (≥ 1 215 restaurés, dont ≥ 660 en overshields) ; chronométrer le gate suivant | 2,5 s → les overshields comptent (Azure remplaçables) ; 1,68 s → ils ne comptent pas |
| T3 | Consommation par paires | Lancer à 5 m, entrer dans un satellite, subir un tir unique ; compter les satellites restants | 2 perdus pour 1 gate → C2 confirmé |
| T4 | Chronologie de Grenade Fan | Images entre l'appui et l'animation, l'atterrissage, puis le satellite visible ; avec et sans Amber Casting Speed | Durées réelles ; effet ou non de Casting Speed |
| T5 | Statuts et Toxin pendant un gate | Infested de niveau ≈ 60–100, où le Toxin n'est pas encore létal (un tick d'aura Septic vaut alors moins de 968). Réduire les shields si besoin pour qu'un coup déclenche le gate, puis rester dans un nuage Toxin ; observer l'icône de statut et les ticks après le gate | Icône pendant le gate → C5 confirmé |
| T6 | Overguard gagné pendant un shield gate | Gate actif, tirer au Fortifier sur un Eximus | Le gate se coupe ou non |
| T7 | Passif sur Roar (Helminth) | Roar en 4e cast contre hors 4e cast, Growing Power actif | Buff ≈ 110 % contre ≈ 80 % |
| T8 | Le proc Heat hérite‑t‑il du multiplicateur de tourelle ? | Cible faiblement blindée, une seule tourelle ; comparer les ticks à la somme des tirs | Ticks ≈ 0,5 × Σ tirs × 2 → hypothèse de l'annexe B confirmée |
| T9 | Cadence réelle de l'Epitaph et enchaînement d'Overguard | Compter les tirs par seconde ; sous le feu, sur un Eximus, mesurer la durée de survie sans shields | ≥ 2 tirs/s : chaîne possible avec l'Epitaph |
| T10 | Seuil de Mercy à très haut niveau | Unité lourde au‑delà du niveau 300, 0 puis 10 procs Impact ; lire le crochet jaune | Le crochet bouge ou reste à 10 % |
| T11 | Panzer en larve | CD du Glaive avec le Panzer adulte puis en larve ; la larve vole‑t‑elle les satellites ? | Tenacious actif ou non ; vol ou non |
| T12 | Multiplicateur Heavy du Glaive | Combo ×1 : dégâts affichés de la détonation contre 1 184 × mods | Rapport ≈ 2 → ×2 à intégrer |
| T13 | Ordre entre le death gate de l'ancre et Escapist | Ancre active, Escapist chargé, coup fatal | Qui se déclenche, stacks consommés ou non |
| T14 | Remboursement à l'ancre et orbes effacées | Test 1 du guide | — |
| T15 | Ré‑attache de la tourelle suiveuse | Test 2 du guide | — |
| T16 | Untreatable en Icebind | Ramasser une orbe renforcée sous Untreatable | +110 énergie → note U36.0 confirmée sur l'Icebind |

---

## 12. Sources directes et version

Wiki consulté le **26/10/2026**, patch **U44.1.3** (22/10/2026). Les notes de patch officielles citées sont celles que reproduit le wiki.

- **Survie :** [Shield § Shield Gating](https://wiki.warframe.com/w/Shield#Shield_Gating) (formule, overshields à 1 200, recharge 4 s, notes U34) · [Invulnerability](https://wiki.warframe.com/w/Invulnerability) · [Rolling Guard](https://wiki.warframe.com/w/Rolling_Guard) · [Primed Sure Footed](https://wiki.warframe.com/w/Primed_Sure_Footed) · [Overguard](https://wiki.warframe.com/w/Overguard) · [Secondary Fortifier](https://wiki.warframe.com/w/Secondary_Fortifier) · [Arcane Escapist](https://wiki.warframe.com/w/Arcane_Escapist) · [Parazon / Mercy](https://wiki.warframe.com/w/Parazon) · [Impact Damage](https://wiki.warframe.com/w/Damage/Impact_Damage) · [Focus/Vazarin](https://wiki.warframe.com/w/Focus/Vazarin) · [Operator/Gameplay](https://wiki.warframe.com/w/Operator/Gameplay) · [Martyr Symbiosis](https://wiki.warframe.com/w/Martyr_Symbiosis)
- **Compétences :** [Grenade Fan](https://wiki.warframe.com/w/Grenade_Fan) · [Blaze Artillery](https://wiki.warframe.com/w/Blaze_Artillery) · [Dispensary](https://wiki.warframe.com/w/Dispensary) · [Temporal Anchor](https://wiki.warframe.com/w/Temporal_Anchor) · [Temporal Artillery](https://wiki.warframe.com/w/Temporal_Artillery) · [Roar](https://wiki.warframe.com/w/Roar) · [Passif de Protea](https://wiki.warframe.com/w/Protea/Abilities/Passive) · [Protea Prime](https://wiki.warframe.com/w/Protea/Prime) · [Protea](https://wiki.warframe.com/w/Protea) · [Abilities § Casting Speed](https://wiki.warframe.com/w/Abilities#Casting_Speed) · [Natural Talent](https://wiki.warframe.com/w/Natural_Talent)
- **Mods, arcanes, shards :** [Archon Vitality](https://wiki.warframe.com/w/Archon_Vitality) · [Archon Stretch](https://wiki.warframe.com/w/Archon_Stretch) · [Equilibrium](https://wiki.warframe.com/w/Equilibrium) · [Growing Power](https://wiki.warframe.com/w/Growing_Power) · [Arcane Sculptor](https://wiki.warframe.com/w/Arcane_Sculptor) · [Molt Augmented](https://wiki.warframe.com/w/Molt_Augmented) · [Arcane Energize](https://wiki.warframe.com/w/Arcane_Energize) · [Archon Shard](https://wiki.warframe.com/w/Archon_Shard) · [Transient Fortitude](https://wiki.warframe.com/w/Transient_Fortitude) · pages individuelles de chaque mod (coût de base, rang, polarité)
- **Dégâts :** [Heat Damage](https://wiki.warframe.com/w/Damage/Heat_Damage) (Heat Inherit, retrait d'armure) · [Toxin Damage](https://wiki.warframe.com/w/Damage/Toxin_Damage) · [Magnetic Damage](https://wiki.warframe.com/w/Damage/Magnetic_Damage) · [Overview Table](https://wiki.warframe.com/w/Damage/Overview_Table) · [Armor](https://wiki.warframe.com/w/Armor) · [Enemy Level Scaling](https://wiki.warframe.com/w/Enemy_Level_Scaling) · [The Steel Path](https://wiki.warframe.com/w/The_Steel_Path)
- **Armes :** [Torid](https://wiki.warframe.com/w/Torid) · [Torid Incarnon Genesis](https://wiki.warframe.com/w/Torid_Incarnon_Genesis) · [Epitaph Prime](https://wiki.warframe.com/w/Epitaph_Prime) · [Glaive Prime](https://wiki.warframe.com/w/Glaive_Prime) · [Melee § Heavy Attack](https://wiki.warframe.com/w/Melee#Heavy_Attack) · [Melee Duplicate](https://wiki.warframe.com/w/Melee_Duplicate) · [Primary Merciless](https://wiki.warframe.com/w/Primary_Merciless) · [Kuva Nukor](https://wiki.warframe.com/w/Kuva_Nukor) · [Phantasma Prime](https://wiki.warframe.com/w/Phantasma_Prime)
- **Compagnons :** [Panzer Vulpaphyla](https://wiki.warframe.com/w/Panzer_Vulpaphyla) · [Viral Quills](https://wiki.warframe.com/w/Viral_Quills) · [Panzer Devolution](https://wiki.warframe.com/w/Panzer_Devolution) · [Sepsis Claws](https://wiki.warframe.com/w/Sepsis_Claws) · [Tenacious Bond](https://wiki.warframe.com/w/Tenacious_Bond) · [Tandem Bond](https://wiki.warframe.com/w/Tandem_Bond) · [Vicious Bond](https://wiki.warframe.com/w/Vicious_Bond) · [Restorative Bond](https://wiki.warframe.com/w/Restorative_Bond) · [Vulpaphyla](https://wiki.warframe.com/w/Vulpaphyla) · [Nautilus Prime](https://wiki.warframe.com/w/Nautilus/Prime) · [Cordon](https://wiki.warframe.com/w/Cordon)
- **Ennemis :** [Eximus](https://wiki.warframe.com/w/Eximus) · [Heavy Gunner](https://wiki.warframe.com/w/Heavy_Gunner) · [Toxic Ancient](https://wiki.warframe.com/w/Toxic_Ancient) · [Ancient Disruptor](https://wiki.warframe.com/w/Ancient_Disruptor) · [Nullifier Crewman](https://wiki.warframe.com/w/Nullifier_Crewman)
- **Modes et patchs :** [The Icebind](https://wiki.warframe.com/w/The_Icebind) · [Update 44](https://wiki.warframe.com/w/Update_44) (44.1 et 44.1.3) · [Deep Archimedea](https://wiki.warframe.com/w/Deep_Archimedea) (notes U36.0 sur Untreatable) · [Temporal Archimedea](https://wiki.warframe.com/w/Temporal_Archimedea) · [Simulacrum](https://wiki.warframe.com/w/Simulacrum)

---

## Annexe A — Contre‑expertise de l'audit v1 (12 corrections intégrées en v1.1)

| # | Problème initial | État en v1.3 | Nouvelle erreur induite | Verdict |
|---|---|---|---|---|
| 1 | Gate de 5 s présenté comme acquis | Timing fondé sur 2,5 s, doublement marqué non confirmé (VÉRIFIÉ) | Les « stations à 4–6 m » se consomment par paires (C2) ; protocole de test au 9999 irréalisable ; question des overshields ignorée | **Partiellement résolu** |
| 2 | « Le Slash traverse les shields » | Corrigé, citation du wiki VÉRIFIÉE | « Toxin = seule menace qui traverse les shields » (drains Leech) | **Résolu** (nuance mineure) |
| 3 | Aucun anti‑mort | Escapist ajouté (mécanique VÉRIFIÉE) | Impact au cap CONTESTÉ ; Overguard bloque le Mercy ; 3 vies non renouvelables | **Partiellement résolu** |
| 4 | Urgence « satellites à tes pieds » | RG d'abord | Séquence RG, Grenade Fan, atterrissage, marche en moins de 3 s jamais mesurée ; « à tes pieds » brûle encore tout | **Partiellement résolu** |
| 5 | Viral par défaut contre Grineer | Corrosive (57/60) et Magnetic (60/60) ajoutés (CALCULÉ ✔) | — | **Résolu** |
| 6 | « Combo ×6 garanti » | Plancher ×2 annoncé | Tandem Bond « indispensable » dépend de la forme adulte du Panzer (intermittente au cap) | **Partiellement résolu** |
| 7 | Infested « meilleure faction » | « Pire en survie » | Menace de référence périmée (aura du Toxic Ancient retirée en U38.0) ; la vraie menace (fléau de 7 m) est absente | **Partiellement résolu** |
| 8 | Passif sur l'Helminth affirmé | Marqué « à vérifier » | — (toujours NON VÉRIFIÉ, aucune seconde source) | **Résolu** |
| 9 | Pénalités de mission absentes | Table ajoutée | Mode Icebind à 6 joueurs dans un guide solo ; Untreatable faux ; Archimedea « 999+ » ; modificateurs anti‑spam absents | **Ouvert, avec erreurs nouvelles** |
| 10 | Ouverture Sculptor | Attendre l'atterrissage | Énergie de départ (75) insuffisante pour Roar en 5e cast | **Partiellement résolu** |
| 11 | Option A équivalente au cap | Panzer imposé au 9999 | Valeur du Panzer au cap surévaluée (larve, spores, Restorative Bond) | **Partiellement résolu** |
| 12 | Amber Casting jugée inutile | Variante Amber ajoutée | Effet sur Grenade Fan NON VÉRIFIÉ ; coût surestimé (−10 % contre −5 %) | **Partiellement résolu** |

**Erreurs propres à l'audit v1 :**
- son tableau 2.1 donne Untreatable comme fatal au moteur d'énergie (« −26,8/s ») : **RÉFUTÉ** par les notes U36.0 ;
- son protocole « Simulacrum, ennemi niveau 9999 » est irréalisable ;
- il ne voit pas que The Icebind est réservé aux escouades de 6 joueurs ;
- sa note de robustesse de 6/10 après corrections ne tient pas compte de C2 à C5.

---

## Annexe B — Hypothèses du modèle de calcul

- **Tourelle :**
  - tir n = 500 × Str × (1 + k × n) ;
  - 3 tirs/s ;
  - durée de vie = 3 s × Duration ;
  - 3 emplacements relancés à l'expiration (boucle 1.12 du guide) ;
  - Roar : ×(1 + R) sur le direct, ×(1 + R)² sur les ticks.
- **Heat :**
  - tick = 0,5 × Σ des dégâts des stacks actifs, 1 s après le premier proc, puis toutes les secondes ;
  - tous les stacks sont rafraîchis par chaque proc (Heat Inherit) ;
  - Archon Vitality = 2 stacks par proc.
- **Hypothèse non vérifiée (T8) :** le proc Heat hérite du multiplicateur cumulatif du tir. Les comparaisons Strength / Duration (7.3) **ne dépendent pas** de cette hypothèse ; les temps de mise à mort (7.4) en dépendent.
- **Ennemis :**
  - [Heavy Gunner](https://wiki.warframe.com/w/Heavy_Gunner) : 300 PV et 500 d'armure de base, niveau de base 8 (VÉRIFIÉ), ×2,5 sur la santé en Steel Path ;
  - armure plafonnée à 2 700 (90 % de réduction), réduction = 0,9 × √(armure / 2 700) ;
  - formules de scaling de la page Enemy Level Scaling (ensemble de courbes du haut).
- **Satellites :** les quatre grenades atterrissent à la même distance le long de leur angle ; rebonds et flottement ignorés.
- **Couverture sous feu continu :** chaque coup est létal et la cadence de tir ennemie est assez élevée pour qu'un shield restauré soit vidé aussitôt.

---

## Notes finales (estimations qualitatives, pas des mesures)

| Axe | Guide v1.3 tel quel | Après corrections V1 |
|---|---|---|
| Performance (dégâts) | **7/10** : tourelles létales même au cap (Heat Inherit) ; armes à stacks inertes au cap | **7,5/10** |
| Robustesse (montée solo au 9999) | **4/10** : paires de satellites, Toxin, pile surévaluée, ressources finies | **5,5/10** (≈ 6,5 en V3 sur fenêtres courtes, après tests) |
| Difficulté d'exécution (10 = la plus élevée) | **9/10** : timings sub‑secondes non mesurés, ≥ 1 Grenade Fan toutes les 5 s sous feu, prévention constante | **8,5/10** |
| Confiance dans les résultats | **5/10** : chiffres justes, cadre et modèle de risque faux, 16 points non testés | **6/10**, à réévaluer après T1–T5 |
