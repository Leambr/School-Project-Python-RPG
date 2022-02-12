
from init_var_classes_and_items import player_health_condition
from init_global_functions import erased_previous_input, clear, next_instruction
from menus import main_menu
from introduction import introduction_and_player_assignment
from part_1_map_navigation_system import navigation_system
from part_2_market_place_and_recruitment import market_place_and_team_building_system
from combat import final_boss_combat


while True:
    if main_menu() == "Quit": #Si le joueur décide de sortir du jeu
        clear()
        break
    player = introduction_and_player_assignment()

    # --------------------------- PARTIE 1 ----------------

    navigation_system(player)

    # --------------------------- PARTIE 2 ----------------

    if player_health_condition["health_condition"] == "alive":
        market_place_and_team_building_system(player)

    # --------------------------- PARTIE 3 ----------------
    
        final_boss_combat(player)
        if player_health_condition["health_condition"] == "alive":
            print("A vous de vous occuper de l'avenir de la forêt...")
            next_instruction()



            