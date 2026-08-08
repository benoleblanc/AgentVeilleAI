"""
Utilitaires partagés entre le générateur PDF et le générateur de site :
conversion Markdown → HTML et environnement de templates Jinja2.
"""
import markdown as md_lib
from jinja2 import Environment, FileSystemLoader, select_autoescape

import config

_jinja_env = Environment(
    loader=FileSystemLoader(str(config.TEMPLATES_DIR)),
    autoescape=select_autoescape(["html", "j2"]),
)

MARKDOWN_EXTENSIONS = ["tables", "fenced_code", "nl2br", "sane_lists", "toc"]


def get_template(nom_fichier: str):
    return _jinja_env.get_template(nom_fichier)


def markdown_vers_html(texte_markdown: str) -> str:
    return md_lib.markdown(texte_markdown, extensions=MARKDOWN_EXTENSIONS)


def lire_css(nom_fichier: str) -> str:
    return (config.TEMPLATES_DIR / nom_fichier).read_text(encoding="utf-8")
