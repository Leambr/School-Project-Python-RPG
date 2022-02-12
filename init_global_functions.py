
from os import system
from time import sleep
from random import randint
from init_var_classes_and_items import weapons_dict, fruits_dict, plants_dict
import keyboard

# --------------------------------------------- FONCTIONS POUR NETTOYER LE TERMINAL OU DONNER DES INSTRUCTIONS DE BASE AU JOUEUR ---------------------------------------------

def clear():
    return system('cls')

def next_instruction():
    print("\nSuivant... (espace)")
    while True:
        if keyboard.is_pressed("space"):
            sleep(0.4)
            clear()
            return

def erased_previous_input():
    for i in range(50):
        keyboard.press("delete")
        keyboard.press("left")

def alert_print(text):
    clear()
    print(text)
    sleep(1.5)

# --------------------------------------------- ATTRIBUTION ALEATOIRE D'UN ANIMAL ET DE SES STATISTIQUES AU JOUEUR ---------------------------------------------

def random_animal_assigned(all_animals_classes_list):
    player = all_animals_classes_list[randint(0, len(all_animals_classes_list) - 1)]
    return player

# --------------------------------------------- MISE A JOUR DE L'INVENTAIRE ---------------------------------------------

def random_item_generator(all_item_list):
    calcul = randint(0, 25)
    if calcul >= 0 and calcul <= 9:
        for i in range(2):
            if randint(0, 2) == 0:
                return all_item_list[i]
        return all_item_list[i + 1]
    
    elif calcul >= 10 and calcul <= 17:
        for i in range(3,5):
            if randint(0, 2) == 0:
                return all_item_list[i]
        return all_item_list[i + 1]

    elif calcul >= 18 and calcul <= 22:
        for i in range(6,10):
            if randint(0, 4) == 0:
                return all_item_list[i]
        return all_item_list[i + 1]

    elif calcul >= 23 and calcul <= 25:
        for i in range(11,15):
            if randint(0, 4) == 0:
                return all_item_list[i]
        return all_item_list[i + 1]

def update_player_inventory_for_item_event(player,item):
    if item in weapons_dict:
        player["inventory"]["weapons"][item]["nb"] += 1
    elif item in fruits_dict:
        player["inventory"]["fruits"][item]["nb"] += 1
    elif item in plants_dict:
        player["inventory"]["plants"][item]["nb"] += 1
    elif item == "Piège":
        player["current_life"] -= 3
    elif item == "Noisettes":
        player["nuts"] += randint(4,10)

def delete_player_item_inventory_for_trade_event(player, item):
    if item in weapons_dict:
        player["inventory"]["weapons"][item]["nb"] -= 1
    elif item in fruits_dict:
        player["inventory"]["fruits"][item]["nb"] -= 1
    elif item in plants_dict:
        player["inventory"]["plants"][item]["nb"] -= 1

# --------------------------------------------- AMELIORATION DES STATISTIQUES DES PNJ SELON LE NIVEAU DU JOUEUR ---------------------------------------------

def pnj_evolution(pnj,player_level):
    amelioration_list = ["damage","max_life","speed","defense"]
    for stats in amelioration_list:
        pnj[stats] += randint(3 * player_level, 6 * player_level)
        if player_level > 3:
            pnj["level"] = randint(player_level-1,player_level+1)
        else:
            pnj["level"] = player_level
    pnj["current_life"] = pnj["max_life"]