# GVH–CHH — Jupiter H0 : audit final (référence JPL)

## Statut

**PASS TECHNIQUE :** 11 vérifications sur 11, 12 ajustements sur 12 convergés. Le notebook archivé contient les sorties d'exécution. Il n'y a aucun corps caché ni équation originale GVH dans les modèles H0.

Verdict exact : `PASS_TECHNICAL_H0_FORCE_ABLATION__JPL_REFERENCE_ONLY__CHH_ORIGINALITY_OPEN`.

## Entrées et séparation

- Io, Europe, Ganymède, Callisto, Soleil ; chacun 97 époques JPL Horizons, grille commune 6 h (1–25 septembre 2026).
- Ajustement de l'état initial des cibles Io et Ganymède : 12 paramètres par modèle.
- Entraînement jusqu'au jour 10 ou jusqu'au jour 15 ; réserve commune des époques strictement après le jour 18, 24 époques.
- La référence est une **éphéméride numérique JPL**, pas une mesure astrométrique indépendante.

## Erreur RMSE_xyz sur réserve commune (km)

| Variante H0 | 10 jours d'entraînement | 15 jours d'entraînement |
|:---|---:|---:|
| KEPLER | 279.761463 | 244.575413 |
| J2_ONLY | 312.017766 | 266.903407 |
| MUTUAL_ONLY | 73.472518 | 61.267263 |
| J2_MUTUAL | 19.201090 | 13.170108 |
| J2_MUTUAL_SUN | 18.392036 | 13.176263 |
| J2_J4_J6_MUTUAL_SUN | 18.375196 | 13.160046 |

## Contrôles vrais dans le JSON final

`five_real_jpl_csv_exist`, `all_hashes_present`, `matching_time_grid`, `reserved_after_training`, `fixed_12_nuisance_states`, `no_hidden_bodies`, `no_gvh_or_alma`, `zonal_gradient_math`, `kepler_propagation_smoke`, `fit_convergence`, `expected_rows`.

## Lecture scientifique

L'ajout conjoint des interactions entre lunes et du terme J2 réduit fortement l'erreur prédictive par rapport au modèle képlérien. J2 seul n'apporte pas cette amélioration dans ce protocole de calibration : cela ne réfute évidemment pas l'aplatissement de Jupiter. Les différences de quelques mètres à dizaines de mètres entre les variantes riches ne sont pas validées observationnellement et peuvent dépendre de la fenêtre et des approximations.

Le Soleil est utilisé comme forçage externe issu des éphémérides, y compris sur la période réservée (`external_sun_forcing_uses_reserved_ephemerides=true`). Cela limite toute qualification de « prédiction complètement aveugle ».

## Provenance

- ZIP d'entrée SHA-256 : `8ab29522fd7001e3f03e6c02efda1de8d173abe635bdc69dc6a733af17bfdb2d` (102067 octets).
- ZIP de résultats SHA-256 : `52f1c63a0d5761091d1d0367bb77a406e04b51f0a8f40f091d84fddeaef486cf` (7404 octets).
- Le JSON du ZIP final porte les empreintes des cinq CSV et du JSON prédécesseur ; les fichiers sources sont conservés dans le ZIP d'entrée. Les réponses API JPL brutes ne sont pas incluses.

**Interdiction d'inférence :** ces résultats n'établissent ni supériorité CHH, ni nouvelles équations de mouvement GVH, ni existence d'un corps invisible.
