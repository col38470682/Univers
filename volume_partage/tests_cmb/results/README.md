# Résultats

Ce dossier contient les tableaux numériques, les statistiques et les résultats produits par les notebooks d'analyse du projet **tests_cmb** (voir `../notebooks/README.md` pour le détail du pipeline).

---

## Résumé exécutif

> **Conclusion générale :** aucune signature thermo-relationnelle cosmologique globale n'a été mise en évidence dans les deux catalogues étudiés.

Les corrélations initialement observées entre le gradient thermique du fond diffus cosmologique (`D_T`) et le redshift (`z`) sont entièrement expliquées par les propriétés géométriques et observationnelles des relevés utilisés, sans qu'il soit nécessaire d'invoquer un mécanisme physique reliant directement ces deux quantités.

---

## Tableau comparatif final

| Critère | Pantheon+ (SNe Ia) | SDSS DR16 (Quasars) |
|----------|--------------------|---------------------|
| **Taille de l'échantillon** | 1543 supernovae uniques (749 après sélection intermédiaire) | 50 000 quasars (49 702 après masque galactique) |
| **Carte CMB utilisée** | Planck Commander-Ruler (NSIDE=256) | Planck Commander-Ruler (NSIDE=256) |
| **Corrélation de Spearman (brute)** | −0.054 | −0.0238 |
| **p-value classique** | 0.140 | 9.85 × 10⁻⁸ |
| **Permutation naïve** | p ≈ 0.142 | p ≈ 0.0 |
| **Masque galactique** | appliqué | effet négligeable (99,4 % des objets déjà hors du plan galactique) |
| **Test méthodologique décisif** | Analyse de la couverture par quadrants RA | Permutation par blocs spatiaux (HEALPix NSIDE=8) |
| **Résultat du contrôle** | Forte concentration des observations dans un seul quadrant | Le signal devient compatible avec l'hypothèse nulle Permutation par blocs spatiaux :r = −0.0237 p = 0.671 |
| **Conclusion** | Biais de couverture du survey | Biais de sélection spatial et temporel du survey |

⸻

    ## Contenu du dossier

Fichier	Description
pantheon_df_real.csv	Catalogue Pantheon+ enrichi avec D_T, gal_l et gal_b.
pantheon_df_mid.csv	Sous-échantillon Pantheon+ utilisé pour les analyses intermédiaires.
pantheon_quadrant_table.csv	Répartition des supernovae par quadrant RA.
pantheon_permutation_results.csv	Résultats des permutations contrôlées sur Pantheon+.
sdss_qso_df.csv	Catalogue SDSS DR16 enrichi avec D_T, gal_l et gal_b.
sdss_qso_quadrant_table.csv	Répartition des quasars par quadrant RA.
sdss_qso_permutation_naive.csv	Résultats de la permutation globale des redshifts.
sdss_qso_permutation_blocks.csv	Résultats de la permutation par blocs spatiaux (HEALPix NSIDE=8).

⸻

    ## Interprétation statistique

1. Significativité statistique et taille d’effet

Une faible p-value ne signifie pas nécessairement qu’un effet est physiquement important.

Dans le catalogue SDSS (50 000 objets), une corrélation de Spearman de seulement −0.024 produit une p-value extrêmement faible en raison de la très grande taille de l’échantillon, alors que cette corrélation n’explique qu’une fraction négligeable de la variance du redshift.

⸻

2. Importance des contrôles méthodologiques

Les analyses montrent qu’une corrélation brute peut être entièrement induite par la géométrie d’observation d’un survey.

Le contrôle par permutation spatiale préserve les propriétés régionales du relevé tout en détruisant une éventuelle association physique locale.

Le fait que la corrélation disparaisse après ce contrôle indique qu’elle provient des caractéristiques observationnelles du survey et non d’une propriété cosmologique.

⸻

3. Pourquoi les deux catalogues conduisent-ils à des biais différents ?

Bien que Pantheon+ et SDSS DR16 conduisent tous deux à une conclusion négative, les mécanismes responsables diffèrent.

Pantheon+

* couverture du ciel fortement hétérogène ;
* observations concentrées dans quelques champs ciblés ;
* biais identifié par l’analyse des quadrants RA.

SDSS DR16

* couverture spatiale beaucoup plus homogène ;
* différentes générations du survey (SDSS-I/II, BOSS et eBOSS) ciblent des régions du ciel différentes selon le redshift ;
* biais identifié par la permutation par blocs spatiaux.

⸻

    ## Limites

Les conclusions présentées concernent exclusivement :

* les catalogues Pantheon+ et SDSS DR16 ;
* la carte Planck Commander-Ruler (NSIDE=256) ;
* la méthodologie étudiée.

Elles ne permettent pas d’exclure de manière générale toute hypothèse thermo-relationnelle cosmologique.

Elles montrent uniquement qu’aucune signature robuste n’a été détectée dans les jeux de données analysés après contrôle des principaux biais observationnels identifiés.

⸻

    ## Reproductibilité

Tous les résultats présentés dans ce dossier sont entièrement reproductibles à partir :

* des notebooks présents dans ../notebooks/ ;
* des données publiques référencées dans ../data/README.md.

Aucune donnée simulée n’a été utilisée au cours de cette étude.

⸻

    ## Conclusion

Cette campagne constitue une validation méthodologique importante du protocole d’analyse.

Elle montre qu’une corrélation statistiquement significative ne constitue pas, à elle seule, une preuve d’un mécanisme physique.

Les contrôles méthodologiques (masques, permutations et tests spatiaux) sont indispensables pour distinguer une véritable signature cosmologique d’un biais induit par la géométrie des relevés observationnels.
