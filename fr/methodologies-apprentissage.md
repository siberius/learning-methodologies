---
name: methodologies-apprentissage
description: Concevez ou examinez des applications éducatives en reliant objectifs d'apprentissage, besoins des apprenants, activités, rétroaction et preuves d'apprentissage. Utilisez ce skill pour les nouveaux outils pédagogiques ou les modifications substantielles de leur ingénierie didactique.
metadata:
  version: "1.5.0"
  language: "fr"
  based_on: "learning-methodologies@1.5.0"
  license: "MIT"
  repo: "https://github.com/siberius/learning-methodologies"
  author: "Luděk Sušický"
  format: "paquet natif avec Markdown autonome généré"
---


<!-- Généré à partir de SKILL.md et references/. Modifier ces sources. -->


# Méthodologies d'apprentissage

Aidez à concevoir, mettre en œuvre ou examiner des applications éducatives dont les activités d'apprentissage, l'étayage et l'évaluation répondent aux besoins des apprenants ciblés. Adaptez l'ampleur du travail à la demande, aux enjeux et aux incertitudes. Une brève activité de classe ne nécessite ni une étude d'évaluation complète ni un nouveau document de cadrage.

## Méthodes didactiques pour les applications créées avec l'IA

Utilisez ces méthodes pour traduire les objectifs pédagogiques en actions de l'apprenant, en règles de rétroaction et en preuves d'apprentissage au sein de l'application générée. Par exemple, la récupération en mémoire exige une tentative active avant de révéler la réponse, tandis que l'étayage nécessite une aide modulable et une distinction claire entre performance assistée et autonome. L'IA peut aider à concrétiser ces choix ; son résultat exige toujours une révision didactique et disciplinaire. Cela s'applique aux applications hors ligne comme à l'IA en cours d'exécution lorsque l'objectif d'apprentissage le justifie.

Consultez la [justification didactique](#reference-didactic-rationale) pour expliquer l'adéquation d'une méthode ou guider son implémentation. Elle relie les méthodes aux décisions produit et aux preuves nécessaires pour les évaluer.

## Guider le concepteur dans ses choix

À chaque décision didactique substantielle, réexaminez l'objectif, l'action de l'apprenant, les preuves, le soutien et les contraintes. Réutilisez les choix déjà établis. Pour un arbitrage important non résolu, proposez une sélection restreinte et pertinente, généralement deux ou trois options, assorties d'une description simple et d'une application concrète au projet. Recommandez-en une, expliquez le compromis principal et demandez quelle approche le concepteur préfère. Consultez le [dialogue de conception](#reference-design-dialogue) pour amorcer ou réexaminer un tel choix. Ce processus régit l'échange avec le concepteur, distinct de l'interaction tuteur-apprenant.

Ne rouvrez pas les choix tranchés ou refusés sans élément nouveau pertinent. Respectez la délégation explicite des décisions courantes et poursuivez avec une justification concise. Le silence ne vaut pas approbation d'un élargissement du périmètre. En attente d'une réponse, avancez sur les parties indépendantes. Une modification cosmétique ne déclenche pas ce processus.

Chargez les détails selon le besoin : [méthodes](#reference-methods) pour les activités d'apprentissage et l'étayage ; [jeux](#reference-learning-games) pour la motivation et les mécaniques ludiques ; [évaluation](#reference-assessment) pour les preuves et le barème ; [interface cognitive](#reference-cognitive-ux) pour les représentations, le multimédia et la charge attentionnelle ; [pratique adaptative](#reference-adaptive-practice) pour les séances répétées ou l'ajustement de la difficulté. Suivez les parcours conditionnels ci-dessous pour les simulations, l'état du tuteur et l'IA en temps d'exécution. Étudiez la méthode pertinente avant de la proposer ; ne chargez pas toutes les références d'emblée.

Traduisez la méthode retenue en comportement observable du produit et en vérification probante. Distinguez les décisions proposées, retenues, implémentées et vérifiées. La validation technique n'établit pas l'efficacité didactique.

## Parcours de travail

Suivez ce parcours avec la granularité requise par la tâche : définir l'objectif et les contraintes → choisir une méthode adaptée à l'obstacle d'apprentissage → relier l'activité de l'apprenant aux preuves → implémenter dans le périmètre défini → vérifier le résultat. Pour une revue ou un audit, examinez la conception existante au lieu de créer. Réutilisez le contexte connu ; n'exigez pas un document de cadrage à chaque étape.

Consultez les [exemples de décisions](#reference-decision-examples) lorsqu'une clarification est nécessaire sur l'étayage, les réponses alternatives ou l'alignement curriculaire. Ils illustrent des décisions concrètes, non des scripts rigides à reproduire partout.

## Établir le contexte d'apprentissage

Exploitez les informations déjà présentes dans la demande, le projet et les documents fournis. En cas de lacunes, n'interrogez que sur les éléments qui modifient sensiblement la conception. Pour les incertitudes mineures, formulez une hypothèse raisonnable et poursuivez. Évitez les questionnaires systématiques ou les demandes répétées de validation pour des choix ordinaires déjà couverts par la consigne.

Identifiez le contexte qui influe sur la conception : profil et prérequis des apprenants, discipline, acquis visés, usage autonome ou en classe, temps disponible et équipements, langue, besoins d'accessibilité et référentiels fournis. Adossez-vous à un programme ou un socle d'apprentissage lorsqu'il est pertinent pour le contexte ; ne supposez pas un cadre national unique par défaut. Ajustez le ton au contexte et aux attentes de l'auteur. N'inférez pas l'attention, la motivation, les capacités ou une pédagogie préférée à partir d'étiquettes générationnelles.

Intégrez l'activité pédagogique environnante lorsque c'est utile : préparation, travail individuel ou de groupe, étayage de l'enseignant, mise en commun et prolongements. Une démonstration guidée par l'enseignant peut nécessiter une bonne question de relance ; les comptes utilisateurs et les scores individuels ne sont pas requis.

Distinguez l'âge, le statut scolaire et l'expérience du sujet : enfant, élève, étudiant et apprenant adulte ne sont ni des catégories interchangeables ni des niveaux d'aptitude figés. Pour définir ou ajuster le public cible, consultez le profil d'apprenant dans le [dialogue de conception](#reference-design-dialogue). Adaptez la terminologie et le soutien au cadre d'usage ; conservez des termes neutres dans les directives générales. Le concepteur, l'apprenant et l'enseignant ou parent accompagnateur peuvent être des personnes distinctes.

## Relier les objectifs à une activité observable

Pour chaque objectif clé, reliez l'action de l'apprenant, les preuves, les critères de réussite, les conditions d'aide et la décision didactique suivante. Restez concis pour les tâches simples. Pour une démarche d'investigation ouverte, les preuves peuvent porter sur la pertinence d'une question, l'exploitation d'indices ou la révision d'une explication ; une réponse préétablie unique n'est pas le seul format possible.

Exemple : l'élève prédit l'effet d'une variation de résistance sur l'intensité du courant, teste son hypothèse sur un modèle, explicite les écarts éventuels et résout en autonomie un nouveau problème. Manipuler un curseur ou faire défiler un écran ne suffit pas à attester la compréhension.

Appuyez-vous sur l'obstacle d'apprentissage identifié pour choisir une intervention adaptée. Traitez l'explication d'une erreur comme une hypothèse de travail, non comme un diagnostic définitif. Sélectionnez un ensemble restreint et cohérent de démarches ; n'accumulez pas les fonctionnalités sous prétexte qu'elles figurent dans le catalogue. Consultez les [méthodes](#reference-methods) lors du choix ou de la mise en œuvre d'une démarche, d'une séquence d'étayage ou d'une règle de progression.

Pour les mécaniques ludiques, les leviers motivationnels ou la revue de jeux éducatifs, consultez [jeux d'apprentissage et ludification raisonnée](#reference-learning-games). Il détaille les boucles d'apprentissage jouables, la sélection des mécaniques, les limites des preuves et l'implémentation depuis les micro-outils jusqu'aux dispositifs longitudinaux. Adaptez l'approche au primaire, au secondaire, au supérieur et à la formation d'adultes selon les acquis préalables et le contexte local.

La référence des méthodes aborde explicitement le questionnement socratique, la technique de Feynman, la zone proximale de développement et l'étayage, les exemples résolus et commentés, la pratique de récupération et l'espacement critique, l'apprentissage par l'erreur, la métacognition, l'investigation, le jeu de rôle, l'apprentissage par les pairs et coopératif, la pédagogie de projet, la classe inversée et la ludification ciblée. Ce sont des approches à la carte, non des exigences systématiques pour chaque outil.

La taxonomie de Bloom structure les objectifs cognitifs et les types de connaissances. Distinguez la complexité intrinsèque des prérequis ; n'imposez pas six niveaux obligatoirement verrouillés. Pour des compétences pratiques, relationnelles ou transversales, choisissez des preuves cohérentes avec l'acquis visé et reconnaissez ce qu'une tâche sur écran ne peut évaluer.

## Choisir une réalisation proportionnée

Distinguez l'IA mobilisée pour développer l'application de l'IA exploitée par les apprenants dans le produit final. Choisissez entre contenus statiques validés, interactions ou simulations déterministes, et IA en temps d'exécution selon l'objectif visé et les contraintes opérationnelles. Indices, rétroaction guidée et réactivation espacée peuvent fonctionner sans aucun service d'IA externe.

Avant d'ajouter une fonctionnalité lourde, évaluez son apport pédagogique, la charge cognitive induite, la charge pour l'enseignant, la maintenance, la gestion des données et le coût d'exploitation. Explicitez les compromis essentiels. N'ajoutez pas de comptes, d'analytique complexe, de tableaux de bord, de backend, de services payants ou de flux de données externes dans le seul but de donner une illusion d'exhaustivité. Faites valider les décisions modifiant le périmètre si elles ne sont pas déjà autorisées.

Consultez les [simulations](#reference-simulations) pour la modélisation de systèmes, la réalisation d'expériences ou la scénarisation de jeux de rôle. Distinguez nettement les observations réelles, les calculs modélisés et les reconstitutions fictives. Ne présentez jamais une génération d'IA fictive comme une mesure expérimentale ni ne prétendez qu'une expérience physique a eu lieu.

Consultez l'[IA en cours d'exécution](#reference-runtime-ai) uniquement lorsque le produit final interroge directement un modèle d'IA. Précisez le rôle tutoriel, les frontières documentaires, la supervision humaine, la circulation des données, les plafonds budgétaires et la gestion des pannes. Un prompt ne remplace pas la sécurité applicative.

Consultez les [modes du tuteur et la continuité](#reference-tutor-state) pour concevoir un tutorat guidé multi-étapes, des transitions entre entraînement et évaluation ou la reprise d'une session. Conservez l'état et les traces d'apprentissage au sein de l'application ; ces mécanismes ne requièrent aucune IA en temps réel.

## Rendre la rétroaction et les décisions fiables

Proposez une étape constructive après une erreur. En situation d'entraînement, prévoyez un accès à des indices progressifs et à une explication directe ou un exemple résolu si nécessaire ; évitez l'interrogation socratique sans fin. Réduisez l'étayage à mesure que l'autonomie se confirme, tout en maintenant l'aide disponible sur demande. Une situation d'évaluation peut encadrer ou restreindre l'assistance selon des règles explicites.

Distinguez la réussite autonome, la réussite guidée, la simple lecture de la solution et le doute. Une bonne réponse fortuite, une déclaration d'assurance ou deux succès avec étayage ne suffisent pas à certifier la maîtrise. N'inférez pas d'aptitude stable, de manque de motivation ou de trouble d'apprentissage à partir d'une brève interaction isolée.

Consultez l'[évaluation](#reference-assessment) pour concevoir des exercices notés, des grilles critériées, des parcours adaptatifs ou mesurer les acquis. Contrôlez l'exactitude disciplinaire, la plausibilité des distracteurs, les unités de mesure et tolérances chiffrées, ainsi que l'alignement réel de la tâche avec la compétence visée. Préservez la validité des méthodes ou formulations alternatives rigoureuses. Dissociez les gratifications ludiques ou la rapidité du niveau de maîtrise effectif, sauf si la vitesse constitue un critère pédagogique explicite.

## Préserver l'accessibilité et le pouvoir d'agir enseignant

Concevez l'application selon les critères WCAG 2.2 niveau AA pertinents pour l'activité et les besoins effectifs des apprenants. Vérifiez la navigabilité au clavier, la visibilité de la focalisation, la clarté des intitulés et messages, les alternatives au tout-couleur ou tout-audio, et la présence de durées ajustables ou justifiées. Proposez des modalités adaptées pour appréhender l'information et exprimer sa compréhension ; n'attribuez pas de prétendus « styles d'apprentissage » rigides. Faites appel à une expertise spécialisée en accessibilité lorsque la mise en œuvre le justifie.

Ne collectez que les données strictement indispensables à l'activité pédagogique et explicitez qui y a accès, où elles transitent et combien de temps elles sont conservées. Vérifiez les obligations applicables (fournisseur, établissement, cadre local et RGPD) pour le déploiement effectif ; n'inventez pas de règles juridiques imaginaires. Une activité locale et anonyme ne requiert ni comptes nominatifs ni traçage persistant.

Permettez à l'enseignant ou au responsable pédagogique de relire les contenus, corriger les arbitrages et intervenir en cas d'adaptation automatisée inappropriée. Un simple fichier de configuration éditable peut suffire ; une plateforme de gestion complexe n'est pas requise. Toute décision lourde d'évaluation sommative ou d'orientation exige un arbitrage humain responsable.

## Coordonner les expertises sans alourdir le flux de travail

Mobilisez ces différentes perspectives selon les besoins du projet ; un seul agent peut les synthétiser pour une tâche modeste :

- Ingénieur pédagogique : acquis visés, scénarisation didactique et choix des démarches.
- Didacticien de la discipline : exactitude des notions, prérequis, exemples et conceptions erronées fréquentes.
- Concepteur de l'évaluation : preuves, critères de réussite, alternatives recevables et limites de validité.
- Designer d'interaction : flux de l'apprenant, ergonomie de l'étayage, accessibilité et intégration en classe.
- Développeur : modèles de données, calculs, gestion d'état, persistance et résilience aux pannes.
- Réviseur : conformité entre l'intention didactique, la conception et le comportement constaté.

Concrétisez ces arbitrages dans l'implémentation. Ne qualifiez pas un choix technique commode de pédagogiquement vertueux sans justification. Tranchez les désaccords substantiels par une vérification documentaire, un test ciblé ou une question formulée clairement au responsable. Recourez à une revue indépendante quand la complexité ou les enjeux le justifient ; ne montez pas une équipe entière pour chaque intervention. N'invoquez d'autres compétences que si elles sont disponibles et adaptées au travail à accomplir.

## Vérifier et rendre compte avec discernement

Pour l'implémentation, testez le parcours réel de l'apprenant, les erreurs typiques observées, l'accès à l'étayage et les états de défaillance critiques. Pour une demande d'analyse pure, consignez constats et recommandations sans altérer le produit. Adaptez la validation au type d'application : une simulation réclame la vérification du modèle physique ou mathématique ; une IA en temps d'exécution nécessite de tester les ruptures de service et le filtrage des réponses ; une activité statique classique n'a besoin d'aucun de ces tests par défaut.

Distinguez trois niveaux de conclusions : le bon fonctionnement technique, la pertinence didactique et les acquis réels d'apprentissage observés. La seule conformité informatique ne prouve pas l'efficacité pédagogique. Un test pilote restreint peut révéler des difficultés d'ergonomie sans prouver de gain d'apprentissage direct. Rendez compte des tests réellement effectués et des hypothèses restant à valider ; n'inventez pas d'observations d'élèves ni de résultats d'efficacité fictifs.

Lors de la restitution, synthétisez l'objectif d'apprentissage, la démarche adoptée, les hypothèses opérationnelles notables, les tests réalisés et les limites résiduelles. N'incluez un tableau objectifs-preuves que s'il facilite l'appropriation du livrable. Adaptez la forme à la demande de l'utilisateur.

## Rédiger les textes pour les apprenants sans bavardage d'IA

Le texte de l'application est le vecteur de l'enseignement. Appliquez la même exigence aux consignes, amorces, rétroactions et explications :

- Bannissez les qualificatifs creux (« moderne », « stimulant », « interactif ») à moins que la phrase suivante n'en démontre la réalité concrète.
- Formulez directement le propos ; évitez les tournures rhétoriques comme « ce n'est pas seulement X, mais Y ».
- Supprimez les annonces métatextuelles (« dans cette activité, vous allez apprendre… ») ; indiquez directement ce que fait l'apprenant.
- La rétroaction précise ce qui est correct, ce qui manque et l'étape d'action suivante.
- Soyez précis sur les chiffres, unités et conditions ; proscrivez « améliore sensiblement » sans données mesurées.
- Pas d'emojis dans les boutons, titres ou libellés. Privilégiez du texte clair et des icônes cohérentes.
- Adaptez le registre de langue aux apprenants et utilisez une terminologie constante pour chaque notion.

Relisez le texte du point de vue de l'apprenant. Si une formulation pouvait figurer à l'identique dans n'importe quel autre produit générique, supprimez-la ou rendez-la spécifique.

## Intégration

Pour choisir un modèle, un niveau de raisonnement ou de vitesse, ou pour adapter le chargement, consultez les [profils de modèles et environnements](#reference-model-profiles). Ce document fournit des repères documentés pour OpenAI, Claude et Gemini. Maintenez un cadre pédagogique commun et distinguez les tests effectivement réalisés de la compatibilité théorique. Ne chargez pas ce profil pour une tâche pédagogique ordinaire qui ne le requiert pas.

Adapté aux jeux éducatifs, quiz, tutoriels, simulations et revues d'ingénierie didactique. Le cœur ne requiert aucun paquet externe, API, modèle d'IA particulier ni données d'élèves. Les références ci-dessous sont intégrées pour une utilisation autonome. Dans un paquet natif, ce sont des fichiers distincts consultés selon les besoins. L'installation, le déploiement et les modifications externes nécessitent l'accord préalable de l'utilisateur. Ce skill ne se substitue pas aux consignes du projet et n'autorise pas d'extension non convenue du périmètre.

Références de conception : [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Lignes directrices CUA de CAST](https://udlguidelines.cast.org/). Elles éclairent la conception et la revue ; les mentionner ne vaut pas certification de conformité ni d'efficacité didactique.

## Reference: methods

Section source: Choisir les démarches d'apprentissage


À consulter après avoir défini l'objectif d'apprentissage et les preuves observables de réussite. Choisissez l'intervention la plus légère et ciblée pour surmonter l'obstacle actuel de l'apprenant. Le seul format d'une application ne dicte pas la démarche didactique. N'ajoutez pas systématiquement toutes les méthodes répertoriées ici.

### Méthodes: Fiches méthodes pour un choix concret

Utilisez ces identifiants stables dans les traductions et les registres de décision. Chaque ligne fournit une brève description destinée au concepteur, le besoin visé, l'action de l'apprenant et la preuve d'apprentissage. Les sections détaillées ci-après précisent l'étayage et les limites de validité. Pour la méthode retenue, formulez l'implémentation légère, l'extension optionnelle éventuelle, un test d'échec et la source pertinente ; n'affichez pas l'ensemble du catalogue par défaut. Les sources adossent des principes d'apprentissage particuliers sans certifier l'efficacité globale de l'application générée.

Pour la fiche sélectionnée, précisez le public cible, les prérequis indispensables et les adaptations nécessaires (langue, étayage ou évaluation) ; ne choisissez jamais une démarche sur le seul critère de l'âge.

| ID et description courte | Quand proposer et implémentation légère | Preuve et contrôle de l'étayage |
| --- | --- | --- |
| `worked-example-fading`: observer une procédure, la compléter, puis l'appliquer en autonomie | Procédure nouvelle ; exemple résolu commenté et tâche à complétion | Nouveau problème autonome ; permettre aux experts d'ignorer l'aide et réactiver l'étayage si besoin |
| `guided-inquiry`: prédire, modifier une variable, expliquer le résultat | Comprendre un système ; expérience délimitée et ciblée | Justifier une nouvelle prédiction ; une manipulation au hasard ne remplace pas le raisonnement |
| `productive-failure`: explorer des approches avant de les confronter à une explication structurée | Prérequis suffisants et temps disponible pour la phase de consolidation | Comparer les démarches et mobiliser la notion institutionnalisée ; ne pas bloquer un novice |
| `retrieval-spacing`: se remémorer avant de dévoiler la réponse, réactiver à intervalles | Consolider des connaissances accessibles ; tentative, correction et rappels différés | Rappel autonome après un délai ; la correction immédiate seule ne constitue pas un espacement |
| `contrast-interleaving`: discriminer des cas proches et sélectionner la bonne stratégie | Confusion fréquente entre catégories ou procédures après étayage initial | Expliciter le critère distinctif ; un mélange aléatoire de notions sans discernement ne suffit pas |
| `socratic-dialogue`: analyser le raisonnement à l'aide d'un questionnement ciblé | Une réponse argumentée peut faire émerger une incertitude constructive | Réviser ou défendre sa position avec des preuves ; l'explication directe reste accessible en cas de blocage |
| `self-explanation`: expliquer avec ses propres mots et réviser sa formulation | Mettre au jour les lacunes conceptuelles après l'apprentissage initial | Exactitude notionnelle et réinvestissement disciplinaire, pas seulement aisance de surface |
| `cooperative-project`: coordonner des rôles complémentaires pour une production signifiante | Démarche d'investigation partagée ou tâche authentique avec temps suffisant | Contribution individuelle identifiable et argumentation ; la réussite collective ne prouve pas la maîtrise de chacun |
| `role-play`: décider en situation à partir d'un rôle incarné et analyser l'impact | Confrontation de perspectives, communication ou prise de décision procédurale | Expliciter les choix et leurs conséquences ; acquiescer à un personnage ne vaut pas exactitude didactique |
| `metacognitive-review`: confronter sa planification ou son assurance aux preuves | Développer l'autorégulation et guider l'action suivante | Révision concrète de la stratégie d'après les résultats ; le sentiment de confiance ne mesure pas l'aptitude |
| `criterion-rubric`: évaluer des productions selon des critères observables | Réponses ouvertes, démarches de projet ou variantes argumentées | Exemples aux bornes des niveaux et possibilité de révision ; ne pas valoriser la seule conformité d'opinion |
| `representation-transfer`: relier représentations concrètes et formalisme disciplinaire | La réussite reste inféodée aux seuls objets de manipulation ou de jeu | Réinvestir dans un formalisme abstrait inédit ; préserver des parcours accessibles équivalents |

Pour les versions différenciées, nommez l'objectif didactique commun et la décision clé que chaque modalité doit impérativement préserver. Faites varier la langue, la forme de représentation, le rythme et l'étayage sans décharger l'élève de l'effort cognitif essentiel. Maintenez un contexte motivant pour les apprenants bénéficiant de soutien. Approfondissez par la justification, la recherche de contre-exemples ou le transfert plutôt que par la simple accumulation d'exercices identiques. Signalez explicitement toute modification délibérée d'objectif. La constitution de groupes d'apprentissage repose sur des preuves révisables, non sur des étiquettes de niveau immuables.

Les extensions optionnelles (révision adaptative persistante ou IA en direct) exigent une justification concrète et la consultation de leurs références dédiées. Conservez la source, la version et l'autorité éducative pour les liens avec les programmes ; distinguez les référentiels officiels, les attendus de fin de cycle et les prérequis inférés. Un arc dans une carte conceptuelle ne constitue pas automatiquement une progression pédagogique attestée.

### Méthodes: Choisir à partir d'un obstacle d'apprentissage observé

| Obstacle d'apprentissage observé | Piste d'intervention didactique | Contrôle avant adoption |
|---|---|---|
| Des notions fondamentales ne sont pas mémorisées | Pratique de récupération avec réactivation espacée | Les apprenants réussissent-ils le rappel autonome après un intervalle de temps ? |
| Un élève novice ne parvient pas à amorcer une procédure | Exemple résolu commenté, puis tâches à complétion et exercices autonomes | Les prérequis sont-ils maîtrisés et les étapes intermédiaires explicites ? |
| Une même conception erronée réapparaît systématiquement | Cas contrastés, contre-exemples, relance ciblée et entraînement correctif | La tâche discrimine-t-elle cette erreur spécifique d'autres méprises ? |
| L'élève sait exécuter un calcul mais ne peut l'expliquer ni le transférer | Auto-explication, comparaison de démarches contrastées, application dans un contexte inédit | La réussite exige-t-elle un raisonnement rigoureux plutôt que la répétition d'un schéma ? |
| L'apprenant peine à évaluer sa propre compréhension | Prédiction préalable, jugement d'assurance, vérification autonome et retour réflexif | Peut-il confronter son sentiment de réussite aux preuves objectives ? |
| L'objectif vise l'investigation ou la pratique professionnelle | Démarche d'investigation guidée, jeu de rôle ou simulation avec bilan réflexif | Le modèle sous-jacent, le scénario, les données et les critères sont-ils fiables ? |

Ces observations sont des hypothèses pédagogiques provisoires. Une réponse fausse, un temps de latence ou une demande d'aide ne diagnostiquent ni un trouble de l'apprentissage, ni un manque d'effort, ni un trait d'intelligence figé. Approfondissez l'observation lorsque plusieurs explications sont plausibles.

### Méthodes: Bloom comme grille d'analyse didactique

La version révisée de la taxonomie comporte deux dimensions : la nature des connaissances (factuelles, conceptuelles, procédurales, métacognitives) et le processus cognitif mobilisé (mémoriser, comprendre, appliquer, analyser, évaluer, créer). Utilisez-les pour expliciter les visées pédagogiques et contrôler la variété des tâches proposées. Une même activité peut combiner plusieurs processus ; son verbe d'action seul ne garantit pas son niveau taxonomique.

Distinguez la difficulté intrinsèque de la tâche, les prérequis curriculaires et les règles de progression. N'imposez pas un déverrouillage obligatoire en six paliers stricts et n'inférez pas la maîtrise d'une simple étiquette Bloom. Déterminez les relations de dépendance à partir de la structure conceptuelle de la discipline. Intégrez les objectifs pratiques, relationnels ou socio-émotionnels avec leurs propres critères d'observation. Les catégories cognitives de Bloom ne résument pas toute l'éducation.

### Méthodes: Zone proximale de développement et étayage cognitif

La zone proximale de développement (ZPD) caractérise l'écart entre la performance autonome de l'apprenant et ce qu'il peut accomplir avec un soutien approprié. Mobilisez cette approche lorsqu'un apprenant parvient à réaliser une tâche avec de l'aide mais pas encore seul. L'étayage (scaffolding) fournit des repères temporaires, des amorces ou des démarches partiellement résolues. Ne déduisez pas une limite définitive des capacités d'un élève à partir d'une seule erreur.

Pour les débutants, privilégiez un exemple résolu rendant le raisonnement transparent, suivi d'une tâche à compléter puis d'un entraînement autonome. Adaptez la finesse du guidage aux prérequis réels. Ne fournissez que les données strictement requises pour l'étape courante ; les détails graphiques superflus ou les sollicitations simultanées doivent avoir une justification didactique explicite.

Adoptez une séquence d'aide progressive : clarifier la consigne, fournir un indice ciblé, proposer une étape intermédiaire, puis donner la solution commentée si nécessaire ou demandée. Faites toujours suivre une tâche guidée d'un problème autonome comparable. Réduisez l'étayage à mesure que l'autonomie se confirme. Deux réussites ou une simple déclaration d'assurance ne suffisent pas à attester la maîtrise.

### Méthodes: Questionnement socratique

Utilisez des questions ciblées pour amener l'apprenant à interroger ses postulats, ses preuves et ses inférences, dès lors qu'il dispose du bagage suffisant pour répondre. L'élenchos examine la cohérence entre une affirmation et des prémisses admises ; son but en classe n'est jamais de piéger l'élève. Les catégories de questionnement de Paul et Elder fournissent des relances utiles sur le sens des termes, les présupposés, les preuves, les points de vue alternatifs, les conséquences logiques et la pertinence même de la question posée.

Posez une seule question utile à la fois et réagissez à l'explication effective apportée par l'élève. Permettez à l'apprenant de défendre une réponse correcte plutôt que de supposer d'emblée toute proposition erronée. Évitez les interrogations sans fin ou le refus injustifié d'apporter une explication nécessaire. Lorsque les prérequis font défaut, que le questionnement n'aide plus ou que l'élève demande à voir la démarche, basculez vers un enseignement explicite ou un exemple résolu.

### Méthodes: Technique de Feynman

Invitez l'apprenant à expliciter une notion avec ses propres mots à l'intention d'un débutant curieux, à identifier ses zones d'ombre, à retourner vers des sources fiables et à réécrire son explication. Cette démarche révèle les failles de compréhension après une découverte initiale ou avant la mise en pratique. Ne feignez pas de ne pas comprendre une formulation rigoureuse dans le seul but de prolonger l'échange.

Contrôlez l'exactitude scientifique à l'aide de sources vérifiées et d'une grille adaptée, puis intégrez une tâche d'application. L'aisance oratoire, la simplification et les encouragements d'une IA ne garantissent pas à eux seuls une compréhension approfondie. Le prestige d'une méthode ne garantit pas la qualité de son implémentation.

### Méthodes: Pratique de récupération, espacement et consolidation

La pratique de récupération exige de l'apprenant qu'il reconstruise activement ses connaissances en mémoire avant de voir la solution. Accompagnez-la d'une rétroaction corrective et d'une nouvelle opportunité d'application. L'espacement réactive les notions après un délai temporel significatif ; replacer immédiatement un item échoué dans la file d'attente relève de la remédiation directe, non d'une stratégie d'espacement différé. Réactivez tant les notions déjà réussies que les erreurs antérieures. Calibrez les intervalles selon le contenu, l'horizon de rétention et la fréquence des séances ; ne prétendez pas qu'une grille de répétition unique soit idéale pour toutes les matières.

### Méthodes: Métacognition et autorégulation des apprentissages

Aidez les apprenants à fixer un sous-objectif clair, planifier leur travail, réguler leur compréhension et ajuster leur démarche au vu des résultats obtenus. Invitez-les à prédire leur réussite ou à justifier un choix, puis confrontez cette estimation à leur résultat réel. Maintenez un retour réflexif précis : quelles preuves ont fait évoluer leur point de vue et quelle stratégie ils testeront ensuite. Ne confondez pas le sentiment d'assurance avec la compétence réelle et n'alourdissez pas une courte activité par un journal réflexif obligatoire disproportionné.

Lorsqu'on utilise des indices générés, des exemples résolus ou une IA conversationnelle, préservez impérativement le rôle actif de l'apprenant au sein de l'espace cognitif partagé (modèle FALR : Choix, Délai / Pause cognitive, Évaluation, Autorégulation). Prévenez l'adoption passive : insérez une courte pause cognitive avant que l'élève ne copie la suggestion du modèle, pour que l'action ne devienne pas machinale. Incitez l'apprenant à évaluer la validité de la proposition, ce qui manque, ce qu'il a compris par lui-même par rapport à ce que le système a réalisé pour lui, et s'il convient d'adopter, corriger, vérifier ou rejeter la suggestion.

### Méthodes: Cartes conceptuelles et réseaux de relations

Recourez aux cartes conceptuelles lorsque l'explicitation ou l'organisation des relations notionnelles constitue un objectif en soi. Proposez à l'apprenant de construire un schéma simple, qualifier un lien manquant ou critiquer une organisation proposée, puis confrontez sa production à des références validées ou une grille descriptive. Une carte exhaustive générée clé en main pour l'élève est un document de synthèse, non une preuve de sa compréhension personnelle.

Qualifiez explicitement chaque lien : est un prérequis de, fait partie de, s'oppose à, est associé à, ou cause sous telles conditions. Ne déduisez pas une relation causale d'une simple corrélation spatiale et ne réduisez pas un réseau réticulé complexe à une arborescence binaire simpliste. Acceptez les structures alternatives valides ; évaluez le sens et la justification des liens plutôt que leur disposition géométrique à l'écran. Ne supposez pas que le document source répertorie toutes les connexions possibles.

Sur le plan technique, utilisez des identifiants stables et des relations orientées et typées. Prévoyez une alternative textuelle ou sous forme de liste et une manipulation intégrale au clavier si la construction est interactive ; le glisser-déposer ne doit pas être la seule manière de répondre. Un tableau concis de relations peut remplir l'objectif didactique sans nécessiter d'éditeur de graphes complexe. Vérifiez une variante valide et un lien erroné type face aux règles de rétroaction prévues.

### Méthodes: Méthodes contextualisées

- Démarche d'investigation : étayez l'élaboration de questions, l'émission d'hypothèses, le protocole expérimental, l'observation et la formalisation des résultats. Les affirmations relatives au monde réel doivent s'appuyer sur des données empiriques valides ou un modèle étalonné ; les représentations graphiques indicatives doivent signaler explicitement leurs limites d'approximation. La narration d'un modèle de langage ne saurait remplacer une preuve expérimentale.
- Jeu de rôle didactique : définissez le rôle incarné, le cadre de la situation, les critères de réussite et un temps de débriefing réflexif. Signalez tout dialogue historique comme une reconstitution et distinguez les faits documentés des répliques fictives. Une mise en situation narrative peut susciter un engagement affectif ou social notable.
- Apprentissage coopératif : structurez une tâche partagée avec responsabilité individuelle démontrable et critères d'explication mutuelle clairs. Prévoyez une modalité d'arbitrage des désaccords et contrôlez l'assimilation de chaque élève.
- Enseignement par les pairs : amenez les apprenants à s'expliquer les démarches et s'évaluer selon des grilles compréhensibles, avec recours possible à une correction validée ou à l'enseignant. Ne transformez pas un élève novice en autorité suprême sur la justesse disciplinaire.
- Pédagogie de projet : définissez une production authentique, des jalons de travail intermédiaires et des preuves d'apprentissage personnelles. Une esthétique finale flatteuse ne prouve pas l'atteinte des acquis visés.
- Classe inversée : articulez explicitement la phase de découverte autonome avec son réinvestissement actif en classe, et ménagez une modalité pour les élèves n'ayant pas accompli le travail préparatoire. Il s'agit d'une organisation du temps scolaire, pas d'un gage automatique d'apprentissage.
- Ludification : mobilisez des indicateurs de progression ou des éléments narratifs lorsqu'ils étayent l'objectif. La compétition collective, les récompenses matérielles et les scores de rapidité exigent une justification rigoureuse et une alternative accessible.

### Méthodes: Preuves et lectures complémentaires

- [Krathwohl, 2002, A Revision of Bloom's Taxonomy](https://people.ucsc.edu/~ktellez/blooms_taxonomy.pdf) : deux dimensions et une hiérarchie assouplie aux catégories imbriquées.
- [IES, Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/PracticeGuide/1) : recommandations étayées par la recherche sur l'espacement, la récupération active, les exemples résolus et le questionnement explicatif.
- [UNESCO, Orientations pour l'IA générative dans l'éducation et la recherche](https://www.iicba.unesco.org/en/africa-education-knowledge-platform/guidance-generative-ai-education-and-research) : pouvoir d'agir humain et validation des usages éducatifs.
- Zinger, D. (CFM / FALR – Four-Action Learner Regulation Framework) : autorégulation de l'apprenant dans un espace cognitif partagé avec l'IA (Choix, Délai / Pause cognitive, Évaluation, Autorégulation).

## Reference: assessment

Section source: Preuves d'apprentissage, évaluation et rétroaction


### Évaluation: Commencer par la décision pédagogique

Pour chaque objectif d'apprentissage majeur, précisez l'action de l'apprenant, les preuves recueillies, les critères de réussite et la décision didactique consécutive. Précisez les conditions matérielles : accès aux indices, ressources documentaires, travail collaboratif et limites de temps éventuelles. Établissez des critères pratiques ou relationnels lorsque ce sont les acquis réellement visés, plutôt que de leur substituer un simple quiz de restitution mémorielle.

Exemple : face à un circuit électrique inconnu, l'élève prédit l'effet d'une modification et explicite son raisonnement. Les preuves incluent la prédiction et l'explication causale. Une grille critériée vérifie la mobilisation du principe pertinent, son application et la rigueur du raisonnement. La mise en évidence d'une conception erronée déclenche un contre-exemple ciblé et une nouvelle tentative autonome.

### Évaluation: Expliciter les finalités de l'évaluation

En mode entraînement, l'apprenant peut solliciter des explications, retenter une tâche et mobiliser un étayage progressif. Enregistrez le recours à l'aide séparément de la réussite autonome. La rétroaction doit désigner ce qui est correct, identifier l'écart précis et fournir une étape concrète immédiatement exploitable, suivie d'une opportunité de révision ou de réinvestissement.

En mode évaluation, définissez l'assistance autorisée et le barème avant l'épreuve. Maintenez l'assistance du tuteur en cohérence stricte avec ces conditions. Explicitez si la rétroaction est immédiate ou différée, et pourquoi. Ne convertissez pas silencieusement des scores d'entraînement en notes sommatives officielles. L'évaluation formative exploite les preuves pour réguler les apprentissages en cours ; l'évaluation sommative atteste des acquis au regard de critères prédéfinis. Un score sans décision pédagogique subséquente ne constitue pas en soi une évaluation formative.

### Évaluation: Concevoir des tâches rigoureuses et fiables

Vérifiez le corrigé de référence, les explications et les réponses alternatives plausibles. Pour les questions à choix multiples (QCM), privilégiez des distracteurs signifiants liés à des erreurs documentées et évitez les indices fortuits. Pour les réponses ouvertes, acceptez les formulations équivalentes, les démarches alternatives valides et les hypothèses explicitées. Ne faites pas d'une réponse modèle unique la seule formulation recevable.

Utilisez une grille critériée descriptive courte comportant des critères observables, des descripteurs de performance et des exemples, y compris des cas limites et des variantes recevables. Séparez les dimensions lorsque c'est pertinent : exactitude factuelle, rigueur du raisonnement, procédure, clarté d'expression ou coopération. Ne pénalisez la maîtrise formelle de la langue que si elle fait partie intégrante de l'objectif visé. La rapidité d'exécution et le classement public nécessitent une justification pédagogique explicite ; les points d'assiduité, badges et certificats de complétion ne démontrent pas la maîtrise.

Lors de la mise en place d'une banque d'exercices, explicitez les décisions utiles dans le format de données existant. Les champs pertinents peuvent comprendre : identifiant stable de la tâche, identifiant de l'objectif, énoncé, réponses acceptées ou grille d'évaluation, explication, indices, source et état de relecture. Intégrez les unités de mesure et les tolérances numériques si nécessaire. Conservez les traces de réponse séparément : réponse formulée, aide sollicitée, numéro d'essai et statut d'évaluation. Il s'agit d'un exemple indicatif, non d'un schéma obligatoire ; une démonstration collective simple n'exige pas de traçage individuel.

### Évaluation: Limites du jugement de l'IA

Traitez une note ou une classification d'erreur issue d'une IA comme un jugement provisoire. Validez-la par rapport à des exemples relus par des enseignants et des vérifications disciplinaires lorsque c'est possible. En cas de preuve ambiguë, demandez une clarification ou signalez-la pour révision humaine ; ne simulez pas une fausse certitude et n'utilisez pas un indice de confiance non calibré comme une preuve. Donnez aux apprenants un moyen de contester une rétroaction et offrez aux enseignants une possibilité de dérogation manuelle avec affichage de la réponse d'origine et du motif d'évaluation. Toute décision lourde requiert un processus de revue humaine responsable et adapté au contexte.

### Évaluation: Évaluer la réalité de l'apprentissage

Lorsque c'est réalisable, comparez une tâche initiale à une tâche autonome comparable après la phase d'apprentissage, puis vérifiez la rétention après un intervalle de temps et le transfert vers un contexte nouveau. Interprétez les gains avec prudence : la répétition des mêmes items, les indices fournis et des niveaux de départ hétérogènes peuvent fausser les scores. Une expérimentation restreinte en classe permet d'identifier des dysfonctionnements, mais ne démontre pas à elle seule une causalité didactique.

Mesurez la complétion, l'assiduité, le temps passé, l'attrait perçu, la latence et les erreurs comme des indicateurs d'exploitation ou d'ergonomie. Distinguez-les rigoureusement des acquis d'apprentissage réels. Collectez le minimum de données nécessaires à la décision didactique et explicitez ce que les preuves recueillies ne permettent pas de conclure.

### Évaluation: Sources

- [EEF, Teacher Feedback to Improve Pupil Learning](https://educationendowmentfoundation.org.uk/education-evidence/guidance-reports/feedback) : intentions d'apprentissage, identification des écarts, temporalité ciblée et opportunités réelles d'agir sur la rétroaction. Ces recommandations pour l'enseignant ne valident pas automatiquement toute implémentation de feedback par IA.
- [Guide de pratique de l'IES](https://ies.ed.gov/ncee/wwc/PracticeGuide/1) : la pratique de récupération autonome et la réactivation différée inspirent la démarche d'évaluation proposée.

Le flux de travail, la grille critériée d'exemple et les choix de mise en œuvre ci-dessus constituent des recommandations de conception. Leur pertinence doit être appréciée au regard du profil des apprenants, de la discipline, des enjeux de l'évaluation et des preuves observables.

### Évaluation: Vérifier les choix et remédier aux conséquences

Pour un item à réponse unique, résolvez l'énoncé réel de manière indépendante et assurez-vous que chaque option est analysée au regard des unités, de la précision et des hypothèses posées. Une seule option doit rester défendable. Pour les items à réponses multiples, appliquez la règle de correction déclarée ; pour les tâches ouvertes, maintenez les alternatives légitimes. Appliquez ensuite chaque démarche erronée supposée aux données concrètes de l'item : elle doit aboutir précisément au distracteur visé. Revérifiez les options après toute modification d'énoncé. Des fractions équivalentes ou des arrondis implicites ne doivent pas créer une seconde bonne réponse involontaire.

Reliez chaque réponse observée à une explication plausible, à une question de relance discriminante et à une action concrète immédiate. Une seule réponse erronée ne suffit pas à diagnostiquer sa cause profonde. Dans une conception centrée sur les preuves (Evidence-Centered Design), identifiez la compétence cible, les preuves observables et la situation qui permet de les susciter. Les actions dans un jeu peuvent résulter de difficultés motrices, d'exploration fortuite ou de devinette ; la télémétrie seule ne renseigne ni sur la persévérance ni sur la personnalité. Justifiez toute collecte de données.

Si le contenu, le corrigé ou l'explication du tuteur comporte une erreur, reconnaissez-la et corrigez-la sans délai, puis inspectez les indices associés, les tâches dépendantes, les scores et la progression enregistrée. Ne traitez pas une tentative faussée par un énoncé erroné comme une lacune de l'élève. Préservez les traces d'origine nécessaires et l'historique des versions de contenu ; signalez l'incertitude et proposez une nouvelle vérification équitable. Les vues enseignant et apprenant doivent s'appuyer sur la même version des énoncés et des options.

Ces protocoles de vérification sont adaptés, en tant que principes de conception, des [ressources de vérification de la compréhension de Learning Commons](https://github.com/learning-commons-org/agent-skills/tree/main/skills/k12-check-for-understanding). Ils n'en reprennent ni les formats figés, ni les référentiels scolaires états-uniens par défaut, ni les restrictions d'attribution des sources.

## Reference: simulations

Section source: Simulations et jeux de rôle


À consulter lorsqu'un produit modélise un système, soutient une démarche expérimentale ou invite les apprenants à agir au sein d'une mise en situation. Ne réalisez que les vérifications pertinentes pour l'outil considéré.

### Simulations: Identifier la nature des résultats présentés

Distinguez clairement ces catégories d'éléments dans les textes présentés à l'apprenant :

- **Mesure :** observations issues d'un instrument réel, d'un jeu de données authentique ou d'une expérience enregistrée. Indiquez la source et les incertitudes de mesure applicables.
- **Calcul ou simulation :** résultats générés par un modèle mathématique ou algorithmique explicite. Précisez les hypothèses posées et le domaine de validité du modèle.
- **Fiction ou reconstitution :** événements, dialogues, personnages ou conséquences inventés à des fins didactiques. Indiquez-les explicitement comme tels.

Ne qualifiez jamais des données synthétiques de mesures empiriques réelles, ni un dialogue généré de citation historique authentique. Une simulation illustre une hypothèse théorique ; ses résultats seuls ne prouvent pas le comportement du monde physique réel.

### Simulations: Définir et vérifier le modèle

Documentez l'objectif d'apprentissage, les variables d'état, les paramètres d'entrée, les unités, les plages de valeurs autorisées, les hypothèses simplificatrices, les lois d'évolution et les sorties observables. Explicitez les approximations qui influent sur l'interprétation. Proposez des commandes d'interaction qui mettent en valeur la relation didactique visée sans contraindre les apprenants à deviner des réglages cachés.

Pour les aspects quantitatifs, calculez les sorties à l'aide d'un moteur de calcul vérifié ou de règles déterministes strictes. Isolez ce moteur de calcul de tout commentaire produit par un modèle de langage. L'IA peut commenter les résultats effectivement calculés, mais ne doit en aucun cas inventer des valeurs manquantes ou feindre qu'une expérience de laboratoire a été menée.

Appliquez quelques contrôles adaptés au modèle : un cas étalon connu, un cas limite, la cohérence dimensionnelle des unités et une tendance qualitative attendue. Pour les modèles stochastiques, précisez la source d'aléa et permettez la fixation d'une graine (seed) reproductible si nécessaire. Documentez les limites du modèle plutôt que de lui attribuer une portée universelle trompeuse.

### Simulations: Concevoir la boucle d'apprentissage

Demandez à l'apprenant de formuler une prédiction argumentée avant de lancer la simulation lorsque cela sert l'objectif didactique. Permettez-lui de modifier des paramètres signifiants, d'observer le résultat effectif, de le confronter à sa prédiction et de réviser son explication. Intégrez un temps de mise en commun ou de bilan réflexif qui distingue le comportement simulé des réalités du monde physique et interroge les limites de validité du modèle.

Ne validez pas la compréhension sur le seul critère de l'obtention d'une valeur cible par essais-erreurs mécaniques. Exigez une explication causale, une comparaison critique ou un transfert vers une situation nouvelle.

### Simulations: Jeux de rôle historiques et sociaux

Précisez si un personnage est fictif, composite ou inspiré d'une figure historique documentée. Distinguez sans ambiguïté les faits historiques attestés des propos romancés ou reconstitués. Indiquez l'origine des sources historiques et mentionnez les controverses historiographiques le cas échéant. Ne prétendez pas dévoiler les pensées intimes réelles d'une figure historique et ne fabriquez pas de fausses citations d'archives.

Définissez le rôle incarné, le cadre de la situation, l'objectif d'apprentissage et le débriefing consécutif. Offrez la possibilité de quitter le jeu de rôle à tout moment et d'accéder à une explication factuelle directe. Adaptez l'intensité émotionnelle et le sujet au public et au cadre de la classe ; proposez une activité alternative pour les thématiques sensibles. Évaluez la rigueur de l'argumentation ou la qualité de la communication selon des critères explicites ; le simple acquiescement au personnage ne constitue pas une preuve de maîtrise.

## Reference: runtime-ai

Section source: L'IA en cours d'exécution dans les applications éducatives


À consulter uniquement lorsque l'application finale interroge directement un service d'IA en cours d'utilisation. Mobiliser l'IA pour écrire du code ou rédiger des contenus préalablement relus par un enseignant ne relève pas de l'IA en temps d'exécution. Maintenez les activités hors ligne déconnectées, à moins que l'objectif d'apprentissage n'exige impérativement un service distant.

### IA à l'exécution: Définir un rôle didactique délimité

Précisez ce que le modèle est autorisé à faire, quels contenus ou sources vérifiés il peut exploiter et comment il doit réagir en cas d'élément probant manquant. Lorsque l'exactitude des faits est primordiale, déterminez les ressources de référence approuvées et conservez la traçabilité des sources. N'inventez pas de références bibliographiques d'apparence plausible. Acceptez le doute méthodique et la correction ; bannissez les diagnostics hâtifs ou les affirmations catégoriques sur les capacités d'un apprenant à partir d'un court échange.

Adaptez l'étayage à la nature de l'activité. L'entraînement peut mobiliser des questions de relance, des indices progressifs, des exemples résolus ou une explication directe à la demande ou lorsque le questionnement s'avère stérile. Une évaluation peut restreindre l'aide selon les consignes explicites de l'enseignant. N'imposez pas un questionnement socratique sans fin ni une interdiction absolue de fournir la réponse. Permettez à l'apprenant de demander de l'aide, d'interrompre l'échange ou de solliciter l'enseignant.

Concevez l'interface d'IA pour empêcher le copier-coller passif, où l'outil se substitue à la réflexion de l'élève. Avant d'adopter une démarche ou une réponse générée, exigez un bref contrôle cognitif de l'apprenant : clarifier son intention avant la requête, marquer une pause réflexive sur la proposition, évaluer sa complétude et sa justesse, et choisir l'action suivante (poursuivre, vérifier, reformuler ou rejeter la suggestion).

Appuyez-vous sur des grilles critériées explicites pour la rétroaction et l'évaluation des réponses ouvertes. Confrontez les jugements du modèle à des étalons validés par des enseignants avant de vous y fier. Toute décision certificative, d'orientation ou disciplinaire exige une révision humaine responsable ; une réponse de modèle ne peut en aucun cas être le seul décisionnaire. Enregistrez les incertitudes et prévoyez la possibilité pour l'enseignant d'invalider une évaluation automatique.

### IA à l'exécution: Réduire les données des apprenants au strict minimum

Documentez les données transmises au fournisseur de modèle, ce qui est conservé, qui y a accès et les modalités de suppression. Ne collectez que le strict nécessaire à l'activité pédagogique. N'ajoutez pas automatiquement de comptes personnels, de noms réels, de profils persistants ou d'historiques intégraux de conversation. Recourez à des identifiants d'activité anonymes ou pseudonymes lorsque c'est suffisant, tout en reconnaissant que cela ne constitue pas une garantie d'anonymat absolu.

Avant tout déploiement auprès d'élèves mineurs, vérifiez la tranche d'âge, les conventions de l'établissement, les conditions contractuelles du fournisseur et les exigences légales applicables (notamment le RGPD) auprès de l'institution responsable. N'inventez pas d'âge de consentement universel ou de règle juridique imaginaire. Expliquez le traitement des données aux élèves et aux enseignants dans un langage clair et adapté.

### IA à l'exécution: Mettre en place des garde-fous architecturaux

Conservez les identifiants et clés d'API au sein d'un composant serveur sécurisé dès qu'un service distant exige des secrets. Ne les exposez jamais dans le code exécuté par le navigateur client. Appliquez les contrôles d'autorisation, les quotas de requêtes et les restrictions d'outils en dehors du prompt textuel. Traitez les entrées des apprenants, les documents récupérés et les réponses du modèle comme des données non fiables par défaut.

Séparez rigoureusement les instructions système des contenus injectés, restreignez les accès et cibles des outils, validez les sorties structurées et assainissez les contenus affichés dans le navigateur. Empêchez le texte généré de devenir directement du code exécutable ou de déclencher des actions à privilèges. Un prompt ordonnant au modèle d'ignorer les attaques par injection ne constitue pas une garantie de sécurité. Diligentez un audit de sécurité dédié pour l'architecture mise en œuvre.

### IA à l'exécution: Anticiper les coûts, les pannes et la continuité

Définissez un budget d'exploitation réaliste, des plafonds par session, des délais d'attente (timeouts) et la possibilité d'annuler une requête. Affichez un état compréhensible pendant les temps de traitement. Gérez la perte de réseau, l'indisponibilité des modèles, les formats de sortie invalides et l'épuisement des quotas sans jamais perdre le travail en cours de l'élève. Ne retentez les requêtes que de façon sécurisée et strictement délimitée.

Prévoyez une solution de repli adaptée : indices prédéfinis relus, exercices statiques, sauvegarde de l'avancement ou recours à l'enseignant. Signalez explicitement qu'une rétroaction est momentanément indisponible plutôt que de fabriquer une réponse artificielle. Avant tout usage en classe, testez le parcours nominal, une réponse erronée, une demande d'aide, une rétroaction ambiguë et une panne totale du service. Documentez les limites non résolues et les responsabilités de contrôle de l'enseignant.

### IA à l'exécution: Vérifier les contenus générés dans des limites définies

Avant de diffuser des exercices générés, effectuez les vérifications nécessaires : exactitude notionnelle, solvabilité mathématique ou logique, cohérence des transitions d'état et qualité du rendu. N'exigez l'unicité que pour les exercices qui la garantissent formellement. Validez les permissions et les schémas de sortie structurée en dehors du modèle ; un schéma formel ne garantit pas la véracité d'un contenu et des tests déterministes n'assurent que les propriétés qu'ils contrôlent effectivement. Rejetez ou isolez les contenus invalides et conservez une ressource de secours préalablement validée. Pour corriger les indices, évaluations et progressions dépendantes, appliquez la procédure de remédiation détaillée dans `assessment.md`.

## Reference: model-profiles

Section source: Modèles, niveau d'effort, vitesse et adaptation aux environnements hôtes


À consulter pour recommander un modèle, régler l'effort de raisonnement ou la vitesse, ou adapter la modalité de chargement du skill selon l'environnement hôte. Conservez des instructions pédagogiques identiques quel que soit le fournisseur.

### Profils de modèles: Ce que cette référence ne prétend pas

Ces préconisations constituent des points de départ opérationnels pour ce flux de travail, non un banc d'essai exhaustif ou un classement d'efficacité mesuré. Elles ne prouvent pas qu'une famille de modèles enseigne mieux qu'une autre et ne prédisent pas la latence. Les appellations commerciales, les paramètres disponibles, les abonnements et les tarifs évoluent rapidement. Avant d'utiliser un modèle mentionné, vérifiez la liste des modèles réellement accessibles à l'utilisateur et la documentation officielle à jour. Un libellé dans une interface n'est pas nécessairement un identifiant de modèle d'API. Validez une configuration sur des tâches représentatives avant de la qualifier de vérifiée.

Documentation vérifiée au : 04/11/2026.

### Profils de modèles: Choisir selon la tâche avant de choisir un nom

Mobilisez un modèle léger pour les retouches délimitées aux critères explicites, un modèle intermédiaire pour la conception et l'implémentation ordinaires, et un modèle de pointe pour l'arbitrage de sources contradictoires, les simulations complexes ou les audits à fort enjeu. Ce sont des catégories de tâches, non des garanties intrinsèques de performance. Conservez le choix actuel de l'utilisateur dès lors qu'il répond aux exigences.

Le tableau ci-dessous constitue une **recommandation de départ non testée empiriquement pour ce skill**, déduite de la documentation des constructeurs.

### Profils de modèles: Règles d'escalade et d'interruption

Pour une tâche claire, débutez avec le niveau d'effort par défaut ou un paramétrage ayant déjà fait ses preuves. Face à des sources contradictoires ou un modèle scientifique complexe, envisagez un effort accru d'emblée. Si la réponse omet une contrainte explicite, contredit son propre barème, échoue à un calcul significatif ou génère de manière répétée des exercices non valides, vérifiez d'abord si les données d'entrée et la référence étaient accessibles. Corrigez un paramètre manquant ou un critère ambigu avant de changer de modèle.

Si une correction ciblée échoue toujours sur le même critère majeur, préconisez d'augmenter le niveau d'effort supporté et réévaluez ce critère. Si l'échec persiste, recommandez un modèle plus puissant disponible ou une relecture humaine indépendante selon l'impact de la tâche. Ne bouclez pas indéfiniment et ne dépassez pas le budget alloué. En cas de source documentaire absente, d'outils inaccessibles ou de coupure de service, traitez la dépendance ou explicitez la limite technique ; un surplus de raisonnement ne peut suppléer des données manquantes. Signalez les échecs non résolus. Ne modifiez les réglages que par les commandes autorisées par l'hôte.

Ne réduisez l'effort ou ne basculez vers un modèle plus petit qu'après validation des tests probants ; conservez la trace de cet arbitrage. Traitez la vitesse de service séparément : le débit standard est le point de départ ; une accélération payante requiert une justification de temps ou de coût et l'accord préalable de l'utilisateur.

### Profils de modèles: Maintenir les recommandations à jour

Réexaminez les conseils spécifiques dès que la version du modèle ou de l'hôte change, qu'un réglage disparaît, que le fournisseur modifie ses accès ou que le comportement observé contredit la documentation. Jusqu'à vérification formelle, considérez cette association comme non vérifiée et appuyez-vous sur les catégories de tâches et les réglages par défaut de l'hôte. N'inventez pas de réglage équivalent pour un modèle non répertorié. N'introduisez des palliatifs propres à un fournisseur qu'après qu'un échec reproductible en a prouvé la nécessité ; notez la version concernée et supprimez le contournement dès qu'il n'est plus justifié.

### Profils de modèles: Faire correspondre la tâche et le contrôle

| Tâche | Point de départ OpenAI | Point de départ Claude | Point de départ Gemini |
|---|---|---|---|
| Retouches textuelles précises ou revue d'items structurés | GPT-6 Luna, High ; réduire l'effort seulement après succès des tests | Haiku 5.5, Medium | Gemini 3.5 Flash-Lite, Low si disponible |
| Conception et développement d'une activité d'apprentissage délimitée | GPT-6.1 Sol, effort par défaut ou Medium | Sonnet 5.5, Medium pour le travail agentique bien cadré | Gemini 3.8 Flash, Medium |
| Audit didactique complexe, sources divergentes, simulation lourde ou architecture | GPT-6 Astra, Light/Low ou Medium ; augmenter si nécessaire | Opus 5.5, Medium, puis High si nécessaire | Gemini 4 Argon, Medium, puis High si nécessaire |

Ces correspondances sont les recommandations de l'auteur déduites des documentations constructeurs. Si un modèle sélectionné est indisponible, suggérez une alternative accessible et signalez ce changement ; ne modifiez pas le choix de l'utilisateur sans autorisation. Par exemple, un flux de travail existant sur Gemini 3.1 Pro peut conserver ce modèle et ses niveaux de réflexion supportés. Mesurez une tâche représentative en conditions réelles pour apprécier la latence effective.

Distinguez trois leviers : le modèle, l'effort de réflexion (thinking / reasoning effort) et le niveau de vitesse de service prioritaire. Un effort moindre réduit le travail d'inférence ; le niveau Fast d'un fournisseur constitue une commande distincte pouvant engendrer un surcoût. Un modèle nommé Flash appartient à une gamme technique et n'est pas un simple commutateur d'accélération. Des mentions identiques telles que Low, Medium ou High ne garantissent pas un raisonnement ou une latence équivalents d'un produit à l'autre.

Commencez par la vitesse de service standard. Ne proposez un niveau Fast payant que si le temps d'attente est critique et que les droits d'accès et tarifs le justifient. Ne l'activez pas sans accord formel. Le streaming améliore la visibilité de l'avancement ; il ne constitue pas une preuve d'achèvement plus rapide ni d'une qualité supérieure. Évaluez le temps global de bout en bout, incluant relectures, appels d'outils et corrections.

### Profils de modèles: OpenAI et Codex

Utilisez le paquet natif lorsque l'environnement supporte les skills et peut lire les références. Dans Codex, l'invocation explicite peut mentionner `$learning-methodologies` ou `$methodologies-apprentissage`. Ne présumez pas d'une découverte similaire sur le système de fichiers dans un chat ordinaire ; fournissez plutôt l'édition Markdown autonome comme document d'entrée.

La documentation actuelle préconise Sol pour les travaux substantiels, Luna pour les tâches ciblées et Astra pour les flux exigeants ; Luna High et Astra Light/Low sont des réglages de départ documentés. Dans Codex, Fast correspond à une vitesse d'inférence distincte de l'effort de raisonnement. Les disponibilités et quotas dépendent du modèle, du compte et du client. Vérifiez les valeurs supportées avant de soumettre une configuration ; un libellé d'interface n'est pas forcément l'identifiant API du modèle.

Fournissez un livrable concret, un périmètre strict, les fichiers concernés et des critères d'acceptation observables. Demandez des arbitrages concis et des preuves, non le dévoilement d'un flux de pensée interne privé. Utilisez les outils et permissions de l'hôte ; ne supposez pas d'accès shell ou navigateur à partir du seul nom du modèle.

Sources : [modèles](https://learn.chatgpt.com/docs/models), [vitesse](https://learn.chatgpt.com/docs/agent-configuration/speed), [skills](https://developers.openai.com/plugins/concepts/skills).

### Profils de modèles: Claude et Claude Code

Claude Code prend en charge les paquets `SKILL.md` et leurs fichiers d'appui. L'invocation explicite peut utiliser `/learning-methodologies` ou `/methodologies-apprentissage` après découverte. Dans un autre environnement Claude, vérifiez la prise en charge des skills ou fournissez l'édition autonome. N'ajoutez pas de hooks exclusifs à Claude, de substitutions shell ou de forçages de modèles dans le frontmatter commun.

Pour le travail agentique avec Sonnet 5.5, la documentation relative à l'effort conseille Medium pour les tâches bien délimitées et un niveau plus élevé pour les problèmes ardus. Opus 5.5 est réglé par défaut sur Medium ; les modèles antérieurs et les interfaces clientes peuvent diverger. Le contrôle d'effort de l'API et le mode réflexion (thinking) sont des concepts distincts. Toutes les versions ne prennent pas en charge les mêmes combinaisons. Privilégiez les commandes officielles de l'hôte plutôt que de recopier un paramètre d'API dans une consigne textuelle. Le mode Fast de Claude est une option payante distincte tributaire du modèle.

Délimitez strictement la tâche, les ressources documentaires et le livrable attendu. Indiquez où l'agent dispose d'une marge d'arbitrage et ce qui exige une justification probante. Fournissez un exemple pertinent pour lever une ambiguïté ; évitez de répéter l'intégralité du skill ou d'imposer une longue transcription réflexive. Ce choix de conditionnement favorise la portabilité et ne relève pas d'une prétendue spécificité cognitive propre à Claude.

Sources : [skills](https://code.claude.com/docs/en/skills), [modèles](https://platform.claude.com/docs/en/models/overview), [effort](https://platform.claude.com/docs/en/build-with-claude/effort), [mode Fast](https://platform.claude.com/docs/en/build-with-claude/fast-mode).

### Profils de modèles: Gemini et Gemini CLI

Gemini CLI découvre les skills natifs dans les répertoires supportés, y compris l'alias `.agents/skills`. Vérifiez la liste avec `/skills list` et rechargez avec `/skills reload` si nécessaire. La confiance accordée à l'espace de travail et l'autorisation d'activation relèvent de l'hôte ; ne cherchez pas à les contourner. AI Studio ou une interface de chat classique doivent recevoir le fichier Markdown autonome lorsqu'aucun mécanisme natif de skill n'est disponible.

Le guide documenté sur la réflexion liste Low, Medium et High pour Gemini 4 Argon et Gemini 3.8 Flash. D'autres versions de Gemini ont des niveaux et réglages par défaut différents. N'utilisez que les valeurs supportées par le modèle et l'API/client effectifs ; ne transposez pas littéralement un paramètre d'effort d'OpenAI ou de Claude. Un nom de version préliminaire (preview) et un nom stable ne sont pas interchangeables.

Pour `gemini-3.1-pro-preview`, la documentation API mentionne Low, Medium et High, High étant la valeur par défaut. Pour ce point de terminaison, nous suggérons Medium pour la conception ordinaire et High pour un audit difficile, dès lors que l'hôte expose ces leviers. Un libellé affiché comme Gemini 3.1 Pro ne préjuge pas du point d'accès technique ou des options réelles du client.

Formulez des consignes concises précisant le but, les contraintes et les preuves attendues. Joignez les documents référencés afin que le modèle puisse réellement les consulter ; un simple chemin de fichier dans un message ne vaut pas accès physique au fichier. Préservez l'état de conversation requis pour les outils lors du développement d'une application avec l'API Gemini, conformément à la documentation officielle. Ce skill n'implémente pas cette couche d'API et n'autorise pas à en ajouter une de sa propre initiative.

Sources : [modèles](https://ai.google.dev/gemini-api/docs/models), [réflexion](https://ai.google.dev/gemini-api/docs/thinking), [skills Gemini CLI](https://geminicli.com/docs/cli/tutorials/skills-getting-started/).

### Profils de modèles: Usage portable et protocole de vérification

Conservez des métadonnées minimales : `name` et `description`, suivis de Markdown standard. Les métadonnées facultatives décrivent l'édition linguistique ; ne vous appuyez pas sur un champ propriétaire d'un hôte pour garantir une règle de sécurité. Utilisez les références relatives groupées dans un agent capable de lire des fichiers locaux, ou l'édition autonome complète dans une invite de chat. Ne chargez pas simultanément plusieurs éditions linguistiques par défaut. Rétablissez le périmètre essentiel et les travaux en cours après une perte de contexte de l'hôte plutôt que de présumer qu'il les a conservés.

Les emojis peuvent véhiculer du sens mais ne doivent jamais constituer l'unique signal de consigne ou de priorité. Conservez des libellés textuels explicites. Les recherches sur la [sémantique des emojis](https://arxiv.org/abs/2409.10760) et l'[ambiguïté contextuelle](https://arxiv.org/abs/2511.07193) ne démontrent pas qu'orner ce skill améliore la conformité aux consignes. Testez ces ajustements sur les modèles et tâches réels avant d'en revendiquer le bénéfice.

Avant de déclarer une association modèle/hôte validée, vérifiez la découverte ou le chargement autonome réussi, l'accès effectif aux références pertinentes, la production d'un livrable représentatif et le respect des limites critiques. Consignez l'identifiant exact du modèle ou son nom affiché, l'hôte et sa version, la langue, le niveau d'effort, la vitesse de service, les outils, la date, les artefacts générés et les échecs constatés. Distinguez la compatibilité sur catalogue de l'exécution empirique constatée. Ne transposez jamais la validation d'un modèle à l'ensemble de sa famille.

Pour une étude comparative, utilisez strictement la même tâche et les mêmes données brutes, et faites évaluer les livrables par un relecteur selon les mêmes critères didactiques. Intégrez la réutilisation du contexte connu, la modération de l'aide, l'acceptation d'une réponse alternative valide, le rejet d'allégations curriculaires infondées, le respect des frontières modèle/données et la gestion d'une coupure d'outil ou de service. Ne réduisez l'effort ou ne retenez un modèle plus léger que tant que les vérifications critiques restent satisfaites. Si l'accès direct à un fournisseur n'est pas possible, indiquez-le comme non testé plutôt que d'extrapoler des résultats.

## Reference: decision-examples

Section source: Exemples de décisions


Consultez l'exemple pertinent pour trancher une ambiguïté concrète. Adaptez la discipline et la tranche d'âge ; préservez le principe de décision sous-jacent.

### Exemples de décision: Accepter une réponse équivalente

Tâche : exprimer 1,5 A en milliampères. L'apprenant saisit `1500 mA` alors que le validateur automatique attend strictement `1500`. Acceptez la grandeur équivalente en vérifiant conjointement la valeur numérique et l'unité. Si l'objectif d'apprentissage porte précisément sur la notation des unités, évaluez cet aspect de manière ciblée. Ne traitez pas arbitrairement n'importe quelle chaîne comme équivalente en supprimant les caractères : `1500 A` est incontestablement faux ici. Pourquoi : les contraintes de formatage ne doivent pas supplanter la preuve didactique de la conversion d'unités.

### Exemples de décision: Mettre fin à une boucle socratique stérile

En phase d'entraînement, un apprenant déclare « Je ne comprends toujours pas, montrez-moi comment faire » après une relance sur la relation entre intensité et résistance. Fournissez une explication concise ou un exemple résolu pas à pas à tension constante, puis proposez une nouvelle prédiction avec étayage optionnel. Ne transformez pas le questionnement en préalable bloquant à l'obtention d'aide. Consignez l'exemple résolu comme une situation d'apprentissage étayée ; un problème indépendant inédit fournira une preuve distincte. Pourquoi : le questionnement doit soutenir le progrès cognitif de l'apprenant, non entraver l'apprentissage. Une situation formelle d'évaluation peut obéir à des règles d'aide différentes.

### Exemples de décision: Corriger une explication Feynman inexacte

Un apprenant explique : « Les plantes puisent leur nourriture dans le sol ; le soleil réchauffe la terre. » Saluez la clarté de l'expression tout en rectifiant l'erreur scientifique. Isolez la conception erronée précise, fournissez ou consultez une source vérifiée adaptée, distinguez l'absorption d'eau et de sels minéraux de la synthèse de matière organique lors de la photosynthèse, puis invitez l'apprenant à reformuler simplement son explication. Vérifiez le transfert sur une situation nouvelle, telle que l'évolution d'une plante privée de lumière. Pourquoi : l'aisance verbale et la simplicité apparente ne valent pas exactitude disciplinaire. N'inventez pas d'observations expérimentales et n'attribuez pas toute la croissance végétale à un seul facteur.

### Exemples de décision: Travailler en l'absence de programme officiel fourni

Un enseignant sollicite « un alignement total sur le programme de notre établissement » sans fournir de référentiel textuel. Exploitez l'objectif pédagogique formulé pour concevoir une activité provisoire. Ne demandez l'extrait du programme que lorsque l'alignement formel exact est indispensable ; explicitez clairement ce qui demeure non vérifié. N'inventez jamais de codes de compétences locaux et ne certifiez pas une couverture notionnelle sans source. Pour les contextes scolaires spécifiques, une référence générique à un cadre national ne garantit pas la conformité au projet pédagogique de l'établissement. Pourquoi : cela permet d'avancer utilement sur la production tout en rendant transparentes les limites documentaires de la proposition.

### Exemples de décision: Insérer une pause cognitive avant d'adopter une production d'IA

Dans une application intégrant un assistant d'IA, un apprenant sollicite une ébauche de solution ou l'explication d'une erreur. Plutôt que de proposer un bouton « Appliquer à ma réponse », insérez une pause cognitive : empêchez le copier-coller direct et posez une question brève de contrôle (« Quelle étape est centrale ici ? Que manque-t-il dans la proposition de l'IA pour traiter ton cas spécifique ? »). Permettez à l'apprenant de retravailler la proposition, de la tester sur un autre exemple ou de décider de ne pas l'utiliser. Enregistrez le texte généré par le modèle comme une aide reçue, et non comme une preuve de compréhension autonome de l'apprenant. Pourquoi : cette pause évite l'adoption passive et acritique de la réponse de l'IA par l'apprenant.

## Reference: tutor-state

Section source: Modes du tuteur et continuité de l'apprentissage


À consulter lors de la conception d'un tuteur guidé à étapes multiples, d'une activité avec reprise de session ou d'un entraînement aux examens. Ces règles s'appliquent également aux applications déterministes hors ligne ; elles n'exigent ni IA en temps réel, ni gestion de comptes, ni base de données distante.

### État du tuteur: Modéliser des modes explicites et leurs transitions

Séparez nettement la phase d'explication, d'entraînement et d'évaluation lorsque l'activité le requiert. L'explication peut présenter un exemple résolu. L'entraînement sollicite une réponse, attend la saisie, fournit une rétroaction critériée et propose de l'aide. L'évaluation applique des règles déclarées régissant l'aide autorisée et le moment de la correction. Permettez à l'apprenant de faire une pause, de solliciter de l'aide ou de quitter l'activité ; une évaluation sommative stricte peut clôturer la tâche ou enregistrer l'essai comme assisté dès qu'une aide notionnelle est appelée. Préservez les aménagements d'accessibilité qui ne dévoilent pas le contenu didactique.

Pour un entraînement conversationnel, maintenez une seule question opérationnelle en attente, sauf si l'activité requiert un travail par lot. Ne générez pas la réponse de l'apprenant à sa place et ne révélez pas la solution pendant qu'il réfléchit. Distinguez les états : inactif (idle), en attente de réponse, en cours d'évaluation, rétroaction affichée et en pause. Bloquez les soumissions répétées ou rattachez-les au même essai ; une réponse tardive d'un service ne doit jamais noter une question ultérieure ni écraser un changement de mode. La production d'un modèle d'IA n'est qu'une proposition ; seul l'enseignant valide les notes et les règles d'évaluation.

Conservez le mode courant, l'objectif, la tâche active, l'identifiant de la tentative, l'état de révélation de la solution et le statut de la rétroaction dans l'état de l'application. Affichez un indicateur de progression concis si utile ; répéter une ligne de statut décorative ne constitue pas une gestion d'état. Lors d'un changement de mode explicite, prévenez des nouvelles conditions d'aide et conservez l'historique des aides consultées. Modifier une étiquette d'interface ne transforme pas un exercice dont la solution a été révélée en évaluation autonome. Proposez une tâche inédite adaptée lorsqu'une nouvelle preuve autonome est requise.

### État du tuteur: Reprendre à partir de preuves d'apprentissage, non d'allégations de maîtrise

N'intégrez de sauvegarde ou d'export que si la reprise entre plusieurs sessions apporte une réelle valeur à l'utilisateur. Une activité courte et anonyme peut se dispenser des deux. Pour une activité avec reprise, conservez un point d'étape minimal adapté à l'implémentation :

- Version du format, version de l'activité/du contenu et identifiants des sources documentaires.
- Objectif, mode actif, identifiant de la tâche/tentative et étape en attente.
- Preuves observées avec leurs conditions d'obtention : autonome, assistée ou solution révélée ; une évaluation non résolue demeure en attente.
- Erreurs précises ou doutes identifiés et prochaine étape pédagogique.
- Données temporelles uniquement si nécessaire pour l'espacement des révisions ou l'interprétation des preuves.

Évitez les diagnostics catégoriques, les données d'identité superflues et les historiques intégraux de conversation. Explicitez le lieu de stockage des données, qui peut y accéder et comment les purger ; sur machine partagée, les élèves doivent disposer d'un bouton explicite pour terminer leur session et effacer leurs traces locales. Un fichier d'export peut contenir des données d'apprentissage personnelles même sans mention nominative. N'exportez jamais de clés d'API secrètes, de corrigés masqués ou de banques de tests confidentielles.

Traitez les fichiers de reprise importés comme des données non fiables. Validez le schéma, les tailles, les identifiants et la compatibilité des versions ; n'exécutez jamais d'instructions incorporées et n'acceptez pas des scores importés comme des notes officielles incontestables. Lorsque les notes ont un enjeu officiel, validez-les auprès du système de gestion de l'établissement avec les contrôles d'accès appropriés. Si le contenu a évolué ou qu'une tâche ne peut être restaurée, expliquez l'écart et reprenez à un état stable vérifié ; ne réinitialisez pas silencieusement les acquis et ne validez pas des preuves obsolètes. La restauration d'une tentative en suspens ne doit ni la soumettre automatiquement ni attribuer les points deux fois.

Une transmission de bilan consigne ce que l'apprenant a démontré, sur quelle tâche et avec quel degré d'étayage. Elle n'affirme jamais une « maîtrise totale » à l'issue d'une seule session. Une tâche ultérieure inédite permettra d'évaluer la rétention et le transfert. Les corrections validées par l'apprenant et les dérogations manuelles de l'enseignant doivent rester discernables de l'observation brute initiale.

### État du tuteur: Cibler la remédiation sans enfermer l'apprenant

Hiérarchisez les erreurs selon leur importance vis-à-vis de l'objectif et des prérequis, la gravité de l'erreur étant traitée comme une interprétation provisoire. Proposez un indice progressif, un cas contrasté ou une explication ciblée, suivis d'une nouvelle situation d'application. Autorisez l'ajournement et la révision ultérieure. N'imposez pas de seuils arbitraires de 8/10 ou 90 %, n'interdisez pas les explications et n'attribuez pas de points à chaque clic. Utilisez des critères transparents lorsque la notation apporte une valeur pédagogique ; la préparation aux examens officiels requiert le barème institutionnel exact.

### État du tuteur: Tests d'implémentation

Ne testez que les parcours pertinents : question → réponse → rétroaction ; aide → preuve assistée enregistrée ; bascule de mode après affichage de la solution ; pause/reprise sans perte ni double comptage d'un essai ; fichier de reprise corrompu ou obsolète ; réponse tardive après changement de question ; rétroaction en suspens après un échec réseau. Vérifiez la concordance stricte entre l'état stocké en mémoire et l'état affiché à l'écran. Ces tests valident le comportement applicatif, non l'efficacité éducative globale.

## Reference: didactic-rationale

Section source: Pourquoi les méthodes didactiques s'imposent dans le développement d'applications assisté par l'IA


À consulter pour expliciter la finalité de ce skill ou déterminer comment une méthode pédagogique doit modifier concrètement une application. Le skill accompagne les développeurs et les éducateurs qui s'appuient sur l'IA pour concevoir et réaliser des applications éducatives. Il encadre également les applications mobilisant l'IA pendant l'apprentissage, lorsque cet usage est justifié. La démarche didactique doit s'incarner dans les actions de l'apprenant, les rétroactions et les preuves observables. Une simple consigne dans un prompt ou une étiquette valorisante dans l'interface ne suffisent pas.

### Justification didactique: Traduire une décision didactique en comportement observable

| Méthode ou angle | Finalité pédagogique | Décision applicative | Preuve à observer |
|---|---|---|---|
| Questionnement socratique | Examiner les postulats et le raisonnement de l'apprenant | Poser une question ciblée, attendre, réagir à la réponse effective ; fournir une explication si le blocage persiste | Capacité de l'apprenant à justifier ou réviser son affirmation, y compris par une alternative valide |
| Technique de Feynman et auto-explication | Rendre l'explication de l'apprenant explicite et analysable | Inviter l'apprenant à expliquer avec ses mots, comparer à des critères validés, traiter une lacune précise, puis proposer un cas inédit | Relations conceptuelles exactes et réinvestissement ; l'aisance verbale seule ne suffit pas |
| Exemples résolus et étayage progressif | Permettre au novice de démarrer et progresser vers l'autonomie | Proposer une étape résolue, une tâche à compléter et un nouveau problème adapté ; maintenir l'aide accessible sur demande | Distinguer la performance étayée d'une tentative autonome ultérieure |
| Pratique de récupération et réactivation espacée | S'entraîner à reconstruire les connaissances et les réactiver après un délai | Interroger avant de dévoiler ; fournir une rétroaction corrective et planifier des rappels différés, y compris sur les notions maîtrisées | Performance avant révélation de la solution, rétention différée et transfert vérifié |
| Cartes conceptuelles | Rendre explicites les interrelations et les prérequis | Utiliser des liens sémantiques qualifiés, accepter les structures valides équivalentes et offrir une alternative accessible | Sens et justification des relations établies, et non simple ressemblance graphique |
| Démarche d'investigation et simulations | Confronter les prédictions aux observations sous des hypothèses explicites | Exposer les variables clés, les unités, les contraintes et les limites du modèle ; intégrer un bilan réflexif | Révision de l'explication par l'apprenant à partir des observations ou des résultats étiquetés du modèle |
| Évaluation formative et métacognition | Décider d'une action pédagogique constructive à partir des preuves | Fournir une rétroaction spécifique et permettre de confronter sa prédiction à sa performance réelle | Action corrective concrète et nouvelles preuves produites ; notes et indices d'assurance ne suffisent pas seuls |
| Apprentissage coopératif et par les pairs | Favoriser la confrontation d'idées et l'explication mutuelle responsable | Assigner une tâche partagée avec contributions individuelles identifiables et résolution argumentée des désaccords | Raisonnement de chaque apprenant ; un clic commun ne prouve pas la compréhension du groupe |
| Régulation en espace cognitif partagé (FALR) | Maintenir l'apprenant actif et critique face aux suggestions de l'IA | Insérer une pause cognitive avant d'adopter un résultat ; demander ce qui manque et ce que l'élève a compris par rapport à l'IA ; permettre le rejet de l'aide | Distinction entre compréhension propre et production du système, suivie d'une étape autonome de l'apprenant |

La taxonomie de Bloom aide à catégoriser les objectifs cognitifs et les types de connaissances ; elle ne dicte pas la difficulté intrinsèque d'une tâche ni un déblocage rigide en six étapes. Une méthode n'est légitime que si elle répond au profil des apprenants, au contenu disciplinaire et à l'obstacle didactique constaté. Ce catalogue n'impose en aucun cas de tout implémenter.

### Justification didactique: Pourquoi cela compte lorsque l'IA participe au développement

L'IA permet de générer en quelques secondes une interface, un validateur de réponses et des messages de rétroaction. Ces éléments requièrent pourtant un contrat pédagogique explicite : ce que l'apprenant doit faire, ce qui constitue une preuve d'apprentissage, quelle aide était accessible et comment s'enchaîne la décision didactique suivante. Utilisez ce contrat pour guider et contraindre le code produit ainsi que les contenus relus. Par exemple, la pratique de récupération modifie le moment où la réponse est dévoilée, tandis que l'étayage structure les commandes d'aide et l'enregistrement des preuves. Nommer une méthode sans implémenter ces comportements concrets trahit l'intention pédagogique.

Distinguez l'IA mobilisée au moment de la création (authoring) de l'IA active lors de l'apprentissage (runtime). Des contenus statiques rigoureusement validés et des vérifications déterministes permettent d'implémenter l'essentiel de ces comportements hors ligne. Si une IA en temps d'exécution est utile pour traiter des réponses ouvertes ou animer un dialogue, délimitez strictement ses sources documentaires, ses critères d'évaluation et ses outils, validez ses sorties et prévoyez une solution de repli en cas de panne. Développer un dialogue plus bavard, durcir les critères d'évaluation ou utiliser un modèle plus volumineux ne garantit en rien un meilleur apprentissage.

### Justification didactique: Délimiter la portée de cette argumentation

Ce document explicite des choix de conception didactique ; il ne prouve pas que ce skill ou chaque application en découlant améliore mécaniquement les résultats scolaires. L'exactitude disciplinaire, l'accessibilité réelle et la faisabilité en classe exigent des vérifications en contexte authentique. Une validation technique réussie ne démontre pas l'apprentissage ; des preuves recueillies auprès des apprenants et, pour les allégations d'efficacité causale, une évaluation méthodologique appropriée demeurent indispensables. Les études citées dans la référence des méthodes éclairent des choix ciblés sans certifier l'ensemble de la solution. Maintenez une révision humaine par l'enseignant pour les décisions à fort enjeu et adaptez les programmes aux réalités de la classe.

## Reference: learning-games

Section source: Jeux d'apprentissage et ludification raisonnée


À consulter lorsqu'un projet nécessite des mécaniques de jeu, des leviers motivationnels ou une refonte substantielle de l'articulation entre jeu et apprentissage. Ces recommandations croisent la recherche empirique et des repères de conception ; elles ne garantissent pas à elles seules l'efficacité d'un nouveau produit. Preuves vérifiées : 14/11/2026.

### Jeux d'apprentissage: Choisir l'activité d'apprentissage avant la récompense

Distinguez le jeu d'apprentissage (l'apprentissage s'opère par l'action de jeu), la ludification ou gamification (des éléments de jeu soutiennent une autre activité) et la simulation (un modèle permet l'investigation sans logique de score ou de victoire). Un excellent outil pédagogique peut se passer entièrement des systèmes de récompense décrits ci-après.

Rédigez un contrat de conception synthétique : apprenant cible et prérequis ; performance visée ; décision du joueur ; conséquence et rétroaction ; preuve autonome ; étape d'apprentissage suivante. Pour une micro-activité, un paragraphe suffit. Identifiez les raccourcis possibles : le joueur peut-il gagner en devinant au hasard, en cliquant compulsivement, en mémorisant des emplacements, en lisant la réponse ou en se reposant sur un partenaire ?

Privilégiez des mécaniques qui sollicitent directement l'opération cognitive visée. Pour enseigner le raisonnement proportionnel, amenez le joueur à ajuster un dosage sous des contraintes signifiantes, à expliciter une prédiction et à résoudre un problème inédit. Un quiz classique reste parfaitement pertinent pour la pratique de récupération mémorielle ; il n'est pas nécessaire de transformer chaque notion en monde virtuel simulé. Pour les objectifs d'exploration, autorisez plusieurs démarches défendables.

### Jeux d'apprentissage: Sélectionner un ensemble restreint et cohérent

| Besoin | Mécanique candidate et implémentation | Condition de vérification ou d'échec |
|---|---|---|
| Débuter sans connaître les commandes | Une première tâche jouable sans risque ; introduire un outil uniquement au moment utile | Un nouvel utilisateur réussit l'action sans que le concepteur n'ait à intervenir |
| Comprendre un système | Prédire, modifier une seule variable, observer les effets, expliciter | Une manipulation désordonnée ne doit pas tenir lieu de prédiction |
| Consolider la mémorisation | Missions de rappel réactivées après un intervalle, avec rétroaction corrective | Performance autonome différée ; rejouer immédiatement relève de la remédiation, non de l'espacement |
| Sélectionner la bonne démarche | Alterner des types de problèmes faciles à confondre après l'étayage initial | L'apprenant choisit et justifie sa stratégie ; un brassage aléatoire sans discernement ne suffit pas |
| Progresser depuis le stade novice | Exemple résolu, complétion partielle, défi autonome | Le recours à l'aide reste traçable ; l'étayage peut être réactivé en cas de besoin |
| Visualiser ses progrès | Une carte personnelle des compétences avec preuves associées et étapes suivantes | La complétion, la réussite avec aide et les preuves autonomes restent distinguables |
| Exercer son autonomie | Choix signifiant de parcours, de contexte ou de méthode dans le cadre de l'objectif | Les choix modifient l'expérience ; les prérequis et parcours alternatifs restent explicites |
| Éveiller la curiosité | Une énigme dont les indices constituent des preuves disciplinaires | La résolution explicite une question didactique ; la lecture narrative ne doit pas supplanter l'entraînement |
| Coopérer efficacement | Rôles complémentaires, production commune, rotation des responsabilités | Chaque participant explicite ou applique un élément de manière identifiable |
| Reconnaissance des acquis | Badges optionnels adossés à des réalisations transparentes | Un badge décrit une preuve concrète ; il ne remplace jamais un jugement de maîtrise |
| Émulation et défi | Défis comparables optionnels ou mesure de son propre progrès | Surveiller le découragement, le désengagement et la précipitation ; offrir une voie sans classement public |
| Engagement dans la durée | Objectifs choisis par l'apprenant, sessions avec reprise aisée, rappels sur demande | L'absence prolongée ne doit ni effacer l'historique d'apprentissage ni bloquer l'accès à l'étayage |

Ce sont des hypothèses de conception, non un palmarès de fonctionnalités universellement éprouvées. Les points, séries (streaks), avatars et tableaux de classement n'ont aucun effet magique universel sur l'apprentissage. Séparez hermétiquement la monnaie de jeu des preuves de compétences scolaires. Ne faites jamais consommer l'accès aux ressources d'apprentissage par les erreurs ordinaires d'un élève. Évitez les mécanismes anxiogènes : récompenses à durée limitée, vies payantes, tirages aléatoires de récompenses ou humiliations publiques par affichage des échecs. Il s'agit d'engagements éthiques de conception produit, et non de l'affirmation que chaque cas a été comparé expérimentalement.

Faites émerger la difficulté de la décision didactique cible. La charge de lecture, la précision motrice ou la pression temporelle peuvent parasiter la mesure de la compétence. N'utilisez la contrainte de vitesse que si l'aisance ou le temps de réponse fait partie intégrante de l'objectif ; maintenez l'exactitude et la vitesse interprétables séparément. Il n'existe pas de taux de réussite universellement optimal. Ajustez le soutien à partir d'observations répétées et permettez aux apprenants ou aux enseignants de corriger un positionnement inadapté.

### Jeux d'apprentissage: Structurer la séquence d'apprentissage

Introduisez un premier problème jouable avant de déployer une économie de jeu élaborée. Faites suivre chaque action d'une conséquence lisible pour l'apprenant, d'une rétroaction exploitable, d'une nouvelle tentative et d'un point d'arrêt naturel. Explicitez une erreur au niveau de la tâche ou de la stratégie mise en œuvre. Une simple animation de félicitations ne corrige pas une conception erronée.

Mobilisez un exemple résolu lorsque le manque de connaissances bloque toute tentative productive. Un problème d'exploration initial peut préparer les apprenants à une explication ultérieure, mais l'échec productif requiert impérativement une phase de consolidation et de synthèse. Cela ne justifie pas d'abandonner un élève débutant dans l'impasse. Distinguez l'apprentissage initial, l'entraînement guidé et l'évaluation autonome. Révéler la solution signale un essai assisté ; évaluez la compétence plus tard sur une tâche différente.

Intégrez la récupération active, l'espacement et l'entremêlement selon la nature de la tâche. Planifiez des retours sur les notions déjà acquises autant que sur les erreurs. Exigez un effort de restitution avant d'afficher la réponse lorsque la mémorisation est visée. Panachez des cas exigeant de discriminer la bonne règle, avec une rétroaction adaptée. Ne vendez pas un algorithme d'espacement à intervalles fixes comme idéal pour toutes les disciplines ou toutes les durées de rétention.

### Jeux d'apprentissage: Adapter selon les âges et les contextes nationaux

Fondez-vous sur les compétences constatées et les besoins d'étayage réels plutôt que sur des stéréotypes générationnels. Les élèves de primaire ont souvent besoin de représentations concrètes et d'une aide à la lecture ; les collégiens et lycéens tirent profit de la confrontation d'explications contrastées ; les étudiants et adultes attendent une authenticité disciplinaire ou professionnelle et un rythme flexible. Ce sont des hypothèses de départ. Un adulte novice peut nécessiter un étayage très fort, tandis qu'un enfant passionné réclamera un défi complexe.

Vérifiez les terminologies locales, le formatage des nombres et unités, le sens de lecture, les références culturelles, la structure scolaire et les équipements disponibles. N'adossez les contenus à un programme officiel qu'en précisant l'autorité éducative et la version du texte. Ne déduisez jamais un programme scolaire de la seule langue de l'interface. Prévoyez les usages sur appareil partagé ou pilotés par l'enseignant. Une simulation d'acte professionnel ne certifie pas une compétence pratique sur le terrain.

Proposez des alternatives au clavier et au pointeur unique pour les glisser-déposer, des textes d'état explicites au-delà de la couleur ou du son, une focalisation visible, des mouvements maîtrisables et des délais ajustables. Préservez la compétence évaluée lorsque vous offrez des modalités de réponse alternatives. L'accessibilité et l'adéquation à l'âge exigent des tests avec les utilisateurs réels ; invoquer la CUA (UDL) ou les WCAG ne prouve ni l'une ni l'autre.

### Jeux d'apprentissage: Implémenter à l'échelle pertinente

Pour une activité courte, commencez avec des contenus vérifiés, des règles déterministes et un état limité à la session. N'ajoutez de persistance locale que si la reprise de session est indispensable. Pour un produit longitudinal, prévoyez le versionnage des compétences et des items, la distinction entre essais autonomes et assistés, la planification des révisions, l'export/suppression des données et la correction manuelle par l'enseignant. Les comptes nominatifs, serveurs distants et télémétries comportementales nécessitent une justification pédagogique concrète.

Si des preuves sont enregistrées, un enregistrement minimal d'essai peut contenir : `skill_id`, `item_version`, `mode`, `support_used`, `response`, `result` et `feedback_version`. Ne stockez que les champs réellement utiles ; les réponses brutes et les horodatages n'ont pas besoin de quitter l'appareil. Isolez les monnaies virtuelles et éléments cosmétiques dans un état de jeu séparé. Une panne réseau ou une soumission répétée ne doit ni dupliquer des récompenses ni altérer une évaluation enregistrée.

Pour l'IA en cours d'utilisation, délimitez les sources autorisées, les bornes de notation, les comportements de repli et l'accès à une révision humaine. Testez des explications plausibles mais fausses, des réponses correctes équivalentes et l'indisponibilité du service. Évaluez les apprentissages une fois l'assistance retirée. Les recherches sur certains tuteurs intelligents ne prouvent pas que tout chatbot soit bénéfique, ni qu'une attente imposée avant l'aide soit profitable. L'usage de l'IA pour coder l'outil n'implique pas d'appels à des modèles dans le produit final.

Lors de la coordination d'experts ou d'agents, attribuez-leur le même objectif didactique, des exemples de tâches et les règles d'administration des preuves. Séparez la validation disciplinaire, l'ingénierie pédagogique, la jouabilité et les tests d'implémentation. Tranchez les désaccords par un exemple concret ou une source documentée. Multiplier les personas dans un même prompt ne constitue pas une validation indépendante ; ne mobilisez des agents distincts que si c'est autorisé et utile.

### Jeux d'apprentissage: Valider trois résultats distincts

1. Fonctionnement technique : réponses correctes et variantes, conceptions erronées, devinettes répétées, affichage de la solution, nouvelle tentative, reprise et pannes réseau éventuelles. Vérifiez qu'une réussite assistée ne se transforme jamais subrepticement en maîtrise autonome.
2. Ergonomie et jouabilité : observez des utilisateurs cibles lors de la première tâche et de la gestion d'une erreur. Notez les incompréhensions, les arbitrages stratégiques et la possibilité de quitter la partie à tout moment. Un test restreint repère les défauts ; il ne saurait établir un effet sur l'ensemble d'une population.
3. Apprentissage effectif : évaluez une tâche autonome inédite, la rétention différée si pertinent et le transfert hors du cadre immédiat du jeu. Pour une comparaison d'efficacité, utilisez une alternative pédagogique crédible à temps et contenus équivalents ; prenez en compte le niveau initial, l'attrition et l'assiduité inégale. Exprimez les incertitudes et refusez d'assimiler le temps passé à l'écran ou le plaisir déclaré à un progrès cognitif réel.

Pour les projets modestes, documentez l'hypothèse d'apprentissage et un test pilote réaliste. Pour les dispositifs à fort enjeu, fixez les indicateurs et le comparateur avant toute collecte de données. Dissociez les indicateurs de jeu des indicateurs d'apprentissage. Supprimez ou remaniez toute mécanique qui favorise les raccourcis de devinette, décourage la demande d'aide ou alourdit l'interface sans gain didactique avéré.

### Jeux d'apprentissage: Les preuves et leurs limites

- [Sailer & Homner, 2020](https://doi.org/10.1007/s10648-019-09498-w) : méta-analyse montrant des bénéfices moyens de la ludification avec de fortes disparités ; les effets motivationnels et comportementaux apparaissent moins stables sous les critères d'évaluation méthodologique les plus stricts. Cela ne garantit aucun effet pour un badge ou un classement particulier.
- [Clark et al., 2016](https://doi.org/10.3102/0034654315582065) : les comparaisons entre jeux et dispositifs classiques soulignent l'importance primordiale de la conception pédagogique et de l'étayage. Le médium seul ne détermine pas l'apprentissage.
- [Li et al., 2024](https://doi.org/10.1007/s11423-023-10337-7) : gain modéré sur la motivation intrinsèque sur 35 interventions analysées. Le sentiment de compétence perçu reste distinct de la maîtrise disciplinaire mesurée.
- [Habgood & Ainsworth, 2011](https://doi.org/10.1080/10508406.2010.508029) : deux études sur un jeu mathématique confirment l'intérêt d'intégrer le contenu d'apprentissage au cœur même de l'action de jeu. Les échantillons restreints ne permettent pas d'ériger ces résultats en recette universelle.
- [Agarwal et al., 2021](https://doi.org/10.1007/s10648-021-09595-9) et [Ruitenburg et al., 2026](https://doi.org/10.1007/s10648-026-10225-5) : données en contexte scolaire sur la récupération et la planification de l'entraînement selon le contexte. Ce dernier distingue rappel actif, espacement et entremêlement.
- [Wisniewski et al., 2020](https://doi.org/10.3389/fpsyg.2019.03087) : l'impact des rétroactions varie fortement ; l'apport d'informations constructives et opérationnelles est déterminant. [Sinha & Kapur, 2021](https://doi.org/10.3102/00346543211019105) : la résolution de problèmes avant l'enseignement direct peut être bénéfique sous certaines conditions de scénarisation rigoureuses.
- [Almeida et al., 2023](https://doi.org/10.1016/j.infsof.2022.107142) : cartographie identifiant les effets pervers documentés et les stratégies de contournement. Recenser des signalements négatifs ne quantifie pas la fréquence réelle de ces désagréments.
- [MIT / Learning Games Network, 2015](https://education.mit.edu/wp-content/uploads/2018/10/BalancedDesignGuide2015.pdf) : cadre de conception reliant objectifs, actions et preuves. [George Fan, GDC 2012](https://media.gdcvault.com/gdc2012/slides/Design%20Track/Fan_George_How%20I%20Got.pdf) : retour de praticien sur la prise en main jouable progressive. Tous deux guident la conception sans fournir de preuve causale d'efficacité scolaire.
- [Bastani et al., 2025](https://doi.org/10.1073/pnas.2422633122) et [Kestin et al., 2025](https://doi.org/10.1038/s41598-025-97652-6) : des expérimentations distinctes démontrent pourquoi la conception du tuteur et la mesure des résultats autonomes sont cruciales.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) fournit les critères d'accessibilité numérique ; [CAST UDL 3.0](https://udlguidelines.cast.org/) apporte un cadre de conception universelle. Leur fonction méthodologique diffère des expérimentations comparatives d'apprentissage.

### Jeux d'apprentissage: Relier expérience, mécaniques et transfert

Utilisez le modèle MDA (Mécaniques, Dynamiques, Esthétiques) comme grille d'analyse : décrivez l'expérience vécue visée, le comportement attendu du joueur et les règles formelles qui le suscitent. Par exemple, la découverte suppose un modèle manipulable et des observations probantes ; la liberté d'expression requiert plusieurs voies de résolution recevables. N'enfermez pas chaque matière dans un genre vidéoludique unique. La théorie de l'autodétermination (TAD / SDT) permet d'interroger le sentiment d'autonomie, de compétence et de lien social ; ni le modèle MDA ni une étiquette Octalysis ne prouvent l'efficacité pédagogique réelle.

Pour une tâche de résolution technique ouverte, définissez des contraintes et une condition de validation vérifiable sans imposer la solution unique de l'auteur. Permettez à l'apprenant de comparer ses solutions valides selon plusieurs critères concurrents, tels que l'économie de ressources et la précision. Un histogramme comparatif communautaire requiert des données réelles et un partage facultatif ; n'inventez pas une distribution fictive. L'optimisation ne doit pas obligatoirement faire gagner de la monnaie de jeu.

Reliez les représentations du jeu au formalisme disciplinaire et aux décisions en situation réelle, puis vérifiez le réinvestissement sur une situation inédite dépouillée des indices ludiques. N'imposez pas un écran scindé ou trois phases fixes à chaque apprenant. L'ambiance de jeu doit souligner les changements d'état signifiants sans masquer le raisonnement sous-jacent. Maintenez les séries et récompenses facultatives et non punitives ; une interruption ne doit jamais détruire les traces d'apprentissage ni l'aide. Rendre ses progrès publics doit toujours résulter d'un choix consenti.

[MDA par Hunicke, LeBlanc et Zubek](https://www.cs.northwestern.edu/~hunicke/MDA.pdf) est un cadre de conception de jeux. Les études citées ci-dessus portent sur des populations et des variables spécifiques ; ne confondez pas les métriques d'engagement d'une application avec des progrès didactiques.

## Reference: design-dialogue

Section source: Dialogue au cours de la conception pédagogique


À utiliser dès le premier arbitrage didactique substantiel et lorsque de nouvelles preuves ou des exigences modifiées conduisent à le réexaminer. Ces règles constituent un protocole de conception, non des allégations expérimentales sur l'apprentissage.

### Dialogue de conception: Identifier l'apprenant et les conditions d'apprentissage

L'âge, le statut scolaire et l'expérience disciplinaire sont des attributs distincts. « Enfant » désigne une tranche d'âge ; « élève » et « étudiant » désignent des statuts institutionnels dont les acceptions varient selon les pays. Ces catégories se recoupent. Utilisez « apprenant » ou « participant » dans la réflexion générale de conception, et une terminologie adaptée au contexte local dans le produit final. Les exemples scolaires ne limitent nullement ce skill à l'enfance. Des consignes directes peuvent simplement énoncer « Essaye », « Explique » ou « Compare ».

Avant de retenir une méthode, établissez un profil d'usage synthétique à partir du contexte connu : tranche d'âge et cadre d'apprentissage ; prérequis sur le thème ; compétences de lecture et de langue ; degré d'autonomie et étayage disponible ; objectif et enjeux de l'évaluation ; équipements matériels et besoins fonctionnels d'accessibilité. Il s'agit de repères de conception ergonomique et didactique, non d'un dossier personnel obligatoire. N'exigez pas de date de naissance, de diagnostic médical ou de cursus scolaire complet. Mentionnez les incertitudes ou hypothèses retenues ; le mot générique « élève » ne suffit pas à les caractériser.

| Contexte et terme usuel | Ce qu'il convient d'établir | Adaptation envisageable si nécessaire |
| --- | --- | --- |
| Petite enfance / préscolaire, sur demande | Décodage, commandes motrices, guidage de l'adulte et finalité de l'écran | Consignes orales courtes et concrètes, jeu partagé et activités hors écran ; ne pas supposer une lecture autonome |
| Élève de primaire / élémentaire | Concepts de base, formalisme, lecture de la consigne et supports numériques | Lier représentations concrètes et notions abstraites, expliciter les commandes et fournir un étayage |
| Collégien / début de secondaire | Prérequis, hétérogénéité de classe et travail en équipe | Comparer les stratégies de résolution, expliciter et choisir son niveau d'aide vers un but partagé |
| Lycéen (général, technologique, professionnel) | Filière de formation, expérience pratique et finalité certificative | Problème disciplinaire authentique, argumentation ou mise en situation ; la simulation ne remplace pas l'évaluation pratique |
| Étudiant de l'enseignement supérieur | Prérequis académiques pointus et degré de familiarité avec le thème | Tâches authentiques, confrontation de preuves et pluralité de démarches ; maintien d'exemples résolus pour les notions nouvelles |
| Apprenant adulte, professionnel ou autodidacte | Objectif personnel/métier, expérience antérieure, temps et contexte réel d'exercice | Situations professionnelles concrètes, possibilité d'ignorer les acquis, rythme flexible et reprise aisée |
| Public senior, si pertinent | Expérience individuelle, langue, aisance motrice et besoins d'accessibilité | Ajuster taille de texte, délais ou commandes ; l'âge n'implique pas une inexpérience numérique |
| Groupe hétérogène ou multiniveau | Besoins partagés et besoins requérant des différenciations | Objectif commun, étayage modulable, tâches d'entrée différenciées et preuves d'apprentissage individualisées |

Ces repères constituent des options de conception ergonomique, non des diagnostics développementaux ni des assignations rigides d'une méthode à un âge. L'organisation des cycles scolaires varie selon les systèmes éducatifs. Un enfant peut être très avancé sur un sujet et un adulte débutant complet. Le soutien linguistique, l'accessibilité et les ajustements de rythme concernent tous les publics. N'attribuez pas de prétendus « styles d'apprentissage » (visuel, auditif, kinesthésique) figés.

Distinguez qui apprend, qui manipule l'outil et qui consulte les résultats. Un enseignant peut piloter un vidéoprojecteur collectif, un parent accompagner un jeune enfant, et le concepteur n'être ni l'un ni l'autre. Le jeune âge du public ne détermine pas automatiquement qui accède aux bilans. Définissez précisément les rôles et droits d'accès en situation réelle d'utilisation.

Lorsqu'une information manquante modifie la conception, demandez par exemple : « Cet outil s'adresse-t-il à de jeunes élèves de primaire, à des collégiens ou à des adultes débutants ? Quels sont leurs prérequis sur cette notion ? » Ciblez les questions ; ne réinterrogez pas sur des données déjà acquises. Ne clarifiez une appellation ambiguë que si le contexte d'usage modifie concrètement la solution technique.

Expliquez à qui profite une démarche recommandée et pourquoi : « Pour ces professionnels débutants, je préconise un exemple résolu tiré de leur quotidien, puis un effacement progressif de l'aide à mesure que les essais autonomes s'améliorent. » Des élèves chevronnés tireront davantage profit d'un défi ouvert. Une modification de public cible conduit à réajuster la langue, le contenu, l'étayage, l'évaluation et l'interface, sans nécessairement remettre en cause tout le projet.

### Dialogue de conception: Proposer au moment opportun

Prenez en compte le public connu, les prérequis, l'objectif, le cadre institutionnel, les terminaux, le temps disponible et les contraintes issues du projet. Ne demandez une précision manquante que si elle fait basculer la décision didactique. Le mode par défaut est un dialogue guidé. Le concepteur peut déléguer un choix ou les décisions courantes consécutives, puis reprendre le guidage ultérieurement.

| Déclencheur | Choix pertinents à expliciter |
| --- | --- |
| Objectif initial et première tâche | Exemple résolu avec effacement progressif (fading), investigation guidée, rappel actif, tâche de construction ou projet authentique |
| Motivation et engagement actif | Visualisation des progrès réels, choix signifiants, rôles coopératifs, mécaniques de jeu ciblées |
| Gestion des erreurs et de l'aide | Indice gradué, contre-exemple contrasté, explication explicite suivie d'un nouvel essai autonome |
| Évaluation | Rétroaction formative, grille critériée descriptive, contrôle autonome, portfolio ou évaluation par les pairs étayée |
| Poursuite d'apprentissage | État limité à la session, persistance locale, révision espacée ou difficulté calibrée |
| Données de test du prototype | Corriger une représentation trompeuse, estomper l'étayage, introduire du transfert ou supprimer une récompense dévoyée |

Ce sont des opportunités de conception, non des passages obligés. Regroupez les choix connexes pour un projet de petite taille. Ne présentez que des options viables, avec une description concise, une illustration concrète dans ce produit et les coûts techniques, exigences de données ou limites associées. Recommandez une option et posez une seule question ciblée. Permettez une version simplifiée ou un ajournement si opportun ; n'exigez pas du concepteur qu'il maîtrise le jargon théorique. D'autres approches restent disponibles sur demande.

### Dialogue de conception: Mémoriser les décisions

Pour les petites interventions, appuyez-vous sur le fil d'échange ; pour un travail plus vaste, utilisez le registre de conception existant du projet. Conservez l'objectif, les contraintes, l'identifiant de la méthode, sa justification, son statut, les alternatives écartées et les questions ouvertes. Statuts préconisés : `offered` (proposé), `selected` (retenu), `implemented` (implémenté), `verified` (vérifié), `deferred` (ajourné), `declined` (refusé). Séparez rigoureusement ce suivi des traces des apprenants. Une nouvelle exigence ne rouvre que les choix directement impactés ; justifiez pourquoi. Ne confondez pas absence de réponse et validation implicite. Poursuivez les chantiers indépendants pendant qu'un arbitrage important est en attente.

### Dialogue de conception: Du choix didactique au produit opérationnel

Appuyez-vous sur l'action de l'apprenant, les preuves, l'étayage et la vérification définis dans la fiche méthode. Maintenez une séquence pédagogique cohérente ; signalez les incompatibilités éventuelles. Un exemple résolu peut préparer un rappel actif ultérieur ; un échec productif exige une phase consécutive de structuration des connaissances. Ni l'un ni l'autre n'implique d'évaluer l'apprenant sur chaque écran.

Pour une activité hors ligne sur les fractions : « Je conseille de manipuler des parts géométriques en affichant l'écriture fractionnaire correspondante, car l'objectif est l'équivalence. Une droite graduée mettrait plutôt l'accent sur le repérage ordinal ; compléter un exemple résolu apporterait un étayage initial plus fort. Quelle approche préférez-vous pour l'activité principale ? » Par la suite, proposez une tâche inédite sans représentations graphiques ou une analyse d'erreur pour tester le transfert. Ne réitérez pas le cadrage initial.

Le concepteur commande une application. Ne transformez pas cet échange en cours magistral descendant, en devoirs de programmation ou en listes interminables de TODO non résolus. À la livraison, montrez précisément où chaque méthode retenue s'applique, ce qui a été testé et les incertitudes résiduelles. La découverte automatique du skill dépend de l'environnement hôte ; testez sa visibilité séparément de son exécution après invocation.

## Reference: cognitive-ux

Section source: Interface cognitive et représentations


À consulter lors de la conception de schémas, de ressources multimédias, de consignes, du positionnement de la rétroaction ou d'une interface risquant d'occulter la tâche d'apprentissage. S'applique aux apprenants et aux terminaux ciblés, sans imposer de style graphique uniforme.

### Interface cognitive: Maintenir l'attention sur la décision d'apprentissage

Éliminez les animations et signaux sonores parasites pendant les phases de travail cognitivement exigeantes ; conservez les repères contextuels et les commandes utiles. Placez les légendes et explications au plus près des éléments auxquels elles se rapportent, sans masquer l'objet d'étude. Sur petit écran, recourez à une mise en surbrillance synchronisée, une description accessible ou un affichage séquentiel lorsque la juxtaposition visuelle est impossible. La couleur seule ne doit jamais porter une distinction critique.

Segmentez les opérations complexes en étapes contrôlées par l'apprenant. Introduisez les commandes et le vocabulaire inconnus avant de les combiner dans une même tâche. Maintenez un parcours direct pour les apprenants expérimentés ainsi qu'un accès permanent à l'aide. Toute animation doit clarifier un changement d'état ou une action ; prévoyez un mode sans animation (reduced-motion) et un état statique équivalent compréhensible.

### Interface cognitive: Articuler les représentations et vérifier le transfert

Lorsque des objets concrets étayent un concept abstrait, montrez comment la même relation se manifeste à travers les manipulations, les schémas et la notation formelle de la discipline. Explicitez les correspondances, puis proposez une nouvelle situation avec moins d'indices de surface. Une vue scindée (split-screen) est une modalité possible, non une obligation. Prévoyez des parcours équivalents au clavier et sans glisser-déposer. Vérifiez que l'apprenant ne peut pas réussir simplement en appariant des couleurs ou des positions géométriques.

Exemple : manipuler des quantités égales, visualiser l'équation correspondante et expliquer pourquoi l'égalité demeure vraie ; puis, dans un second temps, résoudre une nouvelle équation sans support manipulable. Les élèves expérimentés peuvent démarrer directement par le formalisme. Réactivez la représentation concrète si elle aide à surmonter un blocage. Pour les disciplines non mathématiques, le transfert peut consister à évaluer une nouvelle source documentaire ou appliquer une procédure à un cas inédit.

### Interface cognitive: Préserver l'accessibilité et la pertinence des preuves

Évitez les flux d'information simultanés superflus, mais préservez impérativement les sous-titres, transcriptions, options de réécoute, supports linguistiques et la compatibilité avec les lecteurs d'écran. Le principe de redondance ne proscrit pas le texte accompagnant l'audio lorsqu'il répond à un besoin d'accessibilité. Ne masquez pas des consignes essentielles dans des infobulles accessibles uniquement au survol. Si la vitesse ou l'écoute constitue la compétence évaluée, explicitez les conditions et prévoyez des aménagements adaptés.

Lors d'un point d'étape conceptuel, une estimation d'assurance facultative peut aider l'apprenant à confronter sa certitude à sa performance réelle. Ne traitez pas le sentiment de confiance comme une preuve de maîtrise et ne l'imposez pas après chaque action. La rétroaction doit éclairer le contraste pertinent et fournir l'occasion de le mettre en pratique ; ne suscitez pas artificiellement le doute face à un travail rigoureux.

Vérifiez la lisibilité des textes, l'ordre de tabulation, le zoom d'affichage, le comportement sur écran étroit, la prise en compte de la réduction des mouvements et l'intégralité du parcours d'aide et de nouvelle tentative. Examinez la tâche réelle accomplie par l'apprenant, et pas seulement l'esthétique des composants. Mentionnez explicitement les tests non réalisés.

### Interface cognitive: Sources et limites

[Waxman & Goldie, 2023](https://media.repository.chds.hsph.harvard.edu/static/filer_public/ca/62/ca625803-3d73-4855-b3e1-765870ce3772/2023_jwaxman_monograph_cogtheory_multimed.pdf) éclaire les arbitrages de conception sans constituer une interdiction ergonomique absolue. [Matlen et Devlin, 2020](https://web.stanford.edu/~kdevlin/Papers/Matlen-Devlin_CHI2020.pdf) décrit une approche exploratoire orientée transfert, sans valider chaque interface en écran scindé. Les [recommandations W3C sur les sous-titres](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html) précisent les exigences d'accessibilité. Vérifiez les obligations normatives en vigueur pour le déploiement ciblé.

## Reference: adaptive-practice

Section source: Pratique adaptative et poursuite de l'apprentissage


À consulter lorsque le produit nécessite des séances répétées, une planification des révisions ou un ajustement de la difficulté. Distinguez clairement le moment de la révision, le choix de la tâche à présenter et le degré d'étayage à proposer. Ces mécanismes ne reposent pas nécessairement sur le même modèle.

| Besoin | Implémentation légère | Extension optionnelle et prérequis |
| --- | --- | --- |
| Une seule activité | Tâches validées, séquence explicite, aide et état de session | Généralement aucun modèle persistant de l'apprenant |
| Mémorisation sur plusieurs jours | Calendrier de révision explicite et historique local | FSRS pour des items stables et des événements de révision interprétables |
| Sélectionner la difficulté | Niveaux d'items validés et arborescence transparente | Elo avec données de réponse adaptées, gestion de l'incertitude et calibration |
| Suivre les dépendances de compétences | Carte de compétences avec preuves d'apprentissage indépendantes | BKT ou IRT uniquement avec modèle défendable, données suffisantes et validation |
| Plan à long terme | Objectif, temps disponible, phase actuelle et prochaine tâche | Jalons révisables, questions transversales et dates de révision |

Expliquez la fonction pédagogique avant l'algorithme. Préservez la pile technologique existante ; n'installez pas de planificateur, de backend ou de gestionnaire de comptes simplement parce qu'ils sont mentionnés ici. Des règles heuristiques simples restent parfaitement légitimes dès lors que leurs limites sont explicites. Le modèle HLR constitue un autre modèle entraîné de rappel pour des jeux de données appropriés, non une exigence technique par défaut.

### Pratique adaptative: Conditions préalables à l'adaptation

Définissez des identifiants stables d'items/compétences, les versions de contenu, l'interprétation des réponses et les conditions d'assistance. Distinguez soigneusement les réponses devinées, assistées, révélées et autonomes. Respectez la sémantique d'évaluation de la bibliothèque choisie ; ne traitez pas silencieusement chaque réponse avec aide comme un rappel autonome. Gardez les récompenses ludiques en dehors du modèle d'apprentissage. Limitez les données au strict minimum et n'utilisez des horodatages que lorsque la planification l'exige.

Précisez le comportement au démarrage à froid (cold-start) et une solution de repli fonctionnelle lorsque l'historique est absent, corrompu ou obsolète. Examinez les hypothèses au regard de données représentatives, incluant la langue et les conditions d'accès. Permettez la correction par l'enseignant et l'accès de l'apprenant à l'aide. La réussite prédite reste incertaine : ni une cible universelle de 80–90 % de succès ni deux réponses correctes ne mesurent la ZPD ni ne prouvent la maîtrise. Le taux de rétention ciblé relève d'un arbitrage de charge de travail, non d'un résultat d'apprentissage garanti.

Utilisez une implémentation maintenue et vérifiée au niveau des versions si un algorithme est retenu. Testez les mises à jour, les fuseaux horaires et passages de journée, les soumissions en double, les modifications de contenu, l'export/reprise et les données invalides. Comparez l'extension avec une référence simple (baseline) ; la précision de prédiction, l'engagement et l'apprentissage réel sont des résultats distincts. N'inférez pas de trouble cognitif ou de trait de personnalité à partir du temps de réponse.

### Pratique adaptative: Clôturer ou reprendre une phase

Enregistrez le résultat, les conditions d'aide, les questions non résolues et l'étape suivante envisageable. L'achèvement d'une phase ne vaut pas validation de la maîtrise. Créer une nouvelle phase n'achève pas automatiquement la précédente. Les synthèses doivent conserver les pointeurs de preuves nécessaires et l'incertitude plutôt que des transcriptions complètes. Au retour de l'apprenant, vérifiez les hypothèses obsolètes par une tâche ciblée et proportionnée ; une interruption de session ne doit pas effacer arbitrairement les progrès acquis.

### Pratique adaptative: Sources

[Documentation FSRS d'Anki](https://docs.ankiweb.net/manual/deck-options), [Pelánek sur le système Elo éducatif](https://www.fi.muni.cz/~xpelanek/publications/CAE-elo.pdf), et [Settles et Meeder sur HLR](https://research.duolingo.com/papers/settles.acl16.pdf). Ces sources décrivent des modèles et contextes particuliers ; elles ne garantissent pas l'efficacité d'une nouvelle application. Consultez la documentation à jour de la bibliothèque lors de toute intégration.

## Notice de licence

```text
MIT License

Copyright (c) 2026 Luděk Sušický

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
