"""
Configuration centrale de l'Agent de Veille IA Hebdomadaire.

Toutes les valeurs sensibles (clés API) sont chargées
depuis les variables d'environnement — jamais codées en dur ici.
En local, elles peuvent être fournies via un fichier .env (voir .env.example).
"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()  # no-op silencieux si aucun .env n'est présent (ex: CI)

# --- Chemins du projet ---------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parent
REPORTS_DIR = ROOT_DIR / "reports"       # historique brut, source de vérité (committé sur main)
SITE_DIR = ROOT_DIR / "site"             # build regénéré à chaque run (poussé sur gh-pages)
TEMPLATES_DIR = ROOT_DIR / "templates"

# --- Clés API / secrets ---------------------------------------------------
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY", "")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
ANTHROPIC_MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-5")

# Site public une fois déployé (référence informative, ex. dans le README)
SITE_BASE_URL = os.environ.get("SITE_BASE_URL", "")

# Mode de test local : désactive la génération PDF (WeasyPrint nécessite des
# librairies natives absentes par défaut sur Windows).
# Ne jamais activer en production (le workflow GitHub Actions ne le définit pas).
SKIP_PDF = os.environ.get("SKIP_PDF", "false").lower() == "true"

# --- Les 7 thèmes couverts systématiquement chaque semaine ----------------
THEMES = [
    {
        "id": "creation-multimedia",
        "titre": "Création Multimédia (Vidéo, Image & Audio)",
        "requete_fond": "meilleurs outils IA génération vidéo image audio comparatif 2026",
        "requete_actualite": "actualité IA génération vidéo image audio cette semaine annonce",
    },
    {
        "id": "developpement-codage",
        "titre": "Développement, Codage & Intégrations",
        "requete_fond": "meilleurs outils IA codage agents de code IDE comparatif intégration",
        "requete_actualite": "actualité IA codage IDE agent de code intégration cette semaine",
    },
    {
        "id": "plateformes-paiement",
        "titre": "Plateformes de Paiement (Merchant of Record) pour vendre par abonnement",
        "requete_fond": "meilleures plateformes paiement Merchant of Record abonnement SaaS gestion taxes comparatif Stripe Paddle Lemon Squeezy FastSpring Chargebee",
        "requete_actualite": "actualité plateforme paiement Merchant of Record abonnement SaaS interface français nouveauté cette semaine",
    },
    {
        "id": "productivite-recherche",
        "titre": "Productivité & Recherche",
        "requete_fond": "meilleurs outils IA productivité recherche assistant comparatif 2026",
        "requete_actualite": "actualité IA productivité recherche assistant nouveauté cette semaine",
    },
    {
        "id": "agents-automatisations",
        "titre": "Agents & Création d'automatisations",
        "requete_fond": "meilleurs outils agents IA automatisation no-code comparatif 2026",
        "requete_actualite": "actualité agents IA automatisation nouveauté lancement cette semaine",
    },
    {
        "id": "ecriture-naturelle",
        "titre": "Écriture naturelle (\"Écrire comme un humain\") & Prompts clés",
        "requete_fond": "meilleurs outils IA écriture humaine détection contournement style naturel",
        "requete_actualite": "actualité outils IA écriture naturelle humanisation texte prompts cette semaine",
    },
    {
        "id": "actualites-tendances",
        "titre": "Actualités, Tendances & État de la situation",
        "requete_fond": "état de l'industrie intelligence artificielle tendances de fond 2026",
        "requete_actualite": "actualité intelligence artificielle levée de fonds sortie de modèle cette semaine",
    },
]
