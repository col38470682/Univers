# GVH Diagonal Cubic — Protocole de recherche figé

**Identifiant :** `GVH_CHH_PROTOCOL_FROZEN_v1.0`  
**Date :** 18 novembre 2026  
**Objet :** composition CHH, calculs auxiliaires, manifestations hétérogènes, hypothèses nouvelles et piste √22.

## 0. Portée de la règle

La présente règle est une **convention méthodologique du programme GVH/CHH**, à inclure en tête des prochains notebooks. Elle ne prétend pas démontrer une loi physique et n'interdit pas de tester, corriger ou réfuter les hypothèses scientifiques.

## 1. Axiome de travail CHH — composition sans dérivée intrinsèque

La Composition hétérodynamique hiérarchique (CHH) décrit un système composite constitué de sous-cubes hétérogènes. **La CHH, prise comme opération de composition, ne postule aucune dérivée ou équation différentielle globale intrinsèque.** Les sous-cubes conservent des structures, états, échelles, paramètres, manifestations et dynamiques propres.

Écriture descriptive :

\[
C_{S,\ell}=\mathcal A_{\ell,\tau}(\{C_i,D_i\},\{I_{ij}\};\boldsymbol\theta),
\]

avec \(\tau\) la grandeur physique visée (masse, énergie, luminosité, etc.). Ce symbole **n'impose pas** une loi de composition universelle, ni une dérivation d'une loi physique nouvelle.

Les fonctions et règles de composition doivent être définies par grandeur physique et vérifiées quant aux dimensions, conditions d'application, contraintes et données.

## 2. Dérivation mathématique auxiliaire — autorisée et étiquetée

Il est licite de **choisir** une variable collective \(Y_S(t)\), une projection ou un modèle effectif, puis de calculer \(\dot Y_S\), \(\ddot Y_S\) ou une équation d'évolution. Ce choix est **auxiliaire**, non une conséquence intrinsèque de la définition CHH.

Étiquette obligatoire : `AUX-DERIVATIVE` ; renseigner dans chaque notebook :

- variable choisie, unités et dépendance temporelle ;
- opération de composition spécifique à \(\tau\) ;
- hypothèses (masse constante, système fermé, couplages négligés, etc.) ;
- équation physique externe utilisée ;
- précision et domaine de validité ;
- si la dérivée est exacte relativement aux hypothèses, ou seulement une approximation.

**Précision :** le **choix** de dériver une grandeur est libre ; **sa valeur**, une fois la fonction et les hypothèses fixées, n'est pas arbitraire.

Une loi dynamique dérivée par variation de l'action \(S_{\rm cand}\) reste dans la branche `EOM-GVH` ; elle n'est jamais attribuée à la CHH seule.

## 3. Hétérogénéité des manifestations

Ne pas attribuer à tous les sous-cubes un mécanisme interne identique. Exemple : fusion stellaire, tectonique, climat, convection, activité magnétique ou réservoirs de matière peuvent exiger des modèles constitutifs distincts.

Une grandeur composite peut être additive, multiplicative, inverse, fonctionnelle ou couplée selon sa **nature physique**, les unités et les interactions. Le choix d'une opération **ne doit jamais être fait seulement pour rapprocher un nombre cible**.

Dans les systèmes ouverts, documenter les flux traversant la frontière ; ne pas assimiler activité physique à vie biologique.

## 4. Classement obligatoire des affirmations

Chaque résultat reçoit une ou plusieurs étiquettes :

- `CHH-STRUCTURE` : définition/composition ;
- `AUX-DERIVATIVE` : dérivée/projection/calcul auxiliaire ;
- `EOM-GVH` : conséquence variationnelle de l'action explicitement écrite ;
- `KNOWN-PHYSICS` : loi ou donnée connue ;
- `NEW-HYPOTHESIS` : modification proposée, non encore établie ;
- `INVERSE-INFERENCE` : reconstruction à partir d'observables ;
- `NUMERICAL-TEST` : vérification calculatoire dans un domaine donné ;
- `EMPIRICAL-TEST` : confrontation à mesures indépendantes ;
- `OPEN-LOCK` : question non résolue.

Aucun résultat ne doit passer implicitement de `NUMERICAL-TEST` à `EMPIRICAL-TEST` ou de `NEW-HYPOTHESIS` à loi démontrée.

## 5. Hypothèses originales et documents existants

L'exploration de constructions théoriques **n'est pas limitée à reproduire les publications existantes**. Les archives et la littérature sont consultées pour : (a) établir la provenance ; (b) identifier les résultats déjà connus ; (c) comparer les prédictions ; (d) repérer les incohérences ; (e) concevoir des tests discriminants.

Les documents existants **n'interdisent pas** l'introduction d'une hypothèse nouvelle. Inversement, l'absence d'une expression dans un document consulté **ne prouve pas** sa nouveauté absolue. Comparer le plus possible aux sources primaires accessibles, et consigner les limites de recherche.

La comparaison avec la physique existante est un garde-fou scientifique, pas une interdiction de chercher au-delà.

## 6. Statut exact de √22 — à préserver sans extrapolation

Résultats **historiques exacts** de la branche `G284.4.3.1` :

\[
c_2=\frac{\sqrt{22}-4}{9},\qquad
\frac{\omega_+^2}{\kappa^2}=\frac{\sqrt{22}-2}{9}.
\]

La racine \(\sqrt{22}\) est un nombre mathématique connu ; **son apparition dans les relations GVH est un résultat algébrique de cette branche**, pas une preuve que \(\sqrt{22}\) soit une nouvelle constante physique universelle.

Dans l'audit `GVH_CHH_Root22_Cross_System_Invariant_Universality_Gate_FAST`, 20 orbites de six systèmes centraux ont été comparées à un invariant képlérien sans dimension. **Verdict limité à cet observable :** aucun avantage identifiable du facteur libre `A√22` par rapport à une constante libre `A'` ; pas de preuve d'universalité dans ce test. Ce verdict **n'exclut pas** d'autres relations physiques, notamment celles issues d'une dérivation théorique indépendante.

**Garde-fous hérités :** le point historique \((c_{13},\zeta_C,c_2,c_{14})=(0,1,(\sqrt{22}-4)/9,0)\) a présenté un défaut de santé cinétique dans un secteur quadratique réduit ; le rapport \((2-\sqrt{22})/9<0\) a aussi constitué un diagnostic défavorable sur une tranche. Ces avertissements restent actifs pour la branche en question et ne sont ni une preuve de validité ni une réfutation universelle de GVH.

**Pour tester une universalité :**
1. définir avant les calculs un invariant *sans dimension* et les systèmes pertinents ;
2. dériver sa dépendance à \(\sqrt{22}\) sans réétalonner librement un facteur qui annule toute identifiabilité ;
3. comparer à un modèle de référence correctement spécifié et à des constantes témoin ;
4. utiliser calibration et vérification hors échantillon ;
5. publier les cas négatifs, les incertitudes, unités et limites.

## 7. Architecture non négociable des notebooks

1. **Niveau 1 — GVH/CHH :** définitions, hypothèses, composition, statut des paramètres.
2. **Niveau 2 — Physique établie :** modèles concurrents, références, symétries, dimensions.
3. **Niveau 3 — Test analytique/numérique :** critères préenregistrés, cas positifs/négatifs, reproductibilité.
4. **Niveau 4 — Verdict scientifique :** dérivé, ajusté, simulé ou validé ; ouverts et falsifiabilité.

Dans les notebooks de dynamique complète : tracer également séparément les contraintes Dirac, la stabilité, la sélection des champs et les données réelles. Ne jamais laisser un `PASS` informatique masquer un verrou physique ouvert.

## 8. Bloc prêt à copier dans l'introduction d'un notebook

> **Protocole figé : `GVH_CHH_PROTOCOL_FROZEN_v1.0`.** CHH = composition hiérarchique de sous-cubes hétérogènes, sans dérivée globale intrinsèque. Toute dérivée collective est un choix auxiliaire (`AUX-DERIVATIVE`) dont les hypothèses doivent être écrites. Les lois physiques propres aux sous-cubes ou dérivées de l'action GVH sont distinctes de la CHH. \(\sqrt{22}\) reste un résultat algébrique historique et une hypothèse de recherche ouverte, non une constante universelle validée. Les échecs de tests locaux restent consignés ; les théories nouvelles peuvent être explorées et comparées aux connaissances existantes. Quatre niveaux obligatoires : GVH/CHH → physique établie → test → verdict.

## 9. Changements futurs

Le protocole est **figé comme base documentaire**. S'il faut changer une règle, produire `v1.1`, avec date, justification et liste précise des différences : ne jamais réécrire silencieusement `v1.0`. Les résultats physiques restent réfutables et révisables en fonction de nouvelles démonstrations ou données.