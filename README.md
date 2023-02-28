# Groupe de bosiic_m 999550

# SPE-CLO5 / My Booking service

## Etape 0 : Organisation du travai

Rendus :
- Fichier disponible sur ce repository : [./etape0.pdf](./etape0.pdf)  
- Lien vers le fichier : https://docs.google.com/spreadsheets/d/1ufsb6p8eRwyON5eTIRwMJe4tijBMMwSDecvmsCyNkvk/edit#gid=0

Précisions :  
Le rendu contient un tableau avec le listing des différentes tâches à faire jusqu'au rendu final et le temps estimé pour chaque tâche.  
Les couleurs indiquent les personnes responsables de chaque tâche (légende en bas du document).


## Etape 0-Bis : Rapport complet

Rendus :
- Fichier disponible sur ce repository : [./etape0bis.pdf](./etape0bis.pdf)  
- Lien vers le fichier : https://docs.google.com/document/d/1Q53OQLrY6uHWttt-ezsDgwai3MZIuktBeXxoO3o3xk0/edit

## Install

Required:  
- docker
- docker-compose

Pour vos OS respectifs vous pouvez les installer en suivant ces documentations:  
- [Docker engine](https://docs.docker.com/engine/install/)
- [Docker compose](https://docs.docker.com/compose/install/)

Commandes utiles:
```bash
# Lancer en background
docker-compose up -d
# Lancer un des services en background
docker-compose up -d backend
# Voir les logs de tous les containers
docker-compose logs -f
# Voir les logs d'un container spécifique
docker-compose logs -f backend
# Voir les 500 dernières lignes de logs
docker-compose logs -f --tail 500
```


## Launch

Et c'est tout, vous pouvez lancer la db et le backend avec cette commande:
```bash
docker-compose up -d
```

Le swagger est accessible sur -> http://localhost:8888/swagger_ui/
