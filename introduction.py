
from init_var_classes_and_items import all_animals_classes_list, player_health_condition, weapons_dict, fruits_dict, plants_dict, game_launch, yellow_txt, normal_txt
from init_global_functions import sleep, clear, random_animal_assigned, next_instruction, erased_previous_input, alert_print

# --------------------------------------------- CREATION DU JOUEUR ET INTRODUCTION DU JEU ---------------------------------------------

def introduction_and_player_assignment():
    start_choice = "oui"
    tuto_has_been_passed = True
    time_factor_print = 0.8 # ----------------------- Facteur temps des prints de mise en scène

    if game_launch["state"] == "start":
        while True:
            clear()
            erased_previous_input()
            tuto_choice = input("Passer le tutoriel ? (oui) (non) ")
            if tuto_choice == "oui":
                break
            elif tuto_choice == "non":
                tuto_has_been_passed = tutorial()
                break
            else:
                alert_print("Choix indisponible !")

        while True:
            clear()
            erased_previous_input()
            start_choice = input("Passer l'intro ? (oui) (non) ")
            if start_choice == "oui" or start_choice == "non":
                break
            else:
                alert_print("Choix indisponible !")
    clear()
    if start_choice == "oui":
        time_factor_print = 0.2
    print("La partie va commencer !")
    sleep(1.5)
    for i in range(4):
        clear()
        print("Création du plateau" + "." * i)
        sleep(time_factor_print)
    for i in range(4):
        clear()
        print("Attribution d'un animal aléatoire" + "." * i)
        sleep(time_factor_print)

    player = random_animal_assigned(all_animals_classes_list).copy()  # ----------------------- Attribution aléatoire d'un animal et de ses caractéristiques au joueur
    if tuto_has_been_passed == False:
        player["max_life"] += 20
        player["current_life"] = player["max_life"]

    player_health_condition["health_condition"] = "alive" # ----------------------- Réinitialisation de la condition de vie du joueur
    assigned_player_inventory(player)   # ----------------------- Inventaire assigné à la classe du joueur
    clear()
    game_launch["state"] = "played_once"
    print("Voici votre animal :", player["class_name"], "\n")
    sleep(1.5)

    if start_choice == "non": # ----------------------- Print de l'introduction
        print("Vous êtes perdu.e en forêt avec d'autres animaux hostiles.")
        sleep(3)
        print("Votre but est de survivre !\n")
        sleep(2.5)
        print("Pour cela, vous devrez affronter les autres animaux de cette forêt et vous équiper d'objets et d'armes puissantes.\n")
        sleep(2.5)
        print("Si vous réussissez à passer la première partie, vous pourrez alors constituer votre équipe pour anéantir le plus grand prédateur de la forêt : le Tigre.\n")
        sleep(2.5)
        print("Vous pourrez également acheter et vendre des objets chez l'écureuil afin d'améliorer votre condition avant le combat final.\n")
        sleep(4.5)
        print("Si vous ne souhaitez pas mourir, lisez les informations suivantes attentivement...\n")

    print("Pour vous repérer, vous êtes representé.e par ce symbole sur la carte : ⭕\n") # ----------------------- Print des explications des éléments de la carte
    sleep(0.6)
    print("Les combats : ⚡\n")
    sleep(0.6)
    print("Les échanges : ⛺\n")
    sleep(0.6)
    print("Les objets : ⭐\n")
    sleep(0.6)
    print("Et peut-être que votre animal possède des compétences spéciales qui vont vous aider à vous repérer... la nuit ?")
    sleep(0.6)
    next_instruction()
    return player

# --------------------------------------------- CREATION DE L'INVENTAIRE DU JOUEUR ---------------------------------------------

def assigned_player_inventory(player):
    inventory_dict = {}
    inventory_dict["weapons"] = weapons_dict
    inventory_dict["fruits"] = fruits_dict
    inventory_dict["plants"] = plants_dict
    player["inventory"] = inventory_dict

# --------------------------------------------- TUTORIEL D'EXPLICATION POUR APPRENDRE A UTILISER LE JEU ---------------------------------------------

def tutorial():
    clear()
    print("Bienvenue dans le tutoriel de TIGER HOOD !\n")
    sleep(1)
    print("Ici, vous allez apprendre à vous déplacer, combattre et découvrir les bases pour survivre !")
    next_instruction()
    print("Les déplacements :\n")
    print("Les flèches directionnelles de votre clavier vous permettent de vous déplacer sur la carte.\n")
    print("                                         ↑")
    print("                                       ←   →")
    print("                                         ↓")
    next_instruction()
    print("Les combats :\n")
    print("Le système de combat est un combat au tour par tour, mais avec une particularité à lui.\n")
    print("Chaque tour, vous devrez choisir deux actions parmi les différentes actions possibles comme : (Attaque, Défense...)\n")
    print("Une fois ces actions sélectionnées, les deux actions seront lancées à la suite...\n")
    print("C'est ce que l'on appelle une manche !\n")
    next_instruction()
    print("Chaque manche ressemblera à ceci :\n")
    print("Tour :    1\nManche :  1\n\nVie du joueur : 80 | Vie de l'ennemi:  90\n\nChoix du joueur   : Attaque\nChoix de l'ennemi : Attaque\n\nVous attaquez et l'ennemi aussi !\nVous êtes plus lent !\nVous prenez 40 de dégâts\n\nVous attaquez !\nVous faites 43 de dégâts\n")
    print("\nChaque tour est une succession de deux manches.")
    next_instruction()
    print("L'inventaire et le marché :\n")
    print("Lorsque que vous voudrez utiliser un objet dans votre inventaire ou acheter/vendre un objet au marché...\n")
    print("Il vous faudra taper le nom de l'objet en question, sans fautes et avec les accents.\n")
    print("Un peu long mais on s'y habitue 😅\n")
    next_instruction()
    print("Vous avez suivi le tutoriel jusqu'au bout, bravo !")
    sleep(1.2)
    print("Pour vous remercier, voici un petit bonus : +20 de vie max pour votre personnage au lancement de cette partie !")
    next_instruction()
    return False