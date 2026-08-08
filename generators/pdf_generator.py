"""
Génération du PDF "façon magazine" à partir du markdown du rapport, via WeasyPrint.
"""
import logging
from pathlib import Path

from generators.common import get_template, lire_css, markdown_vers_html

logger = logging.getLogger(__name__)


def generer_pdf(rapport: dict, taux: dict, date_rapport: str, date_affichage: str, destination: Path) -> None:
    """
    rapport: {"title": str, "teaser": str, "markdown": str}

    Import de WeasyPrint différé (plutôt qu'en tête de module) : la bibliothèque
    dépend de librairies natives (Pango/GObject) absentes par défaut sur Windows.
    Ainsi, le reste de l'application reste testable localement même sans ces
    dépendances système — seul un appel à cette fonction les requiert.
    """
    from weasyprint import HTML

    content_html = markdown_vers_html(rapport["markdown"])
    template = get_template("report.html.j2")

    html_final = template.render(
        mode="pdf",
        title=rapport["title"],
        teaser=rapport["teaser"],
        content_html=content_html,
        date_rapport=date_rapport,
        date_affichage=date_affichage,
        taux={"USD_CAD": f"{taux['USD_CAD']:.4f}", "EUR_CAD": f"{taux['EUR_CAD']:.4f}"},
        css=lire_css("style_pdf.css"),
    )

    destination.parent.mkdir(parents=True, exist_ok=True)
    logger.info("Génération du PDF: %s", destination)
    HTML(string=html_final, base_url=str(destination.parent)).write_pdf(str(destination))
