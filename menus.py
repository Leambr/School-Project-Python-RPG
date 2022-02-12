
from init_var_classes_and_items import hibou, serpent, renard, singe, aigle_royal, ours_brun, normal_txt, bright_txt, red_txt, weapons_dict, fruits_dict, plants_dict 
from init_global_functions import clear, next_instruction, alert_print
from time import sleep

# --------------------------------------------- INITIALISATION DU MENU PRINCIPAL DU JEU  ---------------------------------------------

def main_menu():
    while True:
        clear()
        print("- Commencer une partie - (1) \n")
        print("        - Codex -        (2) \n")
        print("    - Quitter le jeu -   (3) \n")
        try:
            menu_choice = int(input("Votre choix :             "))
        except ValueError:
            alert_print("Choix indisponible !")
        else:
            if menu_choice == 1: #--------------------------------------------- Lance la partie en sortant de la fonction
                return
            elif menu_choice == 2:
                clear()
                codex()
            elif menu_choice == 3: #--------------------------------------------- Option de quitter le jeu
                alert_print("Le Tigre était si effrayant que ça ?")
                return "Quit"
            else:
                alert_print("Choix indisponible !")

# --------------------------------------------- INITIALISATION DU CODEX, DETAIL DES ELEMENTS DU JEU ---------------------------------------------

def codex():
    while True:
        clear()
        print("     - Personnages -               (1) \n")
        print("       - Objets -                  (2) \n")
        print("   - Détails de la map -           (3) \n")
        print("       - Retour -                  (4) \n")
        try:
            codex_choice = int(input("Votre choix :                       "))
        except ValueError:
            alert_print("Choix indisponible !")
        else:
            if codex_choice == 1:
                clear()
                all_players_information_codex()
            elif codex_choice == 2: 
                clear()
                all_items_information_codex()                
            elif codex_choice == 3: 
                clear()
                map_information_codex()

            elif codex_choice == 4:
                clear()
                return
            else:
                alert_print("Choix indisponible !")

def all_items_information_codex():
    while True:
        clear()
        print("Quelle catégorie d'objets souhaitez-vous découvrir ?\n")
        print("        - Armes -         (1)\n")
        print("       - Fruits -         (2)\n")
        print("       - Plantes -        (3)\n")
        print("       - Retour -         (4)\n")
        try:
            all_items_choice = int(input("Votre choix : "))
        except ValueError:
            alert_print("Choix indisponible !")
        else:
            if all_items_choice == 1:
                clear()
                all_weapons_codex()
            elif all_items_choice == 2:
                clear()
                all_fruits_codex()
            elif all_items_choice == 3:
                clear()
                all_plants_codex()
            elif all_items_choice == 4:
                clear()
                return
            else:
                alert_print("Choix indisponible !") 

def all_players_information_codex():
    while True:
        clear()
        print("Quel personnage souhaitez-vous découvrir ?\n")
        print("        - Hibou -         (1)\n")
        print("       - Serpent -        (2)\n")
        print("       - Renard -         (3)\n")
        print("        - Singe -         (4)\n")
        print("      - Aigle royal -     (5)\n")
        print("      - Ours brun -       (6)\n")
        print("        - Retour -        (7) \n")
        try:
            all_players_choice = int(input("Votre choix : "))
        except ValueError:
            alert_print("Choix indisponible !")
        else:
            if all_players_choice == 1:
                print_animals_stats_for_codex(hibou)
                print(red_txt,bright_txt,"Compétences spéciales :\n", normal_txt)
                print("- La nuit, l'hibou voit les cases combats, objets et échanges de la carte.\n")
                next_instruction()

            elif all_players_choice == 2:
                print_animals_stats_for_codex(serpent)
                print(red_txt,bright_txt,"Compétences spéciales :\n", normal_txt)
                print("- La nuit, le serpent voit les cases combats de la carte.\n")
                next_instruction()

            elif all_players_choice == 3:
                print_animals_stats_for_codex(renard)
                next_instruction()

            elif all_players_choice == 4:
                print_animals_stats_for_codex(singe)
                print(red_txt,bright_txt,"Compétences spéciales :\n", normal_txt)
                print("- La nuit, le singe voit les cases objets de la carte.\n")
                next_instruction()

            elif all_players_choice == 5:
                print_animals_stats_for_codex(aigle_royal)
                next_instruction()

            elif all_players_choice == 6:
                print_animals_stats_for_codex(ours_brun)
                next_instruction()

            elif all_players_choice == 7:
                clear()
                return
            else:
                alert_print("Choix indisponible !")

def print_animals_stats_for_codex(animal):
    clear()
    print(red_txt,bright_txt, animal["class_name"].upper(),"\n", normal_txt)
    print("Vie : ", animal["max_life"], "\n")
    print("Vitesse : ", animal["speed"], "\n")
    print("Défense : ", animal["defense"], "\n")
    print("Dégât : ", animal["damage"], "\n")
    print("Social : ", animal["social"], "\n")
               

def all_weapons_codex():
    clear()
    print("Toutes les armes impactent votre attaque lors des combats.\n")
    print(red_txt,bright_txt, "BÂTON", normal_txt)
    print("Attaque : +", weapons_dict["Bâton"]["value"],"\n")
    print(red_txt,bright_txt, "LIANE", normal_txt)
    print("Attaque : +", weapons_dict["Liane"]["value"],"\n")
    print(red_txt,bright_txt, "PIERRE", normal_txt)
    print("Attaque : +", weapons_dict["Pierre"]["value"],"\n")
    print(red_txt,bright_txt, "NOIX", normal_txt)
    print("Attaque : +", weapons_dict["Noix"]["value"],"\n")
    print(red_txt,bright_txt, "OS", normal_txt)
    print("Attaque : +", weapons_dict["Os"]["value"],"\n")
    sleep(0.5)
    next_instruction()

def all_fruits_codex():
    clear()
    print("Tous les fruits impactent votre vie lors des combats.\n")
    print(red_txt,bright_txt, "RAISIN", normal_txt)
    print("Vie : +", fruits_dict["Raisin"]["value"],"\n")
    print(red_txt,bright_txt, "PASTEQUE", normal_txt)
    print("Vie : +", fruits_dict["Pastèque"]["value"],"\n")
    print(red_txt,bright_txt, "NOIX DE COCO\n", normal_txt)
    print("Vie : +", fruits_dict["Noix de coco"]["value"],"\n")
    print(red_txt,bright_txt, "PÊCHE", normal_txt)
    print("Vie : +", fruits_dict["Pêche"]["value"],"\n")
    print(red_txt,bright_txt, "POMME", normal_txt)
    print("Vie : +", fruits_dict["Pomme"]["value"],"\n")
    sleep(0.5)
    next_instruction()

def all_plants_codex():
    clear()
    print("Les plantes impactent différentes statistiques selon leurs caractéristiques.\n")
    print(red_txt,bright_txt, "MENTHE", normal_txt)
    print("Vitesse : +", plants_dict["Menthe"]["value"],"\n")
    print(red_txt,bright_txt, "EUCALYPTUS", normal_txt)
    print("Vie : +", plants_dict["Eucalyptus"]["value"],"\n")
    print(red_txt,bright_txt, "CHAMPIGNON", normal_txt)
    print("Attaque : +", plants_dict["Champignon"]["value"],"\n")
    print(red_txt,bright_txt, "JACINTHES", normal_txt)
    print("Défense : +", plants_dict["Jacinthes"]["value"],"\n")
    sleep(0.5)
    next_instruction()

# --------------------------------------------- EXPLICATION FONCTIONNEMENT DE LA CARTE DE JEU ---------------------------------------------

def map_information_codex():
    print(red_txt,bright_txt, "INFORMATIONS SUR LA CARTE : \n", normal_txt)
    print("- La journée, tous les éléments sont visibles sur la carte. Vous pouvez donc choisir d'entrer en combat, de trouver un objet ou d'en échanger un.\n")
    print("Certaines cases objets peuvent vous rapporter des noisettes, la monnaie du jeu. Elles seront utiles lors de la partie 2 pour acheter/vendre des objets chez l'écureuil.\n")
    print("\n- La nuit, les éléments ne sont plus visibles sur la carte. Vous vous déplacez donc à l'aveugle, sauf si votre animal dispose de capacités spéciales.\n")
    print(red_txt,bright_txt, "ELEMENTS DE LA CARTE : \n", normal_txt)
    print("Vous êtes représentés sur la carte avec le symbole suivant : ⭕\n")
    print("Les combats sont représentés avec le symbole suivant : ⚡\n")
    print("Les échanges sont représentés avec le symbole suivant : ⛺\n")
    print("Les objets sont représentés avec le symbole suivant : ⭐")
    next_instruction()
