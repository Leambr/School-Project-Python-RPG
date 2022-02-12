
# --------------------------------------------- COULEURS NECESSAIRES POUR LE JEU ---------------------------------------------

normal_txt    = "\x1B[0m"
italic_txt    = "\x1B[3m"
bright_txt    = '\033[1m'
dim_txt       = '\033[2m'
underline_txt = "\u0332"

yellow_txt    = '\033[33m'
green_txt     = '\033[32m'
magenta_txt   = '\033[35m'
cyan_txt      = '\033[36m'
blue_txt      = '\033[34m'
red_txt       = '\033[31m'


# --------------------------------------------- VARIABLES DU JOUEUR AU LANCEMENT DU JEU ---------------------------------------------

hibou =            {"class_name": "Hibou",       "damage": 20, "max_life": 90,  "current_life": 80,  "speed": 50,  "defense": 40,   "social": 5,  "level": 1, "nuts": 0}
serpent =          {"class_name": "Serpent",     "damage": 40, "max_life": 90,  "current_life": 80,  "speed": 40,  "defense": 10,   "social": 0,  "level": 1, "nuts": 0}
renard =           {"class_name": "Renard",      "damage": 30, "max_life": 100, "current_life": 90,  "speed": 30,  "defense": 30,   "social": 10, "level": 1, "nuts": 20}
singe =            {"class_name": "Singe",       "damage": 40, "max_life": 100, "current_life": 90,  "speed": 20,  "defense": 20,   "social": 15, "level": 1, "nuts": 0}
aigle_royal =      {"class_name": "Aigle Royal", "damage": 50, "max_life": 80,  "current_life": 70,  "speed": 50,  "defense": 0,    "social": 5,  "level": 1, "nuts": 0}
ours_brun =        {"class_name": "Ours brun",   "damage": 40, "max_life": 120, "current_life": 110, "speed": 10,  "defense": 40,   "social": 10, "level": 1, "nuts": 0}

tigre_final_boss = {"class_name": "Le Tigre",    "damage": 30, "max_life": 250, "current_life": 250, "speed": 40,  "defense" : 40}

all_animals_classes_list = [hibou, serpent, renard, singe, aigle_royal, ours_brun]

weapons_dict = {"Noix" :         {"item_name": "Noix",   "value": 2,  "alter_stat": "Dégats",  "nb": 0},
                "Liane" :        {"item_name": "Liane",  "value": 5,  "alter_stat": "Dégats",  "nb": 0},
                "Pierre" :       {"item_name": "Pierre", "value": 8,  "alter_stat": "Dégats",  "nb": 0},
                "Bâton" :        {"item_name": "Bâton",  "value": 12,  "alter_stat": "Dégats", "nb": 0},
                "Os" :           {"item_name": "Os",     "value": 18, "alter_stat": "Dégats",  "nb": 0}}

fruits_dict = { "Raisin" :       {"item_name": "Raisin",       "value": 8,    "alter_stat": "Vie", "nb": 0},
                "Pomme" :        {"item_name": "Pomme",        "value": 16,    "alter_stat": "Vie", "nb": 0},
                "Pêche" :        {"item_name": "Pêche",        "value": 22,   "alter_stat": "Vie", "nb": 0},
                "Noix de coco" : {"item_name": "Noix de coco", "value": 30,   "alter_stat": "Vie", "nb": 0},
                "Pastèque" :     {"item_name": "Pastèque",     "value": 40,   "alter_stat": "Vie", "nb": 0}}

plants_dict = { "Menthe" :       {"item_name": "Menthe",      "value": 10,             "alter_stat": "Vitesse",    "nb": 0},
                "Eucalyptus" :   {"item_name": "Eucalyptus",  "value": 10,             "alter_stat": "Vie max",    "nb": 0},
                "Jacinthes" :    {"item_name": "Jacinthes",   "value": 10,             "alter_stat": "Défense",    "nb": 0},
                "Champignon" :   {"item_name": "Champignon",  "value": 10,             "alter_stat": "Dégats",     "nb": 0}}

weapons_for_menu_list = ["Noix","Liane", "Pierre", "Bâton", "Os"]
fruits_for_menu_list = ["Raisin", "Pomme", "Pêche", "Noix de coco", "Pastèque"]
plants_for_menu_list = ["Menthe", "Eucalyptus", "Jacinthes", "Champignon"]
all_item_list = ["Raisin", "Noix", "Pomme", "Liane", "Pierre", "Pêche", "Jacinthes", "Eucalyptus", "Menthe", "Noix de coco", "Bâton", "Piège", "Champignon", "Pastèque", "Os", "Noisettes"]

player_health_condition = { "health_condition" : "alive"}
game_launch = { "state" : "start"}
