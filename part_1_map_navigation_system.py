
from init_global_functions import keyboard, sleep, clear, randint, next_instruction, random_item_generator, erased_previous_input, update_player_inventory_for_item_event, delete_player_item_inventory_for_trade_event, alert_print
from init_var_classes_and_items import weapons_dict, fruits_dict, all_item_list, normal_txt, italic_txt, dim_txt, player_health_condition, weapons_for_menu_list, fruits_for_menu_list, plants_for_menu_list
from combat import combat

# --------------------------------------------- AFFICHAGE DE LA CARTE, MOUVEMENT DU JOUEUR SUR LA CARTE, ACTION DES ELEMENTS DE LA CARTE ---------------------------------------------

def print_map(map):
    for i in range(len(map)):
        print(" | ".join(map[i]))
        print("――――――――――――――――――――――――――――――――――")

def player_navigation_and_interaction_with_map(x, y, player_icon, time_factor):
    print("Tour : 0")
    print(italic_txt + "C'est le matin \n" + normal_txt)
    print("Dans quelle direction souhaitez-vous aller ?\n")
    print_map(map)
    number_move_on_map = 15 # ----------------------- Nombre de tour avant de passer à la partie 2
    day_parts = 0
    i = 0
    while i < number_move_on_map:
        if keyboard.is_pressed("up") or keyboard.is_pressed("down") or keyboard.is_pressed("left") or keyboard.is_pressed("right"):
            clear()
            map[x][y] = "  " #On rester la position du joueur a une case vide

            if keyboard.is_pressed("up"):
                if x == 0:
                    x = len(map) - 1
                else:   
                    x -= 1

            elif keyboard.is_pressed("down"):
                if x == len(map) - 1:
                    x = 0
                else:
                    x += 1

            elif keyboard.is_pressed("left"):
                if y == 0:
                    y = len(map) - 1
                else:
                    y -= 1

            elif keyboard.is_pressed("right"):
                if y == len(map) - 1:
                    y = 0
                else:
                    y += 1

            map[x][y] = player_icon # ----------------------- La nouvelle position du joueur est affichée sur la carte
            player_current_coordinates_list = [x, y]
            encounter_battle_event(player_current_coordinates_list, battle_event_coordinates_list)
            if player_health_condition["health_condition"] == "dead":
                return
            encounter_item_event(player_current_coordinates_list, item_event_coordinates_list)
            encounter_trade_event(player_current_coordinates_list, trade_event_coordinates_list)
            clear()
            print("Tour :", i+1)
            if int(time_factor%2) != 1 and day_parts <= 2: # ----------------------- Affichage du temps pour prévenir que la carte va bientôt passer en nuit ou en jour
                if day_parts == 0:
                    print(italic_txt + "C'est le matin \n" + normal_txt)
                    day_parts +=1
                else:
                    print(italic_txt + "C'est l'après-midi\n" + normal_txt)
                    day_parts +=1
            else:
                if day_parts == 2:
                    print(italic_txt + dim_txt +"C'est le début de la nuit\n" + normal_txt)
                    day_parts +=1 
                else:
                    print(italic_txt + dim_txt +"C'est le milieu de la nuit\n" + normal_txt)
                    day_parts = 0
            print("Dans quelle direction souhaitez-vous aller ?\n")
            display_map_day_night_cycle(battle_event_coordinates_list, item_event_coordinates_list, trade_event_coordinates_list, battle_icon,item_icon,trade_icon,time_factor)
            sleep(0.7)
            time_factor += 0.5
            i +=1


# --------------------------------------------- CREATION ALEATOIRE DES ELEMENTS DE LA CARTE ---------------------------------------------

def event_position_generator(map, player_icon, battle_icon, item_icon, trade_icon, nb_event,event_to_generate):
    event_list = []
    for i in range(nb_event):
        x = randint(0, len(map) - 1)
        y = randint(0, len(map) - 1)
        while map[x][y] == item_icon or map[x][y] == battle_icon or map[x][y] == trade_icon or map[x][y] == player_icon : # ----------------------- Vérification sur la carte que les éléments ne sont pas déjà attribués à un autre élément
            x = randint(0, len(map) - 1)
            y = randint(0, len(map) - 1)
        map[x][y] = event_to_generate      # ----------------------- Attribution du symbole sur la carte à la position aléatoire x, y
        event_list.append([x, y])          # ----------------------- Sauvegarde des coordonnées x et y de l'élément combat sur la carte
    return event_list


# --------------------------------------------- ALTERNANCE MODE JOUR/NUIT DE LA CARTE ---------------------------------------------

def display_map_day_night_cycle(battle_coordinates, item_coordinates,trade_coordinates, battle_icon,item_icon,trade_icon,time_factor):
    if int(time_factor%2) != 0 and player["class_name"] != "Hibou": # ----------------------- Hibou peut voir tous les éléments de la carte la nuit
        night_map = map

        if player["class_name"] == "Singe": # ----------------------- Singe ne voit que les objets la nuit
            for i in battle_coordinates:
                night_map[i[0]][i[1]] = "  "
            for i in trade_coordinates:
                night_map[i[0]][i[1]] = "  "
            print_map(night_map)
        
        elif player["class_name"] == "Serpent": # ----------------------- Serpent ne voit que les combats la nuit
            for i in item_coordinates:
                night_map[i[0]][i[1]] = "  "
            for i in trade_coordinates:
                night_map[i[0]][i[1]] = "  "
            print_map(night_map)

        else: # ----------------------- Tous les autres animaux ne voient aucun élément la nuit
            for i in battle_coordinates:
                night_map[i[0]][i[1]] = "  "
        
            for i in item_coordinates:
                night_map[i[0]][i[1]] = "  "

            for i in trade_coordinates:
                night_map[i[0]][i[1]] = "  "
            print_map(night_map)
    else: # ----------------------- Tous les éléments sont affichés le jour
        for i in battle_coordinates:
            map[i[0]][i[1]] = battle_icon
  
        for i in item_coordinates:
            map[i[0]][i[1]] = item_icon
  
        for i in trade_coordinates:
            map[i[0]][i[1]] = trade_icon
        print_map(map)


# --------------------------------------------- ACTION DES ELEMENTS DE LA CARTE LORSQUE LE JOUEUR TOMBE DESSUS ---------------------------------------------

def encounter_battle_event(player_current_coordinates_list, battle_event_coordinates_list):
    for i in range(len(battle_event_coordinates_list)):
        if player_current_coordinates_list == battle_event_coordinates_list[i]:
            print("Vous entrez en combat !")
            sleep(2)
            combat(player)
            battle_event_coordinates_list.remove(player_current_coordinates_list)
            return

def encounter_item_event(player_current_coordinates_list, item_event_coordinates_list):
    for i in range(len(item_event_coordinates_list)):
        if player_current_coordinates_list == item_event_coordinates_list[i]:
            print("Vous avez trouvé un objet ! \n")
            item_found = random_item_generator(all_item_list)
            item_found_info_print(item_found)
            update_player_inventory_for_item_event(player,item_found)
            item_event_coordinates_list.remove(player_current_coordinates_list)
            return

def encounter_trade_event(player_current_coordinates_list, trade_event_coordinates_list):
    for i in range(len(trade_event_coordinates_list)):
        if player_current_coordinates_list == trade_event_coordinates_list[i]:
            print("Vous avez rencontré un joueur. C'est l'heure de l'échange !")
            next_instruction()
            player_trade_object(player)
            trade_event_coordinates_list.remove(player_current_coordinates_list)
            return


# --------------------------------------------- ACTION 'ECHANGE' DE LA CARTE LORSQUE LE JOUEUR TOMBE DESSUS ---------------------------------------------

def player_trade_object(player):
    items_player_to_trade_list = [] # ----------------------- Liste d'objets du joueur qu'il peut éventuellement échanger
    
    # ----------------------- Vérification s'il y a un objet dans l'inventaire du player -----------------------
    for i in range(len(weapons_for_menu_list)):
        if player["inventory"]["weapons"][weapons_for_menu_list[i]]["nb"] > 0:
            items_player_to_trade_list.append(player["inventory"]["weapons"][weapons_for_menu_list[i]]["item_name"])
    for i in range(len(fruits_for_menu_list)):
        if player["inventory"]["fruits"][fruits_for_menu_list[i]]["nb"] > 0:
            items_player_to_trade_list.append(player["inventory"]["fruits"][fruits_for_menu_list[i]]["item_name"])
    for i in range(len(plants_for_menu_list)):
        if player["inventory"]["plants"][plants_for_menu_list[i]]["nb"] > 0:
            items_player_to_trade_list.append(player["inventory"]["plants"][plants_for_menu_list[i]]["item_name"])

    if len(items_player_to_trade_list) == 0:
        alert_print("Votre inventaire est vide ! Vous ne pouvez rien échanger.")
        next_instruction()
    else:
        item_to_trade = random_item_generator(all_item_list)
        while item_to_trade == "Piège" or item_to_trade == "Noisettes":
            item_to_trade = random_item_generator(all_item_list)
        while True:
            clear()
            random_player_item_to_trade = items_player_to_trade_list[randint(0,len(items_player_to_trade_list) -1)]
            print("L'inconnu souhaite vous échanger l'objet suivant :", item_to_trade," contre votre objet :",random_player_item_to_trade,"\n \nQue souhaitez-vous faire ?\n(1) Echanger\n(2) Refuser")
            try:
                erased_previous_input()
                player_trade_choice = int(input("\nVotre choix : "))
            except ValueError:
                alert_print("Choix indisponible !")
            else:
                if player_trade_choice == 1:
                    clear()
                    delete_player_item_inventory_for_trade_event(player, random_player_item_to_trade)
                    update_player_inventory_for_item_event(player, item_to_trade)
                    print("L'échange s'est effectué sans accroc.")
                    print("Vous avez récupéré l'objet :", item_to_trade)
                    next_instruction()
                    break

                elif player_trade_choice == 2:
                    clear()
                    print("Vous avez refusé l'échange, c'est dommage !")
                    next_instruction()
                    break
                else:
                    alert_print("Choix indisponible !")

def print_player_all_inventories():
    for i in range(len(fruits_for_menu_list)):
        if player["inventory"]["fruits"][fruits_for_menu_list[i]]["nb"] > 0:
            print(player["inventory"]["fruits"][fruits_for_menu_list[i]]["item_name"], " nb :", player["inventory"]["fruits"][fruits_for_menu_list[i]]["nb"],"\n")
    for i in range(len(weapons_for_menu_list)):
        if player["inventory"]["weapons"][weapons_for_menu_list[i]]["nb"] > 0:
            print(player["inventory"]["weapons"][weapons_for_menu_list[i]]["item_name"], " nb :", player["inventory"]["weapons"][weapons_for_menu_list[i]]["nb"],"\n")
    for i in range(len(plants_for_menu_list)):
        if player["inventory"]["plants"][plants_for_menu_list[i]]["nb"] > 0:
            print(player["inventory"]["plants"][plants_for_menu_list[i]]["item_name"], " nb :", player["inventory"]["plants"][plants_for_menu_list[i]]["nb"],"\n")



# --------------------------------------------- PRINT DE L'OBJET TROUVE SUR LA CARTE PAR LE JOUEUR ---------------------------------------------

def item_found_info_print(item_found):
    if item_found in weapons_dict:
        print("Vous avez découvert l'arme:", item_found)
        print("Elle augmente votre attaque de", "+" + str(player["inventory"]["weapons"][item_found]["value"]) +".")
        next_instruction()
    elif item_found in fruits_dict:
        print("Vous avez découvert le fruit :", item_found)
        print("Il peut vous redonner", "+" + str(player["inventory"]["fruits"][item_found]["value"]),"de vie.")
        next_instruction()
    elif item_found == "Piège":
        print("Vous êtes tombé.e sur un", item_found, "! Vous avez perdu -3 de vie ! \n")
        next_instruction()
    elif item_found == "Noisettes":
        print("Vous trouvez quelques noisettes au sol ! \n")
        next_instruction()
    else:
        print("Tu as découvert la plante :", item_found)
        if item_found == "Menthe":
            print("Elle peut améliorer votre vitesse de", "+" + str(player["inventory"]["plants"][item_found]["value"]),"le temps d'un combat.")
        elif item_found == "Eucalyptus":
            print("Elle peut améliorer votre vie maximale de", "+" + str(player["inventory"]["plants"][item_found]["value"]),"le temps d'un combat.")
        elif item_found == "Jacinthes":
            print("Elle peut améliorer votre défense de", "+" + str(player["inventory"]["plants"][item_found]["value"]),"le temps d'un combat.")
        elif item_found == "Champignon":
            print("Elle peut améliorer vos dégats de", "+" + str(player["inventory"]["plants"][item_found]["value"]),"le temps d'un combat.")
        next_instruction()


# --------------------------------------------- PERMET LE LANCEMENT ENTIER DE LA PARTIE 1 ---------------------------------------------

def navigation_system(player_assigned_at_start):
    global item_icon
    global battle_icon
    global trade_icon
    global map
    global battle_event_coordinates_list
    global item_event_coordinates_list
    global trade_event_coordinates_list
    global player   

    player = player_assigned_at_start   #----------------------- Assignation de player au paramètre qui contient le joueur selectionné depuis introduction_and_player_assignment()

    player_icon = "⭕"
    item_icon =   "⭐"
    battle_icon = "⚡"
    trade_icon =  "⛺"
    time_factor = 0     #----------------------- Si le time factor %2 == 0 : alterne du jour à la nuit

    map = []
    map_size = 7
    for row in range(map_size):
        map.append(["  "] * map_size)

    player_pos_x = randint(0, len(map) - 1)        #----------------------- Génération aléatoire de la postion x du joueur
    player_pos_y = randint(0, len(map) - 1)        #----------------------- Génération aléatoire de la postion y du joueur
    map[player_pos_x][player_pos_y] = player_icon  #----------------------- Mise a jour de la carte avec la position du joueur
    
    battle_event_coordinates_list = event_position_generator(map, player_icon, battle_icon, item_icon, trade_icon, 16, battle_icon)
    item_event_coordinates_list = event_position_generator(map, player_icon, battle_icon, item_icon, trade_icon, 14, item_icon)
    trade_event_coordinates_list = event_position_generator(map, player_icon, battle_icon, item_icon, trade_icon, 8, trade_icon)
    player_navigation_and_interaction_with_map(player_pos_x, player_pos_y, player_icon, time_factor)
