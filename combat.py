
from init_global_functions import sleep, clear, randint, next_instruction, random_animal_assigned, keyboard, erased_previous_input, random_item_generator, update_player_inventory_for_item_event, pnj_evolution, alert_print
from init_var_classes_and_items import all_animals_classes_list, tigre_final_boss, weapons_for_menu_list, fruits_for_menu_list, plants_for_menu_list, all_item_list, player_health_condition, italic_txt, normal_txt, dim_txt, bright_txt

stats_dictionary_list = ["name", "damage", "max_life",  "speed", "defense", "social", "level", "nuts"]

def choice_move_fight_player(double_move_player, player_battle_final_boss, special_crew_attack_coul_down , player_alone):

    """Return liste contenant les deux choix du joueur

    Choix des actions du joueur en combat 
    """

    choice_list = []

    i = 0
    while i < 2:
        if player_battle_final_boss == True and special_crew_attack_coul_down["coul_down"] == 0 and player_alone == False:
            choice_move_list_player = ["Coup Spécial","Attaque","Esquive", "Défendre","Inventaire"]
        elif player_battle_final_boss == True and special_crew_attack_coul_down["coul_down"] > 0:
            choice_move_list_player = ["Attaque","Esquive", "Défendre","Inventaire"]
        else:
            choice_move_list_player = ["Attaque","Esquive", "Défendre","Inventaire", "Fuir"]

        if double_move_player != None:
            choice_move_list_player.remove(double_move_player)

        clear()
        if len(choice_list) > 0:
            print(italic_txt + dim_txt + ("Action précédente choisis : " + str(choice_list[-1]) + "\n")+ normal_txt)
        else:
            print(italic_txt + dim_txt + "Vous devez choisir deux actions qui seront executées à la suite lors de cette manche. \n" + normal_txt)

        print("Choix de l'action", bright_txt + str(i+1) + normal_txt,"\n")
        for number in range(len(choice_move_list_player)):
            print(number + 1,choice_move_list_player[number])
        print("")
        try :
            erased_previous_input()
            move_in_battle_choice = int(input("Votre choix : "))
        except ValueError:
            alert_print("Choix indisponible ! \n")
        else:
            if move_in_battle_choice > len(choice_move_list_player) or move_in_battle_choice <= 0:
                alert_print("Choix indisponible ! \n")
            else:
                if choice_move_list_player[move_in_battle_choice -1] == "Coup Spécial":
                    special_crew_attack_coul_down["coul_down"] += 1

                choice_list.append(choice_move_list_player[move_in_battle_choice -1])
                i += 1
    return choice_list

def IA_enemy(enemy,choice_move_enemy):

    """Return liste contenant les deux choix de l'ennemi

    Choix des actions de l'ennemi en fonction de certains critères (vie, défense)
    """

    if enemy["current_life"] >= (enemy["max_life"] / 1.5): # ----------------------- Si la vie de l'ennemi est haut-dessus de 75% de son total

        if "Attaque" in choice_move_enemy: # ----------------------- S'il peut attaquer 
            if randint(0,10) > 3: # ----------------------- 70% de chance d'attaquer
                return "Attaque"
            else: # ----------------------- Sinon choisis au hasard une autre action possible qui n'est pas attaque
                while True:
                    choice_pas_attack = choice_move_enemy[randint(0,len(choice_move_enemy) -1)]
                    if choice_pas_attack == "Attaque":
                        pass
                    else:
                        return choice_pas_attack

        else: # ----------------------- Si l'action attaque n'est pas disponible, choisis au hasard une des actions possibles
            return choice_move_enemy[randint(0,len(choice_move_enemy) -1)]
    else:
        if enemy["current_life"] >= (enemy["max_life"] / 2): # ----------------------- Si la vie de l'ennemi est comprise entre 50% et 75% de sa vie total
            return choice_move_enemy[randint(0,len(choice_move_enemy) -1)] # ----------------------- Choisis au hasard une action possible
        else:
            # ----------------------- Si la vie de l'ennemi est inférieure à 50% de son total
            if "Dodge" in choice_move_enemy: # ----------------------- S'il peut esquiver
                if enemy["speed"] >= 20: # ----------------------- Et que sa vitesse est haut-dessus de 20
                    if randint(0,10) > 3: # -----------------------  70% de chance de faire l'action esquive
                        return "Dodge"
                    else:
                        while True:
                            choice_pas_attack = choice_move_enemy[randint(0,len(choice_move_enemy) -1)]
                            if choice_pas_attack == "Dodge":
                                pass
                            else:
                                return choice_pas_attack
                else:
                    return choice_move_enemy[randint(0,len(choice_move_enemy) -1)]
            else:
                return choice_move_enemy[randint(0,len(choice_move_enemy) -1)]

    return choice_move_enemy

def choice_move_fight_enemy(doublon_move, enemy):

    """Return liste contenant les deux choix de l'ennemi

    Vérifie les précédents choix de l'ennemi et appelle la fonction IA_choice
    """

    choice_move_list_enemy = ["Attaque","Esquive", "Défendre"]
    choice_list = []

    if doublon_move != None:
        choice_move_list_enemy.remove(doublon_move)

    for i in range(2):
        IA_choice = IA_enemy(enemy,choice_move_list_enemy)
        choice_list.append(IA_choice)
    return choice_list


def double_move_verification(choice_list):
    if choice_list[0] == choice_list [1]:
        return choice_list[0]
    return None

def fight_calcul_dodge_or_run(speed_stat,max):
    calcul = randint(1,max + int(speed_stat/2))
    if calcul <= speed_stat:
        return True
    return False

def fight_calcul_attack(attack,target):
    target["current_life"] -= attack
    if target["current_life"] < 0:
        target["current_life"] = 0
    return target


def next_combat_level(player):

    """
    Incrémente le niveau du joueur de 1 et améloration des statistique du joueur
    """

    player["level"] += 1
    while True:
        clear()
        print("Votre niveau :",player["level"],"!\n")
        print("Choisir la statistique a améliorer :\n")
        try:
            erased_previous_input()
            print("Dégâts      (1)\nVie maximum (2)\nVitesse     (3)\nDéfense     (4)")
            upgrade_stat_choice = int(input("\nVotre choix : "))
        except ValueError:
            alert_print("Choix indisponible ! \n")
        else:
            if upgrade_stat_choice > 4 or upgrade_stat_choice < 0:
                alert_print("Choix indisponible ! \n")
            else:
                player[stats_dictionary_list[upgrade_stat_choice]] += 10
                break

def fight_damage_taken_by_target(attacker_text,target,att_attacker,target_text):
    print(attacker_text)
    target = fight_calcul_attack(att_attacker,target)
    print(target_text,att_attacker,"de dégâts \n")

def auto_allocation_of_best_weapon_in_inventory(player):

    """Return l'arme selectionnée si le joueur en possède une sinon return None

    Sélectionne la meilleure arme du joueur
    """
    weapon_none = {"item_name": "None", "value": 0}
    for i in range(1,len(weapons_for_menu_list) + 1):
        if player["inventory"]["weapons"][weapons_for_menu_list[-i]]["nb"] > 0:
            return player["inventory"]["weapons"][weapons_for_menu_list[-i]]
    return weapon_none


def inventory_menu_combat(player, damage_plant_bonus, speed_plant_bonus, defense_plant_bonus, max_life_plant_bonus, max_life_player_round):
    while True:
        clear()
        print("- Fruits -  (1) \n")
        print("- Plantes - (2) \n")
        print("- Retour -  (3) \n")
        try:
            inventory_menu_choice = int(input("Votre choix : "))
        except ValueError:
            alert_print("Choix indisponible ! \n")
        else:
            if inventory_menu_choice == 1:
                inventory_selection_is_empty = True
                clear()
                while True:
                    clear()
                    print("Que voulez-vous utiliser ? \n")
                    for i in range(len(fruits_for_menu_list)):
                        if player["inventory"]["fruits"][fruits_for_menu_list[i]]["nb"] > 0:
                            inventory_selection_is_empty = False
                            print(player["inventory"]["fruits"][fruits_for_menu_list[i]]["item_name"], "[" + str(player["inventory"]["fruits"][fruits_for_menu_list[i]]["nb"]) + "]","\n")
                    if inventory_selection_is_empty == False:
                        fruits_menu_choice = input("Votre choix : ")
                        if fruits_menu_choice in fruits_for_menu_list:
                            player["inventory"]["fruits"][fruits_menu_choice]["nb"] -= 1
                            player["current_life"] += player["inventory"]["fruits"][fruits_menu_choice]["value"]
                            if player["current_life"] > max_life_player_round:
                                player["current_life"] = max_life_player_round
                            print("Vous récupérez :",player["inventory"]["fruits"][fruits_menu_choice]["value"],"points de vie")
                            print("Votre vie est de :",player["current_life"])
                            sleep(4)
                            return
                        else:
                            alert_print("Choix indisponible ! \n")
                    else:
                        alert_print("Vous n'avez aucun fruit !\n")
                        break

            elif inventory_menu_choice == 2:
                inventory_selection_is_empty = True
                clear()
                while True:
                    clear()
                    print("Que voulez-vous utiliser ? \n")
                    for i in range(len(plants_for_menu_list)):
                        if player["inventory"]["plants"][plants_for_menu_list[i]]["nb"] > 0:
                            inventory_selection_is_empty = False
                            print(player["inventory"]["plants"][plants_for_menu_list[i]]["item_name"], "[" + str(player["inventory"]["plants"][plants_for_menu_list[i]]["nb"]) + "]","\n")
                    if inventory_selection_is_empty == False:
                        plants_menu_choice = input("Votre choix : ")
                        if plants_menu_choice == "Menthe":
                            player["inventory"]["plants"][plants_menu_choice]["nb"] -= 1
                            speed_plant_bonus["bonus_points"] += 5
                            print("Vous avez augmenté votre vitesse de 5 points jusqu'à la fin du combat")
                            sleep(3)
                            return
                        elif plants_menu_choice == "Champignon":
                            player["inventory"]["plants"][plants_menu_choice]["nb"] -= 1
                            damage_plant_bonus["bonus_points"] += 5
                            print("Vous avez augmenté votre attaque de 5 points jusqu'à la fin du combat")
                            sleep(3)
                            return
                        elif plants_menu_choice == "Jacinthes":
                            player["inventory"]["plants"][plants_menu_choice]["nb"] -= 1
                            defense_plant_bonus["bonus_points"] += 5
                            print("Vous avez augmenté votre défense de 5 points jusqu'à la fin du combat")
                            sleep(3)
                            return
                        elif plants_menu_choice == "Eucalyptus":
                            player["inventory"]["plants"][plants_menu_choice]["nb"] -= 1
                            max_life_plant_bonus["bonus_points"] += 5
                            print("Vous avez augmenté votre vie maximum de 5 points jusqu'à la fin du combat")
                            sleep(3)
                            return
                        else:
                            alert_print("Choix indisponible ! \n")
                    else:
                        alert_print("Vous n'avez aucune plante !")
                        break

            elif inventory_menu_choice == 3:
                return
            else:
                alert_print("Choix indisponible ! \n")


def battle_phase(player,enemy):
    
# --------------------------------------------- Initialisation des variables nécéssaires pour le combat ---------------------------------------------

    special_crew_attack_coul_down = { "coul_down": -1}
    player_alone = True
    player_battle_final_boss = False

    if enemy["class_name"] == "Le Tigre":
        player_battle_final_boss = True
        if len(player["crew"]) > 0:
            player_alone = False
            special_crew_attack_coul_down["coul_down"] = 0

    damage_plant_bonus = { "bonus_points": 0}
    speed_plant_bonus = { "bonus_points": 0}
    defense_plant_bonus = { "bonus_points": 0}
    max_life_plant_bonus = { "bonus_points": 0}
    current_weapon = auto_allocation_of_best_weapon_in_inventory(player)
    double_move_player = None
    double_move_enemy = None
    run = False
    turn = 1

# --------------------------------------------- Boucle de combat ---------------------------------------------

    clear()
    while player["current_life"] > 0 and enemy["current_life"] > 0 and run != True:

        if special_crew_attack_coul_down["coul_down"] > 0 and special_crew_attack_coul_down["coul_down"] < 4:
            special_crew_attack_coul_down["coul_down"] += 1
        elif special_crew_attack_coul_down["coul_down"] == 4:
            special_crew_attack_coul_down["coul_down"] = 0

        choice_enemy = choice_move_fight_enemy(double_move_enemy,enemy)
        double_move_enemy = double_move_verification(choice_enemy)

        if player_battle_final_boss: # ----------------------- Annule le malus du double choix consécutif uniquement pour le boss
            double_move_enemy = None

        choice_player = choice_move_fight_player(double_move_player, player_battle_final_boss, special_crew_attack_coul_down, player_alone)
        double_move_player = double_move_verification(choice_player)

        clear()
        for i in range(1,3):
            if enemy["current_life"] <= 0:
                break
            elif player["current_life"] <= 0:
                    break
     
            attack_player_round = (randint(player["damage"] - 5,player["damage"] + 5) + current_weapon["value"]  + damage_plant_bonus["bonus_points"]) # ----------------------- Calcul de l'attaque du joueur avec les bonus des plantes
            speed_player_round = player["speed"] + speed_plant_bonus["bonus_points"] # ----------------------- Calcul de la vitesse du joueur avec les bonus des plantes
            defense_player_round = player["defense"] + defense_plant_bonus["bonus_points"] # ----------------------- Calcul de la défense du joueur avec les bonus des plantes
            max_life_player_round = player["max_life"] + max_life_plant_bonus["bonus_points"] # ----------------------- Calcul de la vie maximum du joueur avec les bonus des plantes

            attack_enemy_round = randint(enemy["damage"] - 5,enemy["damage"] + 5)

            clear()
            print("Tour :   ",turn)
            print("Manche : ",i,"\n")
            print("Vie du joueur :",player["current_life"], "| Vie de l'ennemi: ",enemy["current_life"],"\n")
            print("Choix du joueur :   ",choice_player[i -1])
            print("                       VS")
            print("Choix de l'ennemi : ",choice_enemy[i -1], "\n")
            
            # --------------------------------------------- Si le joueur attaque et que l'ennemi attaque aussi ---------------------------------------------
            if choice_player[i -1] == "Attaque" and choice_enemy[i -1] == "Attaque":

                print("Vous attaquez et l'ennemi aussi !")
                if randint(0,1) == 0:
                    fight_damage_taken_by_target("Vous êtes plus rapide !",enemy,attack_player_round,"Vous faites")
                    if enemy["current_life"] <= 0:
                        break
                    else:
                        fight_damage_taken_by_target("L'ennemi attaque !",player,attack_enemy_round,"Vous prenez")

                else:
                    fight_damage_taken_by_target("Vous êtes plus lent !",player,attack_enemy_round,"Vous prenez")
                    if player["current_life"] <= 0:
                        break
                    else:
                        fight_damage_taken_by_target("Vous attaquez !",enemy,attack_player_round,"Vous faites")

            # --------------------------------------------- Si le joueur fait le coup spécial en équipe et que l'ennemi attaque aussi ---------------------------------------------
            elif choice_player[i -1] == "Coup Spécial" and choice_enemy[i -1] == "Attaque":
                for i in range(len(player["crew"])):
                    attack_player_round += int((player["crew"][i]["damage"] + player["crew"][i]["speed"] + player["crew"][i]["defense"]) / 3)

                print("Vous faites votre coup spécial en équipe.")
                fight_damage_taken_by_target("Grâce à vos coéquipiers vous êtes plus rapide !",enemy,attack_player_round,"Vous faites")
                if enemy["current_life"] <= 0:
                    break
                else:
                    fight_damage_taken_by_target("L'ennemi attaque ensuite !",player,attack_enemy_round,"Vous prenez")

            else:
                # --------------------------------------------- Si le joueur attaque et que l'ennemi fait une autre action ---------------------------------------------
                if choice_player[i -1] == "Attaque":
                    if choice_enemy[i -1] == "Esquive":
                        dodge = fight_calcul_dodge_or_run(enemy["speed"],100)
                        if dodge == True:
                            print("L'ennemi a esquivé !")
                        else:
                            fight_damage_taken_by_target("L'ennemi n'a pas réussi à esquiver...",enemy,attack_player_round,"Vous faites")

                    elif choice_enemy[i -1] == "Défendre":
                        attack_player_round -= enemy["defense"]
                        if attack_player_round < 0:
                            attack_player_round = 0
                        fight_damage_taken_by_target("L'ennemi défend",enemy,attack_player_round,"Vous faites")

                # --------------------------------------------- Si le le joueur fait le coup spécial en équipe et que l'ennemi fait une autre action ---------------------------------------------
                elif choice_player[i -1] == "Coup Spécial":

                    for i in range(len(player["crew"])):
                        attack_player_round += int((player["crew"][i]["damage"] + player["crew"][i]["speed"] + player["crew"][i]["defense"]) / 3)
                        
                    if choice_enemy[i -1] == "Esquive":
                        dodge = fight_calcul_dodge_or_run(enemy["speed"],100)
                        if dodge == True:
                            print("L'ennemi a esquivé !")
                        else:
                            fight_damage_taken_by_target("L'ennemi n'a pas réussi à esquiver...",enemy,attack_player_round,"Vous faites")

                    elif choice_enemy[i -1] == "Défendre":
                        attack_player_round -= enemy["defense"]
                        if attack_player_round < 0:
                            attack_player_round = 0
                        fight_damage_taken_by_target("L'ennemi défend",enemy,attack_player_round,"Vous faites")


                # --------------------------------------------- Si le le joueur esquive ---------------------------------------------
                elif choice_player[i -1] == "Esquive":
                    if choice_enemy[i -1] != "Attaque":
                        print("Il ne se passe rien !")
                    else:
                        dodge = fight_calcul_dodge_or_run(speed_player_round,100)
                        if dodge == True:
                            print("Vous avez esquivé !")
                        else:
                            fight_damage_taken_by_target("Vous n'avez pas réussi à esquiver...",player,attack_enemy_round,"Vous prenez")

                #--------------------------------------------- Si le le joueur fuit ---------------------------------------------
                elif choice_player[i -1] == "Fuir":
                        run = fight_calcul_dodge_or_run(speed_player_round,120) #Remplacer by le vrai calcul de la run
                        if run == True:
                            print("Vous avez fuit !")
                            break
                        else:
                            if choice_enemy[i -1] == "Attaque":
                                fight_damage_taken_by_target("Vous n'avez pas réussi à fuir...",player,attack_enemy_round,"Vous prenez")
                            else:
                                print("Tant pis pour la fuite... peut être la prochaine fois !")
                                
                #--------------------------------------------- Si le le joueur choisis l'inventaire ---------------------------------------------
                elif choice_player[i -1] == "Inventaire":
                    if choice_enemy[i -1] == "Attaque":
                        inventory_menu_combat(player, damage_plant_bonus, speed_plant_bonus, defense_plant_bonus, max_life_plant_bonus, max_life_player_round)
                        clear()
                        fight_damage_taken_by_target("",player,attack_enemy_round,"Vous prenez")
                    else:
                        inventory_menu_combat(player, damage_plant_bonus, speed_plant_bonus, defense_plant_bonus, max_life_plant_bonus, max_life_player_round)
                        clear()
                        print("\nL'ennemi fait :", choice_enemy[i -1])

                #--------------------------------------------- Si le le joueur choisis de se défendre ---------------------------------------------
                elif choice_player[i -1] == "Défendre":
                    if choice_enemy[i -1] != "Attaque":
                        print("Il ne se passe rien ! \n")
                    else:
                        attack_enemy_round -= player["defense"]
                        if attack_enemy_round < 0:
                            attack_enemy_round = 0
                        fight_damage_taken_by_target("Vous défendez !",player,attack_enemy_round,"Vous prenez")

            sleep(1.5)
            next_instruction()
            clear()

        choice_player = []
        turn += 1

    print("Fin du combat !")
    sleep(1)
    next_instruction()
    if player["current_life"] <= 0:
        clear()
        print("Vous êtes KO !")
        sleep(2)
        for i in range(4):
            clear()
            print("Retour au menu du jeu" + "." * i)
            sleep(0.5)
        player_health_condition["health_condition"] = "dead"

    elif run == True:
        clear()
        print("Vous vous êtes enfui.e")
        player["current_life"] = player["max_life"]

    else:
        clear()
        if player_battle_final_boss == True:
            print("Vous avez eu raison du Tigre !\n")
        else:
            print("Vous avez mis KO votre ennemi.\n")
            item_enemy_drop = random_item_generator(all_item_list)
            while item_enemy_drop == "Piège":
                item_enemy_drop = random_item_generator(all_item_list)
            if item_enemy_drop != "Noisettes":
                print("L'ennemi a fait tomber l'objet :",item_enemy_drop)
            else:
                print("L'ennemi a fait tomber quelques noisettes")
            update_player_inventory_for_item_event(player,item_enemy_drop)
            print("Vous gagnez 1 niveau")
            next_instruction()
            next_combat_level(player)
            player["current_life"] = player["max_life"]
        next_instruction()
    return

def combat(player):
    battle_is_over = False
    enemy = random_animal_assigned(all_animals_classes_list).copy() #--------------------------------------------- Fait évoluer l'ennemi en fonction du niveau du joueur se défendre
    pnj_evolution(enemy,player["level"])
    while battle_is_over == False:
            battle_is_over = battle_phase(player, enemy)


def final_boss_combat(player):
    print("Le Tigre surgit de nulle part !\n")
    sleep(1)
    if len(player["crew"]) > 0:
        print("Tenez-vous prêt à l'affronter vous et votre équipe !")
    else:
        print("Tenez-vous prêt à l'affronter seul...")
    next_instruction()
    final_boss = tigre_final_boss.copy()
    pnj_evolution(final_boss,player["level"])
    battle_phase(player, final_boss)