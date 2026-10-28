# Analyse comparative 2026 — Protea Prime, deux configs (Steel Path / Level cap)

> 28/10/2026 · Document de travail qui a servi à la [v2.0 du guide](protea-prime-level-cap-endurance.md). Base : guide v1.4, 28 builds de la communauté, wiki officiel (consulté les 26–28/10/2026). **Rien n'a été testé en jeu.** Les scénarios d'énergie reposent sur des hypothèses de rythme de kills, signalées comme telles.

## 1. Méthode et limites

- **Corpus** : les 25 builds Protea Prime les plus votés d'Overframe, plus les builds récents trouvés à part (HEKPYTO, farhax, ret.soccer, Lucid_Wolf) et trois guides (warframegodbuilds, warframe.today « vérifié U44 », guide Steam). Total : 28 builds, dont 12 datés de 2026.
- **Limites** :
  - Overframe encode la plupart des listes de mods : je n'ai que ce qui est écrit dans les descriptions.
  - Les dates d'Overframe sont relatives (« il y a 4 mois »).
  - Les vidéos YouTube sont inaccessibles depuis cet environnement (erreur 429 et captcha).
  - Aucun fil Reddit utile n'est remonté.
- **Modèle chiffré** (scripts de calcul de la session, non versionnés) :
  - Valeurs du wiki ; Heat Inherit et Archon Vitality comme dans l'audit v2.
  - Cible de référence : Heavy Gunner du Steel Path au niveau 9999, 6,1 M PV.
  - Énergie : coûts sous Arcane Sculptor (×0,25), orbes du wiki.
  - **Hypothèses** : Steel Path courant = 50 kills/min et 3 Eximus/min ; level cap = 10 kills/min et 1,5 Eximus/min ; 85 % des orbes ramassées.

## 2. Ce que fait la communauté

| Choix | Corpus (28) | 2026 (12) |
|---|---|---|
| Garde Temporal Anchor | **18** | **8** |
| Kit natif (Dispensary + ancre) | 13 | 6 |
| Roar à la place de l'ancre (notre v1.4) | 6 | 3 |
| Roar à la place de Dispensary | 1 explicite + la note 2026 du build le plus voté | 1 |
| Autre sort à la place de Dispensary (Nourish, Brightbonnet) | 4 | 1 |
| Temporal Artillery / Temporal Erosion | 12 / 7 | 6 / 4 |
| Arcane Sculptor | 5 (tous en 2026) | 5 |
| Molt Augmented / Molt Efficiency / Energize | 9 / 5 / 3 | 6 / 2 / 2 |
| Shards Crimson Duration / Amber Casting / Crimson Strength | 22 / 20 / 6 | 7 / 7 / 3 |
| Shards Azure | 2 (jamais 3) | 1 |
| Mods les plus cités | Equilibrium 13, Archon Vitality 11, Blind Rage 9, Primed Continuity 7, Umbral Intensify 7, Stretch 6, Rolling Guard 4 | — |
| Compagnon cité | Nautilus 5 fois sur 8 | — |

Ce qu'il faut retenir :
- La communauté garde l'ancre presque toujours, le plus souvent **avec** Dispensary.
- Elle ne prend jamais 3 Azure.
- Elle préfère la Duration à la Strength.
- Personne n'utilise Arcane Escapist, le Panzer ou Secondary Fortifier.

## 3. Le choix de fond : quelle compétence sacrifier ?

Grenade Fan (satellites) et Blaze Artillery sont intouchables. Il faut donc renoncer à **une** des trois autres : Dispensary, Temporal Anchor ou Roar.

| Kit | Ce qu'on garde | Dégâts au 9999 (10 s, 3 tourelles, cible blindée)¹ | TTK Heavy Gunner (une voie) | Survie | Énergie |
|---|---|---|---|---|---|
| **A** — v1.4 (Roar à la place de l'ancre) | Dispensary + Roar | ×1,00 avec Corrosive · ×0,51 sans | 10 s · 14 s | Pas de protection contre la mort renouvelable (Escapist ×3) | Excédent énorme (≈ +35 à +48/s) |
| **B** — Roar à la place de Dispensary | Ancre + Roar | **×1,53** (Temporal Erosion) | **8,3 s** | **Protection contre la mort à chaque ancre**, 3 s d'invulnérabilité par lancer, purge des statuts | Dépend des kills (voir §4) |
| **C** — natif | Dispensary + ancre | ×0,40 à ×0,54 (Erosion) · ×0,33 sans | 15 s · 18 s | Identique à B | Excédent énorme |

¹ Base 1,00 = socle v1.4 avec Epitaph Corrosive.

Ce qu'apporte chaque élément :
- **Roar** vaut à lui seul ×2 à ×3, parce qu'il s'applique deux fois sur la Heat.
- **Temporal Erosion** retire 10 % d'armure par coup, multiplié par la Strength, tant que l'ancre est active (wiki). L'armure tombe à zéro en 3 ou 4 tirs. Le gain est de ×10 contre ×7,15 avec Heat + Corrosive, soit +40 %, et l'Epitaph n'a plus besoin de servir au Corrosive.

**Verdict : kit B pour les deux configs.** C'est le seul qui cumule le maximum de dégâts et le maximum de survie. Son point faible, l'énergie, se gère (§4). Le kit C reste le **repli sans gestion d'énergie** : il prend deux fois moins de dégâts que la v1.4, mais ne demande aucun Helminth.

## 4. L'énergie du kit B : la règle de l'ancre

Le rembobinage **rend toute l'énergie dépensée pendant l'ancre**, sauf les 25 de l'ancre elle‑même (wiki et Blazing Lotus). Les tourelles posées pendant l'ancre restent en place.

En contrepartie, il **efface** l'énergie ramassée pendant l'ancre. Maintenir 4 annule l'ancre sans rembobinage : on garde alors ce qu'on a ramassé, mais on paie tout ce qu'on a lancé.

**La règle :**
- par défaut, laisse l'ancre rembobiner : tout lancer devient gratuit, pour seulement −25 par ancre ;
- **si un Eximus est mort pendant l'ancre**, annule-la (maintiens 4) pour garder ses orbes, puis relance.

Énergie nette par seconde avec cette règle (feu dense, 3 tourelles fixes, Sculptor) :

| Config | 3 Eximus/min | 1,5 | 0,75 | 0,4 |
|---|---|---|---|---|
| Level cap : Equilibrium + **Energize** (Duration 199 %) | +8,3 | **+1,6** | −0,2 | −0,9 |
| Level cap : Energize seul (Primed Continuity gardé) | +1,7 | −0,6 | −1,1 | −1,2 |
| Level cap : Equilibrium seul | +4,5 | −0,3 | −1,2 | −1,4 |
| Steel Path : Equilibrium + Molt (sans Energize) | +5,7 | +0,1 | — | — |

- Un Eximus vaut, selon le wiki, **une grande orbe d'énergie (50) + 2 orbes de vie de 50 PV**. Avec Equilibrium et Energize, cela fait ≈ 250 d'énergie, soit 10 ancres.
- Au level cap, il faut donc **Equilibrium et Energize ensemble**. Avec les deux, le kit B tient à partir d'environ 0,8 Eximus tué par minute ; sans Energize (Molt à la place), il en faut ≈ 2.
- En dessous, la réserve de 250 baisse lentement : −0,9/s à 0,4 Eximus par minute (≈ 4,5 minutes), −1,6/s sans aucun Eximus (≈ 2,7 minutes). Elle remonte au prochain Eximus.

## 5. Les choix, un par un

| Élément | Steel Path | Level cap | Pourquoi |
|---|---|---|---|
| Augment de l'ancre (slot Zenurik commun) | **Temporal Artillery** | **Temporal Erosion** | Artillery : tourelle qui suit à 360°, combo 20×, minuteur figé. Erosion : armure à zéro en 4 tirs (3 sur le 4e lancer), +40 % de dégâts contre l'armure, et l'Epitaph est libéré du Corrosive. |
| Arcane n°1 | **Arcane Sculptor** | **Arcane Sculptor** | Indispensable : tout coûte 25 %. 5 builds de 2026 sur 12 l'utilisent. |
| Arcane n°2 | **Molt Augmented** | **Arcane Energize** | Steel Path : l'énergie suit, Molt pousse Roar à +112 %. Level cap : l'énergie est la contrainte. Escapist devient redondant avec la protection renouvelable de l'ancre. |
| Shards (communs aux deux configs) | **3 Crimson Strength + 2 Amber Casting Speed** (Tauforged) | idem | Avec Roar, +1 Crimson Strength = ×1,10 sur la Heat, contre ×1,06 pour Duration. Casting Speed réduit le temps d'exposition pendant les lancers. Azure abandonné : 0 build sur 28 en prend 3, et 5 sources rapportent un gate doublé (5 s) avec un satellite accroché, dont 2 précisent « à 1 100 d'overshield ». **À confirmer par le test T2** ; sinon, retour à 3 Azure + 2 Crimson Strength. |
| Mods communs | Growing Power, Primed Sure Footed, Archon Vitality, Blind Rage, Umbral Intensify, Narrow Minded, Stretch, **Equilibrium** | idem | Equilibrium reste le moteur d'énergie grâce aux orbes d'Eximus et à Synth Deconstruct. |
| Mods propres à la config | **Primed Continuity** + Temporal Artillery | **Rolling Guard** + Temporal Erosion | En Steel Path, l'ancre (invulnérabilité et protection contre la mort) remplace Rolling Guard. Au cap, Rolling Guard est indispensable (Toxin, Magnetic) et prend la place de Primed Continuity, ce qui coûte 21 % de dégâts soutenus aux tourelles. |
| Capacité / Forma | 64/74 | 72/74 | Mêmes polarités que la v1.4 + **1 Forma Zenurik** sur le slot 8 (6 Forma). Au cap, Rolling Guard dans le slot Madurai coûte 15. |
| Compagnon | **Nautilus Prime** (Cordon, Synth Deconstruct, Sacrifice) | **Panzer Vulpaphyla** + Martyr Symbiosis | La communauté prend Nautilus, mais une sentinelle tombe en un coup au 9999. Le Panzer reste présent (larve), propage le Viral et fournit des orbes de vie via Synth Deconstruct. |
| Armes | Torid Viral · Epitaph **Corrosive** + Encumber · Glaive Viral | Torid **Magnetic** · Epitaph **Magnetic** + Fortifier · Glaive Viral | Au cap, Erosion règle l'armure : l'Epitaph passe en Magnetic contre l'Overguard des Eximus (×8 avec Fortifier). |
| École de Focus | **Zenurik** | **Zenurik** | Avec l'ancre active, la Warframe est vulnérable quand l'Operator sort (wiki) : Protective Sling (Vazarin) devient inutilisable. Les passifs de Zenurik (Energy Pulse +50 % sur les orbes d'énergie, Inner Might) marchent sans sortir l'Operator. |

## 6. Les deux configs

| | ① Steel Path | ② Level cap |
|---|---|---|
| Kit | Grenade Fan / Blaze Artillery / **Roar** / Temporal Anchor | identique |
| Strength (Arsenal → mission → 4e lancer) | 288 → 313 (373 avec Molt plein) → 473 % | 288 → 313 → 413 % |
| Duration / Range / Efficiency | 254 % / 79 % / 175 % sous Sculptor | 199 % / 79 % / 175 % |
| Roar | +112 % (+142 % sur le 4e lancer), 76 s | +94 % (+124 %), 60 s |
| Ancre / tourelle | 20,3 s / 7,62 s, 23,7 m | 15,9 s / 5,97 s |
| Satellite | 1 865 shields | 1 565 shields |
| Dégâts au 9999 (×v1.4) | ×1,54 | ×1,52 |
| Énergie | Rembobinage par défaut ; orbes abondantes | Règle de l'ancre + Equilibrium + Energize |

**Ouverture :** la séquence Grenade Fan → tourelle → ancre → Roar coûte 95 et Protea Prime démarre à 75 (56,25 si Inner Might rend Grenade Fan gratuit). Ouvre sur Grenade Fan, attends l'atterrissage, puis ramasse une orbe (ou utilise un Energy Restore) avant l'ancre.

## 7. Erreurs de la v1.4 trouvées en route

- **Orbe de vie normale = 50 PV** (wiki), soit 55 d'énergie avec Equilibrium : la v1.4 disait 27. Synth Deconstruct vaut donc deux fois plus.
- **Un Eximus lâche une grande orbe d'énergie (50)** et 2 orbes de vie, soit ≈ 160 avec Equilibrium. La v1.4 disait +79, en s'appuyant sur une correction de l'audit v2 qui était elle‑même erronée.
- **Protea Prime est vaultée** (wiki) : pour l'obtenir, il faut un retour par Prime Resurgence.
- **Arcane Concentration** (U41) existe : +60 % de Duration pendant 3 s après un lancer. Je l'ai écarté : il n'apporte rien au temps de mise à mort dans le modèle, et l'énergie se règle mieux avec Energize.

## 8. Tests prioritaires

1. **T2, les overshields dans le gate.** Il décide des shards Azure. Teste à 555 shields max avec un satellite accroché, puis chronomètre la barre grise.
2. **La règle de l'ancre en jeu** : remboursement au rembobinage, tourelles conservées, annulation en maintenant 4 qui garde les orbes.
3. **Le rythme d'Eximus tués au cap.** Sous ≈ 0,8 par minute de façon durable, passe au kit C.
4. **Temporal Erosion** : armure à zéro en 4 tirs à 313 %, en 3 tirs si l'ancre est lancée sur le 4e lancer.
5. T13 (ordre entre Martyr Symbiosis et la protection de l'ancre) et T11 (Panzer en larve) restent ouverts.

## 9. Corpus détaillé

| Build | Source | Votes | Date | Kit | Augments | Arcanes | Shards |
|---|---|---|---|---|---|---|---|
| The Blazing Lotus (ninjase) | Overframe | 1143 | 2026-06 | natif (note 2026 : Roar sur Dispensary) | Temporal Erosion | Arcane Sculptor, Arcane Steadfast, Molt Augmented, Molt Efficiency | 1-2 Amber Cast + 3-4 Crimson Dur |
| Siege Tank Protea (ninjase) | Overframe | 398 | 2026-06 | Roar sur Dispensary | Temporal Artillery | Arcane Sculptor, Arcane Steadfast, Molt Augmented, Molt Efficiency | - |
| Tempest Tyrant | Overframe | 87 | 2024 | Tempest Barrage sur l'ancre | — | — | 2 Emerald + 2 Crimson Dur + 1 Amber Cast |
| Armor Strip SPAM (Unbusted-NUT) | Overframe | 80 | 2025-12 | natif | Temporal Artillery, Temporal Erosion | — | 3 Amber (Cast x2, Parkour) + 1 Amber orbs + 1 Crimson Str |
| Invincible Void Destroyer | Overframe | 35 | 2025 | ? | — | — | 3 Crimson Dur + 2 Amber (orbs, energy) |
| Rainollon (Erosion/Artillery) | Overframe | 27 | 2026-09 | natif | Temporal Artillery, Temporal Erosion | — | 2 Amber Cast + 3 Crimson Dur |
| Artillery God (pollzey) | Overframe | 20 | 2025 | natif | — | Molt Efficiency | 2 Amber Cast + 3 Crimson Dur |
| Roar — Defense (T_Rodrigo_24) | Overframe | 10 | 2025 | Roar (probablement sur l'ancre) | — | — | 1 Amber Cast + 4 Crimson Dur |
| Turret stuck on my head (CephalonBread) | Overframe | 8 | 2024 | natif | Temporal Artillery | — | 3 Crimson Dur + 1 Violet + 1 Amber Cast |
| Ultimate Protea Guide (flyingfussel9) | Overframe | 7 | 2024 | natif (Roar en option) | Temporal Artillery | Molt Augmented, Molt Efficiency | 3-4 Crimson Dur + 1-2 Amber Cast |
| Temporal Hot Shot (Wuffadin) | Overframe | 7 | 2025 | natif | — | Arcane Hot Shot | 1 Amber Cast + 4 Crimson Dur |
| Nuker Protea (hodrigocastelo) | Overframe | 6 | 2024 | Ensnare | — | — | 1 Violet + Amber Cast + Crimson Dur |
| PANDAxMANIAC SP | Overframe | 6 | 2025 | Nourish sur Dispensary | Temporal Artillery, Temporal Erosion | — | 2 Amber Cast + 3 Crimson Dur |
| PRO TEA run-n-gun (randomkollega) | Overframe | 6 | 2026-09 | natif ou Brightbonnet | Temporal Artillery, Temporal Erosion | — | 2 Amber Cast + 3 Crimson Dur |
| Highly Mobile Protea (flyingfussel9) | Overframe | 5 | 2024 | Nourish sur Dispensary | Temporal Artillery | — | 2 Amber Cast + 2-3 Crimson Dur |
| Wife Kill (Cyanosys) | Overframe | 4 | 2024 | natif | — | — | 2 Amber Cast + 3 Crimson Dur |
| Nourishing Artillery (takenghoul) | Overframe | 3 | 2024 | Nourish ? | — | — | 2 Amber Cast + 1 Azure + 1 Crimson Dur + 1 Crimson Str |
| Very comfortable (Arianmas) | Overframe | 3 | 2026-03 | Roar (probablement sur l'ancre) | — | — | - |
| Fire Torrets - Roar (Mwven) | Overframe | 3 | 2026-06 | Roar sur l'ancre | — | Arcane Concentration, Arcane Sculptor | 1 Amber Cast + 3 Crimson Dur |
| Void Cascade Roar (yorsume) | Overframe | 2 | 2024 | Roar (probablement sur l'ancre) | — | Arcane Steadfast, Molt Augmented | Amber Cast + Crimson Dur |
| Comfy Temporal Artillery SP+LC (farhax) | Overframe | 1 | 2026-06 | natif | Temporal Artillery | Arcane Sculptor | 4 Crimson Dur + 1 Amber Cast |
| Best Protea Prime (joel01) | Overframe | 0 | 2025 | ancre remplacée (Roar, Larva, Tempest…) | — | Arcane Energize | 1 Violet + 2 Crimson Dur + 2 Crimson Str |
| Simple Protea Guide (Steam) | Steam | — | 2025-04 | natif | Temporal Artillery, Temporal Erosion | Molt Augmented, Molt Efficiency | Crimson Dur + Amber Cast + Amber Preparation |
| Turret Runner (Lucid_Wolf) | Overframe | 0 | 2026-05 | Brightbonnet sur Dispensary | Temporal Artillery | Arcane Concentration, Molt Augmented | 1 Amber + 4 Crimson Dur |
| Doom & Gloom | Overframe | 0 | 2026-05 | Gloom | — | — | 2 Violet + 1 Emerald + 2 Crimson (dmg) |
| Temporal Erosion Artillery LC (HEKPYTO) | Overframe | 0 | 2026-06 | natif | Temporal Erosion | Arcane Energize, Molt Augmented | 2 Amber Cast + 1 Amber orbs + 2 Crimson Str |
| Siege Cannons Endgame | warframegodbuilds | — | 2026-09 | natif | Temporal Artillery | Arcane Sculptor, Molt Augmented | 3 Crimson Str + 1 Crimson Dur |
| warframe.today (U44) | warframe.today | — | 2026-10 | Roar sur l'ancre | — | Arcane Energize, Molt Augmented | 2 Crimson Str + 1 Amber Cast + 1 Azure + 1 Violet |

## Sources

Overframe :
- [The Blazing Lotus](https://overframe.gg/build/668062/protea-prime/the-blazing-lotus-general-use-temporal-anchor-protea-non-helminth-and-variants/)
- [Siege Tank](https://overframe.gg/build/668069/protea-prime/siege-tank-protea-semi-afk-blaze-artillery-dps-non-helminth-and-variants/)
- [HEKPYTO](https://overframe.gg/build/1011403/protea-prime/protea-prime-temporal-erosion-artillery-steel-path-level-cap/)
- [farhax](https://overframe.gg/build/1025309/protea-prime/comfy-temporal-artillery-protea-for-sp-and-level-cap/)
- [Fire Torrets](https://overframe.gg/build/856633/protea-prime/fire-torrets-roar-243-str-288-drt-100-roar-arcane-sculpture-arcane-concentration/)
- [Turret Runner](https://overframe.gg/build/1005612/protea-prime/protea-turret-runner/)
- [Rainollon](https://overframe.gg/build/770232/protea-prime/rainollons-protea-prime-temporal-erosion-temporal-artillery-build/)
- [PRO TEA](https://overframe.gg/build/891684/protea-prime/pro-tea-temporal-anchor-protea-run-n-gun/)
- [Ultimate Guide](https://overframe.gg/build/756312/protea-prime/the-ultimate-protea-guide-to-rule-them-all/)
- [classement Protea Prime](https://overframe.gg/items/arsenal/6534/protea-prime/)

Guides :
- [warframegodbuilds](https://warframegodbuilds.com/frames/protea/builds/protea-blaze)
- [warframe.today](https://warframe.today/frames/protea/)
- [guide Steam](https://steamcommunity.com/sharedfiles/filedetails/?id=3464346134)

Wiki :
- [Temporal Erosion](https://wiki.warframe.com/w/Temporal_Erosion), [Roar](https://wiki.warframe.com/w/Roar)
- [Arcane Energize](https://wiki.warframe.com/w/Arcane_Energize), [Arcane Concentration](https://wiki.warframe.com/w/Arcane_Concentration), [Molt Efficiency](https://wiki.warframe.com/w/Molt_Efficiency)
- [Nourish](https://wiki.warframe.com/w/Nourish), [Brightbonnet](https://wiki.warframe.com/w/Brightbonnet), [Gloom](https://wiki.warframe.com/w/Gloom), [Pillage](https://wiki.warframe.com/w/Pillage)
- [Energy Orb](https://wiki.warframe.com/w/Energy_Orb), [Health Orb](https://wiki.warframe.com/w/Health_Orb), [Eximus](https://wiki.warframe.com/w/Eximus), [Equilibrium](https://wiki.warframe.com/w/Equilibrium)
- [Zenurik](https://wiki.warframe.com/w/Focus/Zenurik), [Archon Shard](https://wiki.warframe.com/w/Archon_Shard), [Helminth](https://wiki.warframe.com/w/Helminth), [Protea Prime](https://wiki.warframe.com/w/Protea/Prime)
