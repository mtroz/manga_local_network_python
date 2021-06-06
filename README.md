# Manager scan local network en python

## modules nécessaire

	- Nmap version 7.80

## librairies python à installer

	- apyzme version 1.0.4

## Avancement projet

### Services du projet à développer

[JG] 
	/!\ Avoir un fichier de configuration type Yaml, pour ajuster localement la configuration hors arguments de lancement (exemple : SMTP) 
	-> rajouter un moduule type PyYaml (`pip install PyYAML`) - voir [la documentation](https://pyyaml.org/wiki/PyYAMLDocumentation) dédiée 


* Gérer et ajuster la configuration locale du module => module pyYAML https://pyyaml.org/wiki/PyYAMLDocumentation 
* Gestion des exceptions pour tout le projet 
	[JG] Avoir des classes dédiées, tout ne doit pas nécessairement au __main__ ( `class MonErreur(Exception): ...` ) 
* Gestion alert => mail ? => module smtp ?
	* Nouvelle machine sur le réseau
	* Changement d'ip d'une machine
* Gestionnaires de sécurité des ports des machines
	* Lister les ports ouvert d'une machine
	* Lister les ports à haut risque d'une machine
* Amélioration du service de mapping
	* Ajout des options de scan de port
	* Ajout d'une option de scan d'une plage d'IP
	* Ajout d'une option pour le scan d'une machine seul

### Services du projet en cours de développement

* SQLITE
	* Mise en place du module SQLITE
	* Récupération des informations depuis SQLITE
	* Gérer le cas ou la base de donnée n'existe pas
	[JG] https://docs.python.org/3/library/os.path.html#os.path.isfile

### Services du projet développés

* Mise en place du système d'argument => module argparse
* Service de récupération des machines connectées