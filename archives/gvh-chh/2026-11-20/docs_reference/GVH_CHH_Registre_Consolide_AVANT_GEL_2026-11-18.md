# GVH Diagonal Cubic — Registre consolidé d'idées AVANT GEL

**État : BROUILLON À RELIRE — NON GELÉ**  
**Date de référence : 18 novembre 2026**  
**Identifiant proposé : `GVH_CHH_IDEAS_PRE_FREEZE_v0.9`**

## Objet
Préserver les idées formulées dans le dialogue, distinguer les acquis conceptuels des résultats mathématiques, des tests numériques et des preuves empiriques. **Ce registre n'altère pas le protocole déjà archivé `GVH_CHH_PROTOCOL_FROZEN_v1.0`.** Après relecture et validation, un addendum versionné (v1.1, ou autre version explicitement acceptée) pourra être figé. Aucun résultat scientifique ne sera artificiellement « figé vrai ».

## A. Principes fondamentaux de CHH — à confirmer comme conventions de recherche

**A1. Composition, non dérivation intrinsèque.** La CHH décrit un assemblage hiérarchique de sous-cubes hétérogènes et de leurs interactions, par exemple

\[
C_{S,\ell}=\mathcal A_{\ell,\tau}(\{C_i,D_i\},\{I_{ij}\};\boldsymbol\theta_\tau).
\]

L'opération de composition **n'impose pas de dérivée globale, d'équation du mouvement, ni de loi universelle commune**. Cela ne signifie pas que les sous-cubes n'évoluent jamais.

**A2. Manifestations propres.** Chaque sous-cube a ses états, échelles, mécanismes, paramètres, interactions et observables propres : la fusion stellaire n'est pas assimilée à la géologie ou à la dynamique atmosphérique. Un sous-cube peut à son tour être composite. Des parties invisibles peuvent devenir résolues grâce à de nouvelles observations.

**A3. Opérations conditionnelles selon la grandeur.** Selon la nature physique de l'observable \(\tau\), une relation collective peut être additive, multiplicative, fondée sur des inverses/quotients, non linéaire ou comporter des interactions \(I_{ij}\). Les unités, les lois pertinentes et les bilans physiques imposent des restrictions ; **on ne choisit pas librement une opération après coup pour faire apparaître une constante-cible**.

**A4. Dérivation auxiliaire explicitement étiquetée.** Les dérivées d'une grandeur choisie, d'un barycentre, d'un signal agrégé ou d'un modèle effectif sont autorisées **à des fins de calcul** avec l'étiquette `AUX-DERIVATIVE`. Le choix de variable est libre ; la valeur de la dérivée, une fois les données/hypothèses fixées, ne l'est pas. Signaler hypothèses, unités, perte d'information, domaine de validité et lois externes utilisées.

**A5. Séparation stricte des opérations.** `CHH-STRUCTURE` (composition) ≠ `EOM-GVH` (variation de l'action candidate) ≠ `INVERSE-INFERENCE` (reconstruction de propriétés cachées) ≠ `AUX-DERIVATIVE` (calcul auxiliaire). Une opération de composition n'est pas réputée démontrer une nouvelle loi gravitationnelle.

## B. Hypothèses et questions mathématiques — à tester, non à décréter

**B1. Coefficient(s) de relation global–local.** Étudier \(Y_S=\mathcal A_{\ell,\tau}(\mathbf X,\mathbf I;\boldsymbol\theta_\tau)\). Des facteurs \(K_\tau\) ou paramètres d'échelle peuvent relier sous-cubes et observables, mais rien ne garantit **un seul coefficient universel**. Distinguer constante de conversion, paramètre effectif, constante physique universelle et coefficient de simple réécriture.

**B2. Décomposition par +, ×, ÷, interactions.** Tester les opérations retenues *avant* la calibration, sous contraintes d'unités et de symétries. Comparer des modèles concurrents de complexités égales et préserver les cas d'échec.

**B3. Identifiabilité.** Une seule valeur globale ne suffit généralement pas à retrouver \(N\) valeurs inconnues. Examiner rang du modèle d'observation, symétries de reparamétrisation, dégénérescences, bruit, variables externes, données réservées et contrôles négatifs. Exemple : \(Y=K\sum_i q_i\) ne détermine pas individuellement les \(q_i\) sans autres contraintes.

**B4. Racine historique √22.** Conserver comme **résultat algébrique documenté**, notamment sur la branche `G284.4.3.1` :

\[
 c_2=\frac{\sqrt{22}-4}{9},\qquad
 \frac{\omega_+^2}{\kappa^2}=\frac{\sqrt{22}-2}{9},\qquad
 \lambda=c_2+\frac29.
\]

Il s'agit de relations issues d'une même chaîne de calcul, **pas de preuves indépendantes d'une constante universelle**. La racine \(\sqrt{22}\) est un nombre connu ; son rôle éventuel dans GVH demeure hypothétique. Ne pas écarter a priori cette piste, mais ne pas prétendre à sa validation. Attention aux transformations \(Y=A\sqrt{22}\) avec \(A\) libre : elles rendent la racine non identifiable. Des opérations supplémentaires doivent être déterminées indépendamment des résultats utilisés pour les juger.

**B5. Verrous historiques de √22.** Le témoin \((c_{13},\zeta_C,c_2,c_{14})=(0,1,(\sqrt{22}-4)/9,0)\) présente un problème de signe cinétique dans une réduction quadratique. D'autres contrôles révèlent \((2-\sqrt{22})/9<0\) pour un secteur de dispersion réduit. Ne pas généraliser un NO-GO local à toute la théorie, ni l'ignorer.

**B6. Premier test inter-systèmes.** L'audit ROOT22 a comparé l'invariant képlérien sans dimension de 20 orbites autour de six centres gravitationnels, sans détecter de valeur universelle √22 pour **cet observable choisi** ; \(A\sqrt{22}\) avec \(A\) libre s'est montré algébriquement redondant. Cela ne teste pas toute possibilité GVH ni tous les systèmes physiques indépendants.

## C. Distinction entre dynamique théorique et CHH

**C1. Action GVH candidate.** L'action vectorielle et le terme cubique \(\zeta_C\mathcal O_C/2\) sont une branche théorique distincte de la composition CHH. Les \(c_i\), \(\zeta_C\) et échelles SI ne sont pas automatiquement des constantes mesurées ou calculées par la CHH.

**C2. Trièdre auxiliaire et dégénérescences.** CHH-09 à CHH-11 : pour un cisaillement spatial symétrique sans trace, un trièdre local peut donner \(\mathcal O_C=0\), tandis que le repère des axes propres atteint \(\mathcal O_C=\sigma_{\mu\nu}\sigma^{\mu\nu}\). La première branche annule la contribution cubique localement ; sur la seconde, ce terme peut être absorbé dans des coefficients de type Einstein-æther. Une signature nouvelle indépendante n'est donc pas automatique.

**C3. Trièdre dynamique : extension hypothétique.** CHH-12 et CHH-13 proposent des termes cinétiques temporels et de gradient spatial pour l'orientation du trièdre. Ils ne découlent **ni** de la seule CHH **ni** de l'ancienne action sans cette extension. La littérature inclut déjà des constructions de trièdre dynamique (spinning æther). Un modèle réduit vecteur–trièdre a été testé, mais **la métrique complète couplée, les contraintes de Dirac et la stabilité générale restent ouvertes**.

**C4. Originalité scientifique.** Ni le succès de tests numériques, ni la présence d'une expression inhabituelle, ni la différence vis-à-vis d'un article particulier ne démontrent une nouvelle loi physique. Une prédiction indépendante, un régime mathématiquement admissible et un test observable sont requis.

## D. Travaux disponibles et limites

| Branche | Éléments disponibles | Ce qui reste ouvert |
|---|---|---|
| CHH-01 à 04 | Formalisation hiérarchique, bilans, modèles effectifs et signatures internes synthétiques | Démontrer une plus-value générale face aux méthodes multi-échelles existantes |
| CHH-05 à 09 | Action candidate et audits variationnels partiels/non restreints au premier jet | Solution gravitationnelle couplée globale avec matière, conditions aux limites |
| CHH-10 à 11 | Branches d'orientation et équivalences locales Einstein-æther | Sélection physique unique, observable non redondante |
| CHH-12 à 13 | Extension cinétique du trièdre, évolution couplée réduite, contrôles locaux | Métrique dynamique, contraintes complètes, originalité générale |
| CHH-INVERSE-01/02/02B/03 | Inférences de corps cachés et de classes planétaires sur simulations | Validation sur observations indépendantes, incertitudes et identifiabilité réelle |
| G284 / ROOT22 | Origine exacte √22, premier contrôle orbital sans avantage propre | Branche saine + lien prédictif indépendant à √22 |
| ALMA | Préenregistrement de NGC 1333 IRAS 4A (X22/X24), sans exploitation opportuniste du signal | FITS/WCS, géométrie A1/A2, analyse préenregistrée, et **GVH_USED=False** jusqu'à autorisation séparée |

Les fenêtres ALMA archivées restent **6,40–7,00 km/s** (cœur) et **7,70–8,30 km/s** (premier plan), sans déplacement a posteriori.

**Attention aux feuilles de route anciennes :** `GVH_CHH_Feuille_de_route_v2_2026-11-18.md` a été écrite avant l'exécution des notebooks 09–13 et INVERSE-02/02B/03 ; les cases anciennes non cochées ne doivent pas faire oublier ces travaux exécutés. Il faut publier un nouveau suivi **daté** plutôt que réécrire silencieusement l'archive.

## E. Briques nécessaires : préparation méthodologique versus preuves

| Code | Brique | Statut pré-gel | Action |
|---|---|---|---|
| P01 | Définition CHH sans dérivée intrinsèque | **Prête à approuver** | Confirmer la portée exacte : composition seulement |
| P02 | Hétérogénéité des sous-cubes et hiérarchie | **Prête à approuver** | Confirmer les observables propres |
| P03 | Opérations conditionnelles (addition, produit, quotient, interactions) | **Prête sous réserve** | Imposer unités/symétries et domaine physique |
| P04 | Dérivées auxiliaires explicitement distinctes | **Prête à approuver** | Étiquetage `AUX-DERIVATIVE` |
| P05 | Coefficients ou constantes et identifiabilité | **Hypothèse à tester** | Fixer modèles, jeux d'entraînement et données réservées |
| P06 | √22 : provenance et limite des tests | **Résultat algébrique documenté ; hypothèse physique ouverte** | Garder avertissements de stabilité et non-universalité étroite |
| P07 | CHH / EOM / inférence distincts | **Prête à approuver** | Étiquettes obligatoires |
| P08 | Trièdre et action étendue | **Tests réduits réalisés ; système complet ouvert** | CHH-14 et contrôle d'équivalence |
| P09 | Observables nouvelles, unités SI, prédiction aveugle | **Manquant scientifiquement** | Résoudre branche admissible, paramètres et prédiction |
| P10 | Données réelles indépendantes | **Non clos** | ALMA distinct, et inférence réelle selon un protocole arrêté |
| P11 | Audit à quatre niveaux, paramètres prescrits/dérivés/mesurés | **Prêt à approuver** | Répéter dans chaque notebook |
| P12 | Gouvernance des versions et des contradictions | **Prête à approuver** | Révisions versionnées, pas d'effacement des échecs |

### Critère du « prêt à figer »

**Figer la méthode et les hypothèses comme un contrat de recherche est possible après accord sur P01–P04, P07, P11, P12 et sur le statut ouvert de P05–P06/P08–P10.** Cela **n'exige pas** que les prédictions soient déjà validées. En revanche, il est interdit de figer les hypothèses scientifiques ouvertes comme des résultats établis.

## F. Trajectoires scientifiques distinctes pour la suite

1. **CHH-14 — Métrique, contraintes, symbole principal et stabilité du trièdre dynamique** (`EOM-GVH`, pas `CHH-STRUCTURE`).
2. **ROOT22 — Santé de branche et prédiction physiquement dérivée** ; seulement ensuite recherche d'invariants inter-systèmes (`NEW-HYPOTHESIS` + `EMPIRICAL-TEST`).
3. **CHH-Conditional-Composition/Identifiability — Opérations +, ×, ÷ et inversion** avec données synthétiques puis indépendantes (`CHH-STRUCTURE` + `INVERSE-INFERENCE`).
4. **ALMA PATCH.10H.1** : vérification continuum/FITS/WCS préalable, reste indépendante et aveugle.

Ces axes peuvent avancer séparément ; la validation de l'un **n'entraîne pas** la validation automatique des autres.

## G. Questions à valider avec l'auteur avant GEL

1. **CHH :** confirmer qu'aucune EOM/dérivée globale n'est postulée *par la seule composition*, mais que les sous-cubes restent soumis à leurs dynamiques physiques propres.
2. **Opérations :** confirmer que le choix +/×/÷ est conditionnel à la grandeur et doit respecter dimensions/lois, et non une simple liberté d'ajustement.
3. **√22 :** confirmer son statut d'**hypothèse physique ouverte à conserver**, sans prétendre à une nouvelle constante mesurée.
4. **Organisation :** confirmer que CHH composition, GVH dynamique et inférence inverse restent des branches distinctes, reliées lorsque les hypothèses explicites le permettent.

**Après validation**, créer un addendum figé de protocole, un registre de formules versionné et une feuille de route mise à jour, avec empreintes SHA-256 et dépendances. **Ce document reste NON GELÉ jusqu'à cette étape.**
