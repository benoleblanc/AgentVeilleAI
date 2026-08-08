"""
Envoi du rapport PDF par courriel via SMTP (identifiants fournis en secrets).
"""
import logging
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import config

logger = logging.getLogger(__name__)


def envoyer_rapport_par_courriel(pdf_path: Path, titre_rapport: str, teaser: str, date_rapport: str) -> None:
    if not all([config.SMTP_SERVER, config.SENDER_EMAIL, config.SENDER_PASSWORD, config.RECEIVER_EMAIL]):
        logger.warning(
            "Configuration SMTP incomplète (SMTP_SERVER/SENDER_EMAIL/SENDER_PASSWORD/RECEIVER_EMAIL) "
            "— envoi du courriel ignoré."
        )
        return

    message = MIMEMultipart()
    message["From"] = config.SENDER_EMAIL
    message["To"] = config.RECEIVER_EMAIL
    message["Subject"] = f"🧠 Veille IA Hebdomadaire — {date_rapport} — {titre_rapport}"

    corps = f"""Bonjour,

Voici le rapport de veille IA de la semaine, généré automatiquement.

{titre_rapport}
{teaser}

Le rapport complet est en pièce jointe (PDF), et l'archive complète est disponible en ligne.

— Agent de Veille IA Hebdomadaire
"""
    message.attach(MIMEText(corps, "plain", "utf-8"))

    with open(pdf_path, "rb") as f:
        piece_jointe = MIMEApplication(f.read(), _subtype="pdf")
        piece_jointe.add_header(
            "Content-Disposition", "attachment", filename=f"veille-ia-{date_rapport}.pdf"
        )
        message.attach(piece_jointe)

    logger.info("Envoi du courriel à %s via %s:%s...", config.RECEIVER_EMAIL, config.SMTP_SERVER, config.SMTP_PORT)
    with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as serveur:
        serveur.starttls()
        serveur.login(config.SENDER_EMAIL, config.SENDER_PASSWORD)
        serveur.send_message(message)

    logger.info("Courriel envoyé avec succès.")
