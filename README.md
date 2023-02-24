# NETFLOOX_manuel_adrien_tarik
Le meilleur système de recommendation


Pour que le système fonctionne il faut un fichier config.yaml dans le dossier netfloox/python_files composé comme ceci :

mysql_azure_netfloox:
    user:       # Nom de l'utilisateur
    password:   # Mot de passe
    host:       # Lien de l'host
    port:       3306
    type:       mysql
    db_name:    # Nom de la bdd


De plus la partie analyze ne fonctionne que avec un fichier dataset qui a été généré séparèment.