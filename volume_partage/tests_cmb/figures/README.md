# Figures

Ce dossier contient les figures générées automatiquement par les notebooks d'analyse du projet **tests_cmb**.

Ces figures illustrent les différentes étapes de l'analyse statistique réalisée afin d'évaluer l'existence éventuelle d'une corrélation entre le gradient thermique du fond diffus cosmologique (CMB) et le redshift des objets cosmologiques.

Les résultats numériques correspondants sont résumés dans `../results/README.md`, tandis que le pipeline complet est documenté dans `../notebooks/README.md`.

---

## Liste des figures

| Figure | Description | Notebook source |
|:-------|:------------|:----------------|
| `fig01_cmb_gradient_mollview.png` | Projection Mollweide du gradient thermique du fond diffus cosmologique (Planck Commander-Ruler, NSIDE=256). Cette carte sert à calculer l'observable `D_T = \|∇T_{CMB}\|`. | `01_load_cmb_map.ipynb` |
| `fig02_pantheon_DT_vs_z_scatter.png` | Nuage de points représentant la relation entre `D_T` et le redshift pour l'échantillon Pantheon+. Le signal apparent est très faible. | `03_pantheon_tests.ipynb` |
| `fig03_pantheon_quadrant_barplot.png` | Répartition des supernovae Pantheon+ par quadrant d'ascension droite (RA). Cette figure met en évidence le biais de couverture du relevé. | `03_pantheon_tests.ipynb` |
| `fig04_pantheon_permutation_histogram.png` | Distribution des coefficients de Spearman obtenus après permutations contrôlées. Le coefficient observé est compatible avec l'hypothèse nulle. | `03_pantheon_tests.ipynb` |
| `fig05_sdss_DT_vs_z_scatter.png` | Nuage de points `D_T`–`z` pour les quasars SDSS DR16. Malgré une significativité statistique élevée, la taille d'effet reste extrêmement faible. | `05_sdss_qso_tests.ipynb` |
| `fig06_sdss_quadrant_barplot.png` | Répartition des quasars SDSS DR16 par quadrant RA. Cette figure illustre l'anisotropie propre au footprint observationnel du SDSS. | `05_sdss_qso_tests.ipynb` |
| `fig07_sdss_permutation_naive_histogram.png` | Distribution obtenue après permutation naïve des redshifts. Le coefficient observé paraît très significatif mais ce résultat est trompeur car il ne contrôle pas les biais spatiaux. | `05_sdss_qso_tests.ipynb` |
| `fig08_sdss_permutation_blocks_histogram.png` | Figure principale du projet. Distribution obtenue après permutation par blocs spatiaux (HEALPix NSIDE=8). Le coefficient observé devient compatible avec l'hypothèse nulle (`p = 0.671`). | `05_sdss_qso_tests.ipynb` |
| `fig09_comparison_summary.png` | Figure de synthèse comparant les résultats obtenus sur Pantheon+ et SDSS DR16 ainsi que les conclusions méthodologiques finales. | `06_comparison_summary.ipynb` |

---

## Convention de nommage

Toutes les figures suivent la convention suivante :

```text
figNN_<catalogue>_<contenu>.png
```

où :

- **fig** indique qu'il s'agit d'une figure produite automatiquement par le pipeline d'analyse ;
- **NN** est un numéro séquentiel à deux chiffres (`01`, `02`, `03`, ...) correspondant à l'ordre logique des analyses ;
- **catalogue** identifie le jeu de données principal :
  - `cmb` : carte du fond diffus cosmologique Planck ;
  - `pantheon` : catalogue Pantheon+SH0ES ;
  - `sdss` : catalogue Sloan Digital Sky Survey DR16 ;
  - `comparison` : comparaison finale entre plusieurs catalogues ;
- **contenu** décrit brièvement le type de figure (`gradient`, `scatter`, `quadrant`, `permutation`, `summary`, etc.).

### Exemples

```text
fig01_cmb_gradient_mollview.png
fig02_pantheon_DT_vs_z_scatter.png
fig03_pantheon_quadrant_barplot.png
fig04_pantheon_permutation_histogram.png
fig05_sdss_DT_vs_z_scatter.png
fig06_sdss_quadrant_barplot.png
fig07_sdss_permutation_naive_histogram.png
fig08_sdss_permutation_blocks_histogram.png
fig09_comparison_summary.png
```

Cette convention permet :

- de conserver un ordre logique identique à celui des notebooks ;
- de faciliter la navigation dans le dépôt GitHub ;
- de garantir une correspondance directe entre les figures, les résultats numériques et les notebooks ;
- de simplifier les citations dans les publications scientifiques ;
- d'assurer la reproductibilité complète du projet.

Toute nouvelle figure devra respecter cette convention.

---

## Figures clés

Parmi l'ensemble des figures produites, deux sont particulièrement importantes :

### Figure 04 — Pantheon+

Cette figure montre que la corrélation observée disparaît après application des contrôles méthodologiques appropriés. Le signal devient compatible avec les fluctuations attendues sous l'hypothèse nulle.

### Figure 08 — SDSS DR16

Cette figure constitue le résultat principal du projet.

La permutation par blocs spatiaux conserve la géométrie du relevé tout en supprimant l'association fine entre les objets et leurs redshifts. Le coefficient observé tombe alors au centre de la distribution nulle (`p = 0.671`), démontrant que le signal apparent provenait entièrement des biais de sélection du relevé.

Ces deux figures constituent le cœur de la validation méthodologique du projet.

---

## Reproductibilité

Toutes les figures de ce dossier peuvent être régénérées automatiquement en exécutant les notebooks présents dans le dossier `../notebooks/`.

Les figures sont produites directement à partir :

- de la carte Planck Commander-Ruler NSIDE=256 ;
- des catalogues Pantheon+SH0ES ;
- du catalogue Sloan Digital Sky Survey DR16.

Aucune figure n'a été modifiée manuellement après sa génération.

---

## Limites

Les figures présentées concernent uniquement :

- les catalogues Pantheon+SH0ES et SDSS DR16 ;
- la carte Planck Commander-Ruler NSIDE=256 ;
- la méthodologie statistique étudiée.

Elles ne permettent pas d'exclure de manière générale toute hypothèse thermo-relationnelle cosmologique.

Elles montrent uniquement qu'aucune signature robuste n'a été détectée dans les données étudiées après contrôle des principaux biais observationnels identifiés.

---

## Conclusion

Cette collection de figures documente l'ensemble de la démarche méthodologique ayant conduit à la conclusion principale du projet :

> **Les corrélations initialement observées entre le gradient thermique du fond diffus cosmologique et le redshift disparaissent après prise en compte des biais géométriques des relevés.**

Les figures constituent ainsi une archive visuelle complète, reproductible et directement reliée aux notebooks d'analyse et aux résultats numériques du projet.
