# Sevagoth Prime : theorycraft complet et auditable

**Version 5.0 du 30/10/2026.** Patch **Hotfix 44.1.4.1** (« Iceblade of Narin : The Icebind »), en ligne sur PSN depuis le 28/10/2026.
Build acté : **F1 « Faucheuse invisible »**, en deux fiches : **A** pour le Steel Path et l'endurance, **B** pour Void Cascade et le level cap. Modèle de calcul : [`sevagoth_model.py`](sevagoth_model.py) (sections M1 à M31). Sortie brute : [`model_output.txt`](model_output.txt). Paramètres et sources : [`model_params.txt`](model_params.txt).

Étiquettes : **CONF** = wiki officiel ou patch notes · **COMM** = communauté · **DÉD** = déduit par le modèle · **TEST** = à mesurer en jeu · **NON TROUVÉ** = aucune source.

---

## Changelog v4 → v5

**Source de la v5 :** (C) la page Overframe de RubyBlossom5 (« The Reaper's Bible », 22/10/2026), sous forme de résumé (COMM), et son calculateur « Sevagoth's Breakpoints » (PDF de 9 pages, lu en entier). Le verdict v4 et les deux fiches ne changent pas.

| # | Changement | Pourquoi | Étiquette |
|---|---|---|---|
| 1 | **Son calculateur donne les mêmes chiffres que le script :** nuke au centième près (253 % → 99,60 % ; 254 % → 99,99 % ; 258 % → 101,56 % ; 273 % → 107,55 %), même drain de Gloom (0,339/s par ennemi), même ralentissement, mêmes tables Viral | Contrôle | CONF + DÉD (M29) |
| 2 | **« Vs Orokin / Anarchs » appartient au bloc Smite**, pas à Roar : c'est la Radiation de Smite à ×0,5. L'égalité avec le True sans Roar est une coïncidence au-dessus de 142,9 %. Roar compte contre toutes les factions : F1 ne change pas | Question posée | CONF |
| 3 | **Point 1 :** détection des mini-ombres à 30 m confirmée. Nouveau : à 175 %, Gloom met 8,2 s à atteindre 28 m, contre 3,9 s pour 16 m à 100 % | Source C | CONF + DÉD |
| 4 | **Point 2 :** drain de Gloom vérifié dans le modèle (0,75/s par ennemi, 10 ennemis au plus). Ralentissement figé au lancer. Death Well à 10 % par kill marqué par Sow et Reap, donc la boucle de Ruby rend visible à chaque pack. Test de figeage gardé | Source C | CONF + COMM |
| 5 | **Point 3 :** ses tables Viral se lisent sans Roar. Le Viral ne prend pas sous Overguard, ce qui limite son conseil sur les Eximus. **Éclats Émeraude en config Tempest :** 1,183 → 1,440 avec 2 tauforgés → 1,652 avec 4. T23 complété | Source C | CONF + DÉD (M31) |
| 6 | **Sa build principale (sans Roar, Viral à l'arme) ne bat pas F1 sur S1 à S3.** Elle gagne si T4 échoue, si l'Helminth est réservé à autre chose, et peut-être contre les Entropiques (T21 e) | Question posée | DÉD (M30) |
| 7 | Mods de « Shadowless Nuke » non reçus (Overframe en 403) : comparaison ligne par ligne en attente | – | – |
| 8 | Script : sections M29 à M31 | – | – |

---

## Changelog v3 → v4

**Sources de la v4 :** (A) la vidéo de RubyBlossom5, auteure du build Overframe cité en v1 (mis à jour le 22/10/2026) ; (B) la vidéo d'un créateur qui a testé en Simulacrum les interactions entre l'Ombre et l'équipement. Les deux sont **COMM**, et la demande n'en contenait que des **résumés**. Contexte joueur : MR9, aucun test en jeu fait à ce jour.

| # | Changement | Pourquoi | Étiquette |
|---|---|---|---|
| 1 | **Portée par défaut en S1/S2 : 175 % « b »** (Stretch, Augur Reach, Transient Fortitude à la place d'Augur Secrets, Intensify, Catalyzing). Force 274 %, soit **1,080 dès le départ**. Coût : −0,56 énergie/s et plus de Catalyzing. La v3 avait raté cette config, qui fait mieux que ses 145 % et ses « 190 % d » | Point 1 (test de Ruby) | DÉD (M24) ; gain réel : TEST (T16) |
| 2 | Le mécanisme de Ruby colle au wiki : les mini-Reap visent **le plus proche ennemi pas encore touché** dans **30 m, fixe**. Elle se trompe sur le rayon (20 m, ou 30 m qui grandirait avec la Portée) | Point 1 | CONF (règle, rayon) ; perte des ombres : COMM → TEST |
| 3 | **Seismic Bond était mal modélisé.** Ce n'est pas +30 % fixe, mais **+3 % par stack**, 12 s chacun, 10 stacks max, un stack par dégât du Huras pendant que Gloom draine. Le +0,55/s de la v3 n'existe qu'à 10 stacks ; **Gloom ne rapporte plus que Gloom coupé qu'à partir de 9 stacks** | Point 2 | CONF + DÉD (M25) → TEST (T22) |
| 4 | **Figeage :** le wiki de Gloom dit que son drain **suit l'efficacité en continu**, Seismic Bond cité en exemple. Si c'était faux : +2,00/s au mieux, donc toujours derrière Gloom coupé, sauf à relancer Gloom une fois les stacks montés | Point 2 | CONF ; hypothèse figée : DÉD |
| 5 | **Boucle de Ruby (Gloom retiré, Ombre gardée) : non retenue.** Reunite casse Stalk à chaque retour, et il faut 7 s pour redevenir invisible : 16 à 47 % du temps visible. L'énergie du corps vaut au mieux « Gloom coupé ». Transference force Reunite. Elle demande aussi Roar en slot 3, incompatible avec F1 | Point 2 | CONF + DÉD (M26) |
| 6 | **Viral :** seuils confirmés (1 stack : 104,5 % avec Roar, 200 % sans ; 9 stacks : Sow + 1 Reap tuent quelle que soit la Force). **Tempest Barrage + Viral Tempest** est la seule source sérieuse ; c'est une variante à tester, pas adoptée. Les griffes du Huras sont un appoint ; l'Epitaph reste le dernier recours | Point 3 | CONF + DÉD (M27) → TEST (T23) |
| 7 | **Secondary Fortifier via l'Ombre : la v3 avait tort.** La page « Unattributed Damage » du wiki (tests de joueurs, vérifiés en 06/2026) dit que les griffes déclenchent les effets de l'arsenal de Sevagoth. Fortifier y garde le **vol d'OG**, mais pas le ×8. C'est la 3e source concordante | Point 4 | COMM (3 sources) → TEST (T18 réécrit) |
| 8 | **Eximus Entropiques :** d'après les précisions des patch notes U44, **les dégâts non-mêlée restent réduits de 90 % même bulle cassée**, et la bulle bloque les compétences **de l'intérieur comme de l'extérieur**. La rotation v3 « casser l'orbe puis nuker » ne marche pas. Fiche B refaite autour de la mêlée ; bénédiction et Tauron Strike sortent du plan | Point 5 | CONF |
| 9 | **Tests : liste courte, 8 tests en 9 étapes ordonnées** (section 12). T16 réécrit avec le protocole de Ruby ; T18 et T21 révisés ; T22 (stacks de Seismic Bond et figeage) et T23 (Viral Tempest) ajoutés | Point 6 | – |
| 10 | Script : sections M24 à M28 ; Overextended aux rangs 0 à 3 ajouté aux mods | – | – |

---

## Changelog v2 → v3

**Sources de la v3 :** trois guides YouTube (V1, V2, et V3 de Gaz, mi-octobre 2026) et le résumé d'un quatrième (V4). Tout cela est **COMM**. La demande contenait des **résumés** de ces vidéos, pas les transcriptions intégrales : chaque affirmation est donc prise telle que résumée, puis recoupée avec le wiki et les patch notes.

| # | Changement | Pourquoi | Étiquette |
|---|---|---|---|
| 1 | **F1 reste, avec la même infusion (Roar en slot 4)**, mais se décline en **deux fiches** : A « SP et endurance » (quasi inchangée) et B « Void Cascade et level cap » (Circumvent à la place de Molt, une mêlée, la bénédiction Iceblade) | Points 2 et 3 | DÉD |
| 2 | **Portée :** ce qui en dépend (bande de Reap, mini-Reap, Sow, Dark Propagation, Gloom) et ce qui est fixe (explosion de 4 m, détection des mini-Reap à 30 m). Nouveau tableau 100 / 145 / 190 / 250 / 280 % avec le coût en Force (M19) | Point 1 | CONF + DÉD |
| 3 | **190 % (V1, V2)** : le one-shot de départ tombe (0,923 au lieu de 1,075, il faut 84 kills de Molt), sauf avec Transient Fortitude (1,141, mais Durée 72,5 %). En endurance, **145 % reste le réglage par défaut** ; la variante 190 % « d » est gardée pour le cas où T15/T16 la justifient | Point 1 | DÉD |
| 4 | « Au-delà de 190 %, les ombres buguent » : **aucune source ne relie ce bug à la Portée**. Le bug existe : une mini-Reap tourne en rond si sa cible meurt avant d'être marquée (wiki Shadow Haze ; forum, 07/2025). Hypothèse : à ~188 %, le rayon de Sow atteint les 30 m de détection des ombres. → T16 | Point 1 | CONF (bug) ; NON TROUVÉ (lien avec la Portée) → TEST |
| 5 | **Explosion de Sow : 4 m, fixe** (wiki), contre 5 m pour V2 et 28 m pour V3. Les 28 m de V3 correspondent au **rayon de lancement de Sow à 175 %** (Stretch + Augur Reach) ou à Dark Propagation à ~187 %, pas à l'explosion | Point 1 | CONF + DÉD |
| 6 | **Eximus Entropiques :** règles exactes (wiki, U44). Tant que l'orbe tient, F1 ne peut ni les cibler ni les atteindre par la zone. Il faut **un coup de mêlée sous bénédiction Iceblade**, ou un **Tauron Strike**. **F2 n'est meilleur ni en Void Cascade ni au level cap** | Point 2 | CONF + DÉD |
| 7 | **Arcane Circumvent devient le plan B n°1 contre l'Overguard** : 2 roulades à tout niveau, sans tirer. Il remplace Molt dans la fiche B | Point 3 (V3 a raison) | CONF ; invisibilité DÉD → T20 |
| 8 | **Secondary Fortifier « hérité » par les griffes (V1)** : contredit par le wiki, l'Ombre n'utilise pas les effets passifs de l'arsenal de Sevagoth. Classé « non soutenu » → T18. **v4 : révisé, probable (section 11.4)** | Point 3 (V1 probablement faux) | CONF → TEST |
| 9 | **Gloom gardé.** Avec Seismic Bond, il rapporte **+0,55 énergie/s net**, et son ralentissement couvre exactement le rayon de Sow. L'argument « le ralentissement baisse les kills/min » est plausible mais n'a jamais été mesuré → T17. **v4 : +0,55 seulement à 10 stacks de Seismic Bond (section 11.2)** | Point 4 | DÉD → TEST |
| 10 | **Archon Stretch :** seules les **compétences** qui infligent de l'Électricité le déclenchent, et une compétence canalisée comme Gloom le bloque (CONF). Le wiki liste les Shadow Claws modées Électricité (Exalted Shadow), **pas le Huras**. Inaccessible à F1 ; si le Huras le déclenchait quand même, couper Gloom rapporterait +1,0/s → T19 | Point 5 | CONF + DÉD |
| 11 | **Seuil : 254,02 % exact** ; à 255 %, le 2e Reap fait 1,0038 des PV actuels. Les vidéos arrondissent, il n'y a pas de désaccord | Point 6 | DÉD (M22) |
| 12 | Tests **T16 à T21** ajoutés. Script : sections M19 à M23 ; Overextended (R4 et R5) et Archon Stretch ajoutés aux mods | – | – |

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

## 1. Verdict (v4, inchangé en v5)

1. **Steel Path et endurance : F1, fiche A, à 175 % de Portée « b »** (274 %, one-shot dès le départ). C'est le nouveau réglage par défaut ; T16 (protocole de Ruby) le confirme ou ramène à 100 %.
2. **Level cap (S3) : F1 à 100 %**, Catalyzing gardé (la moindre fenêtre visible tue). Circumvent à la place de Molt si T1 montre que le nuke ne traverse pas l'Overguard.
3. **Void Cascade / Zariman (fiche B, MR9, sans bénédiction) : F1 + une vraie mêlée + Circumvent.** Aucune compétence ne peut tuer un Entropique : bloquée par la bulle, −90 % même bulle cassée (CONF, U44). Il faut entrer dans la bulle et le tuer à la mêlée.
4. **Gloom reste**, mais il ne rapporte de l'énergie qu'à partir de 9 stacks de Seismic Bond (T22). La boucle « Ombre » de Ruby n'est pas retenue (16 à 47 % du temps visible, même énergie que Gloom coupé).
5. **Viral :** Tempest Barrage + Viral Tempest à la place de Roar est le seul concurrent sérieux (1 stack ×2 bat Roar ×1,82 ; 9 stacks tuent dès le 1er Reap ; v5 : encore plus fort avec des éclats Émeraude). Variante à tester (T23), pas adoptée. Secondary Fortifier via l'Ombre est probable, sans effet sur F1 hors Tombstone.

---

## 2. Fiches finales F1 (v4 : une par contenu, à recopier en jeu)

Les deux fiches sont **deux configs de la même Sevagoth Prime**. L'infusion est la même (Roar en slot 4), donc il n'y a aucun conflit Helminth (CONF : une infusion occupe le même slot dans toutes les configs). L'Ombre, les griffes, le Huras et l'Epitaph sont communs.

### Fiche A : Steel Path et endurance (S1, S2)

**Sevagoth Prime**
- **Helminth :** Roar infusé en **slot 4** (remplace Exalted Shadow ; le passif Tombstone reste actif, CONF).
- **Aura :** Brief Respite (Aura Forma). **Exilus :** Power Drift.
- **Mods :** Shadow Haze · Dark Propagation · Umbral Intensify [U] · Augur Secrets · Intensify · Catalyzing Shields [V] · Primed Continuity [M] · Streamline [N].
  - Capacité 72/74, 2 Forma (Aura + Umbra).
- **v4 : Portée par défaut en S1 et S2 = 175 % « b »** (M24, DÉD ; gain à confirmer par T16) :
  - Augur Secrets → **Stretch**, Intensify → **Transient Fortitude**, Catalyzing Shields → **Augur Reach**. Exilus inchangé (Power Drift).
  - Force **274 %**, 2e Reap **1,080 dès le départ** (pas besoin de Molt), Durée 127,5 % (Roar 38,3 s), Efficacité 130 %, Gloom 95 %.
  - Énergie +2,89/s à 60 kills/min avec 10 stacks de Seismic Bond (contre +3,45 à 100 %). Le gating fiable de Catalyzing disparaît.
  - Mini-Reap de 14 m, Sow de 28 m, sous les 30 m de détection des ombres (CONF).
  - 71/74, **3 Forma** : Aura, Umbra, plus une Madurai (Transient Fortitude et Primed Continuity sont tous deux M).
  - Les réglages v3 à 145 % et à 190 % « d » sont remplacés : 175 % « b » a plus de Force que 145 % et une meilleure Durée que 190 % « d ».
  - **Si T16 ne montre aucun gain sur 100 %**, revenir à la config 100 % ci-dessus (Catalyzing compris).
- **S3 level cap :** rester à 100 % (fiche B).
- **Arcanes :** Molt Augmented + Arcane Energize. **Si T1 donne H0** (le nuke ne traverse pas l'OG) : Arcane Circumvent à la place de Molt. 175 % « b » garde alors son one-shot (274 % sans Molt).
- **Éclats :** 4 × Crimson tauforgé (Force) + 1 × Amber tauforgé (orbes d'énergie +75 %).
- **Focus :** Vazarin. **Parazon :** Hard Reset (−15 s de neutralisation du compagnon par Mercy, CONF).
- **Stats :**
  - Force 273 % → 333 % (Molt plein), Durée 155 %, Portée 100 %, Efficacité 130 % (160 % sous Gloom avec Seismic Bond).
  - 2e Reap **1,075 → 1,332**. Roar ×1,82 → ×2,00 (46,5 s). Gloom **95 % dès le départ**. Énergie +3,45/s à 60 kills/min ; tient dès ~20 kills/min.

**Rotation A**
1. Roar → Gloom. **v4 :** permanent si T22 montre au moins 9 stacks de Seismic Bond en combat ; sinon « à la demande » (Gloom coupé : +2,90/s à 100 %, +2,66/s à 175 % « b »). T17 tranche ensuite sur les kills/min.
2. Par pack : **Reap → Sow → Reap**. Eximus : **+1 Reap** (et Sow avant si T6 dit « consommé »).
3. Roar toutes les 46,5 s (38,3 s à 175 % « b »). Ramasser les orbes.
4. **Aucun tir en S2/S3** (l'invisibilité casse, puis 7 s de recharge).

### Fiche B : Void Cascade (Zariman) et level cap (S3), sans bénédiction (v4)

**Ce qui a changé (CONF, précisions des patch notes U44) :**
- les dégâts **non-mêlée** sont réduits de **90 %** (75 % pour l'Opérateur), **que la bulle soit cassée ou non** ;
- la bulle empêche les compétences de blesser l'Eximus, **de l'intérieur comme de l'extérieur** ;
- les Entropiques apparaissent dans **toutes** les missions Zariman, plus souvent que les autres Eximus, y compris pendant les combats de Void Angels.
- **Conséquence (DÉD) :** le nuke de F1 ne tue jamais un Entropique. Bulle intacte : 0 dégât. Bulle cassée : 10,75 % de ses PV actuels par détonation, soit encore 32 % des PV après 10 détonations (M28). La rotation v3 (« casser l'orbe puis Reap → Sow → Reap → Reap ») était fausse.

**Sevagoth Prime** : mods de la fiche A **à 100 %** (Augur Secrets et Catalyzing gardés). Tu seras visible pendant la mêlée, donc le gating compte.
- **Arcanes :** Arcane Energize + **Arcane Circumvent** (rang 5) à la place de Molt (inchangé).
  - Au level cap hors Zariman, si T1 donne H1 : Arcane Escapist à la place de Circumvent.
  - Jouable dès P4. À P3, garder Molt.
- **Mêlée : c'est maintenant le seul outil contre les Entropiques** (CONF). Prendre ta mêlée la mieux modée ; ce choix n'est pas modélisé. Roar s'applique aussi à ses dégâts (DÉD : c'est un buff de dégâts, la source reste la mêlée).
- **Bénédiction Iceblade :** inutile au plan.
  - Tu ne peux pas la donner (MR30). Tu peux la **recevoir** si un joueur MR30+ la donne dans ton instance de Yuvan Peak (CONF).
  - Elle casse la bulle au premier coup de mêlée, mais ne retire pas les −90 % : pour F1, elle ne fait gagner que le fait de frapper de l'extérieur (DÉD).
- **Tauron Strike : retiré du plan.**
  - Il casse la bulle, mais les −90 % restent.
  - Il demande The Old Peace et l'Artefact Tektolyst (CONF), et se charge à 0,02 % par kill (CONF).
- **Void Cascade, Opérateur (CONF) :**
  - le champ de 20 m d'un Exolizer possédé force la Transference ;
  - en Opérateur, ton corps reste invisible (Stalk continue de le couvrir), mais il n'est plus invulnérable : il prend les dégâts avec 90 % de réduction tant que Gloom est actif (toujours) ou que Roar et Sow durent ;
  - la Transference force aussi Reunite.
  - **Couper Gloom avant d'entrer dans un champ d'Exolizer** (DÉD).
- **Huras :** il ne cible pas les Entropiques (CONF).

**Rotation B, contre un Eximus Entropique**
1. Nuker le pack autour (**Reap → Sow → Reap**). Les ennemis ordinaires **dans** la bulle meurent-ils ? → T21 a.
2. **Entrer dans la bulle**, invisible.
3. **Deux roulades Circumvent à travers lui**, si T21 f montre que ça marche bulle intacte. Sinon, frapper directement.
4. **Mêlée jusqu'à la mort.** L'invisibilité tombe, puis 7 s de recharge (CONF).
5. Reprendre la rotation.
- **Selon T21 g (nuke lancé de l'intérieur de la bulle) :**
  - **ça marche** (contraire aux patch notes) : Reap → Sow → Reap → Reap depuis l'intérieur, avec Circumvent pour l'OG, sans mêlée ;
  - **ça ne marche pas** (attendu, CONF) : on garde les étapes 1 à 5. Si ta mêlée est trop faible au niveau atteint, on ignore les Entropiques (ils ne sont pas l'objectif de Void Cascade) ou on les laisse à l'escouade (mêlée, ou un joueur qui porte la bénédiction). Tauron Strike reste exclu pour la raison ci-dessus.
- **Level cap hors Zariman :** inchangé. Circumvent remplace l'Epitaph : 2 roulades au lieu de 7 tirs chargés visibles (M23).

### Commun aux deux fiches

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

**Arme :** Epitaph Prime + Secondary Fortifier. En v3, c'est le dernier recours anti-Overguard (après Circumvent) et l'amorce. Contre un Entropique, ses dégâts sont réduits de 90 % (CONF).

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
- **P5 — Final.** Plus rien à farmer pour la fiche A : la suite concerne l'Ombre et les griffes Tombstone, plus des Forma de confort.
- **Fiche B (v3)** : jouable dès **P4** (258 % sans Molt, soit 1,016). Elle demande en plus Arcane Circumvent (rang 5) et une mêlée modée.

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
| 2. **Secondary Fortifier ×21** (rang 5) | 168 | Plan B Overguard. **v3 :** passe derrière Circumvent dans le plan B ; il s'achète aussi chez Nightcap et Ordis (CONF), mais reste ici le moins cher des trois achats |
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

**Plan B si le nuke ne traverse pas l'OG** (v3 : Circumvent ajouté en tête), classé du moins au plus coûteux en invisibilité :

| Rang | Moyen | Casse l'invisibilité ? | Efficacité | Coût pour le build |
|---|---|---|---|---|
| **1 (v3)** | **Arcane Circumvent** : une roulade à travers un ennemi à 4 m lui vole 50 % (rang 5) de son armure, de ses boucliers et de son OG ; répétable (CONF) | Non, en principe : une roulade n'est pas une attaque d'arme, et seules les attaques d'arme, certaines compétences et l'inactivité cassent Ghost (CONF page Ghost ; DÉD pour Stalk → **T20**) | Le wiki écrit que « deux roulades retirent tout au rang max » : **2 roulades à tout niveau**, contre 7 tirs d'Epitaph au 9 999 (M23). Si le % porte sur l'OG restant, il en reste 25 % après 2 roulades (T20). Bonus : tu gagnes l'OG volé, plafonné à 10 000 (CONF) | Un slot d'arcane : Molt (fiche B, ou fiche A sous H0). ~50 à 55 p au rang 5, ou 21 × ~3 p au rang 0 (warframe.market, 30/10/2026) ; sinon Roathe, 5 Maphica pièce, ou Descendia SP |
| 2 | **Blast des détonations voisines** : 25 % des PV du voisin × Roar (× vuln si elle touche l'OG) dans 4 m | Non | Il faut **3 Heavy Gunners** à 4 m de l'Eximus de SP175 à 1000, 5 au 9999 ; seulement 1 à 2 si la vulnérabilité touche l'OG (DÉD, M18). Sans effet sur un Entropique dont l'orbe tient (les dégâts de zone ne le traversent pas, CONF) | Aucun ; dépend de la densité (F1 ne regroupe pas) |
| 3 | **Assassin Posture du Huras** : cible les Eximus, +300 % contre l'OG | Non (le Huras attaque sans casser Stalk, CONF) | NON TROUVÉ : dégâts du compagnon au niveau visé (T4). Ne cible pas les Entropiques (CONF) | Aucun |
| 4 | **Amp de l'Opérateur** : l'OG prend +50 % de dégâts Void | Non (attaquer en Opérateur ne casse pas le camouflage, CONF) | Faible à haut niveau (DÉD) ; −75 % contre un Entropique (CONF) | Aucun |
| 5 | **Nidri Tauron Strike + Rift Waters** (Vazarin) : vortex de 20 m pendant 20 s, OG −25 %/s (CONF) ; nœud marqué Opérateur, invulnérable pendant le lancement. Tout Tauron Strike casse aussi l'orbe d'un Entropique (CONF) | À TESTER | Retire tout l'OG en 4 s, quel que soit le niveau. Mais la charge ne vient que de 0,02 % par kill (+10 % par lentille) et de 20 % par orbe de Convergence : quelques fois par heure (DÉD) | The Old Peace + Tektolyst Artifact Vazarin (150 Lyroic Bridge, Ren Hypercore et Ascaris Prime) + nœuds |
| 6 | **Epitaph Prime + Secondary Fortifier** (×8 contre l'OG) | **Oui**, 7 s de recharge (CONF) | 1 tir chargé jusqu'au niveau 1000, 7 au 9999 (M23, DÉD) | Aucun (déjà dans le build) ; risque des 7 s visibles |

**Lecture (v3) :**
- **H0, quel que soit le niveau :** Circumvent d'abord, si T20 confirme qu'il retire l'OG sans casser l'invisibilité. Il rend le plan B indépendant du niveau, ce qu'aucune autre ligne ne faisait.
- **Si T20 l'infirme :** on retombe sur le plan v2.
  - S1/S2 : l'Epitaph suffit (le corps encaisse 7 s avec gating et ralentissement).
  - S3 : rangs 2, 3 et 5 d'abord, l'Epitaph seulement dans une fenêtre sûre ; S3 devient alors nettement plus dur pour F1.

**Secondary Fortifier sur les griffes de l'Ombre (affirmation de V1) : non soutenu en v3. v4 : la v3 avait tort, voir section 11.4.**
- Le wiki dit que l'Ombre « ne peut pas utiliser l'équipement ni les effets passifs de l'arsenal de Sevagoth », avec l'exemple de Primary Dexterity, un autre arcane d'arme (CONF).
- Secondary Fortifier se déclenche sur les dégâts d'une arme secondaire ; les griffes sont une arme de mêlée exaltée.
- Seule exception documentée : certains effets de « Unattributed Damage » profitent à Sevagoth et à l'Ombre pendant Exalted Shadow (CONF). Rien n'indique que Fortifier en fasse partie (DÉD).
- Sans conséquence pour F1 (pas d'Exalted Shadow, sauf au Tombstone). → **T18** si tu veux trancher.

---

## 6. Portée (réécrite en v3)

**Ce qui dépend de la Portée** (CONF ; rayon de base × Portée) :
- **Reap :** bande de 8 m autour du vol ; c'est elle qui choisit les cibles. La longueur du vol (93 m en tap, 186 m en maintien) dépend de la Durée, pas de la Portée (DÉD : 10 m/s × 6 s × 155 %).
- **Mini-Reap de Shadow Haze :** leur rayon d'effet (et leur durée de vol, liée à la Durée).
- **Sow :** 16 m, le rayon de lancement qui sème les ennemis.
- **Dark Propagation :** 15 m, la propagation de Sow quand un ennemi semé meurt. Elle utilise la Portée de Sevagoth.
- **Gloom :** de 4 à 16 m.

**Ce qui est fixe** (CONF ; valeurs sans icône de Portée sur le wiki) :
- **L'explosion de Sow/Reap : 4 m.** Chaque ennemi qui détone inflige 25 % de ses PV actuels en Blast aux *autres* ennemis dans 4 m. V2 dit 5 m, V3 dit 28 m (COMM).
- La détection des mini-Reap : **30 m** autour de chaque ombre.
- La chance critique de Shadow Haze (indépendante de la Portée depuis 33.6.3).

**D'où viennent les 28 m de V3 (DÉD) ?** 16 m × 1,75 = 28 m, soit le rayon de Sow avec Stretch + Augur Reach. Ou bien Dark Propagation à ~187 %. Aucune lecture ne donne une explosion de 28 m. → T16 a.

**« Au-delà de 190 %, les ombres buguent » (V1, V2) :**
- **Aucune source ne lie ce bug à la Portée** (NON TROUVÉ dans le wiki ni dans les patch notes U36 à U44).
- Le bug lui-même est documenté (CONF, wiki Shadow Haze, section Bugs ; forum, 07/2025) : une mini-Reap tourne en rond autour d'une cible morte si cette cible meurt **avant** d'avoir reçu la vulnérabilité.
- Plus la Portée est grande, plus le nuke tue loin et vite pendant que les ombres sont en route ; le bug devrait donc devenir plus fréquent (DÉD, plausible).
- **Coïncidence notable (DÉD, hypothèse) :** à ~188 %, le rayon de Sow atteint 30 m, la portée de détection fixe des mini-Reap. Au-delà, Sow sème des ennemis que les ombres ne peuvent plus détecter. Cela pourrait expliquer la règle empirique des 190 %. → T16 b.

**Tableau (M19, 4 Crimson tauforgés, DÉD)** :

| Option | Portée | Sow / Dark Propagation | Force (début / Molt) | 2e Reap (début / Molt) | Kills de Molt pour 1,00 | Gloom début | Durée | Énergie à 60 kpm (aire\* / pack constant) | Capacité |
|---|---|---|---|---|---|---|---|---|---|
| **100 %** (fiches A et B) | 100 % | 16 / 15 m | 273 / 333 % | **1,075** / 1,332 | 0 | 95 % | 155 % | +3,45 / +3,45 | 72/74 |
| **145 %** : Augur Secrets → Stretch (S2, défaut) | 145 % | 23,2 / 21,8 m | 249 / 309 % | 0,981 / 1,226 | 21 | 87 % | 155 % | +4,78 / +3,45 | 74/74 |
| 190 % a : + Cunning Drift, Catalyzing → Augur Reach | 190 % | 30,4 / 28,5 m | 234 / 294 % | 0,923 / 1,162 | 84 | 82 % | 155 % | +4,78 / +3,45 | 74/74 |
| 190 % b : + Cunning Drift, Intensify → Augur Reach (**= V1** : 204 % / 190 %) | 190 % | 30,4 / 28,5 m | 204 / 264 % | 0,814 / 1,039 | 209 | 71 % | 155 % | +4,78 / +3,45 | 70/74 |
| 190 % c : + Cunning Drift, Streamline → Augur Reach | 190 % | 30,4 / 28,5 m | 234 / 294 % | 0,923 / 1,162 | 84 | 82 % | 155 % | +1,85 / −0,49 | 72/74 |
| **190 % d** : a + Primed Continuity → Transient Fortitude | 190 % | 30,4 / 28,5 m | 289 / 349 % | **1,141** / 1,405 | 0 | 95 % | 72,5 % | +1,84 / +0,51 | 70/74 (3 F) |
| 250 % façon V3 : Stretch, Augur Reach (pour Intensify), Overextended R4 (pour Catalyzing), Transient Fortitude, Power Drift gardé | 250 % | 40,0 / 37,5 m | 224 / 284 % | 0,886 / 1,120 | 126 | 78 % | 72,5 % | +1,84 / +0,51 | 69/74 |
| Max 280 % : Stretch, Augur Reach, Overextended, Cunning Drift | 280 % | 44,8 / 42,0 m | 144 / 204 % | 0,616 / 0,814 | jamais | 50 % | 155 % | +4,78 / +3,45 | 69/74 |
| Max 280 % + Transient Fortitude | 280 % | 44,8 / 42,0 m | 199 / 259 % | 0,797 / 1,020 | 230 | 70 % | 72,5 % | +1,84 / +0,51 | 70/74 |

La bande de Reap vaut 8 m × Portée : 8 / 11,6 / 15,2 / 20 / 22,4 m.
\* Aire : on suppose que les kills par rotation suivent l'aire (15 × Portée², plafonné à 30). C'est une hypothèse TEST (T15). Avec ce plafond, rien ne bouge au-delà de 145 %.

**Lecture :**
- **Chaque palier de Portée se paie en Force ou en énergie.** Les seuls slots libérables sont Augur Secrets, Intensify, Catalyzing, Primed Continuity et Streamline.
- **190 % a :** perd le gating de Catalyzing, et il faut 84 kills de Molt pour retrouver le one-shot.
- **190 % b reproduit exactement V1** (204 % et 190 %) : sous le seuil jusqu'à 209 kills de Molt. C'est cohérent avec V1 seulement si ses éclats ou son Molt diffèrent (DÉD).
- **190 % c :** l'énergie s'effondre (−0,49/s à pack constant).
- **190 % d :** la seule à 190 % qui garde le one-shot dès le départ (1,141), et la seule qui remplit les deux critères de V2 (≥ 255 % et ≤ 190 %). En échange : Durée 72,5 % (Roar 21,8 s, vulnérabilité de Reap plus courte), énergie +1,84/s, plus de gating de Catalyzing.
- **250 % façon V3 :** 0,886 au départ, 126 kills pour passer le seuil. Les « 255 % » de V3 ne sont atteints qu'avec Molt en partie chargé (284 % plein). C'est cohérent si V3 compte Molt (DÉD).
- **280 % :** sans Transient Fortitude, le one-shot n'arrive jamais.

**Décision :**
- **v4 : S1 et S2 passent à 175 % « b » (section 11.1) ; S3 et fiche B restent à 100 %.** Décision v3 d'origine : **S1, S3 et Zariman (fiche B) : 100 %.** En S1, les packs sont denses et le vol de Reap couvre la distance. En S3, le niveau est maximal dès la 1re seconde. En Void Cascade, tes kills comptent dès que tu es dans l'anneau.
- **S2 endurance : 145 % par défaut** (Augur Secrets → Stretch, seulement à partir de P5 ; à P3, le même swap tombe à 0,905 et demande 105 kills de Molt).
- **190 % « d » seulement si les deux conditions sont réunies :** T15 montre plus de 10 % de kills/min en passant de 100 à 145 % (la Portée paie), et T16 b ne montre pas plus de mini-Reap bloquées à 190 % qu'à 145 %.
- **Au-delà de 190 % : refusé pour F1.** On rejoint la limite de V1/V2, mais pour une raison chiffrée (le coût en Force), pas à cause d'un bug non démontré.
- Les autres échanges à 145 % de la v2 restent valables, à départager par T15 :
  - Dark Propagation → Stretch : 1,075, sans coût en Force, mais on perd la propagation de Sow ;
  - Streamline → Stretch : 1,075, énergie +1,85/s ;
  - Intensify → Stretch : 0,957, 46 kills de Molt.
- **L'invisibilité change la donne (DÉD) :** les ennemis ne convergent pas vers un Sevagoth invisible, donc la Portée compte plus qu'en jeu visible. La distance d'engagement typique n'est pas documentée (NON TROUVÉ, T15).

---

## 6 bis. Eximus Entropiques et Void Cascade (v3)

**Règles** (CONF : wiki Eximus#Entropic et Yuvan Peak, patch notes U44) :
- **Où :** Zariman uniquement, où ils apparaissent **plus souvent que les autres Eximus**. Kuva Grineer et Corpus de Juno au sol ; ni Nullifier ni unité volante. Introduits en 44.0.
- **L'orbe rouge** bloque tous les projectiles d'armes et d'Amps. Il protège aussi les alliés proches des attaques à distance (Codex).
- **Tant que l'orbe tient, l'Eximus est immunisé à toutes les compétences**, que tu sois dedans ou dehors. Cela vaut aussi pour les zones (exemple du wiki : Brimstone) et la réduction d'armure.
- **Réductions passives :** armes primaires et secondaires −90 %, Amp −75 %, attaques à distance des glaives et gunblades −90 %.
- **Les attaques radiales et les ondes de slam ne traversent pas l'orbe**, dans un sens comme dans l'autre.
- **Les compagnons ne les ciblent pas.**
- **Armure de base 50**, quel que soit l'ennemi.
- Le wiki conclut : « la mêlée classique est le seul moyen fiable ».
- **Casser l'orbe :**
  - frapper l'orbe ou l'Eximus en mêlée sous **bénédiction Iceblade of Narin** ;
  - ou le toucher avec un **Tauron Strike**.
  - Ensuite, les compétences peuvent le cibler (**v4 :** mais avec −90 % de dégâts, U44).
- **La bénédiction :**
  - donnée à Yuvan Peak par un joueur MR30+, à toute l'instance du hub, sans avoir réussi à retirer l'épée ;
  - 3 h, comme au True Master's Font (le donneur a 23 h de recharge) ;
  - elle ajoute 3 statuts Cold par coup de mêlée et s'applique aussi à la mêlée des compagnons.

**Ce que F1 peut faire :**

| Situation | F1 | Étiquette |
|---|---|---|
| Entropique, orbe actif | **Rien.** Reap, Sow, Gloom et Roar sont sans effet ; l'Epitaph fait −90 % et l'orbe bloque ses projectiles ; le Huras ne le cible pas ; le Blast des voisins ne traverse pas l'orbe | CONF |
| Ennemis ordinaires à l'intérieur de l'orbe | Inconnu. Le Codex dit que l'orbe protège les alliés des attaques à distance, sans rien dire des compétences ; les explosions venues de dehors ne traversent pas (radial) | NON TROUVÉ → T21 a |
| Orbe cassé (mêlée bénie ou Tauron Strike) | ~~Nuke normal~~ **v4 : faux.** Les dégâts non-mêlée restent à −90 % même bulle cassée (U44), donc 10,75 % des PV actuels par détonation (M28). Voir 11.5 | CONF + DÉD |
| Ni bénédiction ni Tauron | Le tuer à la mêlée (armure de base 50, mêlée non réduite), ou le contourner | CONF |

**Ordre de grandeur à la mêlée (M20, DÉD).** Le proxy prend les PV et l'OG du Heavy Gunner Eximus, avec une armure de base 50 mise à l'échelle. L'arme mesurée est celle des griffes de l'Ombre (config F3) ; ce n'est qu'un ordre de grandeur pour une mêlée endgame.

| Niveau | Armure | OG | PV | Griffes 4x, sans DH ni Haze | Griffes 12x, sans DH ni Haze | Mêmes griffes 4x **avec** DH et Haze (Eximus ordinaire) |
|---|---|---|---|---|---|---|
| S1 SP175 | 979 | 324 090 | 1,93 M | 0,56 s | 0,11 s | 0,10 s |
| S2a 500 | 2 139 | 836 472 | 4,19 M | 1,65 s | 0,31 s | 0,30 s |
| S2b 1000 | 2 700 | 1,56 M | 6,95 M | 3,19 s | 0,59 s | 0,59 s |
| S3 9999 | 2 700 | 12,4 M | 36,6 M | 18,85 s | 3,52 s | 3,46 s |

**F2 (Ombre et griffes, Roar en slot 3) devient-il le meilleur pour Void Cascade et le level cap ? Non (DÉD) :**
1. **Contre l'orbe, les atouts de F2 sont des compétences.** La vulnérabilité de Death's Harvest et le critique de Shadow Haze ne passent pas (CONF). Au combo 4x, les griffes deviennent 5 à 6 fois plus lentes (M20). Et l'effet de Shadow Haze sur les griffes est contesté sur le forum depuis 2024 (COMM).
2. **Pire, elles pourraient ne pas toucher du tout.** Le wiki d'Archon Stretch range les coups des Shadow Claws parmi les dégâts de **compétence** (Exalted Shadow y figure, CONF). Si le moteur fait pareil pour l'immunité des Entropiques, les griffes ne les touchent pas tant que l'orbe tient. La page Entropic ne parle pas des armes exaltées (NON TROUVÉ → T21 e).
3. **Les procs Slash forcés** des lourdes contournent l'armure. Mais un Entropique n'a que 50 d'armure de base : l'avantage disparaît justement contre lui.
4. **Au level cap, les griffes dépendent du niveau** (temps ×34 de 175 à 9 999, M20), le nuke non (% des PV actuels). Seul l'OG résiste au nuke, et Circumvent le retire à tout niveau (M23, T20).
5. **F2 met Roar en slot 3**, ce qui est impossible sur la même frame que F1 (CONF). Seul un Sevagoth non-Prime pourrait le porter en parallèle.
- **Repli :** F3 (sans infusion, annexe A) reste possible sur la même frame, si T21 montre que les griffes frappent un Entropique et que la mêlée de Sevagoth l'expose trop. Mais sans Roar, il faut une amorce Viral (0,55 sans).
- **Mêlée du Huras sous bénédiction :** elle casserait aussi l'orbe (CONF), mais le Huras ne cible pas les Entropiques. Un coup accidentel n'est pas une stratégie (DÉD).

---

## 6 ter. Gloom, Seismic Bond, Archon Stretch et seuil (v3)

**Gloom (M21, F1 à P5, 60 kills/min, DÉD) :**

| | Gloom permanent | Gloom coupé |
|---|---|---|
| Énergie | **+3,45/s** | +2,90/s |
| Seismic Bond | actif : +30 % d'efficacité tant que Gloom canalise (CONF) | inutile |
| Ralentissement | 95 % jusqu'à 16 m, **le même rayon que Sow** à toute Portée | – |
| Vol de vie | 13,7 % des dégâts, sur 370 PV | – |

- **Avec Seismic Bond, Gloom se paie lui-même et rapporte +0,55/s :** l'efficacité gagnée sur tous les sorts dépasse son drain. **v4 : seulement à 10 stacks ; Seismic Bond donne +3 % par stack, pas +30 % fixe (section 11.2).**
- **V1 à V3 ont raison sur le vol de vie :** sur 370 PV et contre des coups qui tuent d'un seul, il ne sert presque à rien.
- **« Le ralentissement baisse les kills/min » :** plausible si c'est le débit d'ennemis entrant dans la zone qui limite les kills.
  - Mais le ralentissement agit dans le rayon même de Sow : les ennemis ralentis sont déjà dans la zone du prochain nuke.
  - Et un Sevagoth invisible n'attire pas les ennemis de toute façon (DÉD).
  - Aucune mesure ni d'un côté ni de l'autre → **T17**.
- **Ninjase garde Gloom** (COMM), comme F1.
- **Le choix de F1 n'en dépend pas.** Gloom occupe le slot 3 et Roar le slot 4 : couper Gloom ne libère rien. Pour récupérer quelque chose, il faudrait mettre Roar en slot 3 et garder l'Ombre (V1/V2, soit F2), ce qui est exclu.
- **Règle :** Gloom permanent par défaut. Si T17 montre plus de 10 % de kills/min avec Gloom coupé, passer « à la demande » (l'énergie reste positive à +2,90/s) et remplacer Seismic Bond par un mod de survie sur le Huras.

**Archon Stretch :**
- **Règles (CONF, wiki) :**
  - seules les **compétences** de Warframe ou de compagnon qui infligent de l'Électricité déclenchent le bonus ;
  - il donne 2 énergie/s pendant 5 s (10 au total), sans cumul ni rafraîchissement ;
  - chaque lancement de sort coupe la régénération 1 s ;
  - une compétence canalisée qui draine l'énergie, comme Gloom, la bloque tant qu'elle est active.
- **Côté Sevagoth, le wiki liste Exalted Shadow quand les Shadow Claws sont modées Électricité.** C'est sans doute le mécanisme de V1, qui garde l'Ombre.
- **Côté compagnons, le Huras n'est pas listé.** La liste contient Adarza, Dethcube, Diriga, Helminth Charger, Hound, Panzer, Pharaoh et Vizier (souvent avec Shocking Claws). Aucun Kubrow (CONF ; pour le Huras, NON TROUVÉ → T19).
- **Pour F1, il est inaccessible :** aucune compétence d'Électricité (Exalted Shadow est remplacé par Roar), Huras non listé, et Gloom le bloquerait de toute façon.
- **Si T19 donnait raison à V1 (M21, DÉD) :**
  - Archon Stretch rapporterait au mieux ~1,56/s : 2/s, moins 1 s de pause par lancement, à 0,22 lancement/s.
  - Gloom coupé + Archon Stretch : **+4,46/s**, contre +3,45/s pour Gloom + Seismic Bond, soit **+1,0/s**.
  - Il faudrait mettre Archon Stretch dans le slot de Stretch (fiche A à 145 %) et couper Gloom.
  - À comparer avec ce que T17 dira des kills/min.

**Seuil :** **254,02 %** exact (M22) ; à 255 %, le 2e Reap fait 1,0038 des PV actuels. Les vidéos arrondissent. Les « 6 Reap sans Molt, 2 avec » de V2 collent avec un franchissement du seuil (DÉD).

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

## 8. Tests en jeu : protocoles détaillés (T16, T18, T21 révisés et T22, T23 ajoutés en v4 ; **ordre de passage : section 12**)

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
| T2 | La vulnérabilité de Reap s'applique-t-elle à l'OG ? | Simulacrum, Eximus, Pause AI ; tir chargé d'Epitaph avant et après un Reap | Chiffre de dégâts sur l'OG | ≈×2,36 : oui (plan B rang 2 à 1–2 voisins). ×1 : non (3 voisins) |
| T3 | (variante) Precision Intensify booste-t-il Roar en slot 4 ? | Arsenal, puis mission | Buff Roar dans le HUD | Optionnel : Intensify reste le choix par défaut |
| T5 | Gloom à 95 % ralentit-il la cadence de tir ? | Simulacrum, Heavy Gunner, Gloom on/off | Balles par 5 s | Division par ≈20 : oui |
| T6 | Sow survit-il à une détonation ? | Sow → Reap → Reap sans relancer Sow | Une ou deux détonations | Une : ajouter un Sow avant le 3e Reap sur les Eximus |
| T8 | Tenue d'énergie | SP survival, 20 min, Gloom permanent, palier en cours | Énergie toutes les 2 min | Conforme au tableau des paliers à ±1/s |
| T10 | Le Tombstone coûte-t-il un revive ? Molt est-il réinitialisé ? | Solo, 5 morts contrôlées | Compteur de revives, stacks de Molt | DE (2023) : pas de revive consommé |
| T13 | Un Mercy casse-t-il Stalk ? (Escapist, Hard Reset) | Mercy sur un Eximus affaibli | État du camouflage | Oui : en S3, Escapist seulement dans une fenêtre sûre |
| T14 | Blood Rush se pose-t-il sur Shadow Claws Prime ? (griffes Tombstone) | Arsenal | Le mod s'équipe-t-il ? | Non : True Steel à la place |
| T7, T9, T11, T12 | Abandonnés (F2/F3 non retenues) | – | – | – |
| **T15** | Portée en endurance | Même nœud SP survival, 15 min × 4 configs : 100 %, Augur Secrets → Stretch, Dark Propagation → Stretch, **190 % « d »** (v3) | Kills/min de fin de mission, courbe d'énergie | Plus de 10 % de kills/min pour une config Stretch : l'adopter en S2. 190 % « d » seulement s'il bat 145 % de plus de 10 % et que T16 b est négatif |

### Tests v3 et v4 (T16 à T23)

Pour chaque test : capture vidéo PS5 (bouton Créer), relecture image par image. Le marqueur de waypoint affiche la distance en mètres : c'est lui qui sert à mesurer les écarts.

**T16 (réécrit en v4, protocole de RubyBlossom5) : la Portée améliore-t-elle les mini-Reap ?**
- **Idée :** isoler les mini-Reap de Shadow Haze. Le Reap principal ne touche qu'un appât ; seules les ombres nées de sa mort peuvent atteindre le pack.
- **Mise en place :**
  - Simulacrum, Steel Path ON, Pause AI ON.
  - 1 Lancer « appât » collé à toi, et un pack de 8 Lancers groupés à 10–15 m **dans ton dos** (distances lues au waypoint).
  - Trois configs : 100 % (fiche A de base), **175 % « b »**, et 235 % (M24, 235 % « b »).
- **Déroulé (20 fois par config) :**
  1. Dos au pack, Reap sur l'appât seul.
  2. Le tuer à l'Epitaph : jusqu'à 3 mini-Reap naissent (CONF).
  3. Sur la vidéo, compter les ennemis **différents** du pack qui reçoivent la vulnérabilité, et les ombres qui tournent sur place ou partent dans le vide.
  4. « Kill all », puis respawn.
- **Lecture :**
  - 175 % donne au moins +0,5 ennemi touché par appât et moins d'ombres perdues que 100 % → **175 % « b » confirmé** (fiche A).
  - 100 % aussi bon ou meilleur → retour à 100 %, Catalyzing compris.
  - 235 % pire que 175 % (attendu par Ruby) → aucun réglage au-delà de 175 %.
- **Variante mission (facultative) :** même nœud SP survival, 15 min à 100 % puis 15 min à 175 % « b ». Comparer les kills/min ; au-delà de 10 % d'écart, ce chiffre prime sur le Simulacrum.
- **Ancien T16 a (rayon de l'explosion, 4 m selon le wiki) :** facultatif, il ne change pas le build.

**T17 : Gloom permanent ou coupé (kills/min)**
- **Mise en place :** même nœud SP survival (Infestés d'Eris : ça farme aussi le Moonflesh), fiche A à 145 %.
- **Déroulé :** 4 sessions de 15 min, en alternance Gloom permanent / coupé / permanent / coupé.
- **Mesures :** kills à 15 min, énergie toutes les 2 min, neutralisations du Huras.
- **Lecture :**
  - Gloom coupé à +10 % de kills/min ou plus → Gloom « à la demande », et Seismic Bond remplacé par un mod de survie ;
  - +5 % ou moins → Gloom permanent ;
  - entre les deux → Gloom permanent (pour l'énergie).

**T18 (révisé en v4) : Secondary Fortifier vole-t-il de l'OG via les dégâts de l'Ombre ? (V1, source B)**
- **Mise en place :**
  - config F3 sans infusion (il faut Exalted Shadow) ;
  - Simulacrum, Heavy Gunner Eximus, Steel Path ON, Pause AI ON.
- **Trois passages :** Fortifier R5 (i) sur la secondaire seule, (ii) sur l'arch-gun seul, (iii) nulle part (contrôle). Pour (i), refaire une fois en passant en Ombre avec la secondaire en main, une fois avec la mêlée en main.
- **Mesures :** 10 s de griffes sur l'OG.
  - Qui gagne de l'OG : la barre de Sevagoth ou celle de l'Ombre ?
  - Les chiffres de dégâts sur l'OG sont-ils ×8 ou ×1 ? Le wiki prévoit ×1, avec le vol d'OG conservé.
- **Lecture :**
  - de l'OG gagné en (i) et (ii), pas en (iii) → source B confirmée ;
  - aucune différence entre « secondaire en main » et « mêlée en main » → l'arme n'a pas besoin d'être en main.
  - Pour F1, cela ne touche que le Tombstone : mettre Fortifier sur l'arch-gun, qui sert alors seulement de support à l'arcane.

**T19 : le Huras déclenche-t-il Archon Stretch ?**
- **Mise en place :** Archon Stretch à la place de Stretch ; Huras avec l'élément Électricité utilisé par V1. Gloom **coupé**. Simulacrum, Pause AI OFF, 5 min.
- **Contrôle :** config F3, Shadow Claws modées Électricité. D'après le wiki, l'icône doit apparaître.
- **Lecture :** icône Archon Stretch au HUD quand le Huras attaque → V1 confirmé. Il faut alors rejouer M21 (Gloom coupé + Archon Stretch : +1,0/s) et laisser T17 trancher. Pas d'icône → question close.

**T20 : Arcane Circumvent contre l'Overguard**
- **Mise en place :** Simulacrum, Heavy Gunner Eximus, Steel Path ON, niveau max, Pause AI ON, invincibilité ON. Huras avec Stalk, arcane Circumvent R5.
- **Déroulé :**
  1. Roulade à travers l'Eximus. Noter sa barre d'OG, ta barre d'OG et l'icône d'invisibilité.
  2. Deuxième roulade, mêmes relevés.
  3. Reap → Sow → Reap → Reap.
  4. Refaire le tout à bas niveau.
- **Lecture :**
  - OG à 50 % puis 0 % (lecture linéaire) et invisibilité intacte → plan B n°1 validé, fiche B confirmée ;
  - 50 % puis 25 % (lecture géométrique) → 3 à 4 roulades, toujours à tout niveau ;
  - invisibilité cassée → Circumvent vaut l'Epitaph côté exposition, mais reste indépendant du niveau.

**T21 (révisé en v4) : Eximus Entropiques (Zariman, Void Cascade SP), sans bénédiction**
- **a. Nuke de l'extérieur, bulle intacte :** Reap → Sow → Reap sur un pack qui contient un Entropique. Les ennemis ordinaires **dans** la bulle meurent-ils ?
- **g (v4). Nuke lancé de l'intérieur de la bulle :** entrer dans la bulle (invisible), puis Reap → Sow → Reap → Reap. L'Entropique prend-il des dégâts ? Les patch notes disent non (CONF).
- **f. Roulade Circumvent, bulle intacte :** l'OG est-il volé ?
- **c (v4). Mêlée de l'intérieur, Roar actif :** temps pour tuer l'Entropique (chrono sur la vidéo), au niveau de la mission. Noter l'état de l'invisibilité.
- **b. Facultatif, si un joueur MR30+ te donne la bénédiction :** un coup de mêlée casse-t-il la bulle ? Un nuke juste après ne devrait retirer que ~10 % des PV par détonation (M28).
- **e. Facultatif (config F3) :** une lourde des Shadow Claws, bulle intacte. Y a-t-il des dégâts ?
- **Suite selon le résultat :**
  - **g positif** (contraire aux patch notes) → fiche B : nuke de l'intérieur, Circumvent pour l'OG, mêlée inutile.
  - **g négatif** (attendu) → rotation B à la mêlée (section 2).
    - Si c dépasse ~5 s au niveau joué, les Entropiques te coûtent plus qu'ils ne rapportent : les ignorer (ils ne sont pas l'objectif de Void Cascade) ou les laisser à l'escouade.
    - Tauron Strike reste exclu : il casse la bulle, mais les −90 % restent.
  - **a négatif** (ceux de la bulle survivent) → tuer l'Entropique ou entrer dans sa bulle avant de nuker le pack.
  - **f positif** → Circumvent avant la mêlée. **f négatif** → frapper d'abord ; la mêlée retire l'OG.
  - **e positif** → la config F3 devient une option « chasse aux Entropiques ».

**T22 (v4) : stacks de Seismic Bond et figeage du drain de Gloom**
- **Mise en place :** Simulacrum, Steel Path ON, 10 Lancers sans Eximus (les ondes de Seismic Bond ne touchent pas l'OG, CONF), Pause AI OFF. Fiche A, Huras avec Seismic Bond R5. Vidéo.
- **Étape 1, figeage :**
  1. Attendre 12 s sans compétence canalisée : les stacks expirent.
  2. Lancer Gloom au milieu du pack, puis ne plus rien lancer.
  3. Relever l'énergie toutes les 2 s pendant 20 s, et le nombre de stacks sur l'icône du buff.
  - **Lecture :** le drain ralentit à mesure que les stacks montent → dynamique (attendu, CONF). Le drain reste constant → figé : relancer Gloom une fois 10 stacks atteints.
- **Étape 2, stacks en combat :** 3 min de rotation normale en mission SP. Relever les stacks toutes les 15 s sur la vidéo.
  - **Lecture :**
    - **9 stacks ou plus en moyenne** → Gloom permanent (+3,45/s à 100 %, +2,89 à 175 % « b »).
    - **1 à 8 stacks** → Gloom reste positif (+0,69/s à 3 stacks, +2,27 à 7, à 100 %), mais Gloom coupé rapporte plus (+2,90). Gloom ne se justifie plus que par le ralentissement : T17 tranche.
    - **0 stack** → Gloom à la demande, et Seismic Bond quitte le Huras au profit d'un mod de survie.

**T23 (v4) : Tempest Barrage + Viral Tempest à la place de Roar**
- **Prérequis :** Hydroid absorbé par l'Helminth, Viral Tempest rang 3.
- **Config C** (même frame, Tempest en slot 4 à la place de Roar ; DÉD à partir des règles d'infusion CONF) : fiche A à 100 %, avec Viral Tempest à la place de Catalyzing. La Force reste à 273 %.
- **Mise en place :** Simulacrum, Steel Path ON, Pause AI ON.
  - 10 Lancers groupés, puis 10 Lancers étalés à 0, 5 et 9 m du centre du barrage.
- **Déroulé :**
  1. Tempest Barrage sur le pack.
  2. À 1, 3 et 5 s, compter les stacks Viral (icônes de statut) sur la vidéo.
  3. Sow → **un seul** Reap : compter les morts à la 1re détonation.
  4. Comparer à la fiche A (Roar, puis Reap → Sow → Reap).
  5. **v5 :** refaire 1 à 3 avec 2 Émeraude tauforgés à la place de 2 Crimson. M31 prévoit 1,440 à 1 stack, avec Gloom à 85 %.
- **Lecture :**
  - au moins 90 % du pack tué par Sow → Reap après 4 s de barrage, y compris à 9 m → la config C nettoie en 2 sorts au lieu de 3 et libère la Force. Elle devient candidate : comparer ensuite les kills/min en mission (15 min chacune).
  - seul le centre meurt → Roar reste.

---

## 9. Chiffres clés et ce qui renverserait le verdict

- **Nuke F1** (M11/M12) : seuil 254,0 % de Force. 1,075 à P5, 1,016 à P4, 0,996 à P3 (5 kills de Molt), 1,055 à P1/P2 grâce à Transient Fortitude.
- **Eximus Heavy Gunner** (M4) : 1,93 M PV et 324 k OG au niveau 175 ; 6,9 M et 1,56 M au 1000 ; 36,6 M et 12,4 M au 9999. Une balle tue le corps dès le niveau **415** (M6).
- **Énergie** (M15) : P5 tient dès ~20 kills/min. Sans Energize (P0), −4,73/s même Gloom coupé.
- **Crimson tauforgés** (M13) : 1,45 équivalent par semaine en Elite, 0,99 sans.
- **Taubound** (M17) : 918 Moonflesh, ~2 à 4,5 h de farm.
- **Portée (M19, v3)** : 145 % → 0,981 (21 kills de Molt) ; 190 % → 0,923 (84 kills), sauf variante « d » (1,141, Durée 72,5 %) ; 250 % façon V3 → 0,886 (126 kills) ; 280 % → 0,616 (jamais sans Transient Fortitude).
- **Entropiques (M20, v3)** : sans DH ni Haze, les griffes passent de 0,10 à 0,56 s (SP175) et de 3,5 à 18,9 s (9 999) ; F1 a besoin d'un coup de mêlée bénie ou d'un Tauron Strike.
- **Gloom (M21, v3)** : +3,45/s avec, +2,90/s sans ; Archon Stretch, s'il était déclenchable, ferait +4,46/s Gloom coupé.
- **Circumvent (M23, v3)** : 2 roulades à tout niveau, contre 1 tir d'Epitaph jusqu'au 1000 et 7 au 9 999.

**Ce qui renverserait le verdict :**
- **Le Huras est neutralisé plus de 2 fois par 10 min dès le niveau 500 (T4)** et le Shade ne fait pas mieux : F1 perd sa couche principale en S2/S3.
- **H0 au T1 et Blast voisin insuffisant (étape 7)** : en S3, les Eximus imposent l'Epitaph, donc des fenêtres visibles. F1 reste le meilleur build, mais S3 passe de « viable » à « difficile ».
- **Packs de moins de 8 kills par rotation (T8)** : l'énergie de P5 passe à −0,65/s. Couper Gloom hors des pics, ou passer à la portée (section 6).
- **v3 : T20 négatif** (Circumvent casse l'invisibilité, ou ne retire que 25 % par roulade) : le plan B redevient celui de la v2, et S3 reste « difficile » sous H0.
- **v3 : T21 b/c négatif** (la mêlée bénie ne casse pas l'orbe, ou le nuke échoue ensuite) : en Void Cascade, F1 doit tuer les Entropiques à la mêlée. La fiche B demande alors une vraie mêlée endgame, et F3 (griffes) redevient une option si T21 e est positif.
- **v3 : T17 positif** (Gloom coupé à +10 % de kills/min) : Gloom à la demande. Ce n'est pas un renversement, F1 ne change pas.

---

## 10. Liste de farm priorisée (v3)

Prix : warframe.market, vendeurs en jeu, crossplay, 29/10/2026 (Circumvent : 30/10/2026). Les sources et substituts de la v1 restent valables. La v3 ajoute la ligne 6 et décale les suivantes.

| Priorité | Pièce | Palier | Impact (DÉD) | Où | Coût |
|---|---|---|---|---|---|
| 1 | **Arcane Energize** | P1 | +4,58/s : sans lui, F1 n'est pas viable | Capture de l'Hydrolyst ; Orphix Veil Proxima rotation C | ~210 p |
| 1 | **Molt Augmented** | P1 | +60 % de Force après 250 kills | Cavalero (Holdfasts rang 5) ; Thrax/Void Angels 6,67 % | ~50 p |
| 2 | Roar (Helminth), Shadow Haze, Dark Propagation, Umbral Intensify, Transient Fortitude, Catalyzing Shields, Brief Respite, Augur Secrets, Power Drift, Streamline, Shade | P1 | Base du one-shot (268 %) et du gating | Helminth / Suda ou Perrin / Simaris / coffre de Deimos / Derelict / Orphid / Thumpers / test Lua / Junction / Marché | voir v1 |
| 3 | **Huras Kubrow + Seismic Bond** (+ mods de survie, Assassin Posture) | P2 | +6,14/s sous Gloom permanent | Œuf de Kubrow, incubation aléatoire (taux NON TROUVÉ) ; Son (Entrati rang 3) ; The Business | ~29 p (Seismic) |
| 4 | **Taubound** : Crimson tau, Secondary Fortifier, Amber tau | P4 | 0,996 → 1,016 ; plan B OG ; +0,58/s | Praghasa, Eris, **avant le 17/11** | 918 Moonflesh |
| 5 | **4 Crimson normaux + 1 Amber normal**, **Primed Continuity** | P3 | Permet Transient → Primed Continuity : +2,94/s (+1,18 avec l'Amber) | Bird 3 cette semaine, Archon Hunt, Netracells, Archimedea, Icebind ; Primed Continuity chez Baro | ~155 p (Primed Continuity R10) |
| **6 (v3)** | **Arcane Circumvent** (rang 5) + une **mêlée** modée + la **bénédiction Iceblade** | Fiche B (dès P4) ; plus tôt si T1 = H0 | Plan B n°1 contre l'OG, à tout niveau ; casser l'orbe des Entropiques | Circumvent : marché, Roathe (5 Maphica pièce), Descendia SP ; bénédiction : un joueur MR30+ à Yuvan Peak (gratuit) | ~50 à 55 p (R5) ou 21 × ~3 p (R0) |
| 7 | **3 Crimson tauforgés de plus** | P5 | 1,016 → 1,075, Gloom 95 % dès le départ | Section 4 (2 à 3 semaines) | – |
| 8 | Forma de confort ; Ombre et griffes Tombstone | – | Filet de secours à la mort | v1 | – |

---

## 11. Compléments v4 (sources A et B)

### 11.1 Portée : le test de RubyBlossom5 (point 1)

**Ce que dit le wiki** (CONF, page Shadow Haze) :
- une mini-Reap se verrouille sur **l'ennemi le plus proche pas encore touché** par Reap ou Death's Harvest, dans **30 m** autour d'elle. La valeur est soulignée sur le wiki, donc fixe : elle ne grandit pas avec la Portée ;
- elle vole à 10 m/s, 50 % plus vite quand elle cherche une cible ;
- son rayon d'effet vaut 8 m × Portée de Sevagoth ;
- 3 mini-Reap au plus.
- **Ruby se trompe sur le rayon** (20 m fixe, puis 30 m qui grandirait avec la Portée) : c'est 30 m, fixe.

**Son mécanisme** : avec beaucoup de Portée, la première ombre touche la cible de loin grâce à son grand rayon, et les deux autres, verrouillées sur la même cible, la perdent.
- Il découle logiquement de la règle de verrouillage (DÉD, plausible), mais aucune source ne le décrit (TEST).
- Le wiki documente un bug voisin : une ombre tourne autour d'une cible morte avant d'avoir été marquée (CONF).

**Son test** (COMM, une seule source, Simulacrum) : 175 % donne le meilleur résultat, 235 % gaspille des ombres, 100 % est irrégulier.
- C'est cohérent avec l'hypothèse de la v3 : à 175 %, Sow (28 m) reste sous les 30 m de détection ; au-delà de 187,5 %, il les dépasse (DÉD). Deux raisons indépendantes pointent donc vers « pas plus de ~180 % ».

**Chiffres (M24, toutes les combinaisons de mods, seules les configs non dominées sont gardées, DÉD) :**

| Config | Ajoute | Retire | Force | 2e Reap au départ | Kills de Molt | Durée | Catalyzing | Énergie 60 kpm* | Capacité |
|---|---|---|---|---|---|---|---|---|---|
| 100 % (F1 actuel) | – | – | 273 % | 1,075 | 0 | 155 % | oui | +3,45 | 72/74, 2 F |
| 175 % a | Stretch, Augur Reach, Transient Fortitude | Augur Secrets, Catalyzing, Primed Continuity | 304 % | 1,205 | 0 | 72,5 % | non | +0,51 | 70/74, 3 F |
| **175 % b** | **Stretch, Augur Reach, Transient Fortitude** | **Augur Secrets, Intensify, Catalyzing** | **274 %** | **1,080** | **0** | **127,5 %** | **non** | **+2,89** | **71/74, 3 F** |
| 175 % d | Stretch, Augur Reach | Augur Secrets, Catalyzing | 249 % | 0,981 | 21 | 155 % | non | +3,45 | 74/74, 2 F |
| 175 % g | Stretch, Augur Reach | Augur Secrets, Intensify | 219 % | 0,868 | 146 | 155 % | oui | +3,45 | 70/74, 2 F |
| 190 % a | 175 % a + Cunning Drift | … + Power Drift | 289 % | 1,141 | 0 | 72,5 % | non | +0,51 | 70/74, 3 F |
| 190 % b | 175 % b + Cunning Drift | … + Power Drift | 259 % | 1,020 | 0 | 127,5 % | non | +2,89 | 71/74, 3 F |
| 235 % a | Stretch, Transient Fortitude, Overextended | Augur Secrets, Catalyzing, Primed Continuity | 244 % | 0,961 | 42 | 72,5 % | non | +0,51 | 74/74, 2 F |

\* Énergie à pack constant, avec 10 stacks de Seismic Bond (voir 11.2). Les autres lignes de M24 (c, e, f…) sont dominées ou moins utiles.

**Décision (v4) :**
- **Fiche A (S1, S2) : 175 % « b ».** One-shot dès le départ (1,080), Durée 127,5 %, énergie +2,89/s. Il coûte Catalyzing, c'est-à-dire le gating fiable : risque accepté tant que Stalk tient (T4).
- **Pas 190 % « b » :** sa marge est plus mince (1,020), Sow à 30,4 m dépasse la détection, et le test de Ruby désigne 175 %.
- **S3 et fiche B : 100 %.** Les fenêtres visibles (S3, mêlée contre les Entropiques) rendent Catalyzing précieux.
- **T16 (protocole de Ruby) tranche.** Si 175 % ne bat pas 100 %, on revient à 100 %.

**Apport de la source C (v5) :**
- **Détection des mini-ombres à 30 m :** sa page Overframe donne aussi 30 m (COMM). Avec le wiki (CONF), cela règle la contradiction de la source A.
- **Son calculateur à 190 % donne nos chiffres** (p. 4, COMM ; égal à M19 et M24) : rayon de débuff des mini-ombres 15,2 m, durée de vol 6 s × Durée, propagation de Dark Propagation 28,5 m.
- **Portée idéale de Gloom :** 145 à 175 % selon elle (COMM). 175 % « b » est dans la plage, et sa Force (274 %) atteint le plafond de ralentissement de 95 % (272 %, CONF).
- **Coût nouveau (DÉD, M29) :** le rayon de Gloom grandit de 4 à 16 m × Portée, à 2 m/s × Durée (CONF). Il atteint 16 m en 3,9 s à 100 %, mais 28 m en 8,2 s à 175 % « b » : les ennemis entre 16 et 28 m attendent leur ralentissement.
- Décision v4 inchangée.

### 11.2 Gloom contre l'Ombre : Seismic Bond réel et boucle de Ruby (point 2)

**Seismic Bond** (CONF) :
- +3 % d'efficacité par stack au rang 5, 12 s par stack, plafond +30 % ;
- un stack par dégât infligé par le compagnon **pendant qu'une compétence canalisée est active** ; Gloom figure dans la liste ;
- **Gloom ne compte que s'il draine**, donc avec des ennemis dans son rayon ;
- couper la canalisation n'efface pas les stacks déjà acquis ;
- ses ondes de choc (4 m) ne touchent pas les ennemis sous Overguard.

**Figeage** (CONF, page Gloom) : « le drain d'énergie suit en continu l'Efficacité et la Durée, par exemple Seismic Bond ». Gloom se comporte donc comme Peacemaker, pas comme Balefire.

**Bilan (M25, F1 à 100 %, 60 kills/min, DÉD) :**

| Stacks | Gloom permanent (drain dynamique, CONF) | Gloom figé sans stack (hypothèse) | Gloom coupé |
|---|---|---|---|
| 0 | −0,49 | −0,49 | +2,90 |
| 3 | +0,69 | +0,26 | +2,90 |
| 5 | +1,48 | +0,75 | +2,90 |
| 7 | +2,27 | +1,25 | +2,90 |
| 10 | **+3,45** | +2,00 | +2,90 |

- **Le +0,55 de la v3 n'existe qu'à 10 stacks.** Gloom permanent ne rapporte plus que Gloom coupé qu'à partir de **9 stacks**. À 175 % « b », les chiffres sont +2,89 à 10 stacks, −1,46 à 0, et +2,66 Gloom coupé.
- Combien de stacks le Huras tient vraiment : NON TROUVÉ. Chaque dégât compte, ondes comprises, donc c'est sans doute élevé en pack (DÉD) → **T22**.
- **Si Gloom figeait son efficacité** (le wiki dit que non) : +2,00/s au mieux, toujours derrière Gloom coupé (−0,90/s). Parade : relancer Gloom une fois les 10 stacks montés (50 × 0,4 = 20 d'énergie). Le drain resterait alors figé à 160 %, même si les stacks retombent ensuite.

**La boucle de Ruby** (COMM) : Sow + Reap remplissent le Death Well → Ombre → Death's Harvest → Reunite → Roar → Reap. Elle demande Roar en slot 3 et l'Ombre gardée : c'est F2, incompatible avec F1 sur la même frame (CONF).

| Critère | F1 (Gloom + Huras) | Boucle de Ruby |
|---|---|---|
| Invisibilité | permanente tant que le Huras tient | **cassée à chaque Reunite** (CONF, page Stalk), puis 7 s de recharge : **16 à 47 % du temps visible** pour des boucles de 45 à 15 s (M26, DÉD) |
| Protection | ralentissement de 95 %, sauf sur les unités sous OG et les Void Angels (CONF) ; gating | corps invulnérable et non ciblable pendant l'Ombre, 5 s d'invulnérabilité à l'invocation, soin au Reunite (CONF) |
| Énergie du corps | +3,45 à 10 stacks ; −0,49 à 0 | **au mieux +2,90**, le bilan de « Gloom coupé » : mêmes sorts du corps, et ceux de l'Ombre puisent dans sa propre réserve (CONF + DÉD) |
| Void Cascade | Gloom expose le corps en Opérateur (CONF) | la Transference force Reunite (CONF) |

- **Ruby a raison sur l'énergie si le Huras tient moins de 9 stacks**, et sur la survie **du corps pendant les phases d'Ombre**.
- Elle a tort sur la survie d'ensemble dès que la moindre fenêtre visible tue : une balle tue le corps dès le niveau 415 (M6). Ce cas couvre S2 et S3.
- Que 4 créateurs sur 5 retirent Gloom est un consensus (COMM), pas un mécanisme. Leur conclusion sur l'énergie colle avec M25 pour peu de stacks.
- **F1 ne change pas.** La règle pour Gloom dépend de T22, puis de T17.

**Apport de la source C (v5) :**
- **Drain de Gloom vérifié.** Le modèle utilise bien 0,75 énergie/s par ennemi, 10 ennemis au plus, × (2 − Efficacité) / Durée (CONF).
  - Le calculateur de Ruby (p. 3) donne les mêmes valeurs : 0,339/s par ennemi et 3,387/s à 10 ennemis, à 155 % de Durée et 130 % d'Efficacité (M29).
  - Avec 10 stacks de Seismic Bond, le drain tombe à 1,935/s.
- **Ralentissement figé au lancer, plafond de 95 % à 272 %** (CONF, wiki Gloom ; COMM C). Une config qui compte sur Molt pour atteindre le plafond doit relancer Gloom. F1 (273 %) et 175 % « b » (274 %) y sont dès le départ.
- **Ce que vaut le plafond**, avec sa métrique du « ralentissement effectif », 1 / (1 − ralentissement) (M29, DÉD) :
  - ×20 à 95 % ;
  - ×7,8 à 87 % (config v3 à 145 %) ;
  - ×2,6 à 61 % (sa build à 174 %).
- **Seismic Bond :** elle le cite comme aide contre le drain, sans dire s'il est figé ; son calculateur prévoit un champ Seismic Bond, laissé à 0 %. Le wiki dit « dynamique » (CONF) : **le test de figeage (T22, étape 1) reste en tête de liste.**
- **Death Well :** 5 % par kill de Reap ou de Sow, 10 % par kill marqué par les deux (COMM C). C'est cohérent avec le wiki : 5 % par ennemi et par compétence (CONF).
  - Il atteint donc 75 % après 8 kills : sa boucle peut sortir l'Ombre à chaque pack, avec un Reunite et 7 s de visibilité à chaque fois.
  - Elle se place donc en haut du tableau M26 : ~47 % du temps visible pour des boucles de 15 s (DÉD).
- **Invocation de l'Ombre :** 5 s d'invincibilité (CONF ; COMM C).

### 11.3 Viral (point 3)

**Seuils** (CONF : Viral ×(2 + 0,25 × (n − 1)), 10 stacks au plus, 6 s chacun ; M27) :

| Stacks | Mult. | Force mini pour le one-shot au 2e Reap, avec Roar | sans Roar | 1re détonation seule |
|---|---|---|---|---|
| 0 | ×1 | 254,0 % | 600 % | 0,250 |
| 1 | ×2 | **104,5 %** | **200 %** | 0,500 |
| 2 | ×2,25 | 84,0 % | 155,6 % | 0,563 |
| 5 | ×3 | 38,8 % | 66,7 % | 0,750 |
| 9 | ×4 | – | – | **1,000 : Sow + 1 Reap tuent** |
| 10 | ×4,25 | – | – | 1,063 |

- Les chiffres de Ruby (200 % sans Roar, ~105 % avec, 9 stacks suffisent) sont **exacts**. Le wiki Shadow Haze cite lui aussi les 9 stacks (CONF).
- **Le Viral ne s'applique pas tant que l'Overguard tient** (CONF) : il n'aide pas contre les Eximus avant le retrait de l'OG.

**Sources compatibles avec l'invisibilité :**

| Source | Casse Stalk ? | Couverture | Verdict |
|---|---|---|---|
| **Griffes du Huras** : Frost Jaw (Froid) + Venom Teeth (Toxine), qui se combinent en Viral (DÉD, règle de combinaison). Éviter les mods « … Claws », qui convertissent tout en un seul élément (CONF) | Non (CONF) | Une cible à la fois. Statut de base 5 % (CONF) ; chance finale et cadence NON TROUVÉ. Frenzied Posture (un coup, puis il change de cible, CONF) étale mieux, mais remplace l'Assassin Posture | Appoint, pas structurel |
| **Tempest Barrage + Viral Tempest**, slot 4 à la place de Roar | Non : c'est une compétence (CONF) | Zone fixe de 10 m, visée à distance illimitée, 4 missiles/s, explosion de 5 m × Portée, 10 s × Durée, chance Viral de 100 % × Force par missile, donc plusieurs stacks par impact au-delà de 100 % (CONF). **Au centre : 1 stack en ~0,75 s, 9 en ~3,25 s ; à 9 m : 9 stacks en ~6 s** (M27, DÉD ; répartition des impacts supposée uniforme, NON TROUVÉ) | **Seul concurrent sérieux de Roar → T23** |
| Epitaph, tir non chargé (zone, 50 % de statut) | **Oui** (CONF) | Zone | Dernier recours |

**Tempest contre Roar (DÉD sauf mention) :**
- **Pour :**
  - avec 1 stack, ×2 bat le ×1,82 de Roar (2e Reap 1,18 à 273 %, contre 1,075) ;
  - avec 9 stacks, Sow → Reap tue dès la 1re détonation, quelle que soit la Force : 2 sorts par pack au lieu de 3, et la Force se libère pour la Portée ;
  - même coût par seconde que Roar (25 d'énergie par 15,5 s contre 75 par 46,5 s).
- **Opérateur (Ruby a raison, CONF) :** Tempest laisse le corps invulnérable en Opérateur, alors que Roar le rend vulnérable tant qu'il dure. Mais Gloom (toujours) et Sow (tant qu'il dure) l'exposent aussi : le gain n'existe que Gloom coupé et Sow expiré.
- **Contre :**
  - la zone est fixe et se vise (ligne de vue). Elle couvre ~10 + 5 × Portée m, soit 15 m à 100 % contre 16 m pour Sow, mais 18,75 m contre 28 m à 175 % ;
  - hors zone, l'ennemi n'a ni Viral ni Roar : 0,59 au 2e Reap à 273 %, pas de one-shot ;
  - il faut un slot de mod pour Viral Tempest ;
  - on perd le buff de Roar sur la mêlée, ce qui compte en fiche B ;
  - il faut absorber Hydroid. Viral Tempest coûte ~14 p au rang 0 (warframe.market, 30/10/2026), ou 25 000 de réputation chez Suda ou New Loka (CONF).
- **Verdict :** non adopté avant T23. Si T23 est positif, la config C (Tempest) devient candidate pour la fiche A. La fiche B garde Roar, pour la mêlée.

**Apport de la source C (v5) :**
- **Ses tables Viral se lisent sans Roar** (calculateur p. 1 et p. 7). Stacks nécessaires pour le one-shot au 2e Reap : 4 à 100 % de Force, 1 dès 200 %. Sans vulnérabilité de Reap, il en faut 9. C'est identique à M27 (colonne « sans Roar »).
- **Le Viral à l'arme (sa build) est incompatible avec F1** : tirer casse l'invisibilité (CONF), et F1 ne tire pas.
- **Son conseil sur les Eximus** (« préparer au Viral, puis 2+1 ») bute sur une règle CONF : le Viral ne prend pas sous Overguard. Il faut d'abord retirer l'OG (lourde de l'Ombre, Fortifier ou Circumvent).
- **Éclats Émeraude en config C (M31, DÉD à partir de règles CONF).** Tempest pose du Corrosif à 100 %, et l'Émeraude tauforgé donne +15 % de dégâts de compétence aux ennemis déjà sous Corrosion, cumulable entre éclats. Chaque Crimson tauforgé échangé contre un Émeraude tauforgé fait plus que compenser :

| Éclats (+ Amber) | Force | 1 stack Viral, 2e Reap | 9 stacks, 1re détonation | Ralentissement de Gloom |
|---|---|---|---|---|
| 4 Crimson tau | 273 % | 1,183 | 1,000 | 95,0 % |
| 2 Crimson + 2 Émeraude tau | 243 % | 1,440 | 1,300 | 85,0 % |
| 4 Émeraude tau | 213 % | 1,652 | 1,600 | 74,5 % |

- Le prix : le ralentissement de Gloom retombe, et Viral Tempest pose moins de stacks par missile (2,13 au lieu de 2,73).
- Les Émeraude demandent le segment Helminth Coalescent et une fusion Amber + Azure (CONF).
- **T23 compare désormais aussi 2 Crimson + 2 Émeraude tauforgés.**

### 11.4 Secondary Fortifier et l'Ombre (point 4)

**Deux pages du wiki :**
- **Passif de Sevagoth** (CONF, phrase générale) : « l'Ombre ne peut pas utiliser l'équipement ni les effets passifs de l'arsenal de Sevagoth », avec l'exemple de Primary Dexterity. C'est la base du verdict v3.
- **Unattributed Damage** (page du wiki marquée « Community », tests de joueurs datés) :
  - les Shadow Claws Prime « fonctionnent pour les effets de dégâts non attribués, pour et depuis l'arsenal de Sevagoth » (vérifié le 17/06/2026) ;
  - Secondary Fortifier sur des dégâts non attribués : **pas de ×8 contre l'OG, mais le vol d'OG est conservé** (vérifié le 19/05/2026) ;
  - les arcanes d'un arch-gun marchent sur ces dégâts **même si on ne l'utilise jamais** ;
  - un même arcane peut se cumuler plusieurs fois ;
  - en Ombre, les projectiles encore en vol et les dégâts du compagnon deviennent non attribués, tant qu'on reste en Ombre (vérifié le 13/09/2026).
- **Conclusion :** Scion (V1), la source B et cette page font 3 sources communautaires concordantes. La phrase générale du passif ne parle pas des dégâts non attribués. **La v3 avait tort** de classer l'affirmation « contredite » : elle est probable (COMM), à vérifier par T18.

**Les autres affirmations de B :**
- **« Fortifier sur la secondaire OU sur l'arch-gun »** : conforme à la page (COMM).
- **« De l'OG pour Sevagoth »** : le vol d'OG est conservé, mais on ne sait pas qui le reçoit, Sevagoth ou l'Ombre (NON TROUVÉ → T18).
- **« L'arme doit être en main au passage en Ombre »** :
  - pour Fortifier, non : la page dit que l'arch-gun marche sans être utilisé (COMM) ;
  - pour Evensong, son multishot vient d'Evensong Devotion, +35 % aux alliés pendant 30 s après un kill à l'Evensong (CONF). La condition « en main » n'est donnée que par B (COMM → T18).
- **« Melee Duplicate ajoute du multishot aux griffes »** : Melee Duplicate crée un 2e coup sur les critiques jaunes (CONF), ce n'est pas du multishot. Qu'il se déclenche depuis les griffes via les dégâts non attribués est plausible (COMM).
- **« Les griffes comptent comme compétence ET comme mêlée »** :
  - mêlée : CONF (page Exalted Shadow : Steel Charge et Arcane Fury s'appliquent) ;
  - compétence : CONF (Archon Stretch liste Exalted Shadow).
- **« Le combo des griffes reste sur la mêlée »** : COMM, introuvable ailleurs, sans effet sur F1.

**F2 réévalué :**
- **Gain :** une couche d'OG volé par les griffes (Fortifier plafonne à 15 000, CONF). L'Ombre devient moins fragile.
- **Inchangé :**
  - Reunite casse Stalk, et attaquer avec une arme exaltée aussi (CONF, page Stalk) : F2 se joue donc visible (DÉD) ;
  - Roar en slot 3 reste incompatible avec F1.
- **Contre les Entropiques :** les griffes sont de la mêlée, donc sans doute pas réduites de 90 % (DÉD). Mais la bulle peut les bloquer en tant que compétence (T21 e).
- **Pour F1 :** seul le Tombstone en profite, avec Fortifier sur l'arch-gun comme simple support d'arcane.

### 11.5 Eximus Entropiques sans bénédiction (point 5)

- **Patch notes U44, précisions de DE (CONF) :**
  - « les Entropiques résistent aux attaques non-mêlée, ce qui oblige à s'approcher et à utiliser sa mêlée » ;
  - dégâts non-mêlée **−90 %** (Opérateur −75 %) ;
  - « casser la bulle permet aux compétences de cibler l'Eximus, mais **ne change pas sa résistance** » ;
  - la bulle empêche les compétences de le blesser « **de l'intérieur comme de l'extérieur** ».
- **Notes d'origine (CONF) :**
  - « le meilleur contre est de se glisser dans leur bulle et de les éliminer de l'intérieur » ;
  - ils apparaissent dans **toute mission Zariman**, plus souvent que les autres Eximus, et quelques-uns pendant les combats de Void Angels.
- **Pour F1 (DÉD, M28) :**
  - bulle intacte, le nuke ne fait rien ;
  - bulle cassée, il retire 10,75 % des PV actuels par détonation, et il reste 32 % des PV après 10 détonations.
  - **La mêlée est le seul moyen** ; la bénédiction et le Tauron Strike ne changent pas ce verdict.
- **La bénédiction :** tu ne peux pas la donner (MR30), mais tu peux la **recevoir** d'un joueur MR30+ dans ton instance de Yuvan Peak (CONF). Pour F1, elle permet seulement de casser la bulle de l'extérieur.
- **Fiche B réécrite** (section 2). **T21 complété** avec le nuke lancé de l'intérieur et la suite à donner selon le résultat (section 8).

---

## 12. Tests : liste courte (v4), dans l'ordre

Seuls les tests qui peuvent changer le build sont gardés. Les quatre premiers se font dans la même session de Simulacrum. Protocoles détaillés en section 8.

| # | Test | Mise en place | Ce que tu mesures | Ce qui bascule |
|---|---|---|---|---|
| 1 | **T22, étape 1 : figeage de Gloom** | Simulacrum SP, 10 Lancers, Pause AI OFF, Huras avec Seismic Bond ; Gloom lancé sans stack, plus aucun autre sort | Énergie toutes les 2 s pendant 20 s, stacks sur l'icône | Drain constant → relancer Gloom une fois à 10 stacks. Drain qui ralentit (attendu) → rien à changer |
| 2 | **T1 : le nuke traverse-t-il l'OG ?** | Simulacrum, niveau max, SP, Pause AI, 1 Heavy Gunner Eximus ; Roar, Reap → Sow → Reap → Reap | Barres d'OG et de PV après chaque détonation | **H0** (l'OG tient) → Circumvent à la place de Molt (fiche A), plan B indispensable en S3. **H1** → Molt garde sa place ; en S3, Escapist plutôt que Circumvent |
| 3 | **T20 : Circumvent** | Même session, Circumvent R5, Huras avec Stalk ; 2 roulades à travers l'Eximus, au niveau max puis bas | OG de l'Eximus après chaque roulade, ton OG, icône d'invisibilité | 50 % puis 0 % sans perte d'invisibilité → plan B n°1 validé, fiche B confirmée. Invisibilité cassée ou 50 % puis 25 % → plan B v2 (Epitaph) |
| 4 | **T16 : Portée, protocole de Ruby** | Même session, Pause AI ON, appât collé à toi, 8 Lancers à 10–15 m dans ton dos ; 100 %, 175 % « b », 235 % ; 20 essais chacun | Ennemis différents marqués par les mini-Reap, ombres perdues | 175 % ≥ 100 % + 0,5 ennemi → **175 % « b » gardé**. Sinon → retour à 100 % |
| 5 | **T23 : Tempest + Viral Tempest** (si tu acceptes d'absorber Hydroid) | Simulacrum, config C (Tempest en slot 4, Viral Tempest à la place de Catalyzing) ; pack groupé, puis étalé à 0, 5 et 9 m ; **v5 :** puis avec 2 Émeraude tauforgés à la place de 2 Crimson | Stacks Viral à 1, 3 et 5 s ; morts à la 1re détonation de Sow → Reap | ≥ 90 % du pack tué, y compris à 9 m → config C candidate en fiche A, à confirmer en kills/min. Sinon → Roar reste |
| 6 | **T22, étape 2 : stacks en combat** | Mission SP survival, 3 min de rotation normale | Stacks toutes les 15 s | ≥ 9 → Gloom permanent. 1 à 8 → passer au test 7. 0 → Gloom à la demande, Seismic Bond retiré du Huras |
| 7 | **T17 : Gloom permanent ou coupé** (seulement si le test 6 donne 1 à 8 stacks) | Même nœud, 4 × 15 min en alternance | Kills/min, énergie | +10 % de kills/min Gloom coupé → Gloom à la demande. Sinon → permanent |
| 8 | **T21 : Entropiques** | Void Cascade SP, ~20 min, fiche B ; cas a, g, f, c (b et e facultatifs) | Dégâts du nuke de l'extérieur et de l'intérieur ; OG volé bulle intacte ; temps de mêlée pour tuer | g positif → nuke de l'intérieur. g négatif → mêlée ; si elle dépasse ~5 s, ignorer les Entropiques ou les laisser à l'escouade. f → Circumvent avant ou après la mêlée |
| 9 | **T4 : survie du Huras** | Phase B : Survival SP d'Eris, 60 min (sert aussi au test 7 et au Moonflesh) | Neutralisations du Huras par 10 min, part du temps invisible | Plus de 2 neutralisations par 10 min dès le niveau 500 → Calculated Redirection, puis Shade si ça ne suffit pas |

**Retirés de la liste**, parce qu'ils ne changent pas le build :
- T2 et T6 (rotation) ;
- T3 (variante) ;
- T5 (pour info) ;
- T8 (couvert par 6 et 7) ;
- T10, T13 et T14 (Tombstone et détails) ;
- T15 (fondu dans T16) ;
- T18 (Tombstone seulement) ;
- T19 (le Huras n'est pas dans la liste d'Archon Stretch).

---

## 13. Source C : page Overframe et calculateur de RubyBlossom5 (v5)

### 13.1 Calculateur « Sevagoth's Breakpoints » contre le script

**Ce qui est identique** (M29, écart < 0,005 point) :
- **Nuke (2e Reap avec Roar) :** 253 % → 99,60 % ; 254 % → 99,99 % ; 258 % → 101,56 % ; 273 % → 107,55 % ; Force de base → 48,75 %. Même formule : 0,25 × (1 + 0,5 × Force) × (1 + 0,3 × Force).
- **Drain de Gloom :** 0,339/s par ennemi et 3,387/s à 10 ennemis (Durée 155 %, Efficacité 130 %). 641 d'énergie durent 31 min 33 s pour 1 ennemi et 3 min 10 s pour 10.
- **Ralentissement de Gloom :** 35 % × Force, plafonné à 95 %.
- **Viral :** même multiplicateur (×2 au 1er stack, +0,25 par stack, ×4,25 à 10) et mêmes stacks nécessaires, tables lues sans Roar.

**Ce que son outil n'a pas et le script a :** les stacks de Seismic Bond (son champ existe, laissé à 0 %), l'énergie gagnée (orbes, Energize), l'Overguard des Eximus et les configs de mods complètes.

**Ce que son outil a et le script n'avait pas :** les éclats Émeraude avec Tempest (intégrés en M31), Smite, et d'autres Helminths (13.4).

**Ses autres colonnes, reconstituées à partir de ses valeurs :**
- **Soin de Consume :** 625 × Force², hors sujet pour F1.
- **Précision Intensify :** Roar à 1 + 0,3 × (Force + 0,9). Elle le classe « Trap Mod » ; la v1 le jugeait quasi équivalent à Intensify, et le script retient Intensify. Pas de désaccord pratique.

### 13.2 La colonne « Vs Orokin / Anarchs »

- **Elle appartient au bloc Smite, pas au bloc Roar.** Smite est l'Helminth d'Oberon (CONF, wiki Smite) :
  - il retire 100 % de l'Overguard et de l'armure de sa cible, et vise les Eximus en priorité ;
  - il inflige 35 % × Force des PV actuels en **Radiation**, plafonné à 50 % en version Helminth (atteint à 143 %).
- **Valeur de la colonne :** Smite × vulnérabilité de Reap × **0,5**. La Radiation fait ×0,5 contre Orokin et Anarch, et ×1,5 contre Sentient et Murmur (CONF, wiki Radiation) ; la colonne « Vs Murmur » vaut ×1,5.
- **L'égalité avec le True sans Roar est une coïncidence** (M29) :
  - au-dessus de 142,9 % de Force, Smite est plafonné à 50 %, et 50 % × 0,5 = 25 %, le pourcentage de base de Sow et Reap ;
  - en dessous, les deux colonnes diffèrent : à 63 %, 14,50 % contre 32,88 % ; à 100 %, 26,25 % contre 37,50 %.
- **Roar compte bien contre ces ennemis :**
  - c'est un bonus de dégâts de faction qui s'applique « à toutes les factions » (CONF, wiki Roar et Faction Damage Bonus) ;
  - le True de Sow et Reap n'a aucun modificateur de faction (CONF, wiki True Damage).
  - **F1 ne change pas** contre les Orokin (fissures du Néant) ni contre les Anarchs (Perita Rebellion).
- **Si Roar ne comptait pas** (hypothèse contredite par le wiki) : le 2e Reap tomberait à 0,591 à 273 %. Il faudrait 3 détonations pour descendre sous 7 % des PV, et les fissures deviendraient le contenu où F1 perd le plus.

### 13.3 Ses choix (sans Roar, Viral à l'arme) battent-ils F1 ?

**Sa build principale (COMM C) :** pas d'Helminth, Gloom et Ombre gardés, Force 174 % puis 234 % avec Molt, Portée 145 ou 175 %, Viral posé à l'arme (Kompressa, Epitaph). Chiffres en M30, DÉD.

| Contenu | Build de Ruby | F1 | Avantage |
|---|---|---|---|
| S1 (SP ~175, packs) | 0,935 à 174 % avec 1 stack : il faut 2 stacks par cible (1,052) pendant les 109 premiers kills de Molt, puis 1,085. Le Viral se pose à l'arme sur chaque pack, en restant visible. Gloom à 61 % au départ | 1,075 dès le départ, sans tir et invisible ; Gloom à 95 % | **F1** |
| S2 et S3 (500 à 9 999) | Fenêtres visibles à chaque tir et à chaque Reunite ; une balle tue le corps dès le niveau 415 (M6) | Invisible tant que le Huras tient | **F1** |
| Eximus (hors Entropiques) | Le Viral ne prend pas sous OG (CONF). Elle retire d'abord l'OG avec la lourde de l'Ombre (Slash forcé), puis 2+1 | T1, puis Circumvent (T20) | **À égalité** tant que T1 et T20 ne sont pas faits. Si l'OG résiste au nuke et que Circumvent échoue : avantage Ruby, grâce à l'Ombre |
| Void Cascade (Entropiques) | Les griffes sont de la mêlée (CONF), donc peut-être efficaces dans la bulle (T21 e). Mais la Transference force Reunite | Mêlée de Sevagoth (fiche B) | **Selon T21 e** |
| Huras souvent neutralisé (T4 négatif) | Ne dépend pas de l'invisibilité | Perd sa couche principale | **Ruby** |
| Helminth indisponible ou réservé à autre chose | Fonctionne sans | Demande Roar | **Ruby** |

**Réponse :**
- Sur S1 à S3 tels qu'on les a définis, ses choix ne battent pas F1 (DÉD).
- Ils gagnent dans trois cas : si T4 échoue, si tu veux garder l'Helminth pour autre chose, et peut-être contre les Entropiques si T21 e est positif.
- Son « je n'ai jamais aimé Roar » est un goût, pas un argument de calcul.

### 13.4 Ses variantes, et ce qui reste à faire

- **« Shadowless Nuke : Roar on 4th »** = la structure de F1.
- **« Shadow Nuke : Roar on 3rd »** = F2.
- **« Nuke Cascade : Viral & Tempest »** = la config C (T23, M31).
- **Mods de « Shadowless Nuke » :** pas reçus, et Overframe refuse l'accès automatique (HTTP 403). **La comparaison ligne par ligne avec F1 se fera quand tu les enverras.**
- **Hors sujet, à évaluer plus tard :** son calculateur compare aussi Roar à d'autres Helminths.
  - Rest & Rage et Webbed Embrace posent une vulnérabilité de 50 % × Force (CONF), qui se multiplie avec celle de Reap (CONF, wiki Damage Vulnerability).
  - À 273 %, cela donnerait 1,398 au lieu de 1,075 (DÉD). Mais sur une zone de 5 m (Rage) ou 6,67 m (Webbed Embrace en Helminth), au lieu de tout le rayon de Sow pour Roar.

---

## Annexes (v1, inchangées sauf mention)

## A. Fiches détaillées v1 (F1 détaillée ; F2 et F3 archivées en v2)

*v3 : les fiches à jour sont en section 2 (A et B). Ici, la mention « En S3, remplacer Molt par Arcane Escapist » est remplacée par la fiche B (Circumvent, ou Escapist si T1 = H1).*

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
- **Ajouts v5 (30/10/2026) :** RubyBlossom5, calculateur « Sevagoth's Breakpoints » (PDF joint, 9 pages, export Google Sheets) ; sa page Overframe [« The Reaper's Bible »](https://overframe.gg/build/874263/sevagoth-prime/go-to-sevagoth-shadow-claws-blossoming-death-in-depth-build/) (résumé fourni, accès automatique refusé en 403) ; wiki [Smite](https://wiki.warframe.com/w/Smite), [Radiation Damage](https://wiki.warframe.com/w/Damage/Radiation_Damage), [Anarchs](https://wiki.warframe.com/w/Anarchs), [True Damage](https://wiki.warframe.com/w/Damage/True_Damage), [Faction Damage Bonus](https://wiki.warframe.com/w/Faction_Damage_Bonus), [Archon Shard](https://wiki.warframe.com/w/Archon_Shard) (Émeraude), [Damage Vulnerability](https://wiki.warframe.com/w/Damage_Vulnerability), [Rest & Rage](https://wiki.warframe.com/w/Rest_%26_Rage), [Webbed Embrace](https://wiki.warframe.com/w/Webbed_Embrace).
- **Ajouts v4 (30/10/2026) :** wiki [Shadow Haze](https://wiki.warframe.com/w/Shadow_Haze) (verrouillage, détection 30 m, bug des ombres), [Seismic Bond](https://wiki.warframe.com/w/Seismic_Bond), [Gloom](https://wiki.warframe.com/w/Gloom) (drain dynamique, Seismic Bond seulement si Gloom draine), [Arcane Intention](https://wiki.warframe.com/w/Arcane_Intention) (liste des compétences canalisées), [Channeled Abilities](https://wiki.warframe.com/w/Channeled_Abilities), [Exalted Shadow](https://wiki.warframe.com/w/Exalted_Shadow), [Reunite](https://wiki.warframe.com/w/Reunite), [Stalk](https://wiki.warframe.com/w/Stalk) (Reunite casse l'invisibilité), [Operator/Gameplay](https://wiki.warframe.com/w/Operator/Gameplay) (vulnérabilité du corps en Opérateur par compétence), [Void Cascade](https://wiki.warframe.com/w/Void_Cascade), [Tempest Barrage](https://wiki.warframe.com/w/Tempest_Barrage), [Viral Tempest](https://wiki.warframe.com/w/Viral_Tempest), [Viral Damage](https://wiki.warframe.com/w/Damage/Viral_Damage), [Claws (Beast)](https://wiki.warframe.com/w/Claws_(Beast)), [Beast Claws Mods](https://wiki.warframe.com/w/Beast_Claws_Mods), [Huras Kubrow](https://wiki.warframe.com/w/Huras_Kubrow), [Unattributed Damage](https://wiki.warframe.com/w/Unattributed_Damage) (page communautaire, tests datés), [Melee Duplicate](https://wiki.warframe.com/w/Melee_Duplicate), [Evensong](https://wiki.warframe.com/w/Evensong), [Tauron Strike](https://wiki.warframe.com/w/Tauron_Strike), [Overextended](https://wiki.warframe.com/w/Overextended) ; patch notes [Update 44 : Iceblade of Narin](https://wiki.warframe.com/w/Update_44:_Iceblade_of_Narin) (description des Entropiques et « Entropic Eximus Clarifications ») ; prix [warframe.market, Viral Tempest](https://warframe.market/items/viral_tempest). Vidéos A (RubyBlossom5) et B : connues seulement par les résumés fournis avec la demande (COMM), non visionnées.
- **Ajouts v3 (30/10/2026) :** wiki [Eximus, section Entropic](https://wiki.warframe.com/w/Eximus#Entropic), [Yuvan Peak](https://wiki.warframe.com/w/Yuvan_Peak) (bénédiction Iceblade of Narin), [True Master's Font](https://wiki.warframe.com/w/True_Master%27s_Font) (3 h, 23 h de recharge), [Void Cascade](https://wiki.warframe.com/w/Void_Cascade), [Arcane Circumvent](https://wiki.warframe.com/w/Arcane_Circumvent), [Secondary Fortifier](https://wiki.warframe.com/w/Secondary_Fortifier), [Archon Stretch](https://wiki.warframe.com/w/Archon_Stretch), [Stretch](https://wiki.warframe.com/w/Stretch), [Augur Reach](https://wiki.warframe.com/w/Augur_Reach), [Overextended](https://wiki.warframe.com/w/Overextended), [Cunning Drift](https://wiki.warframe.com/w/Cunning_Drift), [Shadow Haze](https://wiki.warframe.com/w/Shadow_Haze) (section Bugs : ombres qui tournent), [Sevagoth/Abilities, passif](https://wiki.warframe.com/w/Sevagoth/Abilities) (l'Ombre n'utilise pas l'équipement de Sevagoth) ; patch notes [Update 44](https://forums.warframe.com/topic/1523956-update-44-iceblade-of-narin/) ; forum : [Shadows Haze augment spinning shadows, cause of issue found](https://forums.warframe.com/topic/1461820-shadows-haze-augment-spinning-shadows-cause-of-issue-found/) (07/2025), [The fix for Shadow Haze augment still don't work with Sevagoth's Shadow](https://forums.warframe.com/topic/1400398-the-fix-for-shadow-haze-augment-mod-still-dont-work-with-sevagoths-shadow/) (2024) ; prix [warframe.market, Arcane Circumvent](https://warframe.market/items/arcane_circumvent). Guides vidéo V1 à V4 : connus seulement par les résumés fournis avec la demande (COMM), non visionnés.
- **Ajouts v2 :** wiki [Archon Hunt](https://wiki.warframe.com/w/Archon_Hunt), [Netracells](https://wiki.warframe.com/w/Netracells), [Deep Archimedea](https://wiki.warframe.com/w/Deep_Archimedea), [Temporal Archimedea](https://wiki.warframe.com/w/Temporal_Archimedea), [Search Pulse](https://wiki.warframe.com/w/Search_Pulse), [Bird 3](https://wiki.warframe.com/w/Bird_3), [The Icebind](https://wiki.warframe.com/w/The_Icebind), [The Descendia](https://wiki.warframe.com/w/The_Descendia), [Simulacrum](https://wiki.warframe.com/w/Simulacrum), [Companion](https://wiki.warframe.com/w/Companion), [Huras Kubrow](https://wiki.warframe.com/w/Huras_Kubrow), [Tauron Strike](https://wiki.warframe.com/w/Tauron_Strike), [Focus/Vazarin](https://wiki.warframe.com/w/Focus/Vazarin), [Effects Scaling With Enemy Stats](https://wiki.warframe.com/w/Effects_Scaling_With_Enemy_Stats), [Update 31](https://wiki.warframe.com/w/Update_31) (introduction de l'Overguard), modules `Companions/data` et `DropTables/data`. Recherches sans résultat sur l'interaction % PV / Overguard : [vortexgaming.io](https://vortexgaming.io/en/postdetail/696494), [Steam](https://steamcommunity.com/app/230410/discussions/0/3826414483635039170), [forums Warframe](https://forums.warframe.com/topic/1450429-bad-game-design-overguard/).
- Wiki officiel : [Sevagoth/Prime](https://wiki.warframe.com/w/Sevagoth/Prime), [Sevagoth/Abilities](https://wiki.warframe.com/w/Sevagoth/Abilities), [Sevagoth/Patch History](https://wiki.warframe.com/w/Sevagoth/Patch_History), [Reap](https://wiki.warframe.com/w/Reap), [Sow](https://wiki.warframe.com/w/Sow), [Gloom](https://wiki.warframe.com/w/Gloom), [Exalted Shadow](https://wiki.warframe.com/w/Exalted_Shadow), [Death's Harvest](https://wiki.warframe.com/w/Death%27s_Harvest), [Shadow Haze](https://wiki.warframe.com/w/Shadow_Haze), [Dark Propagation](https://wiki.warframe.com/w/Dark_Propagation), [Shadow Claws](https://wiki.warframe.com/w/Shadow_Claws), [Exalted Weapon](https://wiki.warframe.com/w/Exalted_Weapon), [Enemy Level Scaling](https://wiki.warframe.com/w/Enemy_Level_Scaling), [The Steel Path](https://wiki.warframe.com/w/The_Steel_Path), [Overguard](https://wiki.warframe.com/w/Overguard), [Armor](https://wiki.warframe.com/w/Armor), [Archon Shard](https://wiki.warframe.com/w/Archon_Shard), [Helminth](https://wiki.warframe.com/w/Helminth), [Roar](https://wiki.warframe.com/w/Roar), [Ghost](https://wiki.warframe.com/w/Ghost), [Stalk](https://wiki.warframe.com/w/Stalk), [Blood Rush](https://wiki.warframe.com/w/Blood_Rush), [Melee Combo](https://wiki.warframe.com/w/Melee_Combo), [Damage Reduction](https://wiki.warframe.com/w/Damage_Reduction), [Update 38](https://wiki.warframe.com/w/Update_38) à [Update 44](https://wiki.warframe.com/w/Update_44), [Epoch Operation : Taubound](https://wiki.warframe.com/w/Epoch_Operation:_Taubound), modules Lua `Warframes/data`, `Weapons/data`, `Mods/data`, `Arcane/data`, `Stances/data`, `Enemies/data`, `DropTables/data`, `Version/data`.
- Patch notes officielles : [warframe.com, PSN](https://www.warframe.com/patch-notes/psn) (Hotfix 44.1.4 + 4.1, 28/10/2026) ; [RPG Site, sortie d'Iceblade of Narin sur toutes les plateformes](https://www.rpgsite.net/news/21459-warframe-iceblade-of-narin-update-download-free-login-bonus) ; [DE, How to Play Sevagoth](https://www.warframe.com/en/news/how-to-play-sevagoth) (24/11/2023).
- Communauté : [Ninjase, Gloom Reaper Sevagoth](https://overframe.gg/build/717054/sevagoth-prime/gloom-reaper-sevagoth-sp-general-use-nuke-crit-buff-slow-shadow/) (1 531 votes, mise à jour il y a ~10 mois) ; [copie de « Shadow Realm Sevagoth »](https://overframe.gg/build/885203/sevagoth-prime/shadow-realm-sevagoth-pure-nuke-oneshot-levelcap-variant/) (original : 536 votes) ; [RubyBlossom5, The Reaper's Bible](https://overframe.gg/build/874263/sevagoth-prime/go-to-sevagoth-shadow-claws-blossoming-death-in-depth-build/) (98 votes, 22/10/2026) ; [RubyBlossom5, A Ravenous Alliance](https://overframe.gg/build/874330/sevagoth-prime/a-ravenous-alliance-sevagoth-shadow-nuke-partners-roar-build-guide-and-variants/) (19 votes, ~2 mois) ; [gameplay.tips](https://gameplay.tips/guides/warframe-the-ultimate-sevagoth-guide.html) (29/09/2026) ; [togame.io](https://togame.io/a/warframe-sevagoth-prime-best-build-2026/) (non daté, faible confiance). Les vidéos YouTube citées n'ont pas été vues.
- Prix : [warframe.market](https://warframe.market) API v2, vendeurs en jeu, 29/10/2026.

*Hors sujet, une ligne :* un Sevagoth non-Prime peut porter F2 (Roar en 3) sans toucher au Roar en 4 de ton Prime.
