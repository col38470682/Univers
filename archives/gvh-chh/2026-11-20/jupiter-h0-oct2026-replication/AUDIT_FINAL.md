# Jupiter H0 — audit final de réplication temporelle (octobre 2026)

## Validation technique

Le ZIP original a été ouvert sans erreur ZIP, les 11 empreintes SHA256 des entrées ont été recalculées et comparées au JSON final. Les cinq CSV comportent 97 lignes chacune avec la même grille temporelle, positions et vitesses. Le notebook exécuté contient `GVH_CHH_PROTOCOL_FROZEN_v1.0`, `CHH-STRUCTURE`, `AUX-DERIVATIVE`, `EOM-GVH`.

- Contrôles internes enregistrés : **13/13**.
- Ajustements signalés convergés : **12/12**.
- Époques : **2026-10-01 00:00 → 2026-10-25 00:00 TDB**, 6 h ; séparées des données septembre 2026.
- Réserve commune : jours **strictement postérieurs à 18**, 24 dates, Io et Ganymède.
- Statut : `PASS_TECHNICAL_OCT2026_TEMPORAL_REPLICATION__JPL_REFERENCE_ONLY__CHH_UNTESTED`.

## Erreur réservée RMSE_xyz (km)

| Modèle | Entraînement 10 jours | Entraînement 15 jours |
|---|---:|---:|
| KEPLER | 380.925921 | 283.314741 |
| J2_ONLY | 398.152325 | 308.282020 |
| MUTUAL_ONLY | 70.378803 | 60.691909 |
| J2_MUTUAL | **16.880924** | **12.727171** |
| J2_MUTUAL_SUN | 18.350936 | 13.196783 |
| J2_J4_J6_MUTUAL_SUN | 18.339090 | 13.182342 |

KEPLER → J2_MUTUAL : baisse RMSE de **95.568 %** (entraînement 10 jours), **95.508 %** (15 jours).

## Comparaison au contrôle septembre

Sur la réserve commune et 15 jours d'entraînement :
- Septembre 2026 : KEPLER **244.575413 km**, J2_MUTUAL **13.170108 km**.
- Octobre 2026 : KEPLER **283.314741 km**, J2_MUTUAL **12.727171 km**.

Le classement qualitatif se reproduit sur les deux périodes. Les petites différences entre les variantes sophistiquées ne constituent pas un résultat empirique discriminant.

## Distinctions et limites

1. Les entrées sont des éphémérides numériques de **JPL Horizons**, non des mesures instrumentales brutes indépendantes.
2. La période d'octobre est distincte de celle de septembre, mais l'évaluation reste **intra-période** : les états initiaux sont recalibrés en octobre ; ce n'est pas une propagation aveugle de paramètres figés en septembre.
3. Les modèles faisant appel au Soleil utilisent son éphéméride même après le début de la réserve (`external_sun_forcing_uses_reserved_ephemerides=true`), ce qui limite l'autonomie de la prédiction. La comparaison primaire KEPLER vs J2_MUTUAL n'utilise pas ce forçage.
4. Une convergence d'optimiseur et la réussite d'un test mathématique ne prouvent ni adéquation observationnelle fondamentale, ni nouvelle loi gravitationnelle.
5. `J2_ONLY` inférieur à KEPLER dans ce dispositif n'invalide pas l'aplatissement réel de Jupiter ; les interactions manquantes et l'optimisation conditionnent la comparaison.
6. CHH n'a pas de dérivée globale intrinsèque. Les équations de mouvement H0 restent celles de la physique connue, et les dérivées éventuellement utilisées sont auxiliaires.

## Provenance

- Archive ZIP : `4957c18459e95e1a609209fa882a4960adfa4e21c567148a0b2bda1a1f4ab2f0` SHA-256.
- Notebook Colab exécuté : `56933f5206c54169e63b7bb9e2503420e337bba789bfa38955662ac40a78ee17` SHA-256.
- Les cinq réponses brutes à l'API JPL et les onze empreintes des fichiers d'entrée sont intégrées au ZIP.
- Source originale Drive : `GVH_CHH_Jupiter_Archives/GVH_CHH_JUPITER_OCT2026_REPLICATION_RESULTS.zip`.

**Verdict :** réplication numérique H0 franchie ; validation physique indépendante et originalité CHH/GVH restent ouvertes.
