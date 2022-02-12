
from init_global_functions import sleep, clear, randint, next_instruction, erased_previous_input, random_item_generator, update_player_inventory_for_item_event, delete_player_item_inventory_for_trade_event, pnj_evolution, alert_print
from init_var_classes_and_items import all_animals_classes_list, all_item_list, normal_txt, italic_txt, dim_txt, bright_txt, yellow_txt, blue_txt, weapons_for_menu_list, fruits_for_menu_list, plants_for_menu_list, weapons_dict, fruits_dict, plants_dict


def choice_list_generator(max_choice): # ----------------------- Génère une liste pour limiter les erreurs liées aux inputs. Elle return une liste de choix possible en fonction du contexte dans laquelle elle est appelée, grâce au paramètre max_choice
    choice_list = []
    for i in range(1,max_choice+1):
        choice_list.append(str(i))
    return choice_list

# --------------------------------------------- CREATION DE L'INVENTAIRE DE L'ECUREUIL  ET DE SON MARCHE ---------------------------------------------

def squirrel_stuff_sell():
    squirrel_item_to_sell_list = []

    for i in range(3):
        squirrel_item = random_item_generator(all_item_list)
        while squirrel_item == "Piège" or squirrel_item == "Noisettes":
            squirrel_item = random_item_generator(all_item_list)
        while squirrel_item in squirrel_item_to_sell_list:
            squirrel_item = random_item_generator(all_item_list)
        else:
            squirrel_item_to_sell_list.append(squirrel_item)

    return squirrel_item_to_sell_list
  
def squirrel_shop_print(squirrel_item_to_sell_list, player):
    clear()
    print(italic_txt + dim_txt + "Si vous souhaitez quitter le magasin, écrivez 'quitter'", normal_txt + bright_txt + "\n\nQue voulez-vous acheter ?" + normal_txt)
    print("Vous avez : ",  yellow_txt + str(player["nuts"]), "noisettes\n" + normal_txt)
    for i in range(len(squirrel_item_to_sell_list)):
        for item_dict in player["inventory"]:
            for item in player["inventory"][item_dict]:
                if item == squirrel_item_to_sell_list[i]:

                    print(bright_txt + player["inventory"][item_dict][squirrel_item_to_sell_list[i]]["item_name"] + normal_txt)
                    print("Effets : ", blue_txt + "+" + str(player["inventory"][item_dict][squirrel_item_to_sell_list[i]]["value"]), str(player["inventory"][item_dict][squirrel_item_to_sell_list[i]]["alter_stat"]) + normal_txt )
                    print("Prix   : ", yellow_txt + str(player["inventory"][item_dict][squirrel_item_to_sell_list[i]]["value"]*market_price_coefficient), "noisettes\n" + normal_txt)


def market_squirrel(player): 
    market_choice_list = choice_list_generator(2)
    while True:
        clear()
        print("Bienvenue chez le marchand, que voulez-vous faire ?\n")
        print("Acheter     (1) \nVendre      (2)")
        market_player_choice = input("\nVotre choix: ")
        if market_player_choice not in market_choice_list:
            alert_print("Choix indisponible !")
        elif market_player_choice == "1":
            squirrel_list = squirrel_stuff_sell() #A revoir
            buy(squirrel_list, player)
            return
        elif market_player_choice == "2":
            sell(player)
            return


# --------------------------------------------- ACHAT D'OBJETS CHEZ L'ECUREUIL ---------------------------------------------

def buy(squirrel_item_to_sell_list,player):
    while True:
        squirrel_shop_print(squirrel_item_to_sell_list, player)
        player_can_buy_item = True
        player_choosen_item_to_buy = input("Votre choix : ")

        if player_choosen_item_to_buy == "quitter":
            clear()
            print("Vous quittez le magasin !")
            print("Une journée passe...")
            sleep(2.5)
            break
        elif player_choosen_item_to_buy in squirrel_item_to_sell_list:
            for item_dict in player["inventory"]:
                try:
                    if player["nuts"] < player["inventory"][item_dict][player_choosen_item_to_buy]["value"]*market_price_coefficient: # ----------------------- Vérification du nombre de noisettes du joueur avant achat
                        player_can_buy_item = False
                except KeyError:
                    pass

            if player_can_buy_item == False:
                clear()
                print("Vous n'avez pas assez de noisettes pour acheter cet objet")
                next_instruction()
            else:               
                update_player_inventory_for_item_event(player, player_choosen_item_to_buy)
                decrease_player_nuts_buy(player, player_choosen_item_to_buy)
                clear()
                print("Suite à votre achat de l'objet", player_choosen_item_to_buy, "il vous reste", player["nuts"], "noisettes.\n")
                next_instruction()
                return
        else:
            alert_print("Choix indisponible !")


# --------------------------------------------- MAJ DU PORTEFEUILLE DU JOUEUR SELON SES ACHATS OU VENTES ---------------------------------------------

def decrease_player_nuts_buy(player, player_choosen_item_to_buy):
    if player_choosen_item_to_buy in weapons_dict:
        player["nuts"] -= player["inventory"]["weapons"][player_choosen_item_to_buy]["value"]*market_price_coefficient
    elif player_choosen_item_to_buy in fruits_dict:
        player["nuts"] -= player["inventory"]["fruits"][player_choosen_item_to_buy]["value"]*market_price_coefficient
    elif player_choosen_item_to_buy in plants_dict:
        player["nuts"] -= player["inventory"]["plants"][player_choosen_item_to_buy]["value"]*market_price_coefficient

def increase_player_nuts_sell(player, player_choosen_item_to_sell):
    if player_choosen_item_to_sell in weapons_dict:
        player["nuts"] += player["inventory"]["weapons"][player_choosen_item_to_sell]["value"]*market_price_coefficient
    elif player_choosen_item_to_sell in fruits_dict:
        player["nuts"] += player["inventory"]["fruits"][player_choosen_item_to_sell]["value"]*market_price_coefficient
    elif player_choosen_item_to_sell in plants_dict:
        player["nuts"] += player["inventory"]["plants"][player_choosen_item_to_sell]["value"]*market_price_coefficient


# --------------------------------------------- VENTE D'OBJETS CHEZ L'ECUREUIL ---------------------------------------------

def sell(player):
    items_player_to_trade_list = [] # ----------------------- Liste pour vérifier si l'inventaire du joueur est vide ou non avant de pouvoir vendre
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
        alert_print("Votre inventaire est vide ! Vous ne pouvez rien vendre.")
        next_instruction()
    else:
        while True:
            clear()
            print(italic_txt + dim_txt + "Si vous souhaitez quitter le magasin, écrivez 'quitter'", normal_txt + bright_txt + "\n\nQue voulez-vous vendre ?" + normal_txt)
            print("Vous avez : ",  yellow_txt + str(player["nuts"]), "noisettes\n" + normal_txt)

            for i in range(len(fruits_for_menu_list)): # ----------------------- Affiche l'inventaire du joueur et le prix des objets
                if player["inventory"]["fruits"][fruits_for_menu_list[i]]["nb"] > 0:
                    print(bright_txt + player["inventory"]["fruits"][fruits_for_menu_list[i]]["item_name"],"[" + str(player["inventory"]["fruits"][fruits_for_menu_list[i]]["nb"]) + "]" + normal_txt)
                    print("Effets : ", blue_txt + "+" + str(player["inventory"]["fruits"][fruits_for_menu_list[i]]["value"]), str(player["inventory"]["fruits"][fruits_for_menu_list[i]]["alter_stat"]) + normal_txt)
                    print("Prix unitaire :", yellow_txt + str(player["inventory"]["fruits"][fruits_for_menu_list[i]]["value"]*market_price_coefficient),"noisettes","\n"+ normal_txt)
            
            for i in range(len(weapons_for_menu_list)):
                if player["inventory"]["weapons"][weapons_for_menu_list[i]]["nb"] > 0:
                    print(bright_txt + player["inventory"]["weapons"][weapons_for_menu_list[i]]["item_name"],"[" + str(player["inventory"]["weapons"][weapons_for_menu_list[i]]["nb"]) + "]" + normal_txt)
                    print("Effets : ", blue_txt + "+" + str(player["inventory"]["weapons"][weapons_for_menu_list[i]]["value"]), str(player["inventory"]["weapons"][weapons_for_menu_list[i]]["alter_stat"]) + normal_txt)
                    print("Prix unitaire :", yellow_txt + str(player["inventory"]["weapons"][weapons_for_menu_list[i]]["value"]*market_price_coefficient),"noisettes","\n" + normal_txt)
            
            for i in range(len(plants_for_menu_list)):
                if player["inventory"]["plants"][plants_for_menu_list[i]]["nb"] > 0:
                    print(bright_txt + player["inventory"]["plants"][plants_for_menu_list[i]]["item_name"],"[" + str(player["inventory"]["plants"][plants_for_menu_list[i]]["nb"]) + "]"+ normal_txt)
                    print("Effets : ", blue_txt + "+" + str(player["inventory"]["plants"][plants_for_menu_list[i]]["value"]), str(player["inventory"]["plants"][plants_for_menu_list[i]]["alter_stat"]) + normal_txt)
                    print("Prix unitaire :", yellow_txt + str(player["inventory"]["plants"][plants_for_menu_list[i]]["value"]*market_price_coefficient),"noisettes","\n" + normal_txt)


            player_choosen_item_to_sell = input("Votre choix : ")

            if player_choosen_item_to_sell == "quitter":
                alert_print("Vous quittez le magasin")
                break
    
            elif player_choosen_item_to_sell in fruits_for_menu_list or player_choosen_item_to_sell in weapons_for_menu_list or player_choosen_item_to_sell in plants_for_menu_list:
                delete_player_item_inventory_for_trade_event(player, player_choosen_item_to_sell)
                increase_player_nuts_sell(player, player_choosen_item_to_sell)
                clear()
                print("Suite à votre vente de l'objet", player_choosen_item_to_sell, "il vous reste", player["nuts"], "noisettes.\n")
                next_instruction()
                return
            else:
                alert_print("Choix indisponible !")



# --------------------------------------------- GENERE UN NOMBRE DE PNJ ---------------------------------------------

def pnj_generator(animal_li,nb_pnj):
    pnj_li = []
    for i in range(nb_pnj):
        pnj_li.append(animal_li[randint(0,len(animal_li)-1)].copy())
    return pnj_li


# --------------------------------------------- REMPLACER UN PNJ DE L'EQUIPE DU JOUEUR ---------------------------------------------

def replace_pnj(pnj_list,player_choice,player_crew_dict):
    choice_replace_list = choice_list_generator(len(player_crew_dict["crew"]))
    while True:
        for i in range(len(player_crew_dict["crew"])):
            print("(" + str(i+1) + ")", "Remplacer",player_crew_dict["crew"][i]["class_name"],"lvl",player_crew_dict["crew"][i]["level"])
        choice_replace = input(" ")    
        if choice_replace not in choice_replace_list:
            alert_print("Choix indisponible !")
        else:
            choice_replace = int(choice_replace)
            for j in range(len(player_crew_dict["crew"])):
                if choice_replace == j:
                    player_crew_dict["crew"].pop(j)
                    player_crew_dict["crew"].append(pnj_list[player_choice -1])
            break


# --------------------------------------------- DETERMINE SI PNJ REJOINT L'EQUIPE DU JOUEUR ---------------------------------------------

def negociation(pnj_list, player_choice, player_crew_dict, player): 

    social_randint = randint(0,player["social"]+5)
    threshold_nuts_to_recrute_pnj = randint(0,player["nuts"])

    if social_randint >= 5: # ----------------------- Plus la statistique "social" du joueur est élevée, plus il a de chance de recruter ce pnj
        clear()
        print(pnj_list[player_choice -1]["class_name"],"accepte de vous rejoindre.")
        if len(player_crew_dict["crew"]) == 2:
            replace_pnj(pnj_list,player_choice,player_crew_dict)
        else:
            player_crew_dict["crew"].append(pnj_list[player_choice -1])
        sleep(3)
    else:
        if player["nuts"] <= 0:
            print("Vous n'avez pas de noisettes")
            print("Il vous aurait peut être rejoint avec une petite prime !")
            sleep(4)
        else:
            while True:
                clear()
                print(pnj_list[player_choice -1]["class_name"],"ne veut pas rejoindre ton équipe")
                print("Proposez lui quelques noisettes","\n") # ----------------------- En cas d'échec, le joueur peut faire une offre de noisettes au PNJ
                print("Il vous en reste",player["nuts"])
                try:
                    offer = int(input())
                except ValueError:
                    alert_print("Choix indisponible !")
                else:
                    if offer > player["nuts"]:
                        clear()
                        print("Vous ne pouvez pas mettre plus que ce que vous possédez !")
                        sleep(2)
                    else:
                        if offer > threshold_nuts_to_recrute_pnj:
                            clear()
                            print(pnj_list[player_choice -1]["class_name"],"accepte de te rejoindre")
                            player["nuts"] -= offer
                            if len(player_crew_dict["crew"]) == 2:
                                replace_pnj(pnj_list,player_choice, player_crew_dict)
                            else:
                                player_crew_dict["crew"].append(pnj_list[player_choice -1])
                            sleep(2)
                            break
                        else:
                            print(pnj_list[player_choice -1]["class_name"],"n'accepte pas l'offre")
                            sleep(2)
                            break


# --------------------------------------------- PERMET LE LANCEMENT DE TOUTE LA PHASE 'RECRUTEMENT'---------------------------------------------

def recruitment(player, player_crew_dict):
    
    pnj_list = pnj_generator(all_animals_classes_list,2)
    player_crew_list = []

    for i in range(len(pnj_list)):
        pnj_evolution(pnj_list[i],player["level"])

    player_recruitment_choice_list = choice_list_generator(len(pnj_list)+2)
    print("Vous entrez sur la grande place.\nVous rencontrez : ","\n")
    for pnj in pnj_list:
        print(bright_txt + pnj["class_name"] + normal_txt)
        print("Niveau :", pnj["level"])
        print("Dégâts :",pnj["damage"])
        print("Vitesse :",pnj["speed"])
        print("Défense :",pnj["defense"],"\n")
    sleep(2)
    for j in range(len(pnj_list)):
        print("(" + str(j+1) + ")", "Recruter",pnj_list[j]["class_name"],"lvl",pnj_list[j]["level"])

    print("(" + str(len(pnj_list)+1) + ")", "Tous les recruter")
    print("(" + str(len(pnj_list)+2) + ")","Ne rien faire")

    while True:
        player_recruitment_choice = input(" ")

        if player_recruitment_choice not in player_recruitment_choice_list:
            alert_print("Choix indisponible !")
        else:
            player_recruitment_choice = int(player_recruitment_choice)


            if player_recruitment_choice < 3:
                negociation(pnj_list, player_recruitment_choice, player_crew_dict, player)
                break

            if player_recruitment_choice == len(pnj_list)+1:
                for l in range(len(pnj_list)):
                    negociation(pnj_list, l+1, player_crew_dict, player)
                break

            elif player_recruitment_choice == len(pnj_list)+2:
                clear()
                print("Les deux candidats repartent chez eux...")
                sleep(2)
                break

    if len(player_crew_dict["crew"]) > 0:
        clear()
        print("Membres de votre escouade :")
        for m in range(len(player_crew_dict["crew"])):
            print(player_crew_dict["crew"][m]["class_name"],"lvl",player_crew_dict["crew"][m]["level"])
        sleep(3)


# --------------------------------------------- SIESTE, PERMET DE PASSER DES JOURS DE LA PHASE 2 POUR ARRIVER PLUS VITE AU COMBAT AVEC LE TIGRE ---------------------------------------------

def nap(day):
    days_left = choice_list_generator(day)
    while True:
        print("Il vous reste",day,"jour(s) avant l'arrivée du Tigre.")
        print("Pendant combien de jour(s) souhaitez-vous dormir ?")
        days_to_sleep_player_choice = input("\nVotre choix : ")

        if days_to_sleep_player_choice not in days_left:
            alert_print("Choix indisponible !")
        else:
            clear()
            print("Vous vous reposez pendant :", days_to_sleep_player_choice,"jour(s)...")
            next_instruction()
            days_to_sleep_player_choice = int(days_to_sleep_player_choice)
            return days_to_sleep_player_choice


# --------------------------------------------- PERMET LE LANCEMENT DE TOUTE LA PARTIE 2 ---------------------------------------------
    
def market_place_and_team_building_system(player):
    clear()
    print("Votre périple vient de finir. Il est temps de vous préparer pour combattre le Tigre dans quelques jours...\n")
    sleep(3)
    print("Ici, vous pouvez acheter et vendre des objets chez l'écureuil. Vous pouvez également recruter vos équipiers pour le combat final.\n")
    sleep(3)
    print("Si vous souhaitez combattre le Tigre rapidement, vous pouvez faire la sieste pendant le nombre de jours que vous désirez.\n")
    sleep(3)
    next_instruction()

    global market_price_coefficient
    market_price_coefficient = 2
    day = 7
    past_day = 1
    player_crew_dict = {}
    crew_list = []
    player_crew_dict["crew"] = crew_list
    number_choice_in_p2_main_menu_list = choice_list_generator(3)
    while day > 0:
        clear()
        print(day,"jour(s) avant l'arrivée du Tigre\n")
        print("Que voulez vous faire ? :\n")
        print("Recrutement   (1) \nMarché        (2) \nSieste        (3)")

        erased_previous_input()
        p2_main_menu_player_choice = input("\nVotre choix :  ")

        if p2_main_menu_player_choice not in number_choice_in_p2_main_menu_list:
            alert_print("Choix indisponible !")
        else:
            if p2_main_menu_player_choice == "1":
                clear()
                recruitment(player, player_crew_dict)
            elif p2_main_menu_player_choice == "2":
                market_squirrel(player)
            elif p2_main_menu_player_choice == "3":
                clear()
                past_day = nap(day)
            day -= past_day

    player["crew"] = player_crew_dict["crew"]
