GVH — Provenance and AI Assistance Record

Document de provenance scientifique et de transparence sur l’assistance IA
Projet : GVH / GVH_Diagonal_Cubic
Statut : registre vivant — version 0.1
Date de formalisation initiale : 2026-08-22
Objet : documenter l’origine, l’évolution, l’assistance IA, les exécutions reproductibles, la découverte progressive de la littérature et le statut de nouveauté des résultats GVH.

────────

1. Objet du registre

Ce document n’a pas pour fonction de revendiquer que toutes les idées, équations ou structures mathématiques apparues dans GVH sont originales.

Il a quatre fonctions :

1. établir une chronologie vérifiable du développement du projet ;
2. séparer les contributions humaines, l’assistance IA, les calculs exécutés et les apports de la littérature ;
3. identifier les résultats qui ont été obtenus dans la chaîne GVH avant leur comparaison explicite avec des théories existantes ;
4. empêcher toute revendication de nouveauté qui ne serait pas soutenue par une analyse de priorité et de non-redondance.

Le principe directeur est :

> **La reproductibilité d’un résultat et l’originalité d’un résultat sont deux questions différentes.**

Un notebook exécuté, audité et hashé peut démontrer qu’un résultat précis existait dans le projet à un instant donné. Il ne démontre pas, à lui seul, que ce résultat était inconnu de la littérature ou qu’il a été conçu sans influence externe.

────────

2. Déclaration générale sur l’utilisation de l’intelligence artificielle

Le projet GVH est développé avec une assistance substantielle d’intelligence artificielle.

L’IA est utilisée notamment pour :

• formaliser des intuitions ou hypothèses en expressions mathématiques ;
• proposer des dérivations intermédiaires ;
• générer et corriger du code Python / SymPy / mpmath ;
• construire des notebooks Jupyter ;
• effectuer des contrôles algébriques et numériques ;
• organiser des audits scientifiques ;
• comparer des résultats à la littérature connue ;
• rechercher ou signaler des références externes ;
• aider à rédiger les explications et la documentation.

L’utilisation de l’IA implique une limite importante :

> **Même lorsqu’une référence externe n’avait pas encore été explicitement identifiée dans le projet, il n’est pas possible d’affirmer que le modèle d’IA n’avait aucune connaissance statistique ou indirecte de travaux antérieurs présents dans ses données d’entraînement.**

Par conséquent, le projet évite la formulation :

> « découverte totalement indépendante de toute connaissance d’Einstein-æther ».

La formulation acceptable est plutôt :

> **« redérivation documentée au sein du projet GVH avant l’identification explicite de l’équivalence avec Einstein-æther dans la chaîne auditée, avec assistance IA déclarée ».**

Cette formulation décrit ce que les archives peuvent effectivement démontrer sans prétendre prouver l’absence absolue d’influence de la littérature.

────────

3. Responsabilité scientifique humaine

L’assistance IA ne remplace pas la responsabilité scientifique de l’auteur humain du projet.

Les responsabilités humaines comprennent notamment :

• décider quelles hypothèses poursuivre ou abandonner ;
• sélectionner les tests de falsification ;
• exécuter les notebooks dans un environnement indépendant, notamment Google Colab ;
• conserver les sorties exécutées ;
• contrôler les incohérences et demander des réaudits ;
• accepter ou refuser les promotions de statut scientifique ;
• décider ce qui peut être présenté comme hypothèse, résultat, reproduction ou nouveauté ;
• vérifier les références primaires avant publication ;
• assumer la responsabilité finale de tout texte scientifique publié.

Aucun résultat généré par IA ne doit être considéré comme validé simplement parce qu’il a été produit par le modèle.

────────

4. Terminologie de provenance

4.1 Dérivation dans le projet

Dérivation GVH interne : résultat obtenu dans la chaîne de calcul/notebooks GVH.

Cela ne signifie pas nécessairement « découverte humaine originale ».

4.2 Redérivation documentée avant identification externe

Résultat présent dans un artifact GVH daté/hashé avant que l’équivalence ou la référence externe correspondante soit explicitement introduite dans la chaîne auditée.

Cette catégorie peut soutenir une affirmation de développement indépendant au niveau du dossier de projet, mais pas une affirmation absolue d’indépendance vis-à-vis de toutes les connaissances contenues dans un modèle d’IA.

4.3 Vérification guidée par la littérature

Résultat calculé ou vérifié après qu’une source externe pertinente a été identifiée.

Exemple : reprendre une métrique publiée, construire un changement de variable et vérifier avec SymPy qu’elle coïncide avec une forme obtenue auparavant dans GVH.

4.4 Résultat importé

Formule ou résultat emprunté directement à la littérature puis utilisé parce qu’une équivalence a déjà été établie.

Ces résultats doivent toujours être cités comme tels.

4.5 Nouveauté physique

Un résultat ne doit être qualifié de « nouvelle physique GVH » que s’il satisfait au minimum :

1. définition covariante explicite ;
2. origine GVH identifiable ;
3. non-redondance démontrée par rapport aux théories/EFT connues ;
4. algèbre de contraintes et nombre de degrés de liberté réaudités ;
5. limites GR/EA contrôlées ;
6. observable falsifiable distinct.

────────

5. Classes de provenance recommandées

Chaque futur résultat majeur doit recevoir un label.

|Code        |Classe                        |Signification                                                                                              |
|------------|------------------------------|-----------------------------------------------------------------------------------------------------------|
|**H**       |Human-origin evidence         |intuition, contrainte ou construction dont l’origine humaine est documentée par notes/transcriptions datées|
|**AI-F**    |AI-assisted formalization     |formalisation ou dérivation produite avec assistance IA                                                    |
|**C**       |Computationally reproduced    |résultat reproduit par calcul exécuté et archivé                                                           |
|**PRE-LIT** |Pre-explicit-literature record|présent dans le projet avant l’identification explicite de la source correspondante dans la chaîne auditée |
|**LIT-X**   |Literature cross-check        |vérification effectuée après consultation de la littérature                                                |
|**IMP**     |Imported from literature      |formule ou résultat directement repris d’une source externe                                                |
|**NOV-CAND**|Novelty candidate             |candidat potentiellement distinct, non encore qualifié                                                     |
|**NOV-PASS**|Novelty qualified             |nouveauté démontrée après audit de non-redondance                                                          |

Un résultat peut recevoir plusieurs labels, par exemple :

AI-F + C + PRE-LIT

ou :

IMP + LIT-X + C.

────────

6. Seuil documentaire Einstein-æther dans la chaîne GVH

Dans les artifacts actuellement archivés, le notebook :

GVH_Diagonal_Cubic_0.3.2.7.3.7.3.3.21_Einstein_Aether_Equivalence_Interior_Matching_4D_Covariant_and_Preferred_Frame_PPN_Audit_FAST

est le premier jalon canonique explicitement consacré à l’identification et à l’audit de l’équivalence Einstein-æther.

Cela doit être interprété comme :

> **premier jalon explicite d’équivalence dans la chaîne canonique actuellement documentée**,

et non comme :

> « preuve que ni l’auteur ni l’IA ne connaissaient Einstein-æther avant cet instant ».

Cette distinction doit être conservée dans toute publication.

────────

7. Chronologie scientifique minimale documentée

Phase A — chaîne canonique avant l’audit explicite Einstein-æther

Les notebooks suivants matérialisent des résultats GVH avant le jalon .3.3.21 :

|Version  |Objet                                        |Artifact exécuté / SHA-256                                        |Statut de provenance recommandé|
|---------|---------------------------------------------|------------------------------------------------------------------|-------------------------------|
|`.3.3.10`|benchmark Minkowski                          |`7fb04c381ce4671a884be97453ca45926c5a7f8fc67496c7f9b8ca3babf10c66`|`AI-F + C + PRE-LIT*`          |
|`.3.3.14`|réduction scalaire, Poisson, (G_{\rm eff})   |`ad810c82515ea7cae7462894a07351936644e760ebc2ea97f965182302d8e886`|`AI-F + C + PRE-LIT*`          |
|`.3.3.18`|réparation classique et route D              |`972013adffb4b231fa628cddb5ecb109a95c07ab316b2770c9e93425152e973f`|`AI-F + C + PRE-LIT*`          |
|`.3.3.19`|EOM sphériques, régularité, PPN              |`daff136b151f86d1d51a025ef94365a758690c4a7d6e6f0661f3b4ab92928602`|`AI-F + C + PRE-LIT*`          |
|`.3.3.20`|extension interne, ledger 4D, observables 2PN|`b1b092d7e0b2ac7d2e60dec84ba71e3984df01a38ac2a922bdb9d1107e39b368`|`AI-F + C + PRE-LIT*`          |

PRE-LIT* signifie uniquement : antérieur au jalon explicite .3.3.21 dans la chaîne canonique disponible.
Il ne constitue pas une preuve d’absence de connaissance indirecte par l’IA.

Phase B — identification explicite de l’équivalence

|Version  |Objet                                                              |SHA-256 canonique                                                 |Statut     |
|---------|-------------------------------------------------------------------|------------------------------------------------------------------|-----------|
|`.3.3.21`|équivalence Einstein-æther, matching intérieur, PPN preferred-frame|`3cf6c50e518d70c1215c94f13f93d3359001b5d0cf0bb9372425c3336b276d5e`|`LIT-X + C`|

Résultat principal :

• action covariante à quatre couplages reconnue comme équivalente à Einstein-æther ;
• route D reconnue comme famille static-aether connue ;
• indépendance du formalisme Hamiltonien ne signifie pas nouvelle physique.

Phase C — audit de distinctness

|Version  |Objet                                                       |SHA-256 canonique                                                 |Statut     |
|---------|------------------------------------------------------------|------------------------------------------------------------------|-----------|
|`.3.3.22`|distinctness, matière, observables fort-champ exactes       |`b6b3719e759d4ae0203b400e32c28bceb56c84e8c3e9030e4e750ae8faf55a27`|`LIT-X + C`|
|`.3.3.23`|opérateur distinct, matière, extension maximale indépendante|`9c4c9db1ae04eec809e6c8b0d993b3408120cc250330f81a521a3dafb525788f`|`LIT-X + C`|

Résultat principal :

• GVH_DISTINCT_OPERATOR_QUALIFIED = False
• GVH_DISTINCT_MATTER_COUPLING_QUALIFIED = False
• GVH_DISTINCTNESS_GATE_PASS = False
• les observables fort-champ matérialisées sont Einstein-æther-equivalent ;
• aucun observable propre à GVH n’est actuellement démontré.

────────

8. Exemple central : route D

8.1 Forme obtenue dans la chaîne GVH

La route D a été formulée sous la forme :

[
A^2=P(y)=1+2y+\frac{c_{14}}{2}y^2,
]

[
r,y’=-yP(y),
]

avec :

[
y=r\frac{N’}{N}.
]

Cette formulation apparaît dans la chaîne GVH avant le notebook d’équivalence explicite .3.3.21.

8.2 Forme externe Zhu–Li

Zhu & Li utilisent :

[
\mu=\sqrt{1-\frac{c_{14}}2},
]

et une coordonnée (\rho), avec une métrique exacte dans laquelle :

[
R(\rho)=
\frac{\mu R_s}
{\rho(\rho^{-\mu}-\rho^\mu)}.
]

8.3 Audit ultérieur

Après consultation de cette source, .3.3.23 a dérivé :

[
y(\rho)=
\frac{1-\rho^{2\mu}}
{(\mu-1)+(\mu+1)\rho^{2\mu}},
]

puis vérifié symboliquement que :

[
P[y(\rho)]=g_{rr}^{\rm Zhu-Li}.
]

Classification de provenance :

• forme route D initiale : AI-F + C + PRE-LIT*;
• transformation (\rho\leftrightarrow y) et vérification Zhu–Li : LIT-X + C;
• statut physique : même solution Einstein-æther, donc pas NOV-PASS.

────────

9. Résultats qui ne doivent pas être présentés comme découvertes propres à GVH

À la date de ce registre, les éléments suivants appartiennent au secteur reconnu comme Einstein-æther-equivalent :

• vecteur unitaire timelike (u^\mu) avec (u^\mu u_\mu=-1) ;
• quatre couplages (c_1,c_2,c_3,c_4) ;
• combinaisons (c_{13},c_{14},c_{123}) ;
• action covariante quadratique standard en (\nabla u) ;
• vitesse du mode tensoriel ;
• vitesses vectorielle et scalaire dans le secteur correspondant ;
• constante Newton effective ;
• paramètres PPN importés/appliqués après équivalence ;
• famille sphérique static-aether route D ;
• observables photon sphere / ISCO / (b_{\rm crit}) dérivées de cette famille ;
• structure globale de cette même famille lorsqu’elle ne contient aucun nouvel ingrédient GVH.

Toute publication future doit citer la littérature Einstein-æther correspondante.

────────

10. Résultats dont la dérivation peut être décrite comme indépendante au niveau du projet

La formulation recommandée n’est pas :

> « GVH a inventé ces équations indépendamment d’Einstein-æther ».

La formulation recommandée est :

> **« Certaines relations ont été redérivées dans la chaîne GVH, avec assistance IA, avant que leur équivalence avec le secteur Einstein-æther soit explicitement identifiée et auditée dans le projet. »**

Cette phrase est compatible avec les artifacts hashés.

Elle reste volontairement muette sur ce qui pouvait être contenu dans les connaissances internes du modèle d’IA.

────────

11. Apports directement issus de la littérature après identification

Après le jalon d’équivalence, certaines informations ont été explicitement introduites depuis des sources externes.

Exemples :

• expressions PPN preferred-frame (\alpha_1,\alpha_2) ;
• statut historique des solutions static-aether ;
• contraintes Einstein-æther issues de GW170817 et des pulsars ;
• interprétation EFT quantique d’Einstein-æther ;
• extension analytique Zhu–Li 2026.

Ces éléments sont classés IMP ou LIT-X selon qu’ils sont repris directement ou redérivés.

────────

12. Source primaire Zhu–Li 2026 — statut de vérification

La source primaire suivante est désormais disponible dans le dossier de travail :

Jie Zhu & Hao Li, “Revisit Static Aether: Exact Vacuum Solution in Einstein-Aether Theory and Its Analytic Extension”, arXiv:2606.27995v1 (2026).

Le document confirme notamment :

• l’action Einstein-æther standard ;
• la dépendance de la branche static-aether sur (c_{14}) ;
• la limite Schwarzschild (c_{14}=0) ;
• la solution exacte en coordonnée (\rho) ;
• le seuil (\mu=1/2 \leftrightarrow c_{14}=3/2) ;
• l’horizon de Killing extrémal ;
• la branche à signature inversée ;
• la famille discrète de continuation analytique.

La présence de cette source primaire doit être enregistrée comme :

ZHULI_2026_PRIMARY_SOURCE_VERIFIED = True.

Elle ne transforme pas automatiquement toutes les revendications de l’article en résultats indépendamment démontrés par GVH.

────────

13. Distinction entre preuve de provenance et preuve de priorité

13.1 Ce que les SHA-256 démontrent

Un SHA-256 permet de fixer l’identité exacte d’un fichier.

Associé à :

• un commit Git signé ou timestampé ;
• une release GitHub ;
• un dépôt Zenodo/OSF avec DOI ;
• un email daté ;
• un export Colab ;
• un journal de laboratoire ;

il peut contribuer à démontrer qu’un artifact précis existait à une date donnée.

13.2 Ce qu’un SHA-256 ne démontre pas

Il ne prouve pas :

• qui a inventé l’idée ;
• qu’aucune source antérieure n’existait ;
• que l’auteur n’avait jamais vu une théorie similaire ;
• que l’IA n’avait aucune connaissance de la littérature ;
• que le résultat est nouveau.

────────

14. Dossier minimal à conserver pour chaque jalon majeur

Pour chaque notebook canonique :

1. source .ipynb ;
2. copie exécutée utilisateur / Colab ;
3. SHA-256 de la source ;
4. SHA-256 de l’exécuté ;
5. nombre total de cellules ;
6. nombre de cellules de code et markdown ;
7. séquence des execution counts ;
8. nombre d’erreurs ;
9. artifact JSON scientifique ;
10. audit JSON source-vs-exécuté ;
11. commit Git correspondant ;
12. date UTC du commit ;
13. références externes connues à ce moment ;
14. statut de provenance (AI-F, C, PRE-LIT, LIT-X, IMP, etc.).

────────

15. Règle de non-rétroactivité

Lorsqu’une équivalence avec une théorie antérieure est découverte :

• les anciens artifacts doivent être conservés tels quels ;
• ils ne doivent pas être réécrits pour donner l’apparence que la littérature était connue auparavant ;
• un nouveau notebook doit documenter la découverte de l’équivalence ;
• les anciennes revendications de nouveauté doivent être explicitement retirées ou reclassifiées ;
• les publications futures doivent utiliser le statut corrigé.

C’est précisément le rôle joué par .3.3.21, .3.3.22 et .3.3.23.

────────

16. Règle de citation après découverte d’une équivalence

À partir du moment où une source antérieure pertinente est connue :

> **tout résultat ultérieur dans le secteur équivalent doit citer cette littérature, même si une forme semblable avait été obtenue auparavant dans GVH.**

La redérivation historique n’autorise pas à omettre la priorité bibliographique des travaux antérieurs.

────────

17. Déclaration recommandée pour une future publication

Version courte :

> **AI assistance and provenance.** The GVH project was developed with substantial assistance from large language models for mathematical formalization, symbolic/numerical coding, notebook construction, auditing, and literature discovery. Several relations were obtained in the GVH notebook chain before their explicit identification within the project as belonging to the Einstein-aether sector. Once that equivalence was recognized, the corresponding prior literature was incorporated, novelty claims for the equivalent sector were withdrawn, and subsequent work was explicitly classified as reproduction, cross-check, or distinctness testing. All scientific claims remain the responsibility of the human author.

Version française :

> **Assistance IA et provenance.** Le projet GVH a été développé avec une assistance substantielle de modèles de langage pour la formalisation mathématique, le calcul symbolique et numérique, la construction de notebooks, les audits et la recherche bibliographique. Certaines relations ont été obtenues dans la chaîne de notebooks GVH avant leur identification explicite, au sein du projet, comme appartenant au secteur Einstein-æther. Dès que cette équivalence a été reconnue, la littérature antérieure correspondante a été intégrée, les revendications de nouveauté du secteur équivalent ont été retirées et les travaux ultérieurs ont été classifiés comme reproduction, contrôle croisé ou test de distinctness. La responsabilité finale de toutes les affirmations scientifiques appartient à l’auteur humain.

────────

18. Formulations à utiliser / à éviter

À utiliser

• « redérivé dans la chaîne GVH avant identification explicite de l’équivalence »
• « développé avec assistance IA »
• « équivalent à Einstein-æther dans le secteur testé »
• « formalisation Hamiltonienne indépendante »
• « reproduction / cross-check »
• « candidat de nouveauté »
• « nouveauté non établie »
• « source primaire vérifiée »

À éviter sans preuve supplémentaire

• « inventé indépendamment Einstein-æther »
• « première découverte de cette théorie »
• « aucune connaissance antérieure possible »
• « preuve que l’IA ne connaissait pas Einstein-æther »
• « nouvelle physique GVH » pour le secteur déjà équivalent
• « original » sur la seule base d’un notebook ancien

────────

19. Frontière actuelle de distinctness GVH

Le secteur actuellement validé ne contient aucun ingrédient physiquement distinct d’Einstein-æther.

Les pistes conservées comme candidats, et non comme résultats, sont notamment :

1. un opérateur directionnel propre à GVH, par exemple (D_{\mu\nu}) ;
2. une construction dans laquelle une structure 4D émergerait d’une dynamique fondamentalement 3D ;
3. un couplage matière spécifiquement GVH.

Aucune de ces pistes ne doit entrer dans le noyau validé avant :

• formalisation covariante ;
• preuve de non-redondance vis-à-vis d’Einstein-æther / EFT ;
• audit complet des contraintes et DOF ;
• contrôle des limites relativistes ;
• observable distinct et falsifiable.

────────

20. Politique pour les futures interactions IA

À partir de ce registre, toute suggestion scientifique importante fournie par une IA doit recevoir l’un des statuts suivants :

• AI-SUGGESTION_UNVERIFIED
• PRIMARY_SOURCE_VERIFIED
• INDEPENDENT_CALCULATION_REPRODUCED
• CANONICAL_SCIENTIFIC_PASS
• CANONICAL_SCIENTIFIC_FAIL
• OPEN

L’IA ne doit jamais être utilisée comme source bibliographique finale.

La chaîne souhaitée est :

[
\text{suggestion IA}
\rightarrow
\text{source primaire}
\rightarrow
\text{calcul reproductible}
\rightarrow
\text{audit}
\rightarrow
\text{classification scientifique}.
]

────────

21. Registre d’événements de provenance

À compléter et étendre à chaque jalon.

|Date      |Événement                                                                |Artifact / preuve                           |Catégorie                |Commentaire                                                                    |
|----------|-------------------------------------------------------------------------|--------------------------------------------|-------------------------|-------------------------------------------------------------------------------|
|2026-08   |développement de la chaîne classique Minkowski → faible champ → sphérique|`.3.3.10–.3.3.20` + hashes                  |`AI-F + C + PRE-LIT*`    |antérieur au jalon explicite d’équivalence dans la chaîne canonique            |
|2026-08   |audit explicite Einstein-æther                                           |`.3.3.21`, SHA `3cf6c50e…`                  |`LIT-X + C`              |équivalence de l’action et de route D reconnue                                 |
|2026-08   |audit de distinctness                                                    |`.3.3.22`, SHA `b6b3719e…`                  |`LIT-X + C`              |aucune nouvelle physique GVH matérialisée                                      |
|2026-08   |audit extension / opérateur distinct                                     |`.3.3.23`, SHA `9c4c9db1…`                  |`LIT-X + C`              |seuil (c_{14}=3/2), famille analytique discrète, distinctness toujours négative|
|2026-08-22|source Zhu–Li 2026 fournie et vérifiée                                   |PDF arXiv:2606.27995v1                      |`PRIMARY_SOURCE_VERIFIED`|source primaire maintenant disponible                                          |
|2026-08-22|création du présent registre                                             |`GVH_Provenance_and_AI_Assistance_Record.md`|`PROVENANCE_RECORD`      |version 0.1                                                                    |

────────

22. Éléments encore nécessaires pour renforcer la provenance

Le présent document doit être complété par :

• export de l’historique Git avec dates de commits ;
• tags ou releases pour les jalons canoniques ;
• horodatage UTC des notebooks sources et exécutés ;
• export des conversations pertinentes lorsque disponible ;
• identification du premier message où Einstein-æther a été explicitement mentionné ;
• identification, lorsque possible, de l’origine de chaque hypothèse importante : humaine, IA ou littérature ;
• dépôt périodique immuable (Zenodo, OSF ou équivalent) des checkpoints majeurs ;
• éventuellement signature cryptographique des manifests.

────────

23. Règle sur les accusations de plagiat

Le présent registre ne prétend pas constituer à lui seul une preuve juridique.

Son rôle est de fournir une réponse scientifique documentée :

1. le projet utilise explicitement l’IA ;
2. les artifacts successifs sont conservés ;
3. les calculs peuvent être reproduits ;
4. les résultats antérieurs sont cités dès qu’ils sont identifiés ;
5. les revendications de nouveauté sont retirées lorsque l’équivalence est démontrée ;
6. aucune tentative de masquer la littérature antérieure ne doit être tolérée.

La défense scientifique correcte n’est donc pas :

> « nous ne pouvions pas connaître Einstein-æther ».

Elle est :

> **« voici la chronologie vérifiable de ce qui a été calculé, de l’assistance IA utilisée, du moment où l’équivalence a été explicitement identifiée, des sources ensuite intégrées et des revendications que nous avons volontairement reclassifiées ».**

────────

24. Statut scientifique actuel

Au checkpoint .3.3.23 :

```text
GVH_DISTINCT_OPERATOR_QUALIFIED = False
GVH_DISTINCT_MATTER_COUPLING_QUALIFIED = False
GVH_DISTINCTNESS_GATE_PASS = False
REAL_DATA_GVH_NOVELTY_INFERENCE_AUTHORIZED = False
```

Le secteur dynamique matérialisé est actuellement classifié comme Einstein-æther-equivalent.

Les futures recherches de distinctness doivent être traitées séparément et ne doivent pas rétroactivement transformer les résultats Einstein-æther-equivalent en découvertes propres à GVH.

────────

25. Convention de mise à jour

Chaque modification importante de ce registre doit :

1. incrémenter la version du document ;
2. conserver l’ancienne version ;
3. enregistrer le SHA-256 de chaque version ;
4. indiquer les nouvelles sources introduites ;
5. ajouter les nouveaux artifacts canoniques ;
6. signaler toute correction de provenance ou de priorité.

────────

26. Conclusion

Le projet adopte la règle suivante :

[
\boxed{
\text{transparence de provenance}



\text{revendication prématurée de nouveauté}
}
]

et :

[
\boxed{
\text{redérivation assistée par IA}
\neq
\text{preuve d’originalité}
}
]

mais également :

[
\boxed{
\text{assistance IA}
\neq
\text{absence de contribution scientifique humaine}.
}
]

La valeur scientifique du programme doit être jugée sur la clarté des hypothèses, la reproductibilité des calculs, la qualité des audits, la connaissance correcte de la littérature et, pour toute future revendication de nouvelle physique, la démonstration explicite de non-redondance et de falsifiabilité.

────────

Références externes de base à conserver dans le dossier

• T. Jacobson & D. Mattingly, Gravity with a dynamical preferred frame, Phys. Rev. D 64, 024028 (2001), arXiv:gr-qc/0007031.
• B. Z. Foster & T. Jacobson, Post-Newtonian parameters and constraints on Einstein-aether theory, Phys. Rev. D 73, 064015 (2006), arXiv:gr-qc/0509083.
• C. Eling & T. Jacobson, Spherical solutions in Einstein-aether theory: Static aether and stars, Class. Quantum Grav. 23, 5625 (2006), arXiv:gr-qc/0603058.
• T. Jacobson, Einstein-aether gravity: a status report, arXiv:0801.1547.
• B. Withers, Einstein-aether as a quantum effective field theory, arXiv:0905.2446.
• J. Oost, S. Mukohyama & A. Wang, Constraints on Einstein-aether theory after GW170817, Phys. Rev. D 97, 124023 (2018), arXiv:1802.04303.
• J. Oost, S. Mukohyama & A. Wang, Spherically Symmetric Exact Vacuum Solutions in Einstein-Aether Theory, Universe 7, 272 (2021), arXiv:2106.09044.
• J. Zhu & H. Li, Revisit Static Aether: Exact Vacuum Solution in Einstein-Aether Theory and Its Analytic Extension, arXiv:2606.27995v1 (2026).
