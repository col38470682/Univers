# Jupiter · Source effective du terme cubique

23 novembre 2026 · Étape 1 · Premier ordre en couplage cubique

La [note de branche](GVH_Jupiter_Branche_Intermediaire_2026-11-23.md) fixe la solution auxiliaire intermédiaire. On évalue ici la source variationnelle sur le fond faible quasi statique, extérieur aux corps, à un point où la valeur propre normale est simple.

En factorisant le couplage cubique, le tenseur qui multiplie la variation du cisaillement est $Q_{ij}=(3/2)\lambda(e_i e_j-\delta_{ij}/3)$. Dans les variables de champ faible $u^i$ et $h_{ij}$, le cisaillement principal est la partie symétrique sans trace de $\partial_i u^j+\dot h_{ij}/2$. L’intégration par parties donne donc les contributions $-\zeta_C\partial_j Q_{ij}$ et $-\zeta_C\dot Q_{ij}/2$ aux variations des champs, à normalisation commune près. Ces termes précèdent la résolution des contraintes métriques.

Pour les indices planaires $\alpha,\beta$, écrivons $\sigma=\mathrm{diag}(P,\lambda_z)$ sur le plan et $H_\alpha=\partial_z\sigma_{\alpha z}$. La dérivée normale de l’équation propre donne
$$
\partial_z e_\parallel=(\lambda_z I-P)^{-1}H.
$$
En dérivant le noyau faible extérieur à trois sources, avec les notations $w_a=\mathbf n_a\cdot\mathbf v_a$ et $\mu_a=G_N M_a$, on obtient
$$
H_\alpha=\sum_a \frac{\mu_a}{r_a^3}
\left[3(A_L-A_T)w_a n_{a,\alpha}-A_L v_{a,\alpha}\right].
$$
Il en résulte sur le plan
$$
(\nabla\cdot Q)_\parallel =
-\tfrac12\nabla_\parallel\lambda_z
+\tfrac32\lambda_z(\lambda_z I-P)^{-1}H,
\qquad
(\nabla\cdot Q)_z=0.
$$
Le signe du terme à droite des équations dépend du côté auquel on reporte la variation. Cette expression explicite comment la variation normale participe à une source située dans le plan. La réflexion impose la composante normale nulle sur le plan.

Le calcul fournit la source locale à l’ordre linéaire en $\zeta_C$. Il reste à construire une solution spatiale des équations couplées, fixer les conditions aux limites et effectuer le raccordement près des corps. Les points où la valeur propre devient multiple demandent un traitement du sous-espace dégénéré. Aucune correction orbitale chiffrée n’est dérivée ici.
