# Agent de Veille IA Hebdomadaire

Application console Python entièrement autonome qui, chaque **dimanche à 6h00 (heure de Québec)**, génère un rapport hebdomadaire de veille en intelligence artificielle :

- Recherche web (**Tavily**) sur 6 thèmes fixes + taux de change réels du jour (USD/CAD, EUR/CAD).
- Rédaction du rapport en français via l'**API Anthropic** (Claude), avec tous les tarifs convertis en CAD.
- Génération d'un **PDF façon magazine** (WeasyPrint) et mise à jour d'un **site d'archive HTML** (GitHub Pages) — c'est là que le rapport hebdomadaire se consulte, chaque dimanche.
- Automatisation complète via **GitHub Actions**.

## Structure du projet

```
main.py                     # point d'entrée / orchestrateur
config.py                   # thèmes, constantes, variables d'environnement
services/                   # Tavily, taux de change, Anthropic
generators/                 # génération PDF + régénération du site statique
templates/                  # gabarits Jinja2 + CSS (web et PDF)
reports/                    # historique brut (source de vérité, committé sur main)
site/                       # build du site (régénéré à chaque run, jamais committé sur main)
.github/workflows/weekly_report.yml
```

## Mise en place (à faire une seule fois)

### 1. Créer le dépôt GitHub

Aucun `gh` CLI n'est installé sur cette machine — création manuelle requise :

1. Aller sur [github.com/new](https://github.com/new) et créer un dépôt **vide** (sans README/licence/gitignore), par ex. `agent-veille-ia-hebdomadaire`.
2. Copier l'URL du dépôt (ex. `https://github.com/<ton-utilisateur>/agent-veille-ia-hebdomadaire.git`).
3. Revenir ici et me donner cette URL — je ferai `git init`, le premier commit et le push.

   Ou manuellement :
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <URL_DU_DEPOT>
   git push -u origin main
   ```

### 2. Ajouter les secrets GitHub

Dans le dépôt : **Settings → Secrets and variables → Actions → New repository secret**. Ajouter :

| Secret | Description |
|---|---|
| `TAVILY_API_KEY` | Clé API Tavily (⚠️ régénère la clé fournie initialement dans le chat — elle a été exposée) |
| `ANTHROPIC_API_KEY` | Clé API Anthropic |

### 3. Activer GitHub Pages

Après le tout premier run réussi du workflow (qui crée la branche `gh-pages`) :
**Settings → Pages → Source → Deploy from a branch → `gh-pages` / `root`**.

Le site sera ensuite disponible à `https://<ton-utilisateur>.github.io/<nom-du-depot>/`.

### 4. Vérifier la programmation automatique

Le workflow est programmé pour s'exécuter chaque dimanche à 6h00, heure de Québec (le fichier gère automatiquement le passage heure d'été/heure d'hiver — voir commentaires dans `weekly_report.yml`). Aucune action requise.

## Test en local

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt

copy .env.example .env
# ... remplir .env avec tes clés ...

python main.py
```

Vérifie ensuite :
- `reports/<date>/report.md` et `metadata.json` (historique)
- `reports/<date>/rapport.pdf` (PDF généré)
- `site/index.html` et `site/reports/<date>/index.html` (site, ouvrir dans un navigateur)

> Note Windows : WeasyPrint nécessite les bibliothèques GTK (Pango/Cairo). Le plus simple en local est d'utiliser **WSL** ou un conteneur ; en production, le workflow GitHub Actions (Ubuntu) installe automatiquement tout ce qu'il faut.

## Déclenchement manuel du workflow

Dans l'onglet **Actions** du dépôt → sélectionner "Rapport hebdomadaire de veille IA" → **Run workflow**. Ce mode ignore la vérification d'heure locale et s'exécute immédiatement — utile pour tester la chaîne complète (génération → commit → déploiement).

## Consulter le rapport

Le site est mis à jour automatiquement chaque dimanche. Une fois GitHub Pages activé (étape 3), il suffit d'aller à `https://<ton-utilisateur>.github.io/<nom-du-depot>/` pour lire le dernier rapport ou consulter l'archive complète — aucun courriel n'est envoyé, la consultation se fait directement sur le site.

## Sécurité

- Aucune clé API n'est codée en dur dans le code — tout passe par des variables d'environnement / secrets GitHub.
- La clé Tavily initialement partagée en clair dans la conversation doit être régénérée avant la mise en production.
- Le site publié sur GitHub Pages est **public** (limitation du plan GitHub gratuit) ; le contenu (veille technologique) n'est pas sensible.
