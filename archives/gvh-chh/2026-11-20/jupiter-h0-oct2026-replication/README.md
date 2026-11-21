# GVH–CHH | Jupiter H0 : réplication temporelle indépendante (octobre 2026)

**Statut :** `PASS_TECHNICAL_OCT2026_TEMPORAL_REPLICATION__JPL_REFERENCE_ONLY__CHH_UNTESTED`.

Deux fichiers originaux, conservés sans modification :

1. `GVH_CHH_JUPITER_OCT2026_REPLICATION_RESULTS.zip` — 86 185 octets ; cinq CSV Horizons, cinq réponses API JSON brutes, provenance, résultats JSON, métriques, contrastes et empreintes.
2. `GVH_CHH_Jupiter_Horizons_H0_Independent_Oct2026_Temporal_Replication_Gate_FAST_CHH_PROTOCOL_v02.ipynb` — notebook Google Colab exécuté, avec protocole CHH non dérivé explicitement indiqué.

Les rapports ajoutés lors de l'archivage sont `AUDIT_FINAL.md`, `SHA256SUMS.txt` et `NEXT_STEP_MERCURY.md`.

## Expérience gelée

- Référence : NASA/JPL Horizons (éphémérides **calculées**, pas mesures astrométriques indépendantes).
- Dates : 1–25 octobre 2026, pas de 6 heures, 97 instants par corps, positions et vitesses ICRF, centre Jupiter.
- Cinq corps : Io, Europe, Ganymède, Callisto, Soleil ; cibles prédictives : Io et Ganymède.
- Deux fenêtres d'ajustement : jusqu'aux jours 10 et 15. Réserve commune : dates strictement après le jour 18.
- Six modèles H0 de physique classique : KEPLER, J2_ONLY, MUTUAL_ONLY, J2_MUTUAL, J2_MUTUAL_SUN, J2_J4_J6_MUTUAL_SUN.
- Douze paramètres d'état initial ajustés par modèle ; 12 ajustements/12 convergés ; 13 contrôles/13 réussis.
- Pas de satellite caché ; `GVH_USED=false`, `EOM_GVH=false`, `ALMA_USED=false`.

## Résultat principal — entraînement 15 jours

| Modèle | RMSE réservée (km) |
|---|---:|
| KEPLER | 283.314741 |
| J2_ONLY | 308.282020 |
| MUTUAL_ONLY | 60.691909 |
| J2_MUTUAL | **12.727171** |
| J2_MUTUAL_SUN | 13.196783 |
| J2_J4_J6_MUTUAL_SUN | 13.182342 |

Amélioration KEPLER → J2_MUTUAL : **95.51 %** de réduction RMSE sur cette réserve, sans démonstration d'originalité CHH.

Consulter `AUDIT_FINAL.md` pour le protocole complet et les limites.

## Protocole CHH non dérivé

Conformité documentaire : `GVH_CHH_PROTOCOL_FROZEN_v1.0`.
- `CHH-STRUCTURE` : composition hiérarchique sans dérivée globale intrinsèque.
- `AUX-DERIVATIVE` : calcul dérivé auxiliaire autorisé et étiqueté.
- `EOM-GVH` : variation d'action GVH distincte de la CHH.
- `KNOWN-PHYSICS` / `NUMERICAL-TEST` : lois et ajustements de cette étude.

**Limite :** toutes les comparaisons restent à l'intérieur d'une référence Horizons calculée. Le Soleil a un forçage externe connu jusque dans le segment réservé. Ni loi GVH nouvelle ni évidence empirique indépendante.
