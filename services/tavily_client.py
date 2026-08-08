"""
Collecte des actualités IA de la semaine via l'API Tavily, pour chacun des 6 thèmes.

Pour chaque thème, on effectue deux recherches distinctes :
  - une recherche "de fond" (état de la situation / palmarès des outils),
  - une recherche bornée à la semaine écoulée (nouveautés).
"""
import logging

from tavily import TavilyClient

import config

logger = logging.getLogger(__name__)

MAX_RESULTS_PAR_REQUETE = 6


def _search(client: TavilyClient, query: str, time_range: str | None = None) -> list[dict]:
    try:
        params = {
            "query": query,
            "search_depth": "advanced",
            "max_results": MAX_RESULTS_PAR_REQUETE,
            "include_answer": False,
        }
        if time_range:
            params["time_range"] = time_range
        result = client.search(**params)
        return [
            {
                "titre": r.get("title", ""),
                "url": r.get("url", ""),
                "extrait": r.get("content", ""),
            }
            for r in result.get("results", [])
        ]
    except Exception:
        logger.exception("Échec de la recherche Tavily pour la requête: %s", query)
        return []


def collecter_recherches_par_theme() -> list[dict]:
    """
    Retourne une liste (une entrée par thème) contenant les résultats
    de recherche "fond" et "actualité de la semaine".
    """
    if not config.TAVILY_API_KEY:
        raise RuntimeError("TAVILY_API_KEY manquant — impossible d'effectuer les recherches.")

    client = TavilyClient(api_key=config.TAVILY_API_KEY)
    donnees = []

    for theme in config.THEMES:
        logger.info("Recherche Tavily — thème: %s", theme["titre"])
        resultats_fond = _search(client, theme["requete_fond"])
        resultats_semaine = _search(client, theme["requete_actualite"], time_range="week")

        donnees.append(
            {
                "id": theme["id"],
                "titre": theme["titre"],
                "resultats_fond": resultats_fond,
                "resultats_semaine": resultats_semaine,
            }
        )

    return donnees
