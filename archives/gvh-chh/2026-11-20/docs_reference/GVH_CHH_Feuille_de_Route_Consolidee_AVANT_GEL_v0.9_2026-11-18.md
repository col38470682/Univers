# GVH Diagonal Cubic — Feuille de route de consolidation et de recherche

**Version :** `GVH_CHH_ROADMAP_PRE_FREEZE_v0.9`  
**État :** **PROPOSITION NON GELÉE — validation de l'auteur requise**  
**Date de référence :** 18 novembre 2026  
**Sources exclusives pour les priorités et statuts :**
1. `GVH_CHH_Registre_Consolide_AVANT_GEL_2026-11-18.md` ;
2. `GVH_CHH_Checklist_PreGel_2026-11-18.json`.

> **Portée.** Ce document organise les recherches déjà engagées. Il ne réinterprète pas les hypothèses ouvertes comme des faits physiques établis et ne modifie pas `GVH_CHH_PROTOCOL_FROZEN_v1.0`. L'addendum v1.1 sera créé **uniquement après approbation explicite**.

## I. Destination scientifique

**Objectif général :** formaliser une composition hiérarchique de sous-systèmes hétérogènes, rechercher des méthodes de reconstruction identifiables et, séparément, tester l'existence éventuelle d'une dynamique GVH nouvelle, stable et empiriquement discriminante.

**Règle non négociable :**

\[
C_{S,\ell}=\mathcal A_{\ell,\tau}(\{C_i,D_i\},\{I_{ij}\};\boldsymbol\theta_\tau)
\]

La CHH est une **composition**, pas une source intrinsèque de dérivée globale ou d'équations du mouvement. Chaque sous-cube conserve ses manifestations, lois, paramètres et possibilités de composition interne. Les opérations de composition dépendent de l'observable et des contraintes physiques. Toute dérivée auxiliaire est étiquetée `AUX-DERIVATIVE` ; toute dynamique dérivée d'une action GVH est étiquetée `EOM-GVH` et relève d'un chantier distinct.

**Étiquettes obligatoires dans les notebooks :** `CHH-STRUCTURE`, `AUX-DERIVATIVE`, `EOM-GVH`, `INVERSE-INFERENCE`, `NEW-HYPOTHESIS`, `EMPIRICAL-TEST`, avec séparation stricte de : *physique établie*, *conséquence dérivée de l'action*, *hypothèse proposée*, *paramètre prescrit*, *paramètre ajusté*, *mesure observée* et *statut de validation*.

## II. Point de départ certifié

La checklist d'origine contient **9 certificats**, avec **367/367 contrôles rapportés réussis** : CHH-09 (30), CHH-10 (36), CHH-11 (96), CHH-12 (45), CHH-13 (65), ROOT22 algèbre (16), ROOT22 orbites (41), INVERSE-02B (16), INVERSE-03 (22). Leur présence et leur empreinte SHA-256 ont été vérifiées pour cette feuille de route. **Ces contrôles sont des audits de calcul, non une validation empirique d'une nouvelle loi.**

**Acquis utilisables, sans les recommencer inutilement :** CHH-01 à 13 selon leurs portées respectives ; inférences synthétiques INVERSE-01/02/02B/03 ; provenance exacte de `√22` dans G284 ; préenregistrement ALMA `PATCH.10H.0` ; protocole méthodologique v1.0 déjà archivé.

**Limites à ne pas effacer :** branches nulle/maximale du trièdre et redondance potentielle Einstein-æther ; calculs CHH-12/13 avec métrique fixée ; obstacles de signe cinétique et de dispersion autour du témoin G284 comportant `√22` ; premier test inter-orbites ROOT22 non concluant sur l'universalité ; aucune prédiction GVH nouvelle validée sur des données réelles.

## III. Vue d'ensemble des six phases

| Phase | Objet | Priorité / dépendance | Produit de sortie | Condition de passage |
|---|---|---|---|---|
| **P0** | Confirmer quatre décisions conceptuelles et figer la méthode | **Immédiate** ; approbation de l'auteur | Addendum `v1.1` + registre de paramètres/versions, uniquement après accord | Accord explicite sur G1–G4 ci-dessous |
| **P1** | Spécifier l'algèbre de composition par observable | Après P0, ou exploration provisoire sous étiquette brouillon | `CHH-COMP-01` : opérations, unités, symétries, modèles rivaux | Modèles définis avant ajustement ; aucune équation globale CHH imposée |
| **P2** | Auditer la branche dynamique métrique–vecteur–trièdre | Peut démarrer en parallèle de P1 | `CHH-14`, puis audit d'équivalence et système couplé | Contraintes/cohérence/stabilité vérifiées ou échec explicitement conservé |
| **P3** | Traiter `√22` comme piste physique dérivable | En parallèle, mais test empirique bloqué par preuve de santé et prédiction | `ROOT22-HEALTH`, puis `ROOT22-PREDICTION` | Pas de coefficient libre absorbant la racine ; observable fixé avant données |
| **P4** | Effectuer validations indépendantes | ALMA et inférence réelle indépendantes de P2/P3 ; test **GVH** attend P2/P3 | `INVERSE-03B`, `ALMA PATCH.10H.1`, tests réservés | Critères de qualité, provenance, prédiction et contrôle de biais respectés |
| **P5** | Arbitrage scientifique et consolidation | Après les audits concernés | Tableau des résultats, échecs et décisions de poursuite | Récit scientifique différenciant calcul, méthode, physique et observation |

**P0 est un verrou de gouvernance**, et non une preuve physique ; P1–P4 comprennent des sous-projets **parallélisables**. On ne doit pas suspendre les observations ALMA parce que le modèle dynamique GVH reste ouvert.

## IV. P0 — Validation avant gel

Quatre décisions **G1–G4**, directement issues de la section G du registre, nécessitent l'accord de l'auteur :

- **G1 / CHH :** composition seulement ; aucune EOM ni dérivée globale imposée *par la seule CHH* ; maintien des dynamiques propres aux sous-cubes.
- **G2 / opérations :** choix additif, multiplicatif, inverse ou interactif conditionné par la grandeur, les unités et les lois pertinentes ; pas d'ajustement opportuniste a posteriori.
- **G3 / `√22` :** résultat algébrique exact archivé, hypothèse de rôle physique ouverte ; ni « constante universelle mesurée » ni piste définitivement abandonnée.
- **G4 / architecture :** `CHH-STRUCTURE`, `EOM-GVH`, `INVERSE-INFERENCE` et `AUX-DERIVATIVE` restent distincts et reliés uniquement par des hypothèses explicites.

**Livrables après approbation, pas avant :**
1. `GVH_CHH_PROTOCOL_FROZEN_v1.1_ADDENDUM` avec date, rédacteur, SHA-256, changement par rapport à v1.0.
2. `GVH_CHH_Parameter_and_Formula_Register_v1.1` distinguant coefficients prescrits, dérivés, inférés, mesurés et libres.
3. `GVH_CHH_Roadmap_v1.0` (promotion du présent brouillon), copie non modifiable de l'ancien registre et historique des décisions.

**Si l'une des quatre décisions est refusée :** laisser l'état `NON GELÉ`, corriger uniquement la proposition, sans écraser la source.

## V. Quatre chantiers scientifiques parallèles

### A — CHH : composition conditionnelle et inférence

**A1 — `GVH_CHH_Conditional_Composition_and_Coefficient_Identifiability_Gate_FAST`**  
*Nature :* `CHH-STRUCTURE` + `INVERSE-INFERENCE`.  
*Entrées :* principes A1–A5/B1–B3 du registre, acquis CHH-01/04.  
*Opérations candidates :* somme, produits, inverses et couplages ; toutes dimensionnellement cohérentes, définies **avant** l'ajustement.  
*Tests minimaux :* Jacobien/rang, symétries de reparamétrisation, équivalence des modèles (`Y=A√22` contre `Y=B`), bruit, manquants, contrôles négatifs, validation par système **entier** réservé.  
*Sortie :* répertoire des conditions sous lesquelles les propriétés individuelles sont (ou ne sont pas) identifiables.  
*Échec utile :* montrer une dégénérescence plutôt que « retrouver exactement » les sous-cubes en réinjectant leur valeur dans les coefficients.

**A2 — `GVH_CHH_INVERSE_03B_Real_Catalog_SelectionBias_and_Calibration_Gate_FAST`**  
*Nature :* `INVERSE-INFERENCE` + `EMPIRICAL-TEST`.  
*Entrées :* INVERSE-01/02/02B/03, protocole A1.  
*Tests :* observations astronomiques réelles indépendantes ; incertitudes, sélection du catalogue, caractéristiques réellement disponibles, comparaison à des méthodes établies, séparation entraînement/validation/test par corps ou système.  
*Sortie :* performances calibrées, cas non identifiables et bilan de généralisation.  
*Limite :* un succès d'inférence fondé sur Newton ou des relations empiriques usuelles **ne confirme pas une nouvelle gravitation GVH**.

**A3 — `GVH_CHH_Recursive_Subcube_Real_Data_Stress_Gate_FAST`**  
*Précondition :* A2 montre une capacité de reconstruction réellement vérifiable.  
*Tests :* sous-cubes non résolus, détection progressive, séparation d'un composite et mises à jour de résidus ; analyse d'incertitude et alternatives classiques.  
*Sortie :* conditions de résolution hiérarchique et diagnostic des échecs.

### B — GVH dynamique : cohérence physique

**B1 — `GVH_CHH_14_Full_Metric_Spin_Principal_Symbol_and_Dirac_Constraints_GATE_FAST`**  
*Nature :* `EOM-GVH` + `NEW-HYPOTHESIS`. **Priorité scientifique élevée.**  
*Entrées :* CHH-09/10/11, extension explicitement hypothétique CHH-12/13.  
*Mission :* faire varier, sans fixer arbitrairement la métrique pour conclure au système complet, les champs métrique–vecteur–trièdre ; reconstruire contraintes de normalisation/orthonormalité, variables de jauge, symbole principal, degrés de liberté et signes cinétiques.  
*Contrôles :* réduction sur fond plat, limite Einstein-æther, invariance de coordonnées et transformations internes correctement identifiées, vérifications indépendantes par jets/variations ou autre route.  
*Sortie :* classification explicite `PASS`, `FAIL` ou `INCONCLUSIVE` par secteur ; un audit partiel **ne sera pas nommé « solution couplée complète »**.

**B2 — `GVH_CHH_Dynamical_Triad_Spinning_Aether_Operator_Equivalence_Gate_FAST`**  
*Précondition :* expression non ambiguë de l'action de B1.  
*Mission :* comparer les opérateurs temporels/spatiaux du trièdre avec les théories de trièdres dynamiques (dont le spinning æther) ; tests de redéfinitions, intégrations par parties, contraintes et équivalences sur coquille et hors coquille.  
*Sortie :* matrice `déjà connu / potentiellement indépendant / non résolu`, sans revendiquer d'originalité sur la seule différence de notation.

**B3 — `GVH_CHH_Coupled_Source_Boundary_and_SI_Observable_Gate_FAST`**  
*Préconditions :* au moins une branche B1/B2 mathématiquement admissible.  
*Mission :* chercher une solution avec matière, conditions aux limites, échelles SI et paramètres fixés indépendamment ; établir un observable différent de la physique de référence.  
*Sortie :* prédiction chiffrée préenregistrable et intervalle d'incertitude, ou constat documenté d'absence de branche admissible.

### C — Racine `√22` : santé, puis prédiction indépendante

**C1 — `GVH_ROOT22_Healthy_Branch_and_Independent_Prediction_Gate_FAST`**  
*Nature :* `NEW-HYPOTHESIS` + audit `EOM-GVH`, **pas de constante universelle présupposée**.  
*Origine conservée :* `c2=(√22−4)/9`, `ω²_+/κ²=(√22−2)/9`, issus d'une chaîne G284 commune.  
*Verrous reconnus :* témoin exact en échec de santé quadratique réduite ; mode avec `(2−√22)/9<0` dans un autre audit réduit ; ils n'impliquent pas un no-go universel.  
*Travail :* revenir au polynôme, au déterminant/symbole et aux contraintes ; tester d'autres branches admissibles sans extrapoler hors de sa tranche la surface historique `F(c2,c14)=0`.  
*Sortie :* `HEALTHY_CANDIDATE`, `NO_HEALTHY_WITNESS_IN_TESTED_DOMAIN` ou `INCONCLUSIVE`, avec hypothèses et domaine exacts.

**C2 — `GVH_ROOT22_NonAbsorbable_Dimensionless_Prediction_Gate_FAST`**  
*Précondition :* C1 produit une branche admissible et la prédiction découle d'une dynamique spécifiée.  
*Travail :* choisir **avant de consulter le jeu de test** un invariant sans dimension qui pourrait dépendre de `√22`, vérifier l'absence de facteur libre équivalent à un changement de normalisation, préciser le signe et les corrections attendues.  
*Sortie :* observable, domaine, incertitude et critère discriminant préenregistrés ; si la racine s'absorbe dans un paramètre libre, déclarer `NON_IDENTIFIABLE`.

**C3 — `GVH_ROOT22_Independent_System_Blind_Validation_Gate_FAST`**  
*Préconditions :* C2 et observations indépendantes sélectionnées avant ajustement.  
*Travail :* test hors échantillon face à GR/Einstein-æther/modèles rivaux, avec contrôle négatif et sensibilité aux erreurs de catalogue.  
*Sortie :* résultat de test, y compris négatif. Ne pas recycler les 20 orbites du premier audit comme une validation entièrement nouvelle.

### D — Observations et données réelles, avec indépendance stricte

**D1 — `GCOL-OBS-0.3.2.1.1-PATCH.10H.1`**  
*Nature :* `EMPIRICAL-TEST`, **indépendant de la validation GVH**.  
*Mission :* continuum seul pour la géométrie des sources A1/A2, provenance FITS/WCS, certification des axes et des découpes déterministes pour NGC 1333 IRAS 4A, projet ALMA 2015.1.00147.S, ensembles X22/X24.  
*Interdit :* inspecter/retuner le signal de raie avant l'étape de démasquage ; modifier les fenêtres figées **6,40–7,00 km/s** (cœur) et **7,70–8,30 km/s** (premier plan). `GVH_USED=False`.  
*Sortie :* certificat des métadonnées, géométrie et préenregistrement immuable.

**D2 — `GCOL-OBS_PreRegistered_Foreground_Test`**  
*Précondition :* D1 et provenance/certification satisfaisantes.  
*Travail :* ouvrir seulement alors les signaux dans les fenêtres figées, conserver seuils et contrôles négatifs, évaluer sensibilité et incertitude.  
*Sortie :* résultat astrophysique indépendant ; même positif, **pas validation automatique de GVH**.

**D3 — `GVH_CHH_ALMA_Exploratory_Appendix_Only`**  
*Condition :* D2 archivé ; aucune réinterprétation rétroactive du test aveugle.  
*Travail :* étude **exploratoire** des composantes CHH, signalée comme telle ; la vérification GVH exige un nouveau protocole distinct.  
*Sortie :* hypothèses futures, non une confirmation post hoc.

## VI. Arbre de dépendances (exécutable comme ordre logique)

```text
P0 : approbation de G1–G4 ──► addendum v1.1 figé
  │
  ├─► A1 composition/identifiabilité ─► A2 inférence réelle ─► A3 reconstruction récursive
  │
  ├─► B1 CHH-14 contraintes/symbole ─► B2 équivalences ─► B3 solution + observable SI
  │
  ├─► C1 santé de la branche √22 ─────────► C2 observable non absorbable ─► C3 test aveugle
  │
  └─► D1 ALMA PATCH.10H.1 ─► D2 test ALMA figé ─► D3 annexe exploratoire

P5 : synthèse et arbitrage de chaque branche ; aucun succès ne se transmet automatiquement.
```

*Remarque :* D1, et une exploration pré-gel correctement étiquetée, peuvent avancer sans attendre la résolution gravitationnelle B3. Les nouveaux résultats doivent être intégrés par révision datée, jamais par remplacement silencieux d'un ancien verdict.

## VII. Critères uniformes de qualité (« gates »)

Chaque notebook futur doit comporter :

1. **Identité et provenance :** identifiant/version, liens vers les résultats amont, SHA-256 de l'entrée, environnement logiciel et graine numérique lorsque pertinente.
2. **Contrat de variables :** unités, observables, paramètres fixes/libres, domaine de validité, conditions aux limites, statut `CHH-STRUCTURE`/`EOM-GVH`/etc.
3. **Quatre niveaux :** (I) hypothèse GVH/CHH ; (II) physique connue ; (III) essais minimaux reproductibles ; (IV) verdict scientifique sans extrapolation.
4. **Comparateurs :** méthode physique classique, modèle nul et contrôles négatifs ; même budget de paramètres et jeu de données si comparaison statistique.
5. **Identifiabilité et robustesse :** rang, dimensions, invariances, paramètres non identifiables, bruit, incertitudes et cas d'échec.
6. **Séparation des données :** apprentissage, calibration, test réservés par système lorsque nécessaire ; aucun déplacement de seuil après inspection.
7. **Livrables auditables :** `.ipynb` exécuté, `.json` résultats, manifeste SHA-256, décision `PASS/FAIL/INCONCLUSIVE`, point d'arrêt et étape suivante.
8. **Interdiction de transfert de preuve :** réussite d'une simulation ou d'une étude ALMA indépendante ≠ validation d'une nouvelle gravitation GVH.

## VIII. Registre des 12 briques P01–P12 et responsabilités du plan

| Brique du registre | Statut retenu | Phase/chantier où elle est traitée |
|---|---|---|
| P01 — CHH non dérivative | Prête à approuver | P0 / G1 |
| P02 — sous-cubes hétérogènes | Prête à approuver | P0 / G1 ; A1 |
| P03 — opérations conditionnelles | Prête sous réserve | P0 / G2 ; A1 |
| P04 — calcul différentiel auxiliaire | Prête à approuver | P0 / G1 ; tous notebooks |
| P05 — coefficients et identifiabilité | Hypothèse à tester | A1–A3 |
| P06 — `√22` et ses limites | Algèbre documentée ; physique ouverte | P0 / G3 ; C1–C3 |
| P07 — séparation CHH/EOM/inférence | Prête à approuver | P0 / G4 ; tous notebooks |
| P08 — trièdre et action étendue | Réduit testé, complet ouvert | B1–B3 |
| P09 — observable nouvelle et SI | Manquante | B3, C2–C3 |
| P10 — données réelles | Non clos | A2, D1–D2, C3 sous condition |
| P11 — audits à quatre niveaux | Prête à approuver | P0 ; tous notebooks |
| P12 — versionnement/contradictions | Prête à approuver | P0 ; P5 |

## IX. Priorités opérationnelles immédiates

**Premier acte administratif :** l'auteur examine G1–G4 du § IV et approuve, modifie ou rejette chacune. Aucun addendum v1.1 n'est présumé approuvé.

**Première exécution scientifique conseillée après validation (ou comme brouillon explicitement non gelé) :** **A1** `GVH_CHH_Conditional_Composition_and_Coefficient_Identifiability_Gate_FAST`. C'est le chantier qui traduit directement les nouvelles idées du dialogue sans confondre CHH et variation de l'action.

**En parallèle, selon les fichiers et ressources disponibles :** B1 `CHH-14` pour l'action dynamique, C1 audit de santé `√22`, D1 ALMA `PATCH.10H.1` sans signal de raie. Ces chantiers sont distincts et ne doivent pas se bloquer mutuellement.

**Si l'auteur préfère maintenir la priorité gravitationnelle :** commencer par B1 et maintenir A1 dans la première vague. Le registre ne fixe pas d'ordre exclusif entre A1 et B1.

## X. Politique de résultats négatifs et de mise à jour

- Une branche instable n'est **pas** déclarée saine en ajustant un coefficient après le test ; consigner le `FAIL`, puis créer une nouvelle hypothèse numérotée.
- Un test d'universalité négatif d'un **observable donné** ne réfute pas toutes les hypothèses autour de `√22` ; il interdit seulement la revendication testée.
- Une nouvelle hypothèse n'est **pas** rejetée parce qu'elle manque de précédent bibliographique ; elle doit néanmoins être confrontée à l'algèbre, aux contraintes physiques et aux observations appropriées.
- Les anciennes feuilles de route non mises à jour demeurent archivées ; le statut réel d'une étape repose sur ses résultats et sa provenance, pas sur une ancienne case à cocher.
- Après un nouveau résultat, mettre à jour le registre par **nouvelle version** avec journal des différences ; ne pas effacer les erreurs, échecs et limitations antérieurs.

## XI. Décision requise pour passer de `v0.9 NON GELÉ` à `v1.0`

L'auteur doit confirmer :

1. **Oui/non :** CHH = composition sans EOM/dérivée globale intrinsèque ; sous-cubes dynamiques par leurs lois propres.
2. **Oui/non :** opérations +/×/÷ soumises aux unités et observables, non au seul ajustement numérique.
3. **Oui/non :** `√22` reste piste ouverte, avec les échecs historiques consignés et aucune revendication d'universalité.
4. **Oui/non :** séparation et traçabilité permanentes entre CHH, EOM-GVH, inférence et calcul auxiliaire.

**Après les quatre confirmations**, publier l'addendum `v1.1`, promouvoir cette feuille de route en `v1.0`, et commencer les notebooks selon l'arbre de dépendances. Aucun succès numérique futur ne modifiera rétroactivement les conclusions déjà auditées.

---

### Traçabilité documentaire

- Registre source SHA-256 : `4746e9e54888ec182453ce19e092b6510e8f628a2907869dd074998fa4d3a50a`.
- Neuf certificats de la checklist : chaque empreinte listée a été comparée au fichier local correspondant avant génération de ce document.
- Les pourcentages de « préparation » éventuels ne sont **pas** des probabilités de validité scientifique.