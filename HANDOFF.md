# Séances Pilates — dossier de passation pour Claude Code

Objectif : déployer l'appli web de Lud (Ludivine Pina, prof de Pilates, Savigny VD, francophone) sur **GitHub** (dépôt **privé**) et **Vercel**. Lud n'est pas développeuse : explique chaque étape en français, simplement, sans jargon inutile.

## 1. Ce qu'est l'appli
Une page HTML unique, sans framework, sans serveur. Tout tourne dans le navigateur (iPad et Mac).
Fonctions : en-tête (client, séance, n°, date du jour) · échauffement du corps entier adapté à la séance · boutons de séances (Abdos, Bras, Fessiers, Dos, Complète + haltères, Mobilité douce, séances enregistrées) · génération par muscle (biceps, triceps, quadriceps…) · mode « Cours » (toucher un exercice = on ne le fait pas) · bloc à copier vers Excel (D10) · onglet « Trier ma base » (Je fais / Rare / Écarter) · mémoire des réglages.

## 2. Contenu du dossier
```
pilates-app/
├─ HANDOFF.md          ← ce fichier
├─ build.py            ← assemble public/index.html (python3 build.py)
├─ vercel.json         ← sert public/ tel quel, aucun build côté Vercel
├─ .gitignore
├─ src/app.src.html    ← code de l'appli, avec le marqueur __DATA__
├─ data/data.json      ← F = familles>exercices>options ; T = tags ; P = séances prédéfinies (W supprimé au build)
├─ data/use.json       ← fréquences d'usage agrégées (aucun nom de client)
└─ public/index.html   ← résultat du build (déjà généré, ~300 Ko)
```
Pour modifier l'appli : éditer `src/app.src.html` (ou les JSON), lancer `python3 build.py`, committer.

## 3. Étapes à réaliser
1. `git init`, premier commit (le dossier est prêt tel quel).
2. Créer le dépôt GitHub **privé** (`gh repo create pilates-app --private --source=. --push`). Demander à Lud son compte/organisation GitHub si `gh` n'est pas connecté.
3. Déployer sur Vercel : importer le dépôt, **Framework = Other**, pas de build command, **Output directory = `public`** (déjà dans `vercel.json`). Ou `vercel --prod` depuis le dossier.
4. Vérifier l'URL obtenue : la page s'ouvre, l'en-tête affiche la date du jour, les boutons génèrent une séance, « Trier ma base » s'affiche, aucune erreur dans la console.
5. Sur iPad : Safari → Partager → « Sur l'écran d'accueil » pour l'avoir comme une appli.

## 4. Points d'attention (importants)
- **Confidentialité** : l'URL Vercel est publique par défaut. Les données contiennent la base d'exercices de Lud et des séances prédéfinies dont certaines mentionnent des situations de santé (ex. « épaule opérée »). Activer **Vercel Authentication / Password Protection** (peut dépendre du plan) ou ne pas diffuser l'URL, et garder le dépôt GitHub privé. À confirmer avec Lud avant de rendre quoi que ce soit public. Aucun nom de client réel n'est dans `use.json` ; ne pas ajouter de données clients au dépôt.
- **Mémoire** : l'appli enregistre ses réglages et le tri dans le `localStorage` du navigateur. Hors de Claude (donc sur Vercel), il n'y a **pas de synchronisation iPad ↔ Mac** : chaque appareil a sa propre mémoire. Le code essaie `window.claude.use('db')` (disponible seulement dans un artefact Claude) et retombe sur le navigateur sinon, sans erreur. Pour une synchro réelle, il faudrait ajouter un petit stockage (ex. Vercel KV / Upstash Redis ou Supabase) : à proposer à Lud, ne pas le faire sans son accord. En attendant, ajouter un bouton « Exporter / Importer mes réglages (JSON) » serait une amélioration simple.
- **Sauvegarde du tri** : le tri « Je fais / Rare / Écarter » vit dans le navigateur. Vider les données du site efface le tri. À signaler à Lud (d'où l'intérêt de l'export JSON).
- **Fichiers sources de Lud à ne jamais modifier** : `SEANCES.xlsx` (original). Ne pas toucher à ses dossiers iCloud (CURIOSITY/CLIENTS).
- **Statut des données** : les attributions exercice → muscle sont un premier jet de Claude, **non vérifiées** ni relues par Lud. Les fréquences d'usage viennent d'un comptage exact sur ~1 700 PDF d'archives (famille + nom), un exercice donné sous un autre nom compte comme « jamais utilisé ».

## 5. Pas encore fait (ne pas le faire sans demande de Lud)
Lud trie d'abord sa base à la main. Ensuite, dans cet ordre probable : recaler les boutons de séance sur ses vrais types de séances (titres des archives), refaire l'échauffement à partir de ses échauffements les plus donnés, vérifier ensemble les ~40 exercices les plus utilisés (muscles), décider d'ajouter le Reformer, écran « Muscles », enregistrement d'une séance dans le dossier du bon client.

## 6. Vocabulaire de Lud
Famille → exercice → option → sous-option (colonnes D, G, I, J de sa feuille Excel). « Alter » = avec haltères. Bloc collé en D10 au format TSV (D,E,F,G,H,I,J) ; colonne E : ⭐ nouveau / ➕ combiné.
