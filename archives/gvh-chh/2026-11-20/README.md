# Archives GVH / CHH — 20 novembre 2026

Cette archive est un **instantané non destructif** des notebooks Jupyter accessibles dans la bibliothèque ChatGPT et datés du **17 au 20 novembre 2026**. Elle est préparée pour import dans un dépôt GitHub après extraction.

**Périmètre précis :** 48 fichiers `.ipynb` récupérés, soit 39 contenus SHA-256 distincts et 9 copies binaires identiques ; 5 documents méthodologiques complémentaires. Ce n'est **pas** l'intégralité des notebooks historiques GVH, notamment les anciens notebooks de la série `0.2` / `0.3`, et rien ne garantit que tous les notebooks du dialogue aient été transférés dans la bibliothèque.

**Contrôle technique statique des 48 fichiers :** JSON Jupyter lisibles ; aucune sortie d'erreur Jupyter enregistrée dans les fichiers ; 45 fichiers dont les cellules de code portent toutes un numéro d'exécution et 3 copies ALMA avec numéros d'exécution incomplets. Cela **ne remplace pas une réexécution** sous environnement maîtrisé. Un titre `FAST_EXECUTED` et une coche `PASS` ne sont jamais une preuve de validation scientifique.

## Catégories

- `notebooks/00_precurseurs_hierarchie/` — Précurseurs : modèles hiérarchiques, activité, fréquences — **4 fichier(s)**.
- `notebooks/01_chh_composition/` — CHH : structure, agrégation, composition conditionnelle — **5 fichier(s)**.
- `notebooks/02_gvh_dynamique_eom/` — GVH : action, couplages, EOM, métrique, trièdre — **12 fichier(s)**.
- `notebooks/03_inference_inverse/` — Inférence inverse : planètes et sous-cubes cachés — **5 fichier(s)**.
- `notebooks/04_comparaisons_orbitales/` — Validation méthodologique : orbites, Jupiter, modèles nuls — **5 fichier(s)**.
- `notebooks/05_g284_root22/` — G284 / √22 : algèbre, stabilité et non-universalité testée — **3 fichier(s)**.
- `notebooks/06_alma_independant/` — Observations ALMA : métadonnées et contrôles indépendants — **5 fichier(s)**.
- `notebooks/99_copies_identiques/` — Copies strictement identiques conservées pour traçabilité — **9 fichier(s)**.

## Règles méthodologiques conservées

- **CHH-STRUCTURE** : composition hiérarchique de sous-cubes hétérogènes ; aucune équation du mouvement ou dérivée globale intrinsèque n'en découle sans hypothèse supplémentaire.
- **AUX-DERIVATIVE** : calculs auxiliaires étiquetés (barycentres, observables, modèles effectifs), distincts d'une loi fondamentale.
- **EOM-GVH** : branche de dérivation de la dynamique à partir d'une action *candidate*, non assimilable à la composition CHH.
- **INVERSE-INFERENCE** : inférence sous hypothèses physiques spécifiées ; les tests synthétiques ne constituent pas des découvertes de planètes réelles.
- **NEW-HYPOTHESIS** : idées ouvertes, y compris un rôle physique éventuel de √22, à distinguer de ses identités algébriques exactes.
- **EMPIRICAL-TEST** : observations indépendantes et comparaisons, avec contrôles négatifs et données réservées.

**Aucun succès ne se transmet automatiquement** : une simulation, un audit symbolique ou un résultat ALMA indépendant ne valide pas à lui seul une nouvelle gravitation GVH. Les feuilles de route datées peuvent être périmées : toujours privilégier le notebook, son empreinte et son verdict interne plutôt qu'une case ancienne.

## Statuts et gel

Le registre `AVANT_GEL` et la feuille de route v0.9 restent **non gelés** ; les quatre décisions G1–G4 et un éventuel addendum v1.1 ne sont **pas présumés approuvés**. La référence `GVH_CHH_PROTOCOL_FROZEN_v1.0` reste inchangée. Les scripts et notebooks ALMA conservent un statut scientifique séparé, sans autoriser le démasquage a posteriori des fenêtres figées.

## Fichiers clés

- `MANIFEST_NOTEBOOKS.csv` — inventaire exhaustif de cet instantané, SHA-256 par fichier, état des compteurs d'exécution, copies identiques.
- `SHA256SUMS.txt` — empreintes des fichiers archivés ; vérification par `sha256sum -c SHA256SUMS.txt` depuis la racine de l'archive sous Linux/macOS avec `sha256sum` installé.
- `docs_reference/` — cinq sources méthodologiques et leur version d'origine.
- `ARCHIVAGE_ET_SUITE.md` — points d'arrêt scientifiques avant le prochain notebook.

## Import GitHub

1. Extraire le ZIP et créer un dépôt privé, par exemple `gvh-chh-research-archive`.
2. Copier le **contenu du dossier extrait** à la racine du dépôt (pas le ZIP lui-même seul), puis publier le commit initial `archive/2026-11-20`.
3. Vérifier les SHA-256 avant modifications. Ajouter les prochaines révisions sous de **nouveaux noms versionnés**, sans remplacer rétroactivement les fichiers historiques.
4. Ne pas ajouter de clés API, jetons JPL/ALMA, identifiants privés ou données sous licence non redistribuable ; examiner le contenu des notebooks avant de rendre le dépôt public.

L'archive n'est pas directement publiée sur GitHub par cette opération.
