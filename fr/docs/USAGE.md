# Utilisation et installation

## Choisir le bon point d'entrée

Mobilisez ce skill pour concevoir une nouvelle application éducative, apporter une modification substantielle à son ingénierie pédagogique ou conduire une revue critique de sa conception didactique. Une retouche purement esthétique ou une simple correction de bug informatique ne requiert pas de refonte didactique.

Fournissez les éléments connus concernant les apprenants cibles, l'objectif didactique, le cadre d'usage et les contraintes pratiques. L'agent doit exploiter les données déjà disponibles et n'interroger que sur les lacunes contextuelles déterminantes et les arbitrages didactiques en suspens. Il ne doit ni répéter un entretien figé sur le public et le ton, ni solliciter de validation pour des choix ordinaires déjà couverts par la consigne initiale.

## Décisions guidées au fil de la conception

Face à un arbitrage didactique majeur, le skill propose une sélection restreinte d'options pertinentes : une brève explication, une illustration concrète dans le projet et une recommandation motivée. Il mémorise vos choix et les répercute sur l'implémentation et les vérifications. Vous pouvez indiquer « tranche les choix de routine pour moi » pour déléguer ces aspects, ou demander une comparaison approfondie des alternatives. Les activités courtes hors ligne conservent leur légèreté de mise en œuvre. Les fiches méthodes, les repères d'ergonomie cognitive et la pratique adaptative optionnelle étayent ce flux de travail.

## Installation via le CLI Skills

Installez l'édition française avec le [CLI Skills](https://github.com/vercel-labs/skills). L'option `-g` effectue une installation globale pour l'utilisateur et `-a codex` sélectionne Codex. Remplacez par `-a claude-code` pour Claude Code, ou omettez l'option pour un choix interactif. N'installez que les éditions linguistiques dont vous avez l'usage.

```bash
npx skills add siberius/learning-methodologies --skill methodologies-apprentissage --full-depth -g -a codex
```

Sans le paramètre `--agent`, la commande `skills use` affiche une invite préparée. Pour lancer temporairement un agent compatible avec ce skill :

```bash
npx skills use siberius/learning-methodologies --skill methodologies-apprentissage --full-depth --agent codex
```

## Paquet natif du skill

Conservez `SKILL.md`, `LICENSE` et le sous-répertoire `references/` dans le même dossier de skill, généralement nommé `methodologies-apprentissage`. Utilisez le mécanisme d'installation officiel de votre environnement hôte. La seule présence d'un fichier Markdown sur le disque ne garantit pas sa découverte automatique.

Pour les clients s'appuyant sur `~/.agents/skills`, une arborescence type est :

```text
~/.agents/skills/methodologies-apprentissage/
  SKILL.md
  references/
  LICENSE
```

Pour Claude Code, le répertoire équivalent est couramment `~/.claude/skills/methodologies-apprentissage/`. Préservez les fichiers utilisateur existants et vérifiez les éventuels conflits avant installation. Validez la découverte effective au sein du client. L'installation ne préjuge pas de l'usage réel du skill par l'agent.

## Fichier Markdown autonome

Fournissez à un modèle ou environnement gérant les consignes le fichier généré `methodologies-apprentissage.md` en lui demandant explicitement de s'y conformer. Ce document intègre directement l'ensemble des références conditionnelles et ne présente aucune dépendance relative à d'autres fichiers. Cette approche charge davantage de contexte initialement, mais ne requiert qu'un unique fichier d'instructions.

Le nom d'un modèle d'IA ne constitue pas une garantie d'installation. La compatibilité effective dépend de la capacité de l'environnement hôte à charger et appliquer des consignes Markdown, de ses outils disponibles et de ses permissions accordées.

## Travailler selon le besoin

| Besoin | Document de référence |
|---|---|
| Modes du tuteur, reprise de session et points d'étape | `references/tutor-state.md` |
| Justification didactique des démarches et impact sur l'application | `references/didactic-rationale.md` |
| Conception globale, revue critique ou cadrage du périmètre | Fichier cœur `SKILL.md` |
| Formulations d'aide ambiguës, réponses équivalentes ou programmes scolaires | `references/decision-examples.md` |
| Sélection des démarches, étayage et règles de progression | `references/methods.md` |
| Évaluation, grilles critériées, adaptivité et preuves d'apprentissage | `references/assessment.md` |
| Modélisation scientifique, simulation expérimentale ou jeu de rôle | `references/simulations.md` |
| Intégration d'un service d'IA dans l'application finale | `references/runtime-ai.md` |
| Choix du modèle, effort de réflexion, vitesse et configuration hôte | `references/model-profiles.md` |
| Dialogue de conception avec l'auteur et suivi des arbitrages | `references/design-dialogue.md` |
| Ergonomie cognitive, multimédia et charge attentionnelle | `references/cognitive-ux.md` |
| Planification des révisions et ajustement de la difficulté | `references/adaptive-practice.md` |
| Mécaniques ludiques, leviers motivationnels et transfert | `references/learning-games.md` |

Ne chargez pas systématiquement toutes les références en mode natif. Un questionnaire hors ligne peut offrir des rétroactions et des indices de qualité sans requérir d'IA en cours d'exécution. Une démonstration collective au vidéoprojecteur nécessite des questions de relance pour la classe plutôt qu'un suivi individuel complexe. Adoptez une ou plusieurs perspectives selon la tâche, sans lancer inutilement plusieurs agents en parallèle.

## Maintenance des éditions linguistiques

Les sources de travail de l'auteur sont `SKILL.md` et ses fiches de références conditionnelles. Le fichier Markdown autonome est un livrable de distribution généré. Sur le dépôt de développement, reconstruisez-le avec :

```sh
python3 testing/build_portable.py --edition fr
python3 testing/build_portable.py --edition fr --check
python3 testing/build_portable.py --edition all --check
```

Le script de construction réside dans l'outillage local de développement. Les utilisateurs finaux peuvent exploiter l'une ou l'autre des éditions sans devoir exécuter ce script. Il intègre les références avec des ancres uniques évitant toute ambiguïté de titres répétés.

Maintenez le README et le guide enseignant en cohérence étroite avec le document cœur. Préservez la paternité, la version, la traçabilité et la licence MIT. Pour un autre environnement agentique, enregistrez le paquet maintenu plutôt que d'en faire une copie isolée. Il existe des éditions en anglais (`en`), tchèque (`cs`), russe (`ru`), espagnol (`es`) et français (`fr`). Chacune conserve les mêmes principes didactiques fondamentaux. Construisez une édition spécifique avec `--edition` suivi de son code, ou toutes avec `--edition all`. Mesurez les conséquences pour l'ensemble des éditions lors de toute modification d'un principe partagé ; n'imposez pas de cadres scolaires nationaux spécifiques aux projets internationaux.

## Évaluer un résultat

Vérifiez l'action attendue de l'apprenant, les preuves recueillies, la rigueur disciplinaire, la pertinence de la rétroaction, l'étayage, l'accessibilité et les conditions de fonctionnement de l'application. Distinguez la correction logicielle, l'adéquation didactique et les gains réels d'apprentissage. Explicitez ce qui a été vérifié et ce qui demeure non attesté.

Le [protocole d'évaluation de modèles en huit tâches](MODEL-EVALUATION.md) fournit un banc d'essai standardisé et des critères objectifs pour l'évaluateur. N'incluez pas ces critères d'évaluation dans le prompt fourni au modèle testé. Ce banc d'essai est prêt à l'emploi et standardisé ; des tests informels antérieurs ne préjugent pas de la régularité inter-fournisseurs. Ne rendez compte que d'évaluations réellement exécutées, en séparant le premier résultat des corrections consécutives.

Choisissez un modèle en fonction de la complexité de la tâche avant de vous focaliser sur une marque. Si un critère majeur continue d'échouer après une correction ciblée, appliquez les règles d'escalade et d'interruption du document sur les modèles. L'augmentation de l'effort de raisonnement ne supplée pas à l'absence de sources documentaires ou d'outils. La vitesse de traitement standard est la référence ; l'accélération payante relève d'un choix explicite et autorisé.

Lors du choix d'une méthode de développement, consultez la [justification didactique](../references/didactic-rationale.md). Elle démontre comment la démarche transforme les actions de l'apprenant et les rétroactions, sans prétendre garantir d'elle-même l'efficacité didactique de l'application finale.
