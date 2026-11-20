# GVH Diagonal Cubic — Feuille de route consolidée
**Version : ROADMAP-CHH-v2.0 — 18 novembre 2026**

## Règle fondamentale
La **Composition hétérodynamique hiérarchique (CHH)** décrit la constitution de cubes par des sous-cubes aux manifestations internes différentes. Elle **ne constitue pas** la dérivation de leurs équations du mouvement. Trois opérations indépendantes sont à distinguer :
1. **Composition CHH** : construire une représentation hiérarchique et préciser ce qu'elle conserve.
2. **Dérivation dynamique GVH** : dériver, lorsque possible, les équations à partir de l'action candidate, sans les présupposer.
3. **Inférence inverse** : reconstruire des composants ou propriétés cachés à partir d'observations et de lois physiques explicitement indiquées.

**Légende :** ✅ notebook/audit local réalisé ; 🟠 audit partiel ou verrou scientifique ouvert ; ☐ non réalisé. Une coche n'est jamais une validation expérimentale d'une nouvelle physique.

## Branche A — Composition hétérodynamique et agrégation
| État | Étape | Acquis vérifié ou limite |
|---|---|---|
| ✅ | CHH-01 — Définition des cubes hétérogènes | Définition de sous-cubes aux états et dynamiques différents ; tests algébriques de composition. |
| ✅ | CHH-02 — Conservation et agrégation | Bilans vérifiés dans les partitions testées ; information dynamique perdue si l'on réduit trop le système. |
| ✅ | CHH-03 — Dynamique interne et fréquences | Signatures fréquentielles internes masquées ou conservées selon les observables ; mélanges non linéaires ne prouvent pas un couplage. |
| ✅ | CHH-04 — Fermeture des modèles effectifs | Démonstration numérique de fermetures exactes ou impossibles selon les variables retenues, dans un modèle synthétique. |
| ☐ | CHH-04B — Robustesse multi-échelle | Refaire les comparaisons pour systèmes non linéaires, incertitudes, bruit et regroupements successifs ; comparer aux méthodes standard. |

## Branche B — Dérivation dynamique à partir de l'action GVH
| État | Étape | Acquis vérifié ou limite |
|---|---|---|
| 🟠 | CHH-05 — Couplage et EOM | Contrainte du trièdre et terme croisé de cisaillement étudiés ; interaction matérielle entre corps non dérivée. |
| 🟠 | CHH-06 — Source et unités SI | Secteur matière de contrôle ajouté ; échelles SI et observable spécifiquement GVH non déterminées indépendamment. |
| 🟠 | CHH-07 — Source et cisaillement non nul | Témoin vectoriel normalisé et équation scalaire contrôlée ; solution gravitationnelle complète non obtenue. |
| 🟠 | CHH-08 — Variation cubique restreinte | Équation variationnelle réduite avec ζ_C ≠ 0 calculée et testée ; EOM non restreintes/métrique encore ouvertes. |
| ☐ | CHH-09 — Variation non restreinte | Calculer et auditer la variation vectorielle et métrique complète, contraintes du trièdre et termes de bord. |
| ☐ | CHH-10 — Solution couplée | Chercher une solution non triviale satisfaisant simultanément métrique, vecteur, trièdre et matière, avec conditions aux limites. |
| ☐ | CHH-11 — Prédiction discriminante | Fixer indépendamment paramètres et échelles SI ; préenregistrer un observable distinct de la physique établie et tester hors échantillon. |

## Branche C — Inférence inverse de sous-cubes invisibles
| État | Étape | Acquis vérifié ou limite |
|---|---|---|
| ✅ | CHH-INVERSE-01 — Planète cachée | Corps simulé retrouvé grâce à la gravitation newtonienne, avec prédictions sur données simulées réservées et contrôle négatif. Pas une découverte réelle ni une prédiction nouvelle GVH. |
| ☐ | CHH-INVERSE-02 — Reconstruction récursive | Tester 0, 1 et plusieurs corps cachés, y compris un sous-cube composite dont une partie devient visible ; identifiabilité, critères de sélection et faux positifs. |
| ☐ | CHH-INVERSE-03 — Nature et activité interne | Après détection, inférer classe rocheuse/géante/etc. et activité interne seulement si les données additionnelles (rayon, densité, spectres, thermique, variabilité) le permettent ; probabilités et incertitudes. |
| ☐ | CHH-INVERSE-04 — Données indépendantes | Passer d'observations synthétiques à des observations astronomiques réelles, avec contrôle des modèles d'éphémérides, des biais et des données de validation. |

## Branche D — Observations ALMA (indépendante)
| État | Étape | Acquis vérifié ou limite |
|---|---|---|
| ✅ / à confirmer | GCOL-OBS-PATCH.10H.0 | Notebook de préparation et préenregistrement archivé : projet ALMA 2015.1.00147.S, source NGC 1333 IRAS 4A, ensembles X22/X24. Une vérification de fichiers archivée ne certifie pas la couche au premier plan. |
| ☐ | GCOL-OBS-PATCH.10H.1 | Géométrie du continuum, inscription des sources A1/A2, certification FITS/WCS et de l'axe spectral sans inspecter encore le signal de raie. |
| ☐ | Test ALMA préenregistré | Examiner les composantes spectrales dans les fenêtres figées : cœur 6,40–7,00 km/s ; premier plan 7,70–8,30 km/s ; ne pas réajuster les seuils après démasquage. |
| ☐ | Annexe ALMA–CHH | Analyse exploratoire des sous-systèmes, échanges et activité avec vérification contre modèles de transfert radiatif ; **GVH_USED = False** tant que les verrous ne sont pas franchis. |

## Apports conceptuels proposés par les nouvelles idées
| Idée GVH/CHH | Apport à notre programme | Statut vis-à-vis de la littérature et de la validation |
|---|---|---|
| **Hétérodynamique** | Composer des sous-cubes dont les phénomènes internes sont différents, sans les forcer à être identiques. | Formalisation interne ; notions voisines déjà présentes en modélisation multi-échelle et multiphysique. |
| **Activité interne** | Distinguer masse totale et circulation/transformations internes ; actif, dormant, relativement inactif au sens physique. | Démonstrations classiques sur modèles synthétiques ; indicateur universel non dérivé. |
| **Agrégation à information contrôlée** | Sélectionner les variables à conserver selon l'observable et quantifier la perte de fermeture ou d'énergie. | Tests locaux réussis ; avantage sur méthodes standard non démontré. |
| **Sous-cube caché composite** | Rechercher une structure non résolue, puis inférer récursivement les composants invisibles après détection partielle. | Hypothèse testable ; le protocole multi-corps reste à réaliser. |
| **Caractérisation physique du caché** | Aller de la détection de masse/orbite vers classe planétaire et activité sous observations supplémentaires. | À tester ; la gravité seule ne détermine généralement pas la géologie ni la composition. |
| **Séparation composition / dynamique / inférence** | Éviter de présenter une convention de regroupement comme une nouvelle loi gravitationnelle. | Règle méthodologique adoptée pour notre programme. |

## Critères permanents pour chaque notebook
**Niveau 1 — GVH :** hypothèse ou conséquence effectivement dérivée ; **Niveau 2 — physique établie :** référence indépendante ; **Niveau 3 — test numérique :** protocole reproductible, résultats réservés et incertitudes ; **Niveau 4 — verdict scientifique :** PASS local, BLOCKED, réfutation ou validation empirique selon la preuve.

Toujours signaler ce qui est **prescrit**, **dérivé**, **ajouté à l'action**, **mesuré**, **simulé** et **non identifié**. Pas de fréquences SI artificielles, pas de revendication de planète découverte à partir d'un test synthétique et pas de démasquage opportuniste des données ALMA.

## Situation au 18 novembre 2026
- **Neuf notebooks CHH/CHH-INVERSE exécutés** et retrouvés localement (CHH-01 à CHH-08 et CHH-INVERSE-01) avec certificats de résultats locaux. Les tests « PASS » attestent des contrôles définis pour ces modèles, **pas** de la validité physique universelle de GVH.
- **Un verrou théorique majeur :** variation complète et solution couplée de l'action candidate avec matière, cisaillement non nul et métrique dynamique.
- **Un verrou méthodologique majeur :** prouver une plus-value propre à la CHH par comparaison aveugle avec des méthodes de référence.
- **Un verrou observationnel :** confirmer les analyses de données indépendantes et maintenir séparés les tests ALMA préenregistrés.

## Ordre opérationnel recommandé
1. **CHH-INVERSE-02** : reconstruction récursive de deux ou plusieurs corps cachés, modèles nuls, bruit, multi-départs et données réservées.
2. **CHH-09**, en branche théorique parallèle : variations non restreintes de l'action, sans déclarer la fermeture avant preuve.
3. **ALMA PATCH.10H.1**, en branche observationnelle indépendante : préparer la géométrie et les axes, sans lire les amplitudes de raies prématurément.
4. **CHH-INVERSE-03** seulement après la démonstration d'identifiabilité du ou des corps ; utiliser des données non gravitationnelles pour classer leurs propriétés.
5. **CHH-10/11** si les EOM se ferment et si des observables discriminantes peuvent être définies.

**Verdict actuel :** cadre de recherche hiérarchique opérationnel, avec plusieurs audits mathématiques réussis et une inférence inverse synthétique concluante ; **pas encore de nouvelle loi GVH ou de nouvelle planète validée observationnellement.**