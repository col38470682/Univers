# Prochaine étape : Mercure — contrôle de la précession du périhélie

**But :** instaurer un contrôle relativiste sur un système différent, en restant fidèle aux quatre niveaux GVH/CHH → physique établie → test → verdict.

## Niveau 1 — CHH/GVH

CHH = composition hiérarchique hétérogène **sans dérivée intrinsèque** ; `GVH_CHH_PROTOCOL_FROZEN_v1.0`. Les dérivées de position/vitesse et les équations du système de référence sont `AUX-DERIVATIVE` et `KNOWN-PHYSICS` ; ne pas les attribuer à CHH. Les EOM propres GVH ne pourront être discutées que si elles ont été déduites d'une action explicitement formulée.

## Niveau 2 — Références physiques

- Comparer la dynamique képlérienne isolée à une correction 1PN de la relativité générale **dans un problème à deux corps**.
- Calcul analytique de contrôle : `Δω_1PN = 6π GM_sun/[a(1−e²)c²]` radians/orbite ; convertir en arcsecondes par siècle via la période orbitale.
- Les planètes et d'autres perturbations provoquent aussi une précession newtonienne ; ne jamais attribuer **toute** la précession mesurée de Mercure à la GR.

## Niveau 3 — Test numérique

- Enregistrer a, e, GM, c, période, tolérances, intégrateur et méthode de détection des périhélies **avant** le calcul.
- Vérifier qu'un modèle képlérien isolé donne une précession proche de zéro et que la correction GR 1PN reproduit l'expression analytique dans l'incertitude numérique.
- Si JPL Horizons est ensuite interrogé, séparer clairement sa solution globale relativiste (qui contient déjà des effets) d'une mesure instrumentale brute. Ne pas ajuster un effet GR à partir du résidu d'un mauvais modèle newtonien à trois corps.

## Niveau 4 — Verdict

- `KNOWN-PHYSICS` + `NUMERICAL-TEST` si l'analyse deux-corps réussit.
- `EMPIRICAL-TEST` seulement avec des observations indépendantes convenablement modélisées.
- `CHH-STRUCTURE` reste distincte ; aucune validation GVH automatique.
