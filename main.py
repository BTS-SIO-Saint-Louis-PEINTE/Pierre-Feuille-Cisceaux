import random

def pierre_feuille_ciseaux():
    """
    Fonction principale pour jouer au jeu Pierre, Feuille, Ciseaux.
    Le joueur entre son choix, et l'ordinateur fait un choix aléatoire.
    Le jeu compare les résultats pour déterminer le gagnant.
    """
    # Options possibles pour le jeu
    options = ["pierre", "feuille", "ciseaux"]
    
    print("Bienvenue au jeu Pierre, Feuille, Ciseaux!")
    print("Tapez 'pierre', 'feuille' ou 'ciseaux' pour jouer.")
    print("Tapez 'quit' pour quitter le jeu.")
    
    while True:
        # Le joueur entre son choix
        joueur = input("\nVotre choix: ").lower()
        
        # Vérification si le joueur souhaite quitter le jeu
        if joueur == "quit":
            print("Merci d'avoir joué! À bientôt!")
            break
        
        # Validation du choix du joueur
        if joueur not in options:
            print("Choix invalide. Veuillez choisir entre 'pierre', 'feuille' ou 'ciseaux'.")
            continue
        
        # L'ordinateur fait un choix aléatoire
        ordinateur = random.choice(options)
        print(f"L'ordinateur a choisi: {ordinateur}")
        
        # Comparaison des choix pour déterminer le résultat
        if joueur == ordinateur:
            print("Égalité!")
        elif (joueur == "pierre" and ordinateur == "ciseaux") or \
             (joueur == "feuille" and ordinateur == "pierre") or \
             (joueur == "ciseaux" and ordinateur == "feuille"):
            print("Vous avez gagné!")
        else:
            print("Vous avez perdu!")

def main():
    """
    Point d'entrée du programme.
    Lance le jeu Pierre, Feuille, Ciseaux.
    """
    pierre_feuille_ciseaux()

# Appeler la fonction main si le script est exécuté directement
if __name__ == "__main__":
    main()
