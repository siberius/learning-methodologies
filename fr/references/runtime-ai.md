# L'IA en cours d'exécution dans les applications éducatives

À consulter uniquement lorsque l'application finale interroge directement un service d'IA en cours d'utilisation. Mobiliser l'IA pour écrire du code ou rédiger des contenus préalablement relus par un enseignant ne relève pas de l'IA en temps d'exécution. Maintenez les activités hors ligne déconnectées, à moins que l'objectif d'apprentissage n'exige impérativement un service distant.

## Définir un rôle didactique délimité

Précisez ce que le modèle est autorisé à faire, quels contenus ou sources vérifiés il peut exploiter et comment il doit réagir en cas d'élément probant manquant. Lorsque l'exactitude des faits est primordiale, déterminez les ressources de référence approuvées et conservez la traçabilité des sources. N'inventez pas de références bibliographiques d'apparence plausible. Acceptez le doute méthodique et la correction ; bannissez les diagnostics hâtifs ou les affirmations catégoriques sur les capacités d'un apprenant à partir d'un court échange.

Adaptez l'étayage à la nature de l'activité. L'entraînement peut mobiliser des questions de relance, des indices progressifs, des exemples résolus ou une explication directe à la demande ou lorsque le questionnement s'avère stérile. Une évaluation peut restreindre l'aide selon les consignes explicites de l'enseignant. N'imposez pas un questionnement socratique sans fin ni une interdiction absolue de fournir la réponse. Permettez à l'apprenant de demander de l'aide, d'interrompre l'échange ou de solliciter l'enseignant.

Concevez l'interface d'IA pour empêcher le copier-coller passif, où l'outil se substitue à la réflexion de l'élève. Avant d'adopter une démarche ou une réponse générée, exigez un bref contrôle cognitif de l'apprenant : clarifier son intention avant la requête, marquer une pause réflexive sur la proposition, évaluer sa complétude et sa justesse, et choisir l'action suivante (poursuivre, vérifier, reformuler ou rejeter la suggestion).

Appuyez-vous sur des grilles critériées explicites pour la rétroaction et l'évaluation des réponses ouvertes. Confrontez les jugements du modèle à des étalons validés par des enseignants avant de vous y fier. Toute décision certificative, d'orientation ou disciplinaire exige une révision humaine responsable ; une réponse de modèle ne peut en aucun cas être le seul décisionnaire. Enregistrez les incertitudes et prévoyez la possibilité pour l'enseignant d'invalider une évaluation automatique.

## Réduire les données des apprenants au strict minimum

Documentez les données transmises au fournisseur de modèle, ce qui est conservé, qui y a accès et les modalités de suppression. Ne collectez que le strict nécessaire à l'activité pédagogique. N'ajoutez pas automatiquement de comptes personnels, de noms réels, de profils persistants ou d'historiques intégraux de conversation. Recourez à des identifiants d'activité anonymes ou pseudonymes lorsque c'est suffisant, tout en reconnaissant que cela ne constitue pas une garantie d'anonymat absolu.

Avant tout déploiement auprès d'élèves mineurs, vérifiez la tranche d'âge, les conventions de l'établissement, les conditions contractuelles du fournisseur et les exigences légales applicables (notamment le RGPD) auprès de l'institution responsable. N'inventez pas d'âge de consentement universel ou de règle juridique imaginaire. Expliquez le traitement des données aux élèves et aux enseignants dans un langage clair et adapté.

## Mettre en place des garde-fous architecturaux

Conservez les identifiants et clés d'API au sein d'un composant serveur sécurisé dès qu'un service distant exige des secrets. Ne les exposez jamais dans le code exécuté par le navigateur client. Appliquez les contrôles d'autorisation, les quotas de requêtes et les restrictions d'outils en dehors du prompt textuel. Traitez les entrées des apprenants, les documents récupérés et les réponses du modèle comme des données non fiables par défaut.

Séparez rigoureusement les instructions système des contenus injectés, restreignez les accès et cibles des outils, validez les sorties structurées et assainissez les contenus affichés dans le navigateur. Empêchez le texte généré de devenir directement du code exécutable ou de déclencher des actions à privilèges. Un prompt ordonnant au modèle d'ignorer les attaques par injection ne constitue pas une garantie de sécurité. Diligentez un audit de sécurité dédié pour l'architecture mise en œuvre.

## Anticiper les coûts, les pannes et la continuité

Définissez un budget d'exploitation réaliste, des plafonds par session, des délais d'attente (timeouts) et la possibilité d'annuler une requête. Affichez un état compréhensible pendant les temps de traitement. Gérez la perte de réseau, l'indisponibilité des modèles, les formats de sortie invalides et l'épuisement des quotas sans jamais perdre le travail en cours de l'élève. Ne retentez les requêtes que de façon sécurisée et strictement délimitée.

Prévoyez une solution de repli adaptée : indices prédéfinis relus, exercices statiques, sauvegarde de l'avancement ou recours à l'enseignant. Signalez explicitement qu'une rétroaction est momentanément indisponible plutôt que de fabriquer une réponse artificielle. Avant tout usage en classe, testez le parcours nominal, une réponse erronée, une demande d'aide, une rétroaction ambiguë et une panne totale du service. Documentez les limites non résolues et les responsabilités de contrôle de l'enseignant.

## Vérifier les contenus générés dans des limites définies

Avant de diffuser des exercices générés, effectuez les vérifications nécessaires : exactitude notionnelle, solvabilité mathématique ou logique, cohérence des transitions d'état et qualité du rendu. N'exigez l'unicité que pour les exercices qui la garantissent formellement. Validez les permissions et les schémas de sortie structurée en dehors du modèle ; un schéma formel ne garantit pas la véracité d'un contenu et des tests déterministes n'assurent que les propriétés qu'ils contrôlent effectivement. Rejetez ou isolez les contenus invalides et conservez une ressource de secours préalablement validée. Pour corriger les indices, évaluations et progressions dépendantes, appliquez la procédure de remédiation détaillée dans `assessment.md`.
