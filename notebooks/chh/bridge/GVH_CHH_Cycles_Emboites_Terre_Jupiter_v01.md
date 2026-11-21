# CHH → GVH · Cycles emboîtés et contrôles orbitaux

Date de synthèse · 21 novembre 2026

## 1. Structure CHH

Le système Soleil–Terre reçoit l’état de ses constituants et l’influence des niveaux englobants. Chaque retour conserve la phase terrestre, le numéro du tour, la configuration planétaire et, si l’on simule une image, les axes de l’observateur. La phase est la fraction d’un tour modulo 1. Le numéro de tour et la phase continue permettent de suivre un décalage accumulé.

## 2. Physique établie

Pour r = x_Terre − x_Soleil et R_J = x_Jupiter − x_Soleil, l’accélération relative due à Jupiter est

`Δa_J = GM_J [(R_J − r)/|R_J − r|³ − R_J/|R_J|³]`.

Le calcul newtonien direct intègre les trois corps en coordonnées inertielles. La formulation par niveaux intègre les positions relatives au Soleil. La marée galactique est l’approximation locale de l’accélération galactique différentielle. Dans une image de face, centrée sur le Soleil, un axe d’image tournant d’un angle ψ donne θ_apparente = θ_orbitale − ψ. Une translation commune s’élimine dans cette configuration à axes fixes.

## 3. Contrôles numériques

### Soleil–Terre–Jupiter

Scénario synthétique coplanaire, en UA et années juliennes. G M_Soleil = 4π² dans ces unités. Rapports de masse Terre/Soleil = 3,003 × 10⁻⁶ et Jupiter/Soleil = 9,5459 × 10⁻⁴. Terre initialement au périhélie à 0,9833 UA, avec demi-grand axe initial de 1 UA dans le témoin à deux corps. Jupiter démarre à 5,2 UA avec vitesse tangentielle circulaire dans le témoin Soleil–Jupiter. Un retour est le franchissement de y = 0 avec x > 0 et vitesse verticale positive dans le plan.

À l’alignement initial de 0°, le modèle avec Jupiter avance le 12ᵉ retour de 5 125,53 s et augmente la distance héliocentrique au retour de 18,33 km par rapport au modèle sans Jupiter. Les formulations directe et relative concordent à 7,9 µs et 2,6 mm sur les 12 retours dans le contrôle RK4. Le témoin sans Jupiter retrouve la période képlérienne de 365,24945158 jours pour ces paramètres.

| Ordre de l’expansion de l’accélération différentielle de Jupiter à 0° | RMSE temps | RMSE distance |
|---:|---:|---:|
| 1 | 1 042,81 s | 2 841,30 km |
| 2 | 120,09 s | 66,82 km |
| 3 | 37,33 s | 90,82 km |
| 4 | 4,33 s | 2,30 km |

Les ordres désignent les puissances de la séparation Terre–Soleil dans l’expansion newtonienne.

| Alignement initial | RMSE temps, ordre 4 | Max. temps | RMSE distance, ordre 4 | Max. distance |
|---:|---:|---:|---:|---:|
| 0° | 4,33 s | 7,11 s | 2,30 km | 5,17 km |
| 90° | 5,59 s | 8,81 s | 2,72 km | 6,15 km |
| 180° | 1,90 s | 2,95 s | 5,05 km | 6,69 km |
| 270° | 5,25 s | 8,81 s | 2,72 km | 6,13 km |

### Observation extérieure et marée galactique

Au 12ᵉ retour, une translation commune produit zéro décalage dans la géométrie d’image retenue. Une rotation opposée des axes d’image, à la cadence illustrative d’un cycle en 230 millions d’années, produit une avance apparente de 1,592 s sur la même trajectoire. Une marée galactique coplanaire simplifiée à courbe de rotation plate, évaluée par réponse orbitale au premier ordre, produit une avance dynamique d’environ 9,75 ns. Ces deux nombres sont des résultats de scénarios prescrits.

## 4. Portée et comparaison GVH

La composition CHH par niveaux récupère le résultat newtonien pour la perturbation différentielle exacte. Dans la branche centrale statique alignée (audits 28.5–28.6), le cisaillement s’annule, le potentiel faible est −G_N M/r et β_PPN = γ_PPN = 1. Avec les mêmes paramètres centraux, la relativité générale à 1PN et les deux variantes de l’action candidate, avec et sans opérateur cubique, donnent la même avance du périhélie terrestre de 0,03839″ par orbite pour a = 1 UA et e = 0,0167. Cette avance du périhélie est une observable distincte du retour dans une direction fixe.

Point de reprise · Dériver la réponse du secteur directionnel de l’action candidate aux sources mobiles. Calculer ensuite les mêmes 12 retours et distances dans un repère et avec des conditions initiales communs pour la référence relativiste et les variantes GVH avec et sans l’opérateur cubique. La correction orbitale propre à GVH dans le système à trois corps et sa validation observationnelle restent ouvertes.
