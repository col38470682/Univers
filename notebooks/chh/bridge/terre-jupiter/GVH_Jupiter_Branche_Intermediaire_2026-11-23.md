# Jupiter mobile et branche intermédiaire de GVH

23 novembre 2026 · Étape 1 · Calcul de champ faible

Le [témoin orbital synthétique](Simulation_Terre_Jupiter.py) fixe les conditions initiales et les douze retours. La [note sur les sources mobiles](GVH_Reponse_Sources_Mobiles.md) donne le point de départ.

## Cisaillement et orientation

Dans la branche métrique–æther–trièdre à couplage métrique minimal, le calcul quasi statique additionne les contributions transverses des courants et longitudinales des densités mobiles des trois corps. Le champ ponctuel est évalué à l’extérieur des corps. L’équation stationnaire du trièdre est $(S_{AA}-S_{BB})S_{AB}=0$. La branche nulle annule la première variation cubique. La branche alignée reproduit une redéfinition des coefficients de cisaillement et d’expansion. La branche intermédiaire, avec un axe propre de valeur propre $\lambda$, donne $\mathcal L_C=3\zeta_C\lambda^2/4$.

Sur le plan orbital, la normale est axe propre par symétrie. Si $P$ est le bloc planaire, la condition de croisement est $\det(P-\lambda_z I)=0$. Dans le champ de référence, un balayage de 24 001 instants sur trois trajectoires à 10 000, 42 000 et 100 000 km du centre de la Terre, côté opposé au Soleil, et pour $A_L/A_T=0,25;\ 1;\ 4$, ne détecte aucun croisement. La plus petite séparation échantillonnée vaut $1,497\times10^{-12}\ \mathrm{UA}^{-1}$, à 100 000 km et vers 5,724 ans, avec $A_T=1$ et $A_L/A_T=0,25$. Les intervalles entre échantillons restent à contrôler.

## Mode transverse local

Pour $c_{13}=c_-=c_{14}=0,10$, $c_2=-0,06$ et $\zeta_C=0,04$ prescrits, le test au point le plus sensible donne une cinétique positive et $v_p^2/c^2=1,0682$ et $1,0451$ dans les deux directions principales du plan. Le témoin sans opérateur donne 1,0556 dans les deux directions. Ce test utilise le fond sans opérateur et inclut le terme cubique dans les équations des perturbations.

## Réponse couplée du fond coplanaire

La symétrie de réflexion fixe l’axe propre normal sur le plan. Sur ce plan, le terme réduit fournit une contrainte variationnelle proportionnelle à $\sigma_{zz}$. Pour calculer la correction du fond, il faut prolonger cette contrainte dans le domaine spatial hors du plan et résoudre les équations métrique–champ unitaire avec les mêmes sources et conditions aux limites. Pour un couplage faible, si $X_0$ est le fond de référence et $\mathcal D_0$ l’opérateur linéarisé fixé en jauge, le premier correctif satisfait $\mathcal D_0 X_1=-\delta S_C[X_0]/\delta X$. Le calcul sur le plan seul laisse ouverte la source effective hors du plan et son raccordement près des corps. L’accélération relative et la correction aux douze retours restent indéterminées.
