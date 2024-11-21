import time
import unicodedata
import pyautogui

# Importation des listes de pays avec et sans frontières
from Source2 import countries_no_frontier
from Source import countries_w_frontiers


# Fonction pour classer les pays selon leur nombre de frontières
def classerPays(listePays):
    print("Début classerPays")
    liste_valide = []  # Liste des pays déjà validés et ajoutés à la liste ordonnée
    liste_ordonnee = []  # Liste des pays ordonnés par nombre de frontières

    # Boucle jusqu'à ce que tous les pays soient classés
    while len(liste_valide) < len(listePays):
        max_border = 0  # Nombre maximal de frontières pour un pays
        pays_max = ""  # Le pays ayant le plus de frontières valides

        # Parcours de tous les pays pour trouver celui avec le plus de frontières non validées
        for pays in listePays:
            if pays not in liste_valide:  # On ne traite que les pays non validés
                valid_frontier_count = 0  # Compte des frontières valides pour ce pays
                for frontier in pays:  # On parcourt les frontières de chaque pays
                    if frontier not in liste_valide:  # Si la frontière n'a pas encore été validée
                        valid_frontier_count += 1  # On incrémente le compteur de frontières valides
                if valid_frontier_count > max_border:  # Si ce pays a plus de frontières valides
                    max_border = valid_frontier_count  # On met à jour le nombre maximum de frontières
                    pays_max = pays  # On met à jour le pays ayant le plus de frontières valides

        # Si un pays a été trouvé avec des frontières valides
        if pays_max:
            liste_valide.append(pays_max)  # Ajoute ce pays à la liste des pays validés
            liste_ordonnee.append(pays_max)  # Ajoute ce pays à la liste des pays ordonnés

            # Ajout des frontières de ce pays dans la liste des pays validés
            for frontier in listePays[pays_max]:
                if frontier not in liste_valide and frontier in listePays:
                    liste_valide.append(frontier)

    return liste_ordonnee  # Retourne la liste des pays ordonnés


# Fonction pour écrire les noms des pays dans un champ de texte à l'aide de pyautogui
def writeCountry(liste):
    print("Let's go")

    # Compte à rebours avant de commencer à écrire les pays
    for i in range(5):
        print(f"{5 - i}")  # Affiche le compte à rebours
        time.sleep(1)  # Pause de 1 seconde

    # Écriture des pays dans le champ de texte
    for pays in liste:
        pyautogui.typewrite(remove_accents(pays))  # Tape le nom du pays sans accents
        pyautogui.press('enter')  # Appuie sur 'Entrée' pour valider le pays

        # Temps d'attente (commenté ici, mais utile pour ne pas surcharger le programme)
        # time.sleep(0.000005)  # Temps d'attente entre chaque pression de touche (optionnel)


# Fonction pour supprimer les accents des caractères dans une chaîne
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)  # Normalisation de la chaîne pour retirer les accents
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])  # Filtrage des caractères accentués

# Exécution des fonctions (commentées pour éviter l'exécution)
# writeCountry(countries_no_frontier)  # Appelle la fonction pour écrire les pays sans frontières
# liste_ordonne = classerPays(countries_w_frontiers)  # Classe les pays avec frontières
# writeCountry(liste_ordonne)  # Écrit les pays classés avec frontières
