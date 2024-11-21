# Classement et Saisie Automatique de Pays

## Description

Ce projet permet de classer des pays en fonction de leurs frontières et de saisir automatiquement leurs noms dans une interface utilisateur.
Il m'a principalement servi à compléter deux défis sur JetPunk.com
- https://www.jetpunk.com/quizzes/pays-du-monde : En utilisant Source2 et la fonction writeCountry().
- https://www.jetpunk.com/user-quizzes/205316/pays-par-frontieres-dans-90-secondes : En utilisant Source, la fonction classerPays() puis la fonction writeCountry().

## Fonctionnalités

- **Classement des pays** : Trie les pays selon le nombre de frontières
- **Saisie automatique** : Utilise PyAutoGUI pour saisir les noms de pays
- **Gestion des accents** : Suppression automatique des accents

## Prérequis

### Bibliothèques
- Python 3.x
- `time`
- `unicodedata`
- `pyautogui`

### Installation des dépendances
<code>pip install pyautogui</code>

Structure du Projet

main.py : Script principal

Source.py : Liste des pays avec frontières

Source2.py : Liste des pays sans frontières

### Fonctions Principales

classerPays(listePays)  : 
Trie les pays selon leurs connexions frontalières
Retourne une liste ordonnée de pays

writeCountry(liste) : 
Saisie automatique des noms de pays
Compte à rebours avant exécution
Suppression des accents

remove_accents(input_str) : 
Supprime les accents des chaînes de caractères

### Précautions
⚠️ La fonction writeCountry() contrôle le clavier automatiquement
Assurez-vous d'avoir le bon champ de saisie sélectionné
Restez à proximité de votre clavier pendant l'exécution

### Contributeurs et liens utiles

- Matéo Leroy
- Linkedin : www.linkedin.com/in/mateoleroy33


