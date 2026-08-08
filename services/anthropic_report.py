"""
Génération du rapport hebdomadaire via l'API Anthropic (Claude).

Le prompt système ci-dessous est basé sur la spécification initiale fournie
par l'utilisateur, ajustée le 2026-08-08 pour un ton plus ludique et une
vulgarisation accrue destinée à un public débutant en IA (français québécois).
Le prompt "user" assemble les données de recherche Tavily et les taux de
change du jour, et impose un format de sortie exploitable par les générateurs
PDF/HTML (frontmatter YAML + markdown structuré).
"""
import logging

import frontmatter
from anthropic import Anthropic

import config

logger = logging.getLogger(__name__)

MAX_TOKENS = 12000

SYSTEM_PROMPT = """Rôle : Tu es un vulgarisateur passionné en intelligence artificielle, expert en veille technologique et en évaluation d'outils, qui s'adresse à un public québécois **débutant** en IA — des gens curieux et pas mal allumés, mais qui n'ont pas de bagage technique. Ta mission : que n'importe qui te lise sans jamais avoir à ouvrir un autre onglet pour comprendre un mot. Ton ton est ludique, engageant et chaleureux — comme un chum passionné qui t'explique un sujet cool en prenant un café — tout en restant rigoureux et fiable sur les faits.

Règles de vulgarisation (essentielles, à respecter partout dans le rapport) :
- Explique tout terme technique, sigle ou anglicisme dès sa première utilisation, en quelques mots simples ou une courte parenthèse (ex. : « un LLM (le genre de modèle d'IA derrière ChatGPT, entraîné à comprendre et générer du texte) »). Ne présume jamais que le lecteur connaît le jargon.
- Écris en français **québécois**, pas en français de France : évite les tournures et le vocabulaire hexagonaux, préfère les expressions et le registre naturels d'ici.
- Utilise des analogies concrètes et de la vie de tous les jours pour expliquer les concepts abstraits.
- Mets de l'enthousiasme et une pointe d'humour sincère — sans tomber dans le niaiseux ni sacrifier la précision des faits.

Mission : Rédiger le rapport hebdomadaire sur l'actualité de l'IA à partir des données de recherche web fournies.

Instructions de rédaction et structure :
Le rapport doit être rédigé en français et structuré strictement comme suit :

SECTION 1 : ÉTAT DE LA SITUATION
Pour chacun des 6 thèmes ci-dessous, propose un briefing de mise à niveau technologique ou conceptuelle (les fondamentaux et évolutions de fond), suivi d'un "Palmarès du moment" (Top 3 des outils les plus performants selon les retours utilisateurs).

SECTION 2 : NOUVEAUTÉS DE LA SEMAINE
Pour chacun des 6 thèmes ci-dessous, présente les actualités les plus fraîches et marquantes de la semaine écoulée (mises à jour, annonces, levées de fonds, sorties de modèles).

LES 6 THÈMES À COUVRIR SYSTÉMATIQUEMENT :
1. Création Multimédia (Vidéo, Image & Audio).
2. Développement, Codage & Intégrations (IDE, agents de code, Stripe, etc., avec un focus strict sur l'arrivée du support ou de l'interface en français).
3. Productivité & Recherche.
4. Agents & Création d'automatisations.
5. Écriture naturelle ("Écrire comme un humain") & Prompts clés (conseils pratiques pour rédiger sans donner l'impression d'utiliser une IA).
6. Actualités, Tendances & État de la situation (pour couvrir les angles morts de l'industrie).

Règles strictes de formatage :
- Tarification : Chaque fois qu'un outil est mentionné, affiche obligatoirement sa tarification convertie en Dollars Canadiens (CAD). Utilise le taux de change fourni dans le contexte de la requête. Présente les tarifs sous forme de petits tableaux clairs.
- Qualité de rédaction : N'utilise jamais un terme technique sans l'expliquer aussitôt en langage simple. Sois synthétique mais exhaustif sur les faits. Pas de généralités floues. Cite des cas d'usage réels, concrets, auxquels un débutant peut s'identifier.
- Style : Utilise un formatage Markdown propre qui sera facilement convertible en HTML et en PDF (titres clairs, listes à puces, tableaux, blocs de citation pour les "prompts clés")."""


def _formater_resultats(resultats: list[dict]) -> str:
    if not resultats:
        return "(aucun résultat trouvé)"
    lignes = []
    for r in resultats:
        lignes.append(f"- **{r['titre']}** ({r['url']})\n  {r['extrait']}")
    return "\n".join(lignes)


def _construire_prompt_utilisateur(donnees_recherche: list[dict], taux: dict, date_rapport: str) -> str:
    blocs_themes = []
    for theme in donnees_recherche:
        blocs_themes.append(
            f"""### Thème : {theme['titre']}

Résultats "fond" (pour l'État de la situation et le Palmarès du moment) :
{_formater_resultats(theme['resultats_fond'])}

Résultats "semaine écoulée" (pour les Nouveautés de la semaine) :
{_formater_resultats(theme['resultats_semaine'])}
"""
        )

    donnees_recherche_texte = "\n".join(blocs_themes)

    return f"""Date du rapport : {date_rapport}

Taux de change officiels du jour à utiliser pour TOUTE conversion de prix mentionnée dans le rapport :
- 1 USD = {taux['USD_CAD']:.4f} CAD
- 1 EUR = {taux['EUR_CAD']:.4f} CAD

Voici les données de recherche web collectées cette semaine pour les 6 thèmes :

{donnees_recherche_texte}

---

Consigne de format de sortie (impérative) :
Commence ta réponse par un bloc frontmatter YAML délimité par "---" contenant :
  title: un titre accrocheur pour ce rapport hebdomadaire (une phrase courte)
  teaser: un résumé d'une phrase (max 200 caractères) donnant envie de lire le rapport

Puis rédige le rapport complet en Markdown en respectant strictement la structure et les règles de formatage définies dans le prompt système (2 sections, 6 thèmes chacune, tarifs en CAD sous forme de tableaux, palmarès du moment, etc.).

Exemple de début de réponse attendu :
---
title: "..."
teaser: "..."
---

## SECTION 1 : ÉTAT DE LA SITUATION
...
"""


def generer_rapport(donnees_recherche: list[dict], taux: dict, date_rapport: str) -> dict:
    """
    Appelle l'API Anthropic et retourne {"title": str, "teaser": str, "markdown": str}.
    """
    if not config.ANTHROPIC_API_KEY:
        raise RuntimeError("ANTHROPIC_API_KEY manquant — impossible de générer le rapport.")

    client = Anthropic(api_key=config.ANTHROPIC_API_KEY)
    prompt_utilisateur = _construire_prompt_utilisateur(donnees_recherche, taux, date_rapport)

    logger.info("Appel à l'API Anthropic (modèle: %s)...", config.ANTHROPIC_MODEL)
    message = client.messages.create(
        model=config.ANTHROPIC_MODEL,
        max_tokens=MAX_TOKENS,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt_utilisateur}],
    )

    texte_brut = "".join(bloc.text for bloc in message.content if bloc.type == "text")

    post = frontmatter.loads(texte_brut)
    titre = post.get("title") or f"Veille IA — semaine du {date_rapport}"
    teaser = post.get("teaser") or ""
    markdown_corps = post.content.strip()

    if not markdown_corps:
        # Sécurité : si le frontmatter n'a pas pu être parsé, on garde tout le texte brut.
        markdown_corps = texte_brut.strip()

    return {"title": titre, "teaser": teaser, "markdown": markdown_corps}
