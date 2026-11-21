# Jupiter H0 — archive finale de l'ablation des forces

**Programme :** GVH / CHH, couche de contrôle H0 (physique gravitationnelle établie).  
**Archive source :** 20 novembre 2026, complétée par le notebook Colab exécuté et la copie finale sur Google Drive le 21 novembre 2026 (UTC).

## Inventaire

- `GVH_CHH_JUPITER_FULL_FORCE_RESULTS.zip` : cinq CSV JPL Horizons, JSON parent, résidus CSV et image PNG.
- `GVH_CHH_JUPITER_H0_ABLATION_FINAL_RESULTS.zip` : JSON final, CSV des 12 ajustements, CSV des contrastes, SHA256_INPUTS.txt.
- `GVH_CHH_Jupiter_Horizons_H0_Force_Ablation_And_Time_Window_Robustness_Gate_FAST_FINAL_AUDIT_v02.ipynb` : notebook Google Colab réellement exécuté, 11/11 contrôles, 12/12 ajustements.
- `AUDIT_FINAL.md` : bilan des résultats, provenance et limites.
- `SHA256SUMS.txt` : empreintes SHA-256 des trois artefacts binaires archivés.
- `NEXT_STEP.md` : protocole à suivre pour une nouvelle période indépendante.

## Protocole

Éphémérides JPL Horizons calculées, centre Jupiter, coordonnées ICRF, position/vitesse, pas de 6 h, du 1 au 25 septembre 2026, 97 dates communes pour Io, Europe, Ganymède, Callisto et Soleil. Deux cibles évaluées : Io et Ganymède. Fenêtres d'ajustement 10 et 15 jours ; réserve commune après le jour 18 (24 dates). Douze conditions initiales ajustables dans chaque variante, six variantes H0 et douze ajustements.

**Verdict notebook :** `PASS_TECHNICAL_H0_FORCE_ABLATION__JPL_REFERENCE_ONLY__CHH_ORIGINALITY_OPEN`.

## Limites à conserver

Ce succès est **technique et interne aux éphémérides calculées par JPL**, non une validation sur astrométrie brute indépendante, non une découverte de lune, non une démonstration de gravité CHH/GVH. Le forçage Soleil exploite les éphémérides du Soleil jusque dans les dates réservées ; l'étude ne constitue pas une prévision entièrement autonome.

Ne pas écraser les expériences antérieures. Les objets binaires ci-dessus et leurs hashes constituent les artefacts canoniques de cette étape.
