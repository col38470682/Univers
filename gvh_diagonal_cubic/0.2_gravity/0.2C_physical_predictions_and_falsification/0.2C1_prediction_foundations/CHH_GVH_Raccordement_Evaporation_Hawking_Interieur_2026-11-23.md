# Raccordement d’un trou noir en évaporation à un intérieur en expansion

**Date** 23 novembre 2026  
**Statut** Contrôle numérique de référence en relativité générale. Extension GVH classée **NEW-HYPOTHESIS**. Suite mise en attente jusqu’à la fin du travail sur Jupiter.

## Question

Le rayon de piégeage extérieur peut-il diminuer pendant qu’une région intérieure s’étend ? Le calcul distingue le rayon de piégeage \(2M(v)\) du rayon \(R\) d’une frontière comobile. Il utilise un intérieur plat à taux d’expansion imposé \(H>0\), en unités \(G=c=1\).

## Raccordement direct

Sans couche de surface, la continuité de la masse de Misner–Sharp impose \(M=H^2R^3/2\) pour l’intérieur plat. À \(H\) constant, une frontière comobile en expansion donne \(dM/d\tau=3HM>0\), alors que l’évaporation donne \(dM/d\tau<0\) pour une coordonnée extérieure croissante. Le raccordement direct est incompatible avec ces hypothèses.

## Contrôle numérique réduit

L’extérieur est décrit par une géométrie de Vaidya entrante à masse décroissante. Le flux entrant négatif sert de modèle près du rayon de piégeage. Pour \(M(0)=1\) et \(\kappa=0{,}001\), la loi imposée \(dM/dv=-\kappa/M^2\) donne \(M(v)=(1-3\kappa v)^{1/3}\). Un rayon lumineux sortant obéit à \(dr/dv=(1-2M/r)/2\).

Pour \(r(0)=1{,}995\), le rayon se contracte, atteint \(r_{\min}\simeq1{,}99214933=2M(v)\) à \(v\simeq3{,}90994488\), puis augmente. Le passage d’une tolérance relative de \(10^{-9}\) à \(10^{-11}\) change le temps du minimum d’environ \(4\times10^{-8}\). Ce retournement est qualitativement comparable à la figure 3 de Parentani et Piran. Leur masse provient d’un calcul semi-classique couplé. Notre loi de masse est une entrée et les paramètres du contrôle sont choisis pour cet essai.

## Frontière avec couche mince

Pour une frontière comobile, \(\dot R=HR\), où le point désigne la dérivée en temps propre \(\tau\). Sur la branche où le rayon croît dans le sens de la normale de chaque côté, la condition angulaire d’Israel donne

\[
4\pi R\sigma=1-\sqrt{1+H^2 R^2-2M(v)/R}.
\]

Avec \(F=1-2M(v)/R>0\), la normalisation de la vitesse donne \(\dot v=(HR+\sqrt{H^2R^2+F})/F\). Le seuil \(\sigma=0\) correspond à \(H^2R^3=2M(v)\).

| Quantité | Départ | Seuil |
|---|---:|---:|
| Temps propre \(\tau\) | 0 | 10,107189 |
| Temps avancé \(v\) | 0 | 22,263906 |
| Rayon comobile \(R\) | 3,000000 | 6,734122 |
| Rayon de piégeage \(2M\) | 2,000000 | 1,954442 |

Le taux d’essai est \(H=0{,}08\). Après le seuil, la densité surfacique exigée est négative. La frontière du tableau reste à l’extérieur de \(2M\). La pression tangentielle et les conditions d’énergie complètes restent à évaluer. Ce calcul ne détermine ni la survie d’un intérieur derrière le col ni la réponse dynamique de \(H\) à l’évaporation.

## Reproduction numérique

~~~python
import numpy as np
from scipy.integrate import solve_ivp

kappa = 0.001
hubble = 0.08

def mass(v):
    return (1 - 3 * kappa * v) ** (1 / 3)

def outgoing_ray(v, state):
    radius = state[0]
    return 0.5 * (1 - 2 * mass(v) / radius)

outgoing_ray.direction = 1

def comoving_shell(tau, state):
    v, radius = state
    metric_factor = 1 - 2 * mass(v) / radius
    radius_rate = hubble * radius
    v_rate = (np.sqrt(radius_rate**2 + metric_factor) + radius_rate) / metric_factor
    return [v_rate, radius_rate]

def zero_surface_density(tau, state):
    v, radius = state
    return 2 * mass(v) - hubble**2 * radius**3

zero_surface_density.direction = -1

for tolerance in (1e-9, 1e-11):
    ray = solve_ivp(
        outgoing_ray, (0, 30), [1.995], events=outgoing_ray,
        max_step=0.5, rtol=tolerance, atol=tolerance / 10,
    )
    shell = solve_ivp(
        comoving_shell, (0, 15), [0, 3], events=zero_surface_density,
        rtol=tolerance, atol=tolerance / 10,
    )
    assert ray.success and shell.success
    v_turn = ray.t_events[0][0]
    r_turn = ray.y_events[0][0, 0]
    tau_zero = shell.t_events[0][0]
    v_zero, r_zero = shell.y_events[0][0]
    print(tolerance, v_turn, r_turn, tau_zero, v_zero, r_zero, 2 * mass(v_zero))
~~~

## Reprise après Jupiter

Reprendre par le calcul de la pression de la couche dans le contrôle GR. Pour une comparaison quantitative avec Parentani et Piran, intégrer leur système semi-classique à deux coordonnées nulles et suivre séparément le rayon du col et les sphères intérieures. Tester ensuite un raccordement avec un intérieur GVH dont le taux d’expansion est déterminé par les équations.

## Références

- R. Parentani et T. Piran, *Internal Geometry of an Evaporating Black Hole*, Phys. Rev. Lett. 73, 2805 (1994). [Article](https://doi.org/10.1103/PhysRevLett.73.2805) · [Prépublication](https://arxiv.org/abs/hep-th/9405007)
- Étude du candidat cosmologique homogène \((q_\star,H_\star)\). [Notebook GVH .28.21 SIDE-N3](https://github.com/col38470682/Univers/blob/032adfdbe40725c8b6637fe3afe6bc0629bf3cef/gvh_diagonal_cubic/0.2_gravity/0.2C_physical_predictions_and_falsification/0.2C1_prediction_foundations/GVH_Diagonal_Cubic_0.3.2.7.3.7.3.3.28.21_SIDE_N3_Cosmological_Candidate_qstar_Hstar_Map_FAST_COMPLETE.ipynb)
