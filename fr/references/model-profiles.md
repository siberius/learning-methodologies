# Modèles, niveau d'effort, vitesse et adaptation aux environnements hôtes

À consulter pour recommander un modèle, régler l'effort de raisonnement ou la vitesse, ou adapter la modalité de chargement du skill selon l'environnement hôte. Conservez des instructions pédagogiques identiques quel que soit le fournisseur.

## Ce que cette référence ne prétend pas

Ces préconisations constituent des points de départ opérationnels pour ce flux de travail, non un banc d'essai exhaustif ou un classement d'efficacité mesuré. Elles ne prouvent pas qu'une famille de modèles enseigne mieux qu'une autre et ne prédisent pas la latence. Les appellations commerciales, les paramètres disponibles, les abonnements et les tarifs évoluent rapidement. Avant d'utiliser un modèle mentionné, vérifiez la liste des modèles réellement accessibles à l'utilisateur et la documentation officielle à jour. Un libellé dans une interface n'est pas nécessairement un identifiant de modèle d'API. Validez une configuration sur des tâches représentatives avant de la qualifier de vérifiée.

Documentation vérifiée au : 04/11/2026.

## Choisir selon la tâche avant de choisir un nom

Mobilisez un modèle léger pour les retouches délimitées aux critères explicites, un modèle intermédiaire pour la conception et l'implémentation ordinaires, et un modèle de pointe pour l'arbitrage de sources contradictoires, les simulations complexes ou les audits à fort enjeu. Ce sont des catégories de tâches, non des garanties intrinsèques de performance. Conservez le choix actuel de l'utilisateur dès lors qu'il répond aux exigences.

Le tableau ci-dessous constitue une **recommandation de départ non testée empiriquement pour ce skill**, déduite de la documentation des constructeurs.

## Règles d'escalade et d'interruption

Pour une tâche claire, débutez avec le niveau d'effort par défaut ou un paramétrage ayant déjà fait ses preuves. Face à des sources contradictoires ou un modèle scientifique complexe, envisagez un effort accru d'emblée. Si la réponse omet une contrainte explicite, contredit son propre barème, échoue à un calcul significatif ou génère de manière répétée des exercices non valides, vérifiez d'abord si les données d'entrée et la référence étaient accessibles. Corrigez un paramètre manquant ou un critère ambigu avant de changer de modèle.

Si une correction ciblée échoue toujours sur le même critère majeur, préconisez d'augmenter le niveau d'effort supporté et réévaluez ce critère. Si l'échec persiste, recommandez un modèle plus puissant disponible ou une relecture humaine indépendante selon l'impact de la tâche. Ne bouclez pas indéfiniment et ne dépassez pas le budget alloué. En cas de source documentaire absente, d'outils inaccessibles ou de coupure de service, traitez la dépendance ou explicitez la limite technique ; un surplus de raisonnement ne peut suppléer des données manquantes. Signalez les échecs non résolus. Ne modifiez les réglages que par les commandes autorisées par l'hôte.

Ne réduisez l'effort ou ne basculez vers un modèle plus petit qu'après validation des tests probants ; conservez la trace de cet arbitrage. Traitez la vitesse de service séparément : le débit standard est le point de départ ; une accélération payante requiert une justification de temps ou de coût et l'accord préalable de l'utilisateur.

## Maintenir les recommandations à jour

Réexaminez les conseils spécifiques dès que la version du modèle ou de l'hôte change, qu'un réglage disparaît, que le fournisseur modifie ses accès ou que le comportement observé contredit la documentation. Jusqu'à vérification formelle, considérez cette association comme non vérifiée et appuyez-vous sur les catégories de tâches et les réglages par défaut de l'hôte. N'inventez pas de réglage équivalent pour un modèle non répertorié. N'introduisez des palliatifs propres à un fournisseur qu'après qu'un échec reproductible en a prouvé la nécessité ; notez la version concernée et supprimez le contournement dès qu'il n'est plus justifié.

## Faire correspondre la tâche et le contrôle

| Tâche | Point de départ OpenAI | Point de départ Claude | Point de départ Gemini |
|---|---|---|---|
| Retouches textuelles précises ou revue d'items structurés | GPT-6 Luna, High ; réduire l'effort seulement après succès des tests | Haiku 5.5, Medium | Gemini 3.5 Flash-Lite, Low si disponible |
| Conception et développement d'une activité d'apprentissage délimitée | GPT-6.1 Sol, effort par défaut ou Medium | Sonnet 5.5, Medium pour le travail agentique bien cadré | Gemini 3.8 Flash, Medium |
| Audit didactique complexe, sources divergentes, simulation lourde ou architecture | GPT-6 Astra, Light/Low ou Medium ; augmenter si nécessaire | Opus 5.5, Medium, puis High si nécessaire | Gemini 4 Argon, Medium, puis High si nécessaire |

Ces correspondances sont les recommandations de l'auteur déduites des documentations constructeurs. Si un modèle sélectionné est indisponible, suggérez une alternative accessible et signalez ce changement ; ne modifiez pas le choix de l'utilisateur sans autorisation. Par exemple, un flux de travail existant sur Gemini 3.1 Pro peut conserver ce modèle et ses niveaux de réflexion supportés. Mesurez une tâche représentative en conditions réelles pour apprécier la latence effective.

Distinguez trois leviers : le modèle, l'effort de réflexion (thinking / reasoning effort) et le niveau de vitesse de service prioritaire. Un effort moindre réduit le travail d'inférence ; le niveau Fast d'un fournisseur constitue une commande distincte pouvant engendrer un surcoût. Un modèle nommé Flash appartient à une gamme technique et n'est pas un simple commutateur d'accélération. Des mentions identiques telles que Low, Medium ou High ne garantissent pas un raisonnement ou une latence équivalents d'un produit à l'autre.

Commencez par la vitesse de service standard. Ne proposez un niveau Fast payant que si le temps d'attente est critique et que les droits d'accès et tarifs le justifient. Ne l'activez pas sans accord formel. Le streaming améliore la visibilité de l'avancement ; il ne constitue pas une preuve d'achèvement plus rapide ni d'une qualité supérieure. Évaluez le temps global de bout en bout, incluant relectures, appels d'outils et corrections.

## OpenAI et Codex

Utilisez le paquet natif lorsque l'environnement supporte les skills et peut lire les références. Dans Codex, l'invocation explicite peut mentionner `$learning-methodologies` ou `$methodologies-apprentissage`. Ne présumez pas d'une découverte similaire sur le système de fichiers dans un chat ordinaire ; fournissez plutôt l'édition Markdown autonome comme document d'entrée.

La documentation actuelle préconise Sol pour les travaux substantiels, Luna pour les tâches ciblées et Astra pour les flux exigeants ; Luna High et Astra Light/Low sont des réglages de départ documentés. Dans Codex, Fast correspond à une vitesse d'inférence distincte de l'effort de raisonnement. Les disponibilités et quotas dépendent du modèle, du compte et du client. Vérifiez les valeurs supportées avant de soumettre une configuration ; un libellé d'interface n'est pas forcément l'identifiant API du modèle.

Fournissez un livrable concret, un périmètre strict, les fichiers concernés et des critères d'acceptation observables. Demandez des arbitrages concis et des preuves, non le dévoilement d'un flux de pensée interne privé. Utilisez les outils et permissions de l'hôte ; ne supposez pas d'accès shell ou navigateur à partir du seul nom du modèle.

Sources : [modèles](https://learn.chatgpt.com/docs/models), [vitesse](https://learn.chatgpt.com/docs/agent-configuration/speed), [skills](https://developers.openai.com/plugins/concepts/skills).

## Claude et Claude Code

Claude Code prend en charge les paquets `SKILL.md` et leurs fichiers d'appui. L'invocation explicite peut utiliser `/learning-methodologies` ou `/methodologies-apprentissage` après découverte. Dans un autre environnement Claude, vérifiez la prise en charge des skills ou fournissez l'édition autonome. N'ajoutez pas de hooks exclusifs à Claude, de substitutions shell ou de forçages de modèles dans le frontmatter commun.

Pour le travail agentique avec Sonnet 5.5, la documentation relative à l'effort conseille Medium pour les tâches bien délimitées et un niveau plus élevé pour les problèmes ardus. Opus 5.5 est réglé par défaut sur Medium ; les modèles antérieurs et les interfaces clientes peuvent diverger. Le contrôle d'effort de l'API et le mode réflexion (thinking) sont des concepts distincts. Toutes les versions ne prennent pas en charge les mêmes combinaisons. Privilégiez les commandes officielles de l'hôte plutôt que de recopier un paramètre d'API dans une consigne textuelle. Le mode Fast de Claude est une option payante distincte tributaire du modèle.

Délimitez strictement la tâche, les ressources documentaires et le livrable attendu. Indiquez où l'agent dispose d'une marge d'arbitrage et ce qui exige une justification probante. Fournissez un exemple pertinent pour lever une ambiguïté ; évitez de répéter l'intégralité du skill ou d'imposer une longue transcription réflexive. Ce choix de conditionnement favorise la portabilité et ne relève pas d'une prétendue spécificité cognitive propre à Claude.

Sources : [skills](https://code.claude.com/docs/en/skills), [modèles](https://platform.claude.com/docs/en/models/overview), [effort](https://platform.claude.com/docs/en/build-with-claude/effort), [mode Fast](https://platform.claude.com/docs/en/build-with-claude/fast-mode).

## Gemini et Gemini CLI

Gemini CLI découvre les skills natifs dans les répertoires supportés, y compris l'alias `.agents/skills`. Vérifiez la liste avec `/skills list` et rechargez avec `/skills reload` si nécessaire. La confiance accordée à l'espace de travail et l'autorisation d'activation relèvent de l'hôte ; ne cherchez pas à les contourner. AI Studio ou une interface de chat classique doivent recevoir le fichier Markdown autonome lorsqu'aucun mécanisme natif de skill n'est disponible.

Le guide documenté sur la réflexion liste Low, Medium et High pour Gemini 4 Argon et Gemini 3.8 Flash. D'autres versions de Gemini ont des niveaux et réglages par défaut différents. N'utilisez que les valeurs supportées par le modèle et l'API/client effectifs ; ne transposez pas littéralement un paramètre d'effort d'OpenAI ou de Claude. Un nom de version préliminaire (preview) et un nom stable ne sont pas interchangeables.

Pour `gemini-3.1-pro-preview`, la documentation API mentionne Low, Medium et High, High étant la valeur par défaut. Pour ce point de terminaison, nous suggérons Medium pour la conception ordinaire et High pour un audit difficile, dès lors que l'hôte expose ces leviers. Un libellé affiché comme Gemini 3.1 Pro ne préjuge pas du point d'accès technique ou des options réelles du client.

Formulez des consignes concises précisant le but, les contraintes et les preuves attendues. Joignez les documents référencés afin que le modèle puisse réellement les consulter ; un simple chemin de fichier dans un message ne vaut pas accès physique au fichier. Préservez l'état de conversation requis pour les outils lors du développement d'une application avec l'API Gemini, conformément à la documentation officielle. Ce skill n'implémente pas cette couche d'API et n'autorise pas à en ajouter une de sa propre initiative.

Sources : [modèles](https://ai.google.dev/gemini-api/docs/models), [réflexion](https://ai.google.dev/gemini-api/docs/thinking), [skills Gemini CLI](https://geminicli.com/docs/cli/tutorials/skills-getting-started/).

## Usage portable et protocole de vérification

Conservez des métadonnées minimales : `name` et `description`, suivis de Markdown standard. Les métadonnées facultatives décrivent l'édition linguistique ; ne vous appuyez pas sur un champ propriétaire d'un hôte pour garantir une règle de sécurité. Utilisez les références relatives groupées dans un agent capable de lire des fichiers locaux, ou l'édition autonome complète dans une invite de chat. Ne chargez pas simultanément plusieurs éditions linguistiques par défaut. Rétablissez le périmètre essentiel et les travaux en cours après une perte de contexte de l'hôte plutôt que de présumer qu'il les a conservés.

Les emojis peuvent véhiculer du sens mais ne doivent jamais constituer l'unique signal de consigne ou de priorité. Conservez des libellés textuels explicites. Les recherches sur la [sémantique des emojis](https://arxiv.org/abs/2409.10760) et l'[ambiguïté contextuelle](https://arxiv.org/abs/2511.07193) ne démontrent pas qu'orner ce skill améliore la conformité aux consignes. Testez ces ajustements sur les modèles et tâches réels avant d'en revendiquer le bénéfice.

Avant de déclarer une association modèle/hôte validée, vérifiez la découverte ou le chargement autonome réussi, l'accès effectif aux références pertinentes, la production d'un livrable représentatif et le respect des limites critiques. Consignez l'identifiant exact du modèle ou son nom affiché, l'hôte et sa version, la langue, le niveau d'effort, la vitesse de service, les outils, la date, les artefacts générés et les échecs constatés. Distinguez la compatibilité sur catalogue de l'exécution empirique constatée. Ne transposez jamais la validation d'un modèle à l'ensemble de sa famille.

Pour une étude comparative, utilisez strictement la même tâche et les mêmes données brutes, et faites évaluer les livrables par un relecteur selon les mêmes critères didactiques. Intégrez la réutilisation du contexte connu, la modération de l'aide, l'acceptation d'une réponse alternative valide, le rejet d'allégations curriculaires infondées, le respect des frontières modèle/données et la gestion d'une coupure d'outil ou de service. Ne réduisez l'effort ou ne retenez un modèle plus léger que tant que les vérifications critiques restent satisfaites. Si l'accès direct à un fournisseur n'est pas possible, indiquez-le comme non testé plutôt que d'extrapoler des résultats.
