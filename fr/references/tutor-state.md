# Modes du tuteur et continuité de l'apprentissage

À consulter lors de la conception d'un tuteur guidé à étapes multiples, d'une activité avec reprise de session ou d'un entraînement aux examens. Ces règles s'appliquent également aux applications déterministes hors ligne ; elles n'exigent ni IA en temps réel, ni gestion de comptes, ni base de données distante.

## Modéliser des modes explicites et leurs transitions

Séparez nettement la phase d'explication, d'entraînement et d'évaluation lorsque l'activité le requiert. L'explication peut présenter un exemple résolu. L'entraînement sollicite une réponse, attend la saisie, fournit une rétroaction critériée et propose de l'aide. L'évaluation applique des règles déclarées régissant l'aide autorisée et le moment de la correction. Permettez à l'apprenant de faire une pause, de solliciter de l'aide ou de quitter l'activité ; une évaluation sommative stricte peut clôturer la tâche ou enregistrer l'essai comme assisté dès qu'une aide notionnelle est appelée. Préservez les aménagements d'accessibilité qui ne dévoilent pas le contenu didactique.

Pour un entraînement conversationnel, maintenez une seule question opérationnelle en attente, sauf si l'activité requiert un travail par lot. Ne générez pas la réponse de l'apprenant à sa place et ne révélez pas la solution pendant qu'il réfléchit. Distinguez les états : inactif (idle), en attente de réponse, en cours d'évaluation, rétroaction affichée et en pause. Bloquez les soumissions répétées ou rattachez-les au même essai ; une réponse tardive d'un service ne doit jamais noter une question ultérieure ni écraser un changement de mode. La production d'un modèle d'IA n'est qu'une proposition ; seul l'enseignant valide les notes et les règles d'évaluation.

Conservez le mode courant, l'objectif, la tâche active, l'identifiant de la tentative, l'état de révélation de la solution et le statut de la rétroaction dans l'état de l'application. Affichez un indicateur de progression concis si utile ; répéter une ligne de statut décorative ne constitue pas une gestion d'état. Lors d'un changement de mode explicite, prévenez des nouvelles conditions d'aide et conservez l'historique des aides consultées. Modifier une étiquette d'interface ne transforme pas un exercice dont la solution a été révélée en évaluation autonome. Proposez une tâche inédite adaptée lorsqu'une nouvelle preuve autonome est requise.

## Reprendre à partir de preuves d'apprentissage, non d'allégations de maîtrise

N'intégrez de sauvegarde ou d'export que si la reprise entre plusieurs sessions apporte une réelle valeur à l'utilisateur. Une activité courte et anonyme peut se dispenser des deux. Pour une activité avec reprise, conservez un point d'étape minimal adapté à l'implémentation :

- Version du format, version de l'activité/du contenu et identifiants des sources documentaires.
- Objectif, mode actif, identifiant de la tâche/tentative et étape en attente.
- Preuves observées avec leurs conditions d'obtention : autonome, assistée ou solution révélée ; une évaluation non résolue demeure en attente.
- Erreurs précises ou doutes identifiés et prochaine étape pédagogique.
- Données temporelles uniquement si nécessaire pour l'espacement des révisions ou l'interprétation des preuves.

Évitez les diagnostics catégoriques, les données d'identité superflues et les historiques intégraux de conversation. Explicitez le lieu de stockage des données, qui peut y accéder et comment les purger ; sur machine partagée, les élèves doivent disposer d'un bouton explicite pour terminer leur session et effacer leurs traces locales. Un fichier d'export peut contenir des données d'apprentissage personnelles même sans mention nominative. N'exportez jamais de clés d'API secrètes, de corrigés masqués ou de banques de tests confidentielles.

Traitez les fichiers de reprise importés comme des données non fiables. Validez le schéma, les tailles, les identifiants et la compatibilité des versions ; n'exécutez jamais d'instructions incorporées et n'acceptez pas des scores importés comme des notes officielles incontestables. Lorsque les notes ont un enjeu officiel, validez-les auprès du système de gestion de l'établissement avec les contrôles d'accès appropriés. Si le contenu a évolué ou qu'une tâche ne peut être restaurée, expliquez l'écart et reprenez à un état stable vérifié ; ne réinitialisez pas silencieusement les acquis et ne validez pas des preuves obsolètes. La restauration d'une tentative en suspens ne doit ni la soumettre automatiquement ni attribuer les points deux fois.

Une transmission de bilan consigne ce que l'apprenant a démontré, sur quelle tâche et avec quel degré d'étayage. Elle n'affirme jamais une « maîtrise totale » à l'issue d'une seule session. Une tâche ultérieure inédite permettra d'évaluer la rétention et le transfert. Les corrections validées par l'apprenant et les dérogations manuelles de l'enseignant doivent rester discernables de l'observation brute initiale.

## Cibler la remédiation sans enfermer l'apprenant

Hiérarchisez les erreurs selon leur importance vis-à-vis de l'objectif et des prérequis, la gravité de l'erreur étant traitée comme une interprétation provisoire. Proposez un indice progressif, un cas contrasté ou une explication ciblée, suivis d'une nouvelle situation d'application. Autorisez l'ajournement et la révision ultérieure. N'imposez pas de seuils arbitraires de 8/10 ou 90 %, n'interdisez pas les explications et n'attribuez pas de points à chaque clic. Utilisez des critères transparents lorsque la notation apporte une valeur pédagogique ; la préparation aux examens officiels requiert le barème institutionnel exact.

## Tests d'implémentation

Ne testez que les parcours pertinents : question → réponse → rétroaction ; aide → preuve assistée enregistrée ; bascule de mode après affichage de la solution ; pause/reprise sans perte ni double comptage d'un essai ; fichier de reprise corrompu ou obsolète ; réponse tardive après changement de question ; rétroaction en suspens après un échec réseau. Vérifiez la concordance stricte entre l'état stocké en mémoire et l'état affiché à l'écran. Ces tests valident le comportement applicatif, non l'efficacité éducative globale.
