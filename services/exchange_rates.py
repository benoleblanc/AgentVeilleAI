"""
Récupération des taux de change réels du jour USD/CAD et EUR/CAD
via l'API gratuite et sans clé open.er-api.com.
"""
import logging

import requests

logger = logging.getLogger(__name__)

API_URL = "https://open.er-api.com/v6/latest/{base}"
TIMEOUT_SECONDES = 15

# Valeurs de repli si l'API est indisponible (approximatives, avertissement inclus dans le rapport)
TAUX_PAR_DEFAUT = {"USD_CAD": 1.38, "EUR_CAD": 1.49}


def _taux_vers_cad(devise_base: str) -> float | None:
    try:
        reponse = requests.get(API_URL.format(base=devise_base), timeout=TIMEOUT_SECONDES)
        reponse.raise_for_status()
        data = reponse.json()
        if data.get("result") != "success":
            raise ValueError(f"Réponse API inattendue: {data}")
        return float(data["rates"]["CAD"])
    except Exception:
        logger.exception("Échec de récupération du taux %s/CAD", devise_base)
        return None


def obtenir_taux_de_change() -> dict:
    """
    Retourne un dict: {"USD_CAD": float, "EUR_CAD": float, "source_reelle": bool}
    """
    usd_cad = _taux_vers_cad("USD")
    eur_cad = _taux_vers_cad("EUR")

    source_reelle = usd_cad is not None and eur_cad is not None

    return {
        "USD_CAD": usd_cad or TAUX_PAR_DEFAUT["USD_CAD"],
        "EUR_CAD": eur_cad or TAUX_PAR_DEFAUT["EUR_CAD"],
        "source_reelle": source_reelle,
    }
