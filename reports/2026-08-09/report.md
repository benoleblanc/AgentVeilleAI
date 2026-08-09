---
date: '2026-08-09'
teaser: 'Vidéo IA à 30 secondes, agents qui piratent des entreprises, Claude plus
  humain que jamais : ton topo complet sur l''IA, sans jargon, avec les prix en dollars
  canadiens.'
title: 'Seedance 2.5, agents qui pètent les scores et Claude qui écrit comme du monde
  : le récap IA de la semaine'
---

Salut la gang ! ☕ Encore une semaine de fou dans le monde de l'IA — on jase de vidéos générées par ordi qui font limite peur de réalisme, d'agents qui commencent à agir tout seuls (parfois un peu trop), pis de trucs pour écrire sans que ton monde pense que c'est un robot qui a pondu ton courriel. Assis-toi, prends ton café, pis embarque : je t'explique tout ça comme si on jasait sur le perron.

**Petite note technique avant de partir :** tous les prix mentionnés dans ce rapport sont convertis en dollars canadiens (CAD) selon les taux du jour — 1 $US = 1,3956 $CA et 1 € = 1,6122 $CA.

---

## SECTION 1 : ÉTAT DE LA SITUATION

### 1. Création Multimédia (Vidéo, Image & Audio)

**Le topo :** En 2026, la génération vidéo par IA (créer un clip vidéo juste à partir d'un texte ou d'une image, sans caméra ni acteur) est rendue tellement bonne qu'on compare maintenant les modèles entre eux avec un **score ELO** — le même système de classement qu'aux échecs, où de vraies personnes votent à l'aveugle pour dire quelle vidéo est la plus crédible. Les modèles les plus forts génèrent maintenant en **1080p ou même 4K** (la résolution de l'image, plus le chiffre est haut, plus c'est net), avec du **son synchronisé nativement** — autrement dit, l'audio (dialogues, bruits d'ambiance) est créé en même temps que l'image, pile à la bonne frame, sans avoir à recoller le son après coup en post-production.

L'autre grosse tendance : les modèles dits **« multimodaux unifiés »**, qui acceptent plusieurs types d'entrées en même temps (texte, image, vidéo de référence, audio) dans une seule requête. Ça évite de jongler avec cinq applications différentes pour un seul projet.

#### 🏆 Palmarès du moment

| Rang | Outil | Spécialité | Ce qui le démarque |
|---|---|---|---|
| 1 | **Gemini Omni Flash** (Google) | Vidéo texte-vers-vidéo | Score ELO le plus haut du moment (1245), Google a carrément fusionné la vidéo dans sa famille Gemini plutôt que sortir un « Veo 4 » séparé |
| 2 | **MiniMax H3 / Hailuo 3.0** | Vidéo + audio | Entrée fracassante, open source, son stéréo natif généré dans la même passe |
| 3 | **ElevenLabs** | Voix & audio | La référence pour cloner des voix réalistes en plusieurs langues — parfait pour un podcast ou un livre audio |

**Mentions honorables :** Kling, Seedance (ByteDance), Luma Dream Machine et LTX-2.3 (le seul modèle qui roule **localement sur ton ordi**, sans internet — bon point pour la confidentialité).

| Outil | Tarif original | Tarif en CAD |
|---|---|---|
| LTX-2.3 (API) | 0,04 $US/seconde | **0,06 $CA/seconde** |
| HappyHorse 1.1 (Alibaba) | 9,90 $US/minute | **13,82 $CA/minute** |
| Seedance 2.0 | Accès gratuit + formules payantes abordables (montants non précisés) | — |

---

### 2. Développement, Codage & Intégrations

**Le topo :** Un **agent de codage** (coding agent), c'est un cran au-dessus d'un simple autocomplétion de code : il peut lire ta base de code au complet, exécuter des commandes, réparer ses propres bogues, et même gérer plusieurs fichiers en même temps sans que tu lui tiennes la main à chaque ligne. On distingue trois familles : les outils **intégrés à un IDE** (l'environnement où tu écris ton code, comme VS Code), les agents **en ligne de commande/terminal** (pour les mordus qui aiment le clavier plus que la souris), et les agents **asynchrones** qui travaillent en arrière-plan pendant que tu fais autre chose.

Sur le plan du **français** : les gros noms comme Cursor, Claude Code et GitHub Copilot comprennent déjà très bien le français dans leurs conversations (vu que ce sont des LLM multilingues), mais aucune interface dédiée ou support francophone officiel n'a été annoncé cette semaine spécifiquement — on garde ça à l'œil pour les prochaines semaines.

#### 🏆 Palmarès du moment

| Rang | Outil | Idéal pour |
|---|---|---|
| 1 | **Claude Code** (Anthropic) | Le codage profond en ligne de commande — la référence pour le raisonnement sur du code complexe |
| 2 | **Cursor** | L'IDE le plus léché, remplace VS Code pour bien des devs pros |
| 3 | **GitHub Copilot** | Le standard intégré nativement à VS Code et JetBrains |

| Outil | Tarif original | Tarif en CAD/mois |
|---|---|---|
| Cursor | Gratuit / 20 $US / 60 $US / 200 $US | Gratuit / **27,91 $** / **83,74 $** / **279,12 $** |
| Windsurf | Gratuit / 15 $US / 60 $US | Gratuit / **20,93 $** / **83,74 $** |
| GitHub Copilot | 10-19 € | **16,12 $ à 30,63 $** |
| Claude Code | 20-30 € | **32,24 $ à 48,37 $** |
| JetBrains AI Assistant | Gratuit / ~12 $US / ~19 $US | Gratuit / **16,75 $** / **26,52 $** |

---

### 3. Productivité & Recherche

**Le topo :** Les moteurs de recherche IA (comme Perplexity) remplacent tranquillement Google pour ben du monde : au lieu de te donner une liste de liens, l'IA lit le web à ta place et te sort une réponse synthétisée avec les sources citées. Le **« Deep Research »**, c'est une fonction où l'IA fait une vraie recherche approfondie (plusieurs minutes, dizaines de sources) plutôt qu'une réponse rapide — utile pour un vrai travail de recherche, pas juste une question anodine.

#### 🏆 Palmarès du moment

| Rang | Outil | Pourquoi il gagne |
|---|---|---|
| 1 | **Perplexity** | Le « gold standard » de la recherche sourcée — transparent sur ses sources |
| 2 | **ChatGPT (avec Deep Research)** | Polyvalent : recherche, rédaction, analyse de documents, tout en un |
| 3 | **Fireflies.ai** | Transcrit et résume tes réunions Zoom/Teams automatiquement — le stagiaire qui prend des notes à ta place |

| Outil | Tarif |
|---|---|
| ChatGPT Plus | 20 $US → **27,91 $CA**/mois |
| Claude Pro / Max | 20 $US → **27,91 $CA** / 100-200 $US → **139,56 $ à 279,12 $CA**/mois |
| Perplexity | Formule gratuite + payante (montants non précisés dans nos sources cette semaine) |

---

### 4. Agents & Création d'automatisations

**Le topo :** Différence clé à retenir : un **chatbot** suit un script et répond à des questions. Un **agent IA**, lui, peut raisonner, décider quels outils utiliser, exécuter des actions concrètes (appeler une API, fouiller une base de données, écrire un fichier) et gérer une tâche en plusieurs étapes tout seul. Les plateformes **no-code/low-code** (sans avoir à écrire une ligne de code, ou très peu) comme n8n, Zapier et Make permettent à n'importe qui de brancher deux applications ensemble et d'automatiser un processus complet.

#### 🏆 Palmarès du moment

| Rang | Outil | Pourquoi |
|---|---|---|
| 1 | **n8n** | Open source, +300 connecteurs, peut s'auto-héberger, ultra flexible |
| 2 | **Make** (ex-Integromat) | Interface glisser-déposer la plus intuitive du marché |
| 3 | **Zapier** | Le classique, +2000 applications connectées, parfait pour débuter |

| Outil | Tarif original | Tarif en CAD |
|---|---|---|
| Zapier | Gratuit (100 tâches/mois) / 29,99 $US / 103,50 $US | Gratuit / **41,86 $** / **144,45 $**/mois |
| FlowHunt | Gratuit / dès 29 $US | Gratuit / **40,47 $**/mois |
| Lindy | Dès 49,99 $US | **69,77 $**/mois |
| Gumloop | Gratuit / 97 $US | Gratuit / **135,38 $**/mois |

---

### 5. Écriture naturelle ("Écrire comme un humain") & Prompts clés

**Le topo :** Les **détecteurs d'IA** (comme GPTZero, Turnitin ou Originality.ai) analysent ton texte pour repérer des « patterns » typiques de l'IA : phrases trop régulières, vocabulaire trop poli, structure trop parfaite. Résultat : toute une industrie d'**« humaniseurs »** est née pour réécrire un texte IA et le rendre indétectable — mais attention, ces outils ne sont jamais garantis à 100 %, les détecteurs changent chaque semaine.

Le vrai secret pour bien écrire avec l'IA sans que ça sonne robotique : donner des instructions de ton précises, insérer tes propres exemples et anecdotes (ça, l'IA ne peut pas l'inventer à ta place), et **relire toi-même** en coupant le remplissage inutile.

#### 🏆 Palmarès du moment

| Rang | Outil | Pourquoi |
|---|---|---|
| 1 | **Claude** (Anthropic) | Le meilleur pour un ton naturel et le respect des consignes de style, selon plusieurs comparatifs |
| 2 | **Walter Writes AI** | Scores élevés sur Turnitin, GPTZero, ZeroGPT — 80+ langues supportées |
| 3 | **Humanizer (app Mac/iOS)** | 4 modes d'écriture (décontracté, académique, créatif, etc.), score de détection affiché en direct |

| Outil | Tarif original | Tarif en CAD |
|---|---|---|
| Claude Pro | 20 $US/mois | **27,91 $CA**/mois |
| Humanizer (app) | 5,99 $US/semaine / 12,99 $US/mois | **8,36 $CA/semaine** / **18,13 $CA/mois** |
| Jasper AI | 59 $US/mois | **82,34 $CA**/mois |

> 💬 **Prompt clé pour un texte plus humain :**
> « Agis comme un expert. Évalue cette réponse, explique ce qui ne va pas, puis réécris-la en mieux — en variant la longueur des phrases et en évitant les tournures trop parfaites. »

---

### 6. Actualités, Tendances & État de la situation

**Le topo :** Trois grandes lignes de fond façonnent 2026 : (1) l'**IA agentique** — donner un objectif à un système qui se débrouille ensuite pour l'atteindre — devient la norme en entreprise ; (2) les **modèles chinois open source** (DeepSeek, Alibaba, MiniMax, Moonshot, Zhipu) commencent à sérieusement inquiéter la Silicon Valley avec des modèles gratuits et puissants ; (3) après deux ans d'expérimentation tous azimuts, les entreprises passent en mode **« recherche de ROI »** (retour sur investissement) et arrêtent de multiplier les projets pilotes sans lendemain.

#### 🏆 Top 3 tendances à surveiller

1. **L'IA agentique généralisée** — les agents autonomes commencent à agir dans de vraies opérations d'entreprise, avec les risques de sécurité que ça implique.
2. **La montée en puissance chinoise open source** — DeepSeek prépare une levée de fonds historique de 7,4 milliards $US.
3. **La fin du gaspillage IA** — les organisations sélectionnent maintenant 2-3 cas d'usage à fort volume plutôt que de saupoudrer l'IA partout.

---

## SECTION 2 : NOUVEAUTÉS DE LA SEMAINE

### 1. Création Multimédia (Vidéo, Image & Audio)

- **Seedance 2.5 (ByteDance, via Higgsfield)** débarque avec des specs de fou : jusqu'à **30 secondes** de vidéo en un seul plan, **50 références** (images, vidéos, audio, texte) utilisables dans une même génération, édition d'une **zone précise** sans tout régénérer, et audio synchronisé nativement. C'est probablement la plus grosse mise à jour vidéo de l'année selon plusieurs créateurs de contenu qui l'ont testée en primeur.
- **MiniMax H3** vient d'atterrir sur les plateformes d'agrégation d'outils (comme AIxploria) : modèle open source combinant texte, image, vidéo et audio, clips jusqu'à 15 secondes en 2K avec son stéréo natif. API disponible pour les développeurs.
- **InVideo AI** a lancé son **Agent Two**, un agent vidéo pensé pour les cinéastes et agences pub, avec une **mémoire à long terme** (il se souvient des personnages, lieux et style de ton projet même une semaine plus tard) et un montage multi-plans automatisé.
- Attention par contre : des utilisateurs rapportent des **facturations abusives** sur invideo AI (débits en double, crédits jamais reçus) — vérifie toujours tes relevés de carte si tu testes une nouvelle plateforme de génération vidéo.

### 2. Développement, Codage & Intégrations

- **OpenAI et Anthropic** viennent de faire un move surprenant : OpenAI a publié un plugin qui permet à **Codex de réviser le code écrit par Claude Code**, ou de prendre le relais quand Claude bloque. Deux compétiteurs directs qui collaborent plutôt que de s'exclure mutuellement — signe que l'industrie mise maintenant sur l'**interopérabilité**.
- **Claude Code** a lancé un nouveau rendu d'interface en terminal pour régler le fameux problème de scintillement à l'écran (activable via la variable `CLAUDECODENO_FLICKER=1` pour