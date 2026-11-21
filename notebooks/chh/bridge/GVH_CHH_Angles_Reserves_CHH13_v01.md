# Pont CHH → GVH · Test aux angles réservés

**Statut scientifique** · Vérification synthétique du secteur linéarisé CHH‑13 à métrique fixée.

## 1. Composition CHH

L’observable est la moyenne locale de β sur le demi-domaine périodique [−π/2, π/2]. La condition initiale est β = 0 et ∂β/∂t = cos x. La description conserve l’amplitude du mode et l’orientation relative α du trièdre.

## 2. Modèles comparés

La branche candidate engendre les signaux avec q(α) = cβ²(α) = 0,6791666667 + 0,0625 sin²(2α). La moyenne locale est (2/π) sin(√q t)/√q. L’amplitude initiale de vitesse est fixée à 1.

Les trois modèles ajustés utilisent uniquement les séries à 0° et 45°. Les deux lois angulaires interpolent les valeurs ajustées de q à ces angles. Leurs poids sont respectivement sin²(2α) et 2 sin²(α). Le témoin isotrope ajuste une seule valeur commune de q aux deux séries. Aucun paramètre n’est recalibré aux angles réservés.

## 3. Test numérique

200 répétitions, 81 points par série de t = 0 à t = 8, pas 0,1. Bruit gaussien indépendant d’écart-type 0,02 en unités du modèle. Ajustement par moindres carrés sur une grille de q de 0,65 à 0,79 par pas de 0,0001. Graine initiale 20261122, générateur congruentiel 32 bits et transformation de Box–Muller.

| Angle réservé | RMSE GVH | RMSE loi alternative | RMSE isotrope |
|---:|---:|---:|---:|
| 11,25° | 0,020253 | 0,021606 | 0,041700 |
| 22,50° | 0,020100 | 0,029494 | 0,020119 |
| 33,75° | 0,020015 | 0,031653 | 0,042831 |

La RMSE regroupe les points temporels et les répétitions. Sur les trois angles réunis, la loi GVH donne la plus faible erreur dans les 200 répétitions.

## 4. Verdict et portée

La forme angulaire utilisée pour générer les signaux est retrouvée hors des angles de calibration. Dans ce secteur, l’orientation relative fournit une information prédictive sur la moyenne locale. Le test porte sur des signaux synthétiques produits par la branche candidate. La robustesse aux non-linéarités et la validation sur des observations indépendantes restent ouvertes.
