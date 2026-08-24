# Jeu du Pendu

Ce dépôt contient une simple implémentation du jeu du Pendu en Python.

## Description

Le fichier principal `pendu.py` propose une version console du jeu du pendu. Le programme choisit un mot aléatoire dans une liste et le joueur doit proposer des lettres pour deviner le mot avant d'atteindre le nombre maximal d'erreurs.

## Prérequis

- Python 3.x (testé avec Python 3.8+)

Aucune dépendance externe n'est requise.

## Installation

1. Cloner le dépôt :

   ```bash
   git clone https://github.com/bossapp597/project.git
   cd project
   ```

2. (Optionnel) Créer un environnement virtuel :

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS / Linux
   venv\Scripts\activate     # Windows
   ```

## Utilisation

Lancer le jeu :

```bash
python3 pendu.py
```

Le programme affiche un dessin du pendu selon le nombre d'erreurs et le mot masqué. Proposez une lettre à chaque tour jusqu'à gagner ou perdre.

## Personnalisation

- Modifier la liste de mots : éditez la variable `MOTS` dans `pendu.py` pour ajouter ou remplacer des mots.
- Dessins du pendu : les dessins se trouvent dans la liste `PENDU_DESSINS` dans `pendu.py`.

## Contribution

Les contributions sont bienvenues. Pour des modifications simples, ouvrez une pull request avec une description des changements.

## Licence

Ce projet est fourni sans licence explicite. Ajoutez un fichier `LICENSE` si vous souhaitez définir une licence.
