# CHH-COMP-01 · Deux niveaux avec un budget de mesures égal

**Statut scientifique** · Contrôle analytique de propagation du bruit.

## 1. Structure CHH

Ce test prolonge le [contrôle d’identifiabilité](./CHH_COMP_01_Deux_Niveaux_Identifiabilite_v01.md). Les séparations internes sont fixées ici à 1 m pour A et 3 m pour B. Les totaux de groupe sont supposés exacts. Chaque stratégie reçoit deux mesures de moment. Leurs erreurs sont centrées, indépendantes et de même écart-type, 0,20 kg·m.

## 2. Physique de référence

L’erreur sur chaque masse d’un groupe est, au signe près, l’erreur sur son moment divisée par sa séparation interne. Un moment obtenu par différence de deux mesures indépendantes a une variance égale à la somme des deux variances.

## 3. Test analytique

La RMSE sur les quatre masses vaut la racine de la moyenne de leurs erreurs quadratiques attendues. Avec des séparations d_A et d_B, et une variance s² par mesure, sa valeur au carré est s²(u_A/d_A² + u_B/d_B²)/2. Le facteur u vaut 1 pour un moment mesuré directement et 2 pour un moment obtenu par différence.

| Mesures | u_A | u_B | RMSE |
|---|---:|---:|---:|
| Moment global et moment de B | 2 | 1 | 0,205 kg |
| Moment global et moment de A | 1 | 2 | 0,156 kg |
| Moments locaux de A et B | 1 | 1 | 0,149 kg |

## 4. Verdict

Si le moment global est imposé, mesurer directement le moment du groupe A réduit la RMSE d’environ 24 % par rapport à la mesure directe de B. Lorsque les deux moments locaux sont accessibles avec le même bruit et au même coût, cette option minimise la RMSE parmi les stratégies comparées. Une agrégation classique disposant des mêmes mesures donne le même résultat. La comparaison repose sur le modèle d’erreur déclaré et reste analytique.
