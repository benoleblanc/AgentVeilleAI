"""
Gestion de l'historique (reports/, source de vérité sur la branche main)
et régénération complète du site statique (site/, poussé sur gh-pages).
"""
import json
import logging
import shutil

import frontmatter

import config
from generators.common import get_template, lire_css, markdown_vers_html

logger = logging.getLogger(__name__)


def sauvegarder_historique(rapport: dict, taux: dict, date_rapport: str, date_affichage: str) -> None:
    """Écrit reports/<date>/report.md (avec frontmatter) et metadata.json."""
    dossier = config.REPORTS_DIR / date_rapport
    dossier.mkdir(parents=True, exist_ok=True)

    post = frontmatter.Post(
        rapport["markdown"],
        title=rapport["title"],
        teaser=rapport["teaser"],
        date=date_rapport,
    )
    (dossier / "report.md").write_text(frontmatter.dumps(post), encoding="utf-8")

    metadata = {
        "date": date_rapport,
        "date_affichage": date_affichage,
        "title": rapport["title"],
        "teaser": rapport["teaser"],
        "taux": taux,
    }
    (dossier / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    logger.info("Historique sauvegardé: %s", dossier)


def charger_historique() -> list[dict]:
    """Retourne tous les rapports passés (metadata.json), triés du plus récent au plus ancien."""
    if not config.REPORTS_DIR.exists():
        return []

    entrees = []
    for meta_path in sorted(config.REPORTS_DIR.glob("*/metadata.json")):
        try:
            entrees.append(json.loads(meta_path.read_text(encoding="utf-8")))
        except Exception:
            logger.exception("Impossible de lire %s — entrée ignorée.", meta_path)

    entrees.sort(key=lambda e: e["date"], reverse=True)
    return entrees


def regenerer_site() -> None:
    """
    Reconstruit entièrement site/ à partir de l'historique complet (reports/).
    Le résultat peut être poussé tel quel sur gh-pages sans conserver l'ancien contenu.
    """
    historique = charger_historique()

    if config.SITE_DIR.exists():
        shutil.rmtree(config.SITE_DIR)
    config.SITE_DIR.mkdir(parents=True)

    css_web = lire_css("style_web.css")
    template_rapport = get_template("report.html.j2")

    for entree in historique:
        dossier_source = config.REPORTS_DIR / entree["date"]
        report_md_path = dossier_source / "report.md"
        pdf_source = dossier_source / "rapport.pdf"

        if not report_md_path.exists():
            logger.warning("report.md manquant pour %s — entrée ignorée.", entree["date"])
            continue

        post = frontmatter.loads(report_md_path.read_text(encoding="utf-8"))
        content_html = markdown_vers_html(post.content)

        taux = entree.get("taux") or {}
        html_final = template_rapport.render(
            mode="web",
            title=entree["title"],
            teaser=entree["teaser"],
            content_html=content_html,
            date_rapport=entree["date"],
            date_affichage=entree["date_affichage"],
            taux={
                "USD_CAD": f"{taux.get('USD_CAD', 0):.4f}",
                "EUR_CAD": f"{taux.get('EUR_CAD', 0):.4f}",
            },
            css=css_web,
        )

        dossier_dest = config.SITE_DIR / "reports" / entree["date"]
        dossier_dest.mkdir(parents=True, exist_ok=True)
        (dossier_dest / "index.html").write_text(html_final, encoding="utf-8")

        if pdf_source.exists():
            shutil.copy2(pdf_source, dossier_dest / "rapport.pdf")
        else:
            logger.warning("PDF manquant pour %s", entree["date"])

    template_index = get_template("index.html.j2")
    index_html = template_index.render(reports=historique, css=css_web)
    (config.SITE_DIR / "index.html").write_text(index_html, encoding="utf-8")

    logger.info("Site régénéré avec succès: %d rapport(s) archivé(s).", len(historique))
