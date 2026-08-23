import random

# 1. Liste de mots et dessins du pendu
MOTS = ["PYTHON", "ALGORITHME", "FICHIER", "PROGRAMME", "VARIABLE", "FONCTION"]

PENDU_DESSINS = [
    """
       +---+
           |
           |
           |
          ====""",
    """
       +---+
       O   |
           |
           |
          ====""",
    """
       +---+
       O   |

       |   |
           |
          ====""",
    """
       +---+
       O   |
      /|   |
           |
          ====""",
    """
       +---+
       O   |
      /|\\  |
           |
          ====""",
    """
       +---+
       O   |
      /|\\  |
      /    |
          ====""",
    """
       +---+
       O   |
      /|\\  |
      / \\  |
          ==== [PERDU]"""
]

def jouer_pendu():
    # 2. Initialisation de la partie
    mot_a_deviner = random.choice(MOTS)
    lettres_trouvees = set()
    lettres_ratees = set()
    erreurs = 0
    max_erreurs = len(PENDU_DESSINS) - 1

    print("=== BIENVENU AU JEU DU PENDU ===")

    # 3. Boucle principale du jeu
    while erreurs < max_erreurs:
        # Affichage du dessin actuel
        print(PENDU_DESSINS[erreurs])
        
        # Affichage du mot masqué (ex: P _ T H _ N)
        affichage_mot = ""
        for lettre in mot_a_deviner:
            if lettre in lettres_trouvees:
                affichage_mot += lettre + " "
            else:
                affichage_mot += "_ "
        print(f"\nMot : {affichage_mot}")
        print(f"Lettres ratées : {', '.join(lettres_ratees)}")

        # Vérification de la victoire
        if "_" not in affichage_mot:
            print("\n🎉 BRAVO ! Vous avez gagné !")
            print(f"Le mot était bien : {mot_a_deviner}")
            return

        # Saisie du joueur
        proposition = input("Proposez une lettre : ").upper().strip()

        # Validation de l'entrée
        if len(proposition) != 1 or not proposition.isalpha():
            print("Veuillez entrer une seule lettre valide.")
            continue
        if proposition in lettres_trouvees or proposition in lettres_ratees:
            print("Vous avez déjà proposé cette lettre !")
            continue

        # Traitement de la lettre
        if proposition in mot_a_deviner:
            print("Bonne lettre !")
            lettres_trouvees.add(proposition)
        else:
            print("Mauvaise lettre...")
            lettres_ratees.add(proposition)
            erreurs += 1

    # Fin de partie - Défaite
    print(PENDU_DESSINS[erreurs])
    print(f"\n💥 Dommage, vous avez perdu ! Le mot était : {mot_a_deviner}")

# Lancement du jeu
jouer_pendu()