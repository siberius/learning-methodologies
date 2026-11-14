# Pratique adaptative et poursuite de l'apprentissage

À consulter lorsque le produit nécessite des séances répétées, une planification des révisions ou un ajustement de la difficulté. Distinguez clairement le moment de la révision, le choix de la tâche à présenter et le degré d'étayage à proposer. Ces mécanismes ne reposent pas nécessairement sur le même modèle.

| Besoin | Implémentation légère | Extension optionnelle et prérequis |
| --- | --- | --- |
| Une seule activité | Tâches validées, séquence explicite, aide et état de session | Généralement aucun modèle persistant de l'apprenant |
| Mémorisation sur plusieurs jours | Calendrier de révision explicite et historique local | FSRS pour des items stables et des événements de révision interprétables |
| Sélectionner la difficulté | Niveaux d'items validés et arborescence transparente | Elo avec données de réponse adaptées, gestion de l'incertitude et calibration |
| Suivre les dépendances de compétences | Carte de compétences avec preuves d'apprentissage indépendantes | BKT ou IRT uniquement avec modèle défendable, données suffisantes et validation |
| Plan à long terme | Objectif, temps disponible, phase actuelle et prochaine tâche | Jalons révisables, questions transversales et dates de révision |

Expliquez la fonction pédagogique avant l'algorithme. Préservez la pile technologique existante ; n'installez pas de planificateur, de backend ou de gestionnaire de comptes simplement parce qu'ils sont mentionnés ici. Des règles heuristiques simples restent parfaitement légitimes dès lors que leurs limites sont explicites. Le modèle HLR constitue un autre modèle entraîné de rappel pour des jeux de données appropriés, non une exigence technique par défaut.

## Conditions préalables à l'adaptation

Définissez des identifiants stables d'items/compétences, les versions de contenu, l'interprétation des réponses et les conditions d'assistance. Distinguez soigneusement les réponses devinées, assistées, révélées et autonomes. Respectez la sémantique d'évaluation de la bibliothèque choisie ; ne traitez pas silencieusement chaque réponse avec aide comme un rappel autonome. Gardez les récompenses ludiques en dehors du modèle d'apprentissage. Limitez les données au strict minimum et n'utilisez des horodatages que lorsque la planification l'exige.

Précisez le comportement au démarrage à froid (cold-start) et une solution de repli fonctionnelle lorsque l'historique est absent, corrompu ou obsolète. Examinez les hypothèses au regard de données représentatives, incluant la langue et les conditions d'accès. Permettez la correction par l'enseignant et l'accès de l'apprenant à l'aide. La réussite prédite reste incertaine : ni une cible universelle de 80–90 % de succès ni deux réponses correctes ne mesurent la ZPD ni ne prouvent la maîtrise. Le taux de rétention ciblé relève d'un arbitrage de charge de travail, non d'un résultat d'apprentissage garanti.

Utilisez une implémentation maintenue et vérifiée au niveau des versions si un algorithme est retenu. Testez les mises à jour, les fuseaux horaires et passages de journée, les soumissions en double, les modifications de contenu, l'export/reprise et les données invalides. Comparez l'extension avec une référence simple (baseline) ; la précision de prédiction, l'engagement et l'apprentissage réel sont des résultats distincts. N'inférez pas de trouble cognitif ou de trait de personnalité à partir du temps de réponse.

## Clôturer ou reprendre une phase

Enregistrez le résultat, les conditions d'aide, les questions non résolues et l'étape suivante envisageable. L'achèvement d'une phase ne vaut pas validation de la maîtrise. Créer une nouvelle phase n'achève pas automatiquement la précédente. Les synthèses doivent conserver les pointeurs de preuves nécessaires et l'incertitude plutôt que des transcriptions complètes. Au retour de l'apprenant, vérifiez les hypothèses obsolètes par une tâche ciblée et proportionnée ; une interruption de session ne doit pas effacer arbitrairement les progrès acquis.

## Sources

[Documentation FSRS d'Anki](https://docs.ankiweb.net/manual/deck-options), [Pelánek sur le système Elo éducatif](https://www.fi.muni.cz/~xpelanek/publications/CAE-elo.pdf), et [Settles et Meeder sur HLR](https://research.duolingo.com/papers/settles.acl16.pdf). Ces sources décrivent des modèles et contextes particuliers ; elles ne garantissent pas l'efficacité d'une nouvelle application. Consultez la documentation à jour de la bibliothèque lors de toute intégration.
