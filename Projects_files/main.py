import random
import sys
import time
import mysql.connector


connection = mysql.connector.connect(
         host='172.232.129.9',
         port=3306,
         database='efr_mini_test',
         user='root',
         password='123321',
         autocommit=True
         )


def screen_refresh():
    print("\n"*60)
    return


def slowprint(text, speed):
    for char in text:
        print(char, end='', flush=True)  # Print a character without a newline
        time.sleep(speed)
    return


def print_text(option):
    if option == "menu":
        screen_refresh()
        print("""\n::::::::::::::::::
ESCAPE FROM RUSSIA\n
1) Start new game
2) Game story
3) Read manual 
4) Exit\n""")

    elif option == "manual":
        screen_refresh()
        print(f'''You need to find your passport, which is hidden in a random city.
When you arrive at stations, you can only move between neighboring cities. 
As you play, you would be able to memorize one letter of the city by consuming PRIME.
When you get enough letters to guess the name of the city, try to get there without consuming all the PRIME.
One movement costs one PRIME. You can either lose or get PRIME at random events.
To exit the game to menu, type "x" at "Where to:?"
''')
        input("Press enter to continue")
    elif option == "story":
        screen_refresh()
        print(f'''You are an American that were on trip in Russia, but when your trip came to an end,
you realized that you lost your passport at Starbucks cafe, but you don't remember in which city.
You don't have any money left but you still have your PRIME drinks,
that are valued by Russian citizens. Is it going to be over soon or will you get stuck in Russia?
''')
        input("Press enter to continue")
    elif option == "gameover":
        print(f"::::::::::::::::::::::\nYOU ARE OUT OF PRIME\n::::::::::::::::::::::\n\n"
              f"No one believes you now that you are from America and you became a Russian forever. \n")

        input("Press enter to continue")
    elif option == "chuh-chuh":
        print("... ... ... ... ... ... ... ...\n      Chuh-Chuh Chuh-Chuh\n... ... ... ... ... ... ... ...\n\n\n\n")
    elif option == "win":
        print("::::::::::::::::::::: YOU FOUND THE PASSPORT! :::::::::::::::::::::\nYou are now returning safely to America, where PRIME is widely available")

        input("\n\nPress ENTER to continue")
    elif option == "map":
        print("""
        Murmansk-----------Arkhangelsk     ---Pechora--Vorkuta
            |                   |         /                      Surgut--"Novy Urengoy"
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
            sys.exit()


def difficulty():
    chosen = True
    while chosen:
        print("Choose your difficulty: 1, 2 or 3.")
        print("1. Easy (15 PRIME)")
        print("2. Medium (10 PRIME)")
        print("3. Hard (5 PRIME)")

        choose = input()
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
            print("Wrong input! Please try again.")
            print()

    return balance


def get_stations():
    sql = """SELECT StationID, StationName
    FROM stations
    ORDER by RAND()"""
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def get_events():
    sql = "SELECT id, name, balance, probability FROM events;"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def start(resource, current_station, player, stations):
    sql = f"INSERT INTO game (ScreenName, Location, Balance) VALUES ('{player}', '{current_station}', {resource});"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    g_id = cursor.lastrowid

    events = get_events()
    events_list = []

    for event in events:
        for i in range(0, event['probability'], 1):
            events_list.append(event['id'])

    t_stations = stations[1:].copy()

    random.shuffle(t_stations)

#    for i, event_id in enumerate(events_list):        # Removed for-loop due to a bug. Added only passport location to Database
    sql = f"INSERT INTO events_location (game, station, event)" \
          f" VALUES ({g_id}, '{t_stations[0]['StationName']}', {1});"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)

    return g_id


def create_game():
    prime_balance = difficulty()
    screen_name = str(input("Choose your name: "))
    print('\n\n... Loading ...\n\n')
    if screen_name == 'Hero':
        prime_balance = 100000

    all_stations = get_stations()
    current_station = all_stations[0]['StationID']
    game_id = start(prime_balance, current_station, screen_name, all_stations)

    return current_station, game_id


def moveto(station):
    sql = f"UPDATE Game SET Location = '{station}' "
    cursor = connection.cursor()
    cursor.execute(sql)


def get_story():
    sql = "SELECT * FROM stories ORDER BY RAND() LIMIT 1;"
    cursor = connection.cursor()
    cursor.execute(sql)
    story = cursor.fetchone()
    return story[0]


def get_balance(game_id):
    sql = f"SELECT balance FROM game WHERE GameID = '{game_id}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    balance = cursor.fetchone()
    return balance[0]


def get_current_station_name(station_id):
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


def cleartable():
    sql = "DELETE FROM Game"
    cursor = connection.cursor()
    cursor.execute(sql)
    return


def update_balance(amount, game_id):
    sql = f"UPDATE game SET Balance = Balance+({amount}) WHERE GameID = '{game_id}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    return


def get_passport(game_id):
    sql = f"SELECT station FROM events_location WHERE event = 1 AND game = {game_id}"
    cursor = connection.cursor()
    cursor.execute(sql)
    passport_stationname = cursor.fetchone()
    return passport_stationname[0]


def event_trigger_chance():
    result = random.randint(0, 2)
    if result == 1:
        roll = True
    else:
        roll = False

    return roll


def check_event():
    game_id = random.randint(2, 5)
    sql = f"SELECT name, balance FROM events WHERE id = {game_id};"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    event_dictionary = cursor.fetchall()

    return event_dictionary


def main():
    menu(0)
    while True:
        screen_refresh()

        ##################### Start #########################

        current_station, game_id = create_game()
        passport_location = get_passport(game_id)
        while True:
            screen_refresh()
            moveto(current_station)
            update_balance(-1, game_id)




            ################### STATION MENU ################

            station_name = get_current_station_name(current_station)
            if passport_location == station_name[0]:
                print_text("win")
                menu(1)
            balance = get_balance(game_id)
            if balance < 0:
                print_text("gameover")
                break
            print_text('map')
            neighbors = get_neighbors(current_station)

            print(f"\nYou're arriving at {station_name[0]}.\n")
            trigger = event_trigger_chance()
            if trigger:
                event_dictionary = check_event()
                event_name = event_dictionary[0]['name']

                event_balance = event_dictionary[0]['balance']
                update_balance(event_balance, game_id)

                print(f"You met a {event_name}. You're balance got updated by {event_balance}.")
                balance = get_balance(game_id)
            else:
                print(get_story())

            print(f"\nYour balance is {balance} bottles of PRIME.")
            print("Connected stations:\n...")

            for choice in neighbors:
                city, city_id = neighbors[choice]
                print(f"{choice}) {city}")
            print("...")

            current_station = input("Where to: ")

            while (current_station not in neighbors) and current_station != 'x':
                print('\n\nWrong input, please try again.')

                for choice in neighbors:
                    city, city_id = neighbors[choice]
                    print(f"{choice}) {city}")
                current_station = input("Where to: ")

            if current_station == 'x':
                break
            city, current_station = neighbors[current_station]

        menu(0)


main()
