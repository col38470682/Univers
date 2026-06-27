# Notebooks d'analyse — Tests CMB

Ce dossier contient les notebooks d’analyse du projet tests_cmb, dont l’objectif est d’évaluer de manière reproductible et falsifiable l’hypothèse suivante :

L’expansion cosmologique observée pourrait être, au moins en partie, reliée à des gradients thermo-relationnels internes, caractérisés par l’intensité locale du gradient de température du fond diffus cosmologique (D_T = |∇T_{CMB}|), plutôt qu’exclusivement à une expansion globale de l’espace.

Deux catalogues cosmologiques indépendants ont été analysés :

* Pantheon+SH0ES (supernovae de type Ia)
* Sloan Digital Sky Survey DR16 (SDSS) (quasars)

Après application des différents contrôles méthodologiques, aucune corrélation robuste entre D_T et le redshift n’a été mise en évidence. Un résumé des résultats est disponible dans ../results/README.md.

⸻

## Liste des notebooks

| Notebook | Description |
|----------|-------------|
| 01_load_cmb_map.ipynb | Chargement de la carte CMB Planck et calcul du gradient thermique D_T. |
| 02_pantheon_pipeline.ipynb | Chargement de Pantheon+, conversion RA/DEC et association de D_T. |
| 03_pantheon_tests.ipynb | Corrélations, permutations, masque galactique, quadrants RA. |
| 04_sdss_qso_pipeline.ipynb | Téléchargement des quasars SDSS et association de D_T. |
| 05_sdss_qso_tests.ipynb | Corrélations, permutations, blocs spatiaux HEALPix. |
| 06_comparison_summary.ipynb | Comparaison finale et synthèse des résultats. |
⸻

Méthodologie commune

Les deux catalogues suivent exactement la même procédure d’analyse :

1. Calcul de l’observable D_T à partir de la carte CMB réelle (aucune simulation).
2. Calcul des corrélations brutes (D_T ↔ z) à l’aide des coefficients de Pearson et de Spearman.
3. Test de permutation naïf (mélange global des redshifts).
4. Application d’un masque galactique (|b| > 20°).
5. Contrôles des biais de sélection propres à chaque catalogue :

Pantheon+

* analyse de la densité par quadrants RA ;
* contrôle des tranches de redshift ;
* permutation contrôlée.

Ces analyses montrent que la distribution angulaire des observations explique le signal initial.

SDSS DR16

* analyse par quadrants RA ;
* permutation par blocs spatiaux HEALPix.

La permutation par blocs montre que la corrélation observée est entièrement compatible avec la géométrie du survey et sa stratégie de ciblage, sans nécessiter de relation physique entre D_T et le redshift.

⸻

Reproductibilité

Les analyses utilisent exclusivement des données publiques.

Jeux de données :

* Carte CMB Planck Commander-Ruler
    * NSIDE = 256
    * coordonnées galactiques
    * HEALPix NESTED
* Pantheon+SH0ES
* Sloan Digital Sky Survey DR16

Versions logicielles recommandées :

* Python 3.12
* NumPy
* pandas
* SciPy
* healpy
* astropy
* matplotlib

Toutes les analyses présentées reposent exclusivement sur des données observationnelles publiques. Aucune donnée simulée n’a été utilisée.

⸻

Limites

Les conclusions présentées concernent exclusivement les catalogues et la méthodologie étudiés.

L’absence de corrélation robuste entre le gradient thermique du CMB (D_T) et le redshift ne constitue pas une preuve générale contre toute hypothèse thermo-relationnelle. Elle montre uniquement qu’aucune signature robuste n’a été détectée dans les catalogues Pantheon+SH0ES et SDSS DR16 après contrôle des principaux biais observationnels identifiés.

Cette archive documente ainsi un résultat négatif reproductible, utile pour guider de futures investigations et éviter l’interprétation de corrélations induites par la géométrie des relevés.


---

Ce dossier documente l'ensemble du pipeline d'analyse utilisé dans cette étude. Les notebooks sont organisés dans l'ordre chronologique des traitements, depuis le chargement des données jusqu'à l'analyse statistique finale, afin de garantir la reproductibilité complète des résultats.
