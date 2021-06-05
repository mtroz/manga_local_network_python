#Manager scan local network en python

## modules nécessaire

	- Nmap version 7.80

## librairies python à installer

	- apyzme version 1.0.4

## Avancement projet

### Services du projet à développer

* SQLITE
	* Gérer le cas ou la base de donnée n'existe pas
* Gestion des exceptions pour tout le projet
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

### Services du projet développés

* Mise en place du système d'argument => module argparse
* Service de récupération des machines connectées