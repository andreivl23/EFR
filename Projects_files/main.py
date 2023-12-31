import random
import sys
import time
import mysql.connector

RED = '\033[31m'
BLUE = '\033[34m'
RESET = '\033[0m'
GOLD = '\033[38;5;220m'
GREEN = '\033[32m'

connection = mysql.connector.connect(
         host='192.168.1.20',
         port=3306,
         database='efr_mini',
         user='American',
         password='123321',
         autocommit=True
         )


def slowprint(text):
    for char in text:
        print(char, end='', flush=True)  # Print a character without a newline
        time.sleep(0.02)
    return


def screen_refresh():
    print("\n"*60)
    return


def cleartable():
    sql = "DELETE FROM Game"
    cursor = connection.cursor()
    cursor.execute(sql)
    sql = "DELETE FROM events_location"
    cursor.execute(sql)
    return


def print_text(option):
    if option == "menu":
        screen_refresh()
        print("""
███████╗███████╗ ██████╗ █████╗ ██████╗ ███████╗
██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
█████╗  ███████╗██║     ███████║██████╔╝█████╗  
██╔══╝  ╚════██║██║     ██╔══██║██╔═══╝ ██╔══╝  
███████╗███████║╚██████╗██║  ██║██║     ███████╗
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝ """ +  BLUE +  """              
███████╗██████╗  ██████╗ ███╗   ███╗            
██╔════╝██╔══██╗██╔═══██╗████╗ ████║            
█████╗  ██████╔╝██║   ██║██╔████╔██║            
██╔══╝  ██╔══██╗██║   ██║██║╚██╔╝██║            
██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║            
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝     """ + RED + """                       
██████╗ ██╗   ██╗███████╗███████╗██╗ █████╗     
██╔══██╗██║   ██║██╔════╝██╔════╝██║██╔══██╗    
██████╔╝██║   ██║███████╗███████╗██║███████║    
██╔══██╗██║   ██║╚════██║╚════██║██║██╔══██║    
██║  ██║╚██████╔╝███████║███████║██║██║  ██║    
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝╚═╝  ╚═╝  """ + RESET + """                      
::::::::::::::::::
1) Start new game
2) Game story
3) Read manual 
4) Exit\n""")

    elif option == "manual":
        screen_refresh()
        print(f'''You need to find your passport, which is hidden in a random city.
When you arrive at stations, you can only move between neighboring cities.  \n
As you play, at some point you would be able to memorize first letter of the city by consuming PRIME.

One movement costs one PRIME.\nYou can either lose or get PRIME at random events. \n
To exit the game to menu, type "x" at "Where to:?"
''')
        input("Press enter to continue")
    elif option == "story":
        screen_refresh()
        slowprint(f'''You are an American that were on trip in Russia, but when you were on your way to the airport,
you realized that you lost your passport at Starbucks cafe, but you don't remember in which city. \n
You don't have any money left but you still have your {GOLD}PRIME drinks,{RESET}
that are valued by Russian citizens. Will you find your passport and fly back home or will you get stuck in Russia forever? \n
''')
        input("Press enter to continue")
    elif option == "gameover":
        screen_refresh()
        print(RED + """
    ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗████████╗
    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝╚══██╔══╝
     ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗   ██║   
      ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║   ██║   
       ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║   ██║   
       ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   
                                                                             
        """)
        print(f"""            
                        ::::::::::::::::::::                      
                        YOU ARE OUT OF PRIME
                        ::::::::::::::::::::
        """ + RESET)
        slowprint(f"No one believes you now that you are from America and you became a Russian forever. \n\n")
        input("Press enter to continue")
    elif option == "choo-choo":
        screen_refresh()
        print(RED + """   
o o o o o
____      o
][]]_n_n__][.
|__|________)<
'oo 0000---oo\_ + """ + RESET + """  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                """)
        time.sleep(0.2)
        screen_refresh()
        print(RED + """  
 . . . . . o o o o o
 _______    ____      o
[_____(__  ][]]_n_n__][.
[________]_|__|________)<
 oo    oo 'oo 0000---oo\_ """ + RESET + """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                """)
        time.sleep(0.2)
        screen_refresh()
        print(RED + """  
            . . . . . o o o o o
___________ _______    ____      o
[] [] [] [] [_____(__  ][]]_n_n__][.
[_________]_[________]_|__|________)<
oo      oo ' oo    oo 'oo 0000---oo\_ """ + RESET + """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        """)
        #print("... ... ... ... ... ... ... ...\n      Choo-Choo Choo-Choo\n... ... ... ... ... ... ... ...")
        time.sleep(0.2)
        screen_refresh()
        print(RED + """  
                             . . . . . o o o o o
      _________ ___________ _______    ____      o
     |[] [] []| [] [] [] [] [_____(__  ][]]_n_n__][.
     |________|_[_________]_[________]_|__|________)<
      oo    oo 'oo      oo ' oo    oo 'oo 0000---oo\_ """ + RESET + """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                """)
        time.sleep(0.2)
        screen_refresh()
        print(RED + """  
                                            . . . . . o o o o o
                      _________ ___________ _______    ____      o
                     |[] [] []| [] [] [] [] [_____(__  ][]]_n_n__][.
                     |________|_[_________]_[________]_|__|________)<
                      oo    oo 'oo      oo ' oo    oo 'oo 0000---oo\_ """ + RESET + """
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                """)
        time.sleep(0.2)
        screen_refresh()
        print(RED + """  
                                                                            . . . . . o o o o o
                                                     _________ ___________ _______    ____      o
                                                    |[] [] []| [] [] [] [] [_____(__  ][]]_n_n__][.
                                                    |________|_[_________]_[________]_|__|________)<
                                                     oo    oo 'oo      oo ' oo    oo 'oo 0000---oo\_ """ + RESET + """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                       """)
        time.sleep(0.2)
        screen_refresh()
        print(RED + """
                                                                                                             .
                                                                                         _________ ___________
                                                                                        |[] [] []| [] [] [] []
                                                                                        |________|_[_________]
                                                                                         oo    oo 'oo      oo  """ + RESET + """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
       
        """)
        time.sleep(0.2)
        screen_refresh()
    elif option == "win":
        screen_refresh()
        print(GOLD + """
     ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗██╗
     ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║██║
      ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║██║
       ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║╚═╝
        ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║██╗
        ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝
                                                               
        """)
        print(":::::::::::::::::::::::: YOU FOUND THE PASSPORT! ::::::::::::::::::::::::\n"+ RESET )
        slowprint("You are now returning safely to America, where PRIME is widely available!")


        input("\n\nPress ENTER to continue")
    elif option == "map":
        print("""
        Murmansk-----------Arkhangelsk     ---Pechora--Vorkuta
            |                   |         /                      Surgut--Novy Urengoy
        Saints Petersburg---Yaroslavl----/--Perm--|                 |                         Urgal
                  |          /             /      Yekaterinburg--Tyumen  Ust-Ilimsk  Tommot   /   |
            /-----Moscow----/----Kazan----/------/      |           |        |          |    /  Khabarovsk
            |          |                        /       Kurgan----Omsk   Bratsk-------Tynda-/      |
        Voronezh----|   Saratov---------------Ufa                   |   /     |         |       Vladivostok
            |       |       |  |                                    |  /      |         |
        Krasnodar---Volgograd  Orenburg                        Krasnojarsk   Irkutsk--Chita
                        |           |   
                    Astrakhan       Orsk
        """)


def move_use_balance():
    result = random.randint(1, 3)
    if result == 1:
        slowprint("Realizing you need to cover a long distance,\n"
              "you offer a bottle of "+RED+"PRIME"+RESET+" to a fellow passenger in exchange for a ticket to a city.")
    elif result == 2:
        slowprint("You offer a bottle of "+RED+"PRIME"+RESET+" to the station manager\n"
              "as a gesture to secure your passage on the next train to another city.")
    elif result == 3:
        slowprint("By extending a bottle of "+RED+"PRIME"+RESET+" to a Russian teenager,\n"
              "he reciprocates by providing you with a train ticket in exchange.")
    else:
        slowprint("Your train encounters an unexpected delay due to a technical issue.\n"
              "You offer a PRIME bottle to the train conductor,\n"
              "hoping it might expedite the repairs. In return,\n"
              "they prioritize the fix")
    print()


def event_story(name, balance):
    update = balance
    screen_refresh()
    if name == "finnish":
        slowprint("You saw a cheerful Finnish man coming out of the sauna who handed you a bottle of "+GREEN+"PRIME."+RESET)
    elif name == "american":
        slowprint("As you savor the finest drink in hand,\n"
              "a fellow American approaches with "+GREEN+"2 bottles of PRIME"+RESET+" and a sparkling smile.")
    elif name == "bully":
        print("A bully swoops in and snatches one of the "+RED+"PRIME"+RESET+" bottles, leaving you one less bottle of PRIME.")
    elif name == "russian":
        slowprint("As you relish the exquisite drink in your hand,\n"  
              "a friendly Russian comes over with two bottles of PRIME and a warm smile.\n")
        print()
        slowprint("However, in an unexpected turn of events, a mischievous individual swiftly takes "+RED+"2 bottles of PRIME"+RESET+" from you,\n"
              "leaving you empty-handed, but you are determined to stay positive.")
    elif name == "rival":
        loop = True
        slowprint("You meet your Russian twin lookalike brother,\n"
              "who also happens to be your rival, and he offers to play a game with you.")
        print()
        while loop:
            time.sleep(0.2)
            answer = input("\nDo you want to play the game with your rival? (Y/N)\n").upper()
            print()
            if answer == "Y":
                rival_dice = random.randint(1, 6)
                your_dice = random.randint(1, 6)
                slowprint(f"Your rival performs a spirited Russian dance reminiscent of the one in the\n"
                      f"'Dschinghis Khan - Moskau' music video.\n")
                print()
                slowprint(f"With flair, they roll the dice, revealing a {rival_dice}.\n"
                      f"They challenge you to surpass their roll.")

                print()
                dance_loop = True
                while dance_loop:
                    time.sleep(0.2)
                    choice = input("\nDo you wanna dance before rolling? (Y/N)\n").upper()
                    print()
                    if choice == "Y":
                        slowprint("You execute the floss dance with all the flair of a true American Backpack Kid,\n"
                              "accompanied by Katy Perry's 'Swish Swish' blaring from your phone.")

                        print()
                        input("Press enter to roll...")
                        print()
                        dance_loop = False
                    elif choice == "N":
                        print()
                        input("Press enter to roll...")
                        print()
                        dance_loop = False
                    else:
                        print("Invalid input!")

                if rival_dice > your_dice:
                    slowprint(f"You rolled a {RED}{your_dice}{RESET} lower score than your rival,\n"
                          "who continues to dance and laugh mockingly\n"
                          f"as they seize {RED}three bottles of your cherished PRIME.{RESET}\n")
                    update = -1 * balance
                elif rival_dice < your_dice:
                    slowprint(f"You rolled a {GREEN}{your_dice}{RESET} superior score compared to your rival,\n"
                          f"causing them to stumble and drop {GREEN}three bottles of PRIME.{RESET}\n"
                          "They gather the fallen bottles and offer them to you as a token of your victory.\n")
                else:
                    slowprint(f"You rolled {your_dice}."
                          f"The rolls resulted in a perfect tie. Your rival sighs and begins to walk away slowly.\n")
                    update = 0
                loop = False
            elif answer == "N":
                slowprint("Your rival gazes at you with disappointment.")
                update = 0
                loop = False
            else:
                print("Invalid input!")

    return update


def check_event(event_num):
    sql = f"SELECT name, balance FROM events WHERE id = {event_num};"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    event_dictionary = cursor.fetchall()

    name = event_dictionary[0]['name']
    balance = event_dictionary[0]['balance']

    return name, balance


def get_story():
    sql = "SELECT * FROM stories ORDER BY RAND() LIMIT 1;"
    cursor = connection.cursor()
    cursor.execute(sql)
    story = cursor.fetchone()
    return story[0]


def get_num_of_event(current_station, game_id):
    sql = f"Select opened, event from events_location where id = {current_station} and game = {game_id}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    number = result[0][0]
    event = result[0][1]
    if number == 0:
        sql = f"UPDATE events_location set opened = 1 where id = {current_station};"
        cursor.execute(sql)
    return number, event


def prime_for_letter(station, game_id):
    station = str(station)
    loop = True
    choice = True
    while loop:
        slowprint(GOLD + "Do you want to use 5 bottles of PRIME to reveal the first letter of the passport location?"+RESET)
        answer = input("(Y/N)\n").upper()
        if answer == "N":
            loop = False
        elif answer == "Y":
            screen_refresh()
            print(f"{GOLD}        ::::::::::::::::::::::::::::::: The first letter of the station is: {station[2]} :::::::::::::::::::::::::::::::{RESET}")
            update_balance(-5, game_id)
            choice = False
            loop = False
        else:
            print(RED+"Wrong input!"+RESET)
    return choice


def get_balance(game_id):
    sql = f"SELECT balance FROM game WHERE GameID = '{game_id}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    balance = cursor.fetchone()
    return balance[0]


def get_station_name(station_id):
    sql = f"SELECT StationName FROM Stations WHERE StationID = {station_id}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result


def get_neighbors(station_id):
    sql = f"SELECT StationName, StationID from Stations, Connections WHERE StationID2 = StationID AND StationID1 = '"
    sql += f"{station_id}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    neighbors = cursor.fetchall()

    neighbors_dictionary = {}
    num = 0
    for city in neighbors:
        num += 1
        neighbors_dictionary[str(num)] = city

    return neighbors_dictionary


def update_balance(amount, game_id):
    sql = f"UPDATE game SET Balance = Balance+({amount}) WHERE GameID = '{game_id}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    return


def moveto(station,game_id):
    sql = f"UPDATE Game SET Location = '{station}' WHERE gameid = {game_id} "
    cursor = connection.cursor()
    cursor.execute(sql)


def get_passport(game_id):
    sql = f"SELECT id FROM events_location WHERE event = 1 AND game = {game_id}"
    cursor = connection.cursor()
    cursor.execute(sql)
    passport_station_id = cursor.fetchone()
    return passport_station_id[0]


def get_events():
    sql = "SELECT id, name, balance, probability FROM events;"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def start(resource, current_station, player):
    sql = f"INSERT INTO game (ScreenName, Location, Balance) VALUES ('{player}', {current_station}, {resource});"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    g_id = cursor.lastrowid

    events = get_events()
    events_list = []

    for event in events:
        for i in range(0, event['probability'], 1):
            events_list.append(event['id'])

    t_stations = random.sample(range(1,34),33)

    for i, event_id in enumerate(events_list):
        sql = f"INSERT INTO events_location (id, game, event)" \
          f" VALUES ({t_stations[i]}, {g_id}, {event_id});"
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql)

    return g_id, events_list


def difficulty():
    chosen = True
    balance = 0
    while chosen:
        print("Choose your difficulty: 1, 2 or 3.")
        print("1. Easy (15 PRIME)")
        print("2. Medium (10 PRIME)")
        print("3. Hard (5 PRIME)")

        choose = input("Choose: ")
        if choose == "1":
            balance = 15
            chosen = False
        elif choose == "2":
            balance = 10
            chosen = False
        elif choose == "3":
            balance = 5
            chosen = False
        else:
            print(RED +"Wrong input! Please try again."+RESET)
            print()

    print()
    print(f"You start with {balance} bottles of PRIME.")
    return balance


def create_game():
    prime_balance = difficulty()
    screen_name = str(input("Choose your name: "))
    print('\n\n... Loading ...\n\n')
    if screen_name == 'Hero':
        prime_balance = 100000

    current_station = random.randint(1,33)
    game_id, events_list = start(prime_balance, current_station, screen_name)

    return current_station, game_id, events_list


def menu(skip):
    chosen = 0
    if skip == 1:
        main()
    while chosen != "1":
        print_text("menu")
        chosen = input("Choose: ")
        if chosen == "2":
            print_text("story")
        elif chosen == "3":
            print_text("manual")
        elif chosen == "4":
            print('\nSee you again! :)\n')
            #cleartable()
            sys.exit()


def main():
    menu(0)
    while True:
        screen_refresh()
        ##################### Start #########################
        game_round = 0
        current_station, game_id, events_probability = create_game()
        passport_location = get_passport(game_id)
        passport_st_name = get_station_name(passport_location)
        used = True

        while True:
            screen_refresh()
            game_round += 1
            moveto(current_station, game_id)
            update_balance(-1, game_id)
            balance = get_balance(game_id)

            if balance < 0:
                print_text("gameover")
                break
            else:
                move_use_balance()
            time.sleep(1)
            print_text("choo-choo")
            time.sleep(0.2)


            ################### EVENTS ###################

            station_name = get_station_name(current_station)
            print(f"\n\nArriving at {station_name[0]}...")
            time.sleep(1)
            if passport_location == current_station:
                print_text("win")
                menu(1)
            neighbors = get_neighbors(current_station)
            open, event_num = get_num_of_event(current_station, game_id)

            if open == 0:
                event_name, event_balance = check_event(event_num)
                update_event_balance = event_story(event_name, event_balance)

                update_balance(update_event_balance, game_id)
                balance = get_balance(game_id)
                if balance < 0:
                    balance = 0

            else:
                screen_refresh()
                slowprint(get_story())
            print()
            input("\nPress enter to continue...")
            screen_refresh()

            if (game_round % 5) == 0 and balance >= 10:
                if used:
                    choice = prime_for_letter(passport_st_name, game_id)
                    balance = get_balance(game_id)
                    used = choice

            ################### STATION MENU ###################

            print_text('map')
            print(f"You're at {RED}{station_name[0]}{RESET}.")
            print(f"\nYour balance is {GOLD}{balance}{RESET} bottles of PRIME.")
            print("Connected stations:\n...")

            for choice in neighbors:
                city, city_id = neighbors[choice]
                print(f"{choice}) {city}")
            print("...")

            current_station = input("Where to: ")

            while (current_station not in neighbors) and current_station != 'x':
                print(RED + '\n\nWrong input, please try again.'+RESET)

                for choice in neighbors:
                    city, city_id = neighbors[choice]
                    print(f"{choice}) {city}")
                current_station = input("Where to: ")

            if current_station == 'x':
                break
            city, current_station = neighbors[current_station]

        menu(0)


main()
