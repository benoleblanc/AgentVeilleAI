#!/usr/bin/env python3
"""
Agent de Veille IA Hebdomadaire — point d'entrée.

Exécuté chaque dimanche à 6h00 (heure de Québec) via GitHub Actions :
  1. Recherche web (Tavily) sur 6 thèmes + taux de change du jour (USD/CAD, EUR/CAD).
  2. Rédaction du rapport en français via l'API Anthropic (Claude).
  3. Génération du PDF (style magazine) et mise à jour du site d'archive HTML.
  4. Envoi du PDF par courriel.
"""
import logging
import sys
from datetime import datetime, timezone

import config
from generators.pdf_generator import generer_pdf
from generators.site_generator import regenerer_site, sauvegarder_historique
from services.anthropic_report import generer_rapport
from services.email_sender import envoyer_rapport_par_courriel
from services.exchange_rates import obtenir_taux_de_change
from services.tavily_client import collecter_recherches_par_theme

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("main")

MOIS_FR = [
    "janvier", "février", "mars", "avril", "mai", "juin",
    "juillet", "août", "septembre", "octobre", "novembre", "décembre",
]


def formater_date_affichage(dt: datetime) -> str:
    return f"{dt.day} {MOIS_FR[dt.month - 1]} {dt.year}"


def main() -> int:
    maintenant = datetime.now(timezone.utc)
    date_rapport = maintenant.strftime("%Y-%m-%d")
    date_affichage = formater_date_affichage(maintenant)

    logger.info("=== Agent de Veille IA Hebdomadaire — %s ===", date_rapport)

    # 1. Taux de change (ne bloque pas le run en cas d'échec partiel — valeurs de repli utilisées)
    logger.info("Étape 1/5 — Récupération des taux de change...")
    taux = obtenir_taux_de_change()
    if not taux["source_reelle"]:
        logger.warning("Taux de change de repli utilisés (API indisponible).")
    logger.info("Taux du jour: 1 USD = %.4f CAD | 1 EUR = %.4f CAD", taux["USD_CAD"], taux["EUR_CAD"])

    # 2. Recherche web
    logger.info("Étape 2/5 — Recherche web Tavily sur les 6 thèmes...")
    try:
        donnees_recherche = collecter_recherches_par_theme()
    except Exception:
        logger.exception("Échec critique de la recherche web — arrêt du run.")
        return 1

    # 3. Génération du rapport (Anthropic)
    logger.info("Étape 3/5 — Rédaction du rapport via l'API Anthropic...")
    try:
        rapport = generer_rapport(donnees_recherche, taux, date_rapport)
    except Exception:
        logger.exception("Échec critique de la génération du rapport — arrêt du run.")
        return 1
    logger.info("Rapport généré: « %s »", rapport["title"])

    # 4. Sauvegarde historique + PDF + régénération du site
    logger.info("Étape 4/5 — Génération des livrables (historique, PDF, site)...")
    pdf_path = config.REPORTS_DIR / date_rapport / "rapport.pdf"
    try:
        sauvegarder_historique(rapport, taux, date_rapport, date_affichage)
        if config.SKIP_PDF:
            logger.warning("SKIP_PDF actif — génération du PDF ignorée (mode test local).")
        else:
            generer_pdf(rapport, taux, date_rapport, date_affichage, pdf_path)
        regenerer_site()
    except Exception:
        logger.exception("Échec critique de la génération des livrables — arrêt du run.")
        return 1

    # 5. Envoi par courriel (non bloquant : un échec ici ne doit pas faire échouer tout le run,
    #    puisque le rapport est déjà sauvegardé et le site déjà régénéré)
    if config.SKIP_PDF:
        logger.warning("SKIP_PDF actif — envoi du courriel ignoré (pas de PDF à joindre).")
    else:
        logger.info("Étape 5/5 — Envoi du rapport par courriel...")
        try:
            envoyer_rapport_par_courriel(pdf_path, rapport["title"], rapport["teaser"], date_rapport)
        except Exception:
            logger.exception("Échec de l'envoi du courriel (le rapport reste disponible sur le site).")

    logger.info("=== Run terminé avec succès ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
