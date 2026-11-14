# Méthodologies d'apprentissage : ingénierie didactique pour l'IA

[![Skills.sh](https://img.shields.io/badge/skills.sh-Install-blue)](https://skills.sh/siberius/learning-methodologies)

[English](../README.md) · [Čeština](../cs/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Français](README.md)

Un skill d'IA portable pour concevoir, implémenter et examiner des applications éducatives. Il relie les objectifs d'apprentissage, l'activité de l'apprenant, les rétroactions et les preuves observables, puis aide à traduire ces arbitrages en comportements applicatifs concrets.

## Author

**Luděk Sušický** — biologist, secondary-school and university teacher of computing subjects

- E-mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius) — more educational projects and open-source applications

Licence MIT. Cette édition française adapte la base méthodologique internationale et ne présuppose aucun programme national exclusif, aucune IA obligatoire en cours d'exécution, aucun compte utilisateur ni modèle propriétaire particulier.

Version actuelle : **1.5.0**. Toutes les éditions linguistiques intègrent un parcours de travail synthétique, des exemples de décisions, les modes du tuteur et la reprise de session, les cartes conceptuelles, des directives de rédaction des textes pour apprenants et des règles explicites de sélection et d'escalade des modèles. Les configurations mentionnées sont des recommandations de départ documentées, non des bancs d'essai comparatifs exécutés.

Le skill propose une sélection restreinte d'options didactiques pertinentes face à un arbitrage important : explication concise, exemple concret et recommandation motivée. Il mémorise vos choix et les articule avec le développement et les tests. Vous pouvez indiquer « tranche les choix de routine pour moi » pour déléguer, ou demander une comparaison approfondie. Les activités hors ligne légères conservent leur simplicité. Les fiches méthodes, les repères d'interface cognitive et la pratique adaptative optionnelle structurent ce flux.

## Ce que ce skill vous aide à réaliser

- Choisir des démarches didactiques à partir d'un besoin concret et de la réalité de la classe.
- Soutenir l'autorégulation de l'apprenant dans un espace cognitif partagé avec l'IA (cadre FALR : choix, pause cognitive, évaluation et autonomie) pour éviter le copier-coller passif sans réflexion.
- Concevoir un étayage pertinent, des rétroactions d'erreurs constructives et un entraînement autonome.
- Distinguer objectifs, difficulté des tâches, prérequis notionnels et preuves de maîtrise.
- Développer des simulations fiables et un tutorat d'IA délimité lorsque la situation le justifie.
- Prendre en compte l'accessibilité (WCAG 2.2 / CUA), le contrôle de l'enseignant, la minimisation des données d'élèves et les contraintes techniques réelles.
- Distinguer une application qui fonctionne, une ingénierie didactique défendable et les apprentissages réels constatés.
- Sélectionner un modèle, un niveau d'effort et une vitesse adaptés à la tâche à partir de repères documentés (OpenAI, Claude, Gemini), avec un état de validation explicite.

Les méthodes couvrent notamment le questionnement socratique, la technique de Feynman, la zone proximale de développement et l'étayage cognitif, les exemples résolus et commentés, la pratique de récupération et l'espacement critique, la métacognition, la démarche d'investigation, le jeu de rôle, l'apprentissage par les pairs et coopératif, la pédagogie de projet et la classe inversée. Ce sont des approches mobilisables selon les besoins ; installer le skill ne les rend pas toutes obligatoires.

## Installation et démarrage rapide

Installez l'édition française via le [CLI Skills](https://github.com/vercel-labs/skills). L'option `-g` installe pour l'utilisateur et `-a codex` sélectionne Codex. Utilisez `-a claude-code` pour Claude Code, ou omettez l'option pour un choix interactif. N'installez que les éditions dont vous avez l'usage.

```bash
npx skills add siberius/learning-methodologies --skill methodologies-apprentissage --full-depth -g -a codex
```

Sans le paramètre `--agent`, `skills use` génère une invite prête à l'emploi. Pour lancer temporairement un agent compatible avec ce skill :

```bash
npx skills use siberius/learning-methodologies --skill methodologies-apprentissage --full-depth --agent codex
```

## Choisir un format

- [SKILL.md](SKILL.md) et `references/` : paquet natif avec fiches de détail conditionnelles. Conservez les fichiers ensemble.
- `methodologies-apprentissage.md` : fichier autonome généré pour les agents acceptant directement des instructions Markdown complètes. Il rassemble le cœur didactique et l'ensemble des références.

Les deux formats proviennent des mêmes sources maintenues. Éditez `SKILL.md` et les références associées, puis régénérez l'édition autonome.

## Exemple d'invite de démarrage

> Utilise methodologies-apprentissage pour concevoir une activité hors ligne sur les circuits électriques pour des élèves de 16 ans. Ils doivent prédire comment l'intensité varie avec la résistance et justifier leur raisonnement. L'activité servira de support à un échange animé par l'enseignant et doit être entièrement navigable au clavier. Aucun compte utilisateur ni appel à une IA externe.

L'agent exploite ce contexte, propose un étayage mesuré et identifie ce qui constitue une preuve de compréhension. Il n'interroge que sur les informations manquantes déterminantes pour la conception.

## Documentation

- [Utilisation et installation](docs/USAGE.md)
- [Guide enseignant et exemples d'invites](docs/TEACHERS.md)
- [Évaluation de modèles](docs/MODEL-EVALUATION.md)
- [Historique des versions](../CHANGELOG.md)

## Éditions linguistiques

L'édition française adapte le socle méthodologique commun pour une utilisation en français sans imposer un programme scolaire national particulier. L'édition tchèque intègre des repères spécifiques pour les établissements tchèques (RVP/ŠVP, contextes de classe). Des éditions anglaise, tchèque, russe, espagnole et française sont disponibles. Utilisez l'édition linguistique appropriée ; il est déconseillé de charger simultanément plusieurs éditions.

Ce processus est un guide d'ingénierie didactique. Il ne certifie ni l'accessibilité légale, ni l'exactitude scientifique finale, ni l'efficacité scolaire absolue. Procédez aux vérifications adaptées à la matière, au public et aux conséquences de l'évaluation.

## Licences et droits

Licence MIT, copyright 2026 Luděk Sušický. Consultez [LICENSE](LICENSE). Conservez la mention d'auteur et de licence lors de toute redistribution. Les publications et ressources externes citées conservent leurs propres droits.

## Méthodes didactiques pour les applications créées avec l'IA

Consultez la [justification didactique](references/didactic-rationale.md) pour comprendre comment chaque démarche didactique transforme les actions de l'apprenant, les rétroactions et les critères d'évaluation dans l'application finale.
