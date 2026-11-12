---
date: '2026-11-12'
teaser: 'Vidéo 30 secondes en 4K, IntelliJ qui fait rouler 80 agents en parallèle,
  Anthropic qui vise 1 400 G$ en bourse : ton topo complet de la semaine, tout expliqué
  simplement.'
title: 'IA cette semaine : Claude explose, les IDE deviennent des essaims d''agents,
  et le français progresse chez les Merchant of Record'
---

## SECTION 1 : ÉTAT DE LA SITUATION

Avant de plonger dans le "quoi de neuf", faisons un petit *reality check* sur où en est chaque domaine de l'IA en ce moment. Comme ça, même si tu pars de zéro, tu vas suivre le reste du rapport sans perdre le fil.

---

### 1. Création Multimédia (Vidéo, Image & Audio)

**Le topo :** En 2026, la génération vidéo par IA (c'est-à-dire créer une vidéo juste en tapant une description en mots, ou en partant d'une image) est rendue hallucinante de réalisme. Le gros changement de la dernière année : l'**audio natif**, c'est-à-dire que le son (voix, musique, effets) est généré en même temps que l'image, dans le même "passage" du modèle — avant, fallait ajouter le son après coup, un peu comme doubler un film muet. Les meilleurs modèles font aussi du **multi-shot** (plusieurs plans qui s'enchaînent en gardant les mêmes personnages) et acceptent des **références** (tu uploades une photo de ton personnage ou de ton décor, pis le modèle s'en sert pour rester cohérent d'une scène à l'autre).

Le marché se sépare en deux types de joueurs : les **"model studios"** qui créent leur propre modèle (Google, Kuaishou/Kling, ByteDance/Seedance), et les **ateliers multi-modèles** (Runway, Adobe Firefly, Dreamina) qui te donnent accès à plusieurs modèles dans une seule interface, un peu comme un centre d'achats versus des boutiques spécialisées.

**Palmarès du moment :**

| Rang | Outil | Pourquoi il brille |
|---|---|---|
| 🥇 1 | **Google Veo 3.1 (via Flow)** | Le roi du réalisme photo + le seul qui génère un son d'une qualité quasi broadcast en même temps que l'image. Parfait pour une pub réaliste. |
| 🥈 2 | **Kling 3.0 / 4.0 (Kuaishou)** | Imbattable pour le mouvement humain et les scènes d'action ; jusqu'à 30 secondes en continu, 4K, et dialogue synchronisé en 5 langues. |
| 🥉 3 | **Runway Gen-4.5** | Le seul vrai "atelier" tout-en-un : tu génères ET tu montes ta vidéo au même endroit, dans le navigateur. |

**Tarifs (convertis en CAD) :**

| Outil | Prix US/EU affiché | Prix en CAD |
|---|---|---|
| Veo 3.1 (Flow) | Palier gratuit, puis dès 19,99 $ US/mois | ~28,47 $ CAD/mois |
| Kling 3.0 | Dès 6,99 $ US/mois | ~9,95 $ CAD/mois |
| Runway Gen-4.5 | ~14 €/mois | ~22,14 $ CAD/mois |
| Luma Ray3 | 9,99 $ US/mois | ~14,23 $ CAD/mois |
| Pika 2.5 | Dès 7 €/mois | ~11,07 $ CAD/mois |
| Hailuo 2.3 (MiniMax) | 14,99 $ US/mois | ~21,34 $ CAD/mois |

---

### 2. Développement, Codage & Intégrations

**Le topo :** Un **IDE** (Integrated Development Environment — le logiciel où les programmeurs écrivent leur code, un peu comme Word mais pour du code) n'est plus juste un éditeur de texte intelligent : c'est devenu une **plateforme d'agents**. Un **agent de codage**, c'est une IA à qui tu donnes une tâche ("répare ce bug", "ajoute cette fonctionnalité") et qui va lire ton code, l'éditer, lancer des tests, et parfois même déployer le résultat — toute seule, sans que tu valides chaque ligne. La grosse tendance de 2026 : le **travail en parallèle**, où tu lances plusieurs agents en même temps sur différentes tâches, un peu comme avoir plusieurs stagiaires qui travaillent sur ton projet pendant que tu bois ton café.

**Palmarès du moment :**

| Rang | Outil | Pourquoi il brille |
|---|---|---|
| 🥇 1 | **Cursor** | L'IDE le plus populaire chez les devs pros — bâti sur VS Code mais repensé à 100% autour de l'IA, avec des agents qui roulent en arrière-plan. |
| 🥈 2 | **Claude Code (Anthropic)** | Agent "natif terminal" (il tourne en ligne de commande plutôt que dans une fenêtre) très fort pour comprendre des bases de code complexes au complet. |
| 🥉 3 | **GitHub Copilot** | Moins "autonome" que les deux premiers, mais imbattable si ton équipe vit déjà dans l'écosystème GitHub/VS Code. |

**Tarifs (convertis en CAD) :**

| Outil | Prix US affiché | Prix en CAD |
|---|---|---|
| Cursor | Gratuit / 20 $ Pro / 60 $ Pro+ / 200 $ Ultra | ~28,48 $ / 85,44 $ / 284,80 $ CAD/mois |
| Claude Code | Max 100 $/mois, Team 30 $/utilisateur/mois | ~142,40 $ / ~42,72 $ CAD/mois |
| GitHub Copilot | 10 $ à 75 $/mois | ~14,24 $ à 106,80 $ CAD/mois |
| Windsurf | Gratuit / 15 $ à 60 $/mois | ~21,36 $ à 85,44 $ CAD/mois |

---

### 3. Plateformes de Paiement (Merchant of Record) pour vendre par abonnement

**Le topo :** Si tu vends une appli par abonnement à l'international, deux chemins s'offrent à toi. Chemin 1 : tu restes toi-même le vendeur légal (comme avec un processeur de paiement classique style Stripe standard) et TU dois gérer toutes les taxes de vente dans chaque pays où t'as des clients — un vrai cauchemar de paperasse si tu vends partout dans le monde. Chemin 2 : tu passes par un **Merchant of Record (MoR)**, une plateforme qui devient *officiellement* le vendeur à ta place — elle facture le client, calcule et remet les taxes elle-même, et te verse ton montant net. C'est l'équivalent de vendre tes produits à un grossiste qui s'occupe de toute la logistique légale, plutôt que de vendre directement toi-même partout dans le monde.

Le point noir pour nous autres : **l'interface en français reste le parent pauvre** de la plupart de ces plateformes. La majorité des tableaux de bord (back-office) sont en anglais seulement, même si les pages de paiement (checkout) côté client peuvent s'afficher en français dans plusieurs cas.

**Palmarès du moment :**

| Rang | Plateforme | Bonne pour l'abonnement ? | Simple à utiliser ? | Gère les taxes ? | Interface en français ? |
|---|---|---|---|---|---|
| 🥇 1 | **Paddle** | Oui, native (dunning, essais, mises à niveau intégrés) | Oui, assez simple | Oui, 200+ juridictions, 100% MoR | Partiel — checkout multilingue, tableau de bord en anglais |
| 🥈 2 | **Lemon Squeezy** (maintenant intégrée à Stripe Managed Payments) | Oui, bien pour les petites équipes/indies | Oui, très simple | Oui, MoR officiel | Partiel — checkout oui, back-office en anglais |
| 🥉 3 | **FastSpring** | Oui, surtout pour logiciels/entreprises | Moyen — plus de configuration | Oui, MoR mature et éprouvé | Partiel — pages de vente localisables en français, admin en anglais |

**Tarifs (convertis en CAD) :**

| Plateforme | Tarif affiché | Équivalent CAD |
|---|---|---|
| Paddle | 5 % + 0,50 $ US/transaction | 5 % + ~0,71 $ CAD/transaction |
| Lemon Squeezy | 5 % + 0,50 $ US (+1,5 % à l'international) | 5 % + ~0,71 $ CAD/transaction |
| FastSpring | 5,9 % + 0,95 $ US/transaction | 5,9 % + ~1,35 $ CAD/transaction |
| Stripe Managed Payments (alternative) | 3,5 % + frais Stripe standard | 3,5 % + frais standard en CAD |

**Notre recommandation pour un francophone unilingue :** Si tu veux le moins de prise de tête possible avec les taxes internationales, **Paddle** reste le choix le plus solide en 2026 — son taux est clair et tout-inclus (pas de petites surprises cachées), et même si le tableau de bord est en anglais, l'outil est assez visuel et intuitif pour s'y retrouver avec l'aide d'un traducteur ou de Google Traduction au besoin. Si ton volume est encore petit et que tu veux démarrer vite sans case de configuration compliquée, **Lemon Squeezy** (via Stripe Managed Payments) est l'option la plus légère à apprivoiser.

---

### 4. Productivité & Recherche

**Le topo :** Les "assistants IA généralistes" (ChatGPT, Claude, Gemini, Copilot) continuent de s'étendre dans tous les coins de ta vie numérique — mail, documents, recherche web. La **recherche approfondie** ("Deep Research") est devenue un standard : tu poses une question complexe, et l'IA va fouiller plusieurs sources sur le web, les croiser, et te pondre un rapport sourcé — comme si t'avais un stagiaire-chercheur à temps plein.

**Palmarès du moment :**

| Rang | Outil | Pourquoi il brille |
|---|---|---|
| 🥇 1 | **ChatGPT (GPT-5.5)** | Le couteau suisse — texte, image, voix, dans une même conversation, avec la base d'utilisateurs la plus large. |
| 🥈 2 | **Perplexity AI** | Imbattable pour la recherche web en temps réel avec sources citées — l'anti-Google qui te mâche le travail. |
| 🥉 3 | **Claude (Anthropic)** | Le champion pour les documents longs et l'écriture nuancée ; excellent en code aussi. |

**Tarifs (convertis en CAD) :**

| Outil | Prix US affiché | Prix en CAD |
|---|---|---|
| ChatGPT Plus | 20 $ US/mois | ~28,48 $ CAD/mois |
| Perplexity Pro | 20 $ US/mois | ~28,48 $ CAD/mois |
| Perplexity Max (avec agents "Teammates") | 200 $ US/mois | ~284,80 $ CAD/mois |
| Claude Pro | 20 $ US/mois | ~28,48 $ CAD/mois |

---

### 5. Agents & Création d'automatisations

**Le topo :** Un **agent IA**, dans ce contexte, c'est un robot logiciel à qui tu donnes un déclencheur ("quand je reçois un courriel de tel genre...") et une série d'actions à effectuer automatiquement dans d'autres applications, sans que t'aies à lever le petit doigt. Les plateformes **no-code** (sans avoir besoin d'écrire une ligne de code — tout se fait en glissant des blocs visuels) comme Zapier, Make et n8n dominent ce créneau. La vraie tendance 2026 : des agents **persistants**, qui restent "allumés" en continu, retiennent le contexte d'un projet sur plusieurs jours, et coordonnent plusieurs tâches en parallèle — un peu comme une vraie équipe digitale, pas juste un script qui roule une fois.

**Palmarès du moment :**

| Rang | Outil | Pourquoi il brille |
|---|---|---|
| 🥇 1 | **n8n** | Le plus puissant pour les automatisations complexes multi-services ; open source (code ouvert et modifiable) et auto-hébergeable. |
| 🥈 2 | **Zapier** | Le plus simple à prendre en main, +8000 intégrations, idéal pour débuter sans se casser la tête. |
| 🥉 3 | **Make** | L'équilibre parfait entre puissance (branches, conditions) et interface visuelle claire. |

**Tarifs (convertis en CAD) :**

| Outil | Prix US affiché | Prix en CAD |
|---|---|---|
| Zapier | Gratuit (100 tâches/mois) / dès 29,99 $ US/mois | ~42,68 $ CAD/mois |
| Make | Gratuit (1000 crédits/mois) / dès 10,59 $ US/mois | ~15,08 $ CAD/mois |
| n8n | Gratuit en auto-hébergé / 24 $ US/mois en infonuagique | ~34,18 $ CAD/mois |

---

### 6. Écriture naturelle ("Écrire comme un humain") & Prompts clés

**Le topo :** Les textes générés par IA ont souvent un "accent" reconnaissable : phrases trop équilibrées, vocabulaire trop poli, zéro variation de rythme. Les détecteurs d'IA (comme GPTZero ou Originality AI) scannent ces motifs pour flagger un texte comme "probablement généré par IA." Les outils "d'humanisation" réécrivent ton texte pour casser ces patterns — mais attention, le vrai truc qui fonctionne, ce n'est pas un outil magique, c'est de **nourrir l'IA avec TON propre style** (tes anciens textes, ton ton, tes expressions) plutôt que de demander un résultat générique.

**Palmarès du moment :**

| Rang | Outil | Pourquoi il brille |
|---|---|---|
| 🥇 1 | **Walter Writes AI** | Le seul qui combine un bon contournement de détection ET une qualité d'écriture qui reste lisible et cohérente. |
| 🥈 2 | **GPTinf** | Très fort en contournement de détection (90,7 %), bon rapport qualité-prix. |
| 🥉 3 | **Undetectable AI** | Meilleur score de qualité d'écriture pure (71 %), parfait si tu veux retravailler toi-même après. |

**Prompts clés à essayer toi-même (gratuit, sans outil tiers) :**

> Réécris ce texte comme si tu me le racontais en personne, à la machine à café. Varie la longueur de tes phrases, utilise des contractions, et ajoute une petite imperfection volontaire (une hésitation, une parenthèse) ici et là.

> Voici 3 exemples de mes propres textes [coller tes textes]. Apprends mon ton, mon vocabulaire et ma façon de structurer mes idées, puis rédige le texte suivant dans ce même style : [ta demande].

> Donne-moi une émotion ou une intention concrète derrière ce message (curiosité, urgence, fierté) et intègre-la naturellement dans le texte, sans que ça sonne forcé.

---

### 7. Actualités, Tendances & État de la situation

**Le topo :** 2026 marque un vrai point de bascule : on passe de l'IA "qui répond" à l'IA "qui agit" (l'**IA agentique**). Les entreprises délaissent les chatbots génériques pour des systèmes **verticaux** — des IA ultra-spécialisées dans UN métier précis (comptabilité, ingénierie, service client), entraînées sur des données propres à ce domaine. Pendant ce temps, côté finance, le secteur vit une tension énorme entre investissements colossaux et craintes de "bulle de l'IA" — les marchés boursiers sont nerveux face aux valorisations astronomiques.

**Top 3 tendances à surveiller cette semaine :**

1. **La course aux capitaux ne ralentit pas** — malgré les craintes de bulle, les géants lèvent des dizaines de milliards.
2. **L'IA agentique devient la norme en entreprise** — les IDE, les CRM, les outils de bureau intègrent tous des agents persistants.
3. **La concentration du marché s'accentue** — OpenAI, Anthropic et Google captent l'essentiel des capitaux et de l'attention, au détriment des plus petits joueurs.

---

## SECTION 2 : NOUVEAUTÉS DE LA SEMAINE

### 1. Création Multimédia

- **Seedance 2.5 (ByteDance)** pousse la durée des clips à **30 secondes en 4K avec audio natif**, et accepte jusqu'à **50 références visuelles** (images, vidéos, objets) pour garder tes personnages cohérents d'une scène à l'autre — du jamais-vu côté durée.
- **Kling 4.0** vient de sortir : modèle unifié image + vidéo + audio, avec **dialogue synchronisé dans 5 langues**, 30 secondes de clip (le double de la version précédente), et une sortie en **10-bit HDR** (une plage de couleurs beaucoup plus riche qu'avant).
- **MiniMax Hailuo 3.0** est maintenant disponible en **API** (une façon pour les développeurs de brancher le modèle directement dans leurs propres applications) avec audio stéréo généré dans le même passage que l'image.
- **WAN 3.0 (Alibaba)**, lancé au lendemain d'une levée de **10 milliards $ US**, génère 30 secondes en un seul passage et accepte des entrées texte, image, audio, vidéo, et même des documents PDF/PowerPoint comme référence.
- **PixVerse V6** mise sur le multi-shot (plusieurs plans cohérents) et des contrôles audio intégrés pour les créateurs de contenu réseaux sociaux.

### 2. Développement, Codage & Intégrations

- **IntelliJ IDEA 2026.3** lance **"Air"**, un système qui permet de faire rouler **plusieurs agents de codage en parallèle** (plus de 80 agents disponibles dans un "ACP Store", incluant Claude Code, Codex et Junie) directement dans l'IDE, avec révision des changements de chacun avant de les accepter.
- JetBrains annonce aussi **Junie Lite** (un agent de codage gratuit pour les tâches du quotidien) et **Junie Eco** (pour optimiser les coûts d'utilisation des agents).
- Selon un cas d'usage publié par JetBrains, **Netflix a rendu ses agents de codage 20 à 30 % plus efficaces** (jusqu'à 65 % dans le meilleur cas) en combinant l'intelligence de l'IDE avec les agents.
- **IntelliJ IDEA's Java et Kotlin pour Cursor et VS Code** atteint la version **1.0** — ça veut dire que tu peux maintenant profiter de l'intelligence de JetBrains directement dans Cursor ou VS Code, même si tu n'utilises pas leur IDE.

### 3. Plateformes de Paiement

- **Lemon Squeezy** confirme sa transition vers **Stripe Managed Payments** : les factures émises après le 6 avril 2026 référencent déjà cette nouvelle entité, avec des frais de **3,5 % par transaction réussie** en plus des frais standards de traitement de Stripe. L'activation via API est en **bêta publique** depuis le 25 février 2026.
- Du côté des outils de gestion de **chargebacks** (les rétrofacturations — quand un client conteste un paiement auprès de sa banque), plusieurs billets publiés cette semaine (Chargeflow) insistent sur l'importance pour les plateformes d'abonnement d'automatiser ce processus, un angle mort souvent négligé par les débutants qui vendent par abonnement.
- Aucune annonce officielle cette semaine d'un MoR majeur qui ajoute une interface 100% en français — à surveiller dans les prochaines semaines.

### 4. Productivité & Recherche

- **Perplexity lance "Teammates"** : des agents IA persistants (qui restent actifs même quand tu n'es pas devant ton écran) à qui tu peux assigner des rôles distincts, surveillables dans des fils dédiés, avec intégration Slack. Disponible seulement sur le plan **Perplexity Max à 200 $ US/mois** (~284,80 $ CAD), version mobile à venir plus tard.
- **Google lance Gemini 4 Carbon**, avec une fenêtre de contexte de **1 million de jetons** (jetons = les petits morceaux de texte que le modèle traite ; plus la fenêtre est grande, plus le modèle peut "se souvenir" d'un long document d'un coup).
- **Anthropic publie Claude Fable 5.2 et Mythos 5.2**, des modèles ajustés spécifiquement pour le travail agentique ambitieux : meilleur raisonnement multi-étapes, meilleure coordination entre plusieurs agents.
- **Google annonce Gemini 3.6 Flash et 3.5 Flash-Lite**, visant à réduire les coûts et la latence (le délai de réponse) pour les entreprises : 17 % moins de jetons générés en moyenne, jusqu'à 65 % de moins sur certains tests.
- **Hugging Face publie "The Stack v3"** : le plus gros jeu de données de code ouvert jamais publié — 114 To de données, 224 millions de dépôts, 770 langages de programmation. Une ressource énorme pour entraîner de futurs modèles de code.

### 5. Agents & Création d'automatisations

- **Anthropic** mise gros sur l'orchestration multi-agents avec ses nouveaux modèles Fable et Mythos 5.2, conçus pour que des agents **coordonnent et délèguent des tâches entre eux**.
- **Apple pousserait Siri vers un agent plus autonome** : selon Bloomberg, le PDG Apple John Ternus pousserait pour que Siri devienne capable de surveiller le travail et d'agir de façon continue à travers les applications — un lancement potentiel dès 2027.
- **Siemens lance le HyperLynx Agentic Toolkit**, une IA agentique pour automatiser la vérification de systèmes électroniques — un exemple concret de "l'IA verticale" dont on parlait plus haut, appliquée à l'ingénierie.
- Microsoft prépare le déploiement massif d'agents autonomes persistants ("autopilote") intégrés à Copilot, avec un gros lancement attendu lors de sa conférence Ignite cette semaine à San Francisco.

### 6. Écriture naturelle & Prompts clés

- **Writesonic** ajoute une passe d'"humanisation" à son produit, confirmant que même les gros joueurs du marketing de contenu reconnaissent que l'écriture IA brute ne passe plus la rampe sans retouche.
- Plusieurs nouveaux outils d'humanisation misent maintenant sur l'analyse **stylométrique** (l'étude des habitudes d'écriture : longueur de phrase, choix de mots grammaticaux versus mots de sens) plutôt que la simple reformulation — un signe que la technologie de détection ET de contournement devient plus sophistiquée des deux côtés.
- Tendance à surveiller : de plus en plus d'outils proposent d'importer **tes propres anciens textes** pour que l'IA apprenne ton style personnel plutôt que de produire un ton générique — la vraie solution durable contre le "son robotique."

### 7. Actualités, Tendances & État de la situation

- **OpenAI boucle 11 milliards $ US** d'un tour de financement qui pourrait grimper à 20 milliards $, à une valorisation de **1 250 milliards $ US** (~1 780 milliards $ CAD) — une révision à la baisse par rapport à l'objectif initial de 1 400 milliards $, dans un contexte de nervosité boursière face aux dépenses massives en infrastructure IA.
- **Anthropic vise jusqu'à 1 400 milliards $ US de valorisation** (~1 994 milliards $ CAD) pour son entrée en bourse, avec une levée pouvant atteindre 64 milliards $ US. Des géants comme Nvidia, AMD et Alphabet achèteraient pour 26 milliards $ US d'actions sans droit de vote.
- Le chiffre d'affaires trimestriel d'Anthropic aurait grimpé à **17 milliards $ US**, contre seulement 1,4 milliard $ un an plus tôt — une croissance fulgurante qui alimente autant l'enthousiasme que les craintes de surchauffe.
- **OpenAI dévoile GPT-6 Cyber**, un modèle entraîné spécifiquement pour la recherche en cybersécurité (capable autant d'attaquer que de défendre des systèmes).
- **Mercor**, une start-up spécialisée dans l'entraînement de modèles IA, est valorisée à **20 milliards $ US** après une levée de 750 millions $ US — signe que "former les IA" devient un marché en soi, presque aussi gros que les modèles eux-mêmes.
- La Suède bloque l'accès gouvernemental à ChatGPT et Claude tout en poussant Microsoft Copilot — un exemple concret des tensions géopolitiques et de souveraineté numérique qui commencent à façonner les politiques IA en Europe.