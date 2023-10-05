import random
import sys
import time
import mysql.connector


connection = mysql.connector.connect(
         host='172.232.129.9',
         port=3306,
         database='efr_test',
         user='root',
         password='123321',
         autocommit=True
         )


def screen_refresh():
    print("\n"*30)
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
        print(f'''𝐘𝐨𝐮𝐫 𝐠𝐨𝐚𝐥 𝐢𝐬 𝐭𝐨 𝐟𝐢𝐧𝐝 𝐚𝐧 𝐚𝐢𝐫𝐩𝐥𝐚𝐧𝐞, 𝐭𝐡𝐚𝐭 𝐢𝐬 𝐡𝐢𝐝𝐝𝐞𝐧 𝐢𝐧 𝐚 𝐫𝐚𝐧𝐝𝐨𝐦 𝐜𝐢𝐭𝐲.
𝐖𝐡𝐞𝐧 𝐲𝐨𝐮 𝐚𝐫𝐞 𝐚𝐭 𝐬𝐭𝐚𝐭𝐢𝐨𝐧, 𝐲𝐨𝐮 𝐜𝐚𝐧 𝐦𝐨𝐯𝐞 𝐨𝐧𝐥𝐲 𝐭𝐨 𝐬𝐭𝐚𝐭𝐢𝐨𝐧𝐬 𝐧𝐞𝐱𝐭 𝐭𝐨 𝐭𝐡𝐞 𝐜𝐮𝐫𝐫𝐞𝐧𝐭 𝐬𝐭𝐚𝐭𝐢𝐨𝐧.
𝐓𝐲𝐩𝐞 𝐧𝐮𝐦𝐛𝐞𝐫 (𝐢𝐝) 𝐨𝐟 𝐬𝐭𝐚𝐭𝐢𝐨𝐧 𝐭𝐨 𝐜𝐡𝐚𝐧𝐠𝐞 𝐲𝐨𝐮𝐫 𝐥𝐨𝐜𝐚𝐭𝐢𝐨𝐧.
𝐓𝐨 𝐞𝐱𝐢𝐭 𝐭𝐡𝐞 𝐠𝐚𝐦𝐞, 𝐞𝐧𝐭𝐞𝐫 "𝐱" 𝐢𝐧𝐬𝐭𝐞𝐚𝐝 𝐨𝐟 𝐭𝐡𝐞 𝐬𝐭𝐚𝐭𝐢𝐨𝐧 𝐧𝐮𝐦𝐛𝐞𝐫 (𝐢𝐝).
𝐄𝐚𝐜𝐡 𝐭𝐫𝐚𝐯𝐞𝐥 𝐜𝐨𝐬𝐭𝐬 𝐨𝐧𝐞 𝐛𝐨𝐭𝐭𝐥𝐞 𝐨𝐟 𝐯𝐨𝐝𝐤𝐚. 𝐘𝐨𝐮 𝐡𝐚𝐯𝐞 𝐥𝐢𝐦𝐢𝐭𝐞𝐝 𝐚𝐦𝐨𝐮𝐧𝐭 𝐨𝐟 𝐯𝐨𝐝𝐤𝐚.
𝐃𝐮𝐫𝐢𝐧𝐠 𝐲𝐨𝐮𝐫 𝐭𝐫𝐚𝐯𝐞𝐥 𝐛𝐞𝐭𝐰𝐞𝐞𝐧 𝐬𝐭𝐚𝐭𝐢𝐨𝐧𝐬, 𝐭𝐡𝐞𝐫𝐞 𝐢𝐬 𝐚 𝐜𝐡𝐚𝐧𝐜𝐞 𝐬𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠 𝐰𝐢𝐥𝐥 𝐡𝐚𝐩𝐩𝐞𝐧.
𝐈𝐧 𝐭𝐡𝐨𝐬𝐞 𝐞𝐯𝐞𝐧𝐭𝐬, 𝐲𝐨𝐮 𝐜𝐚𝐧 𝐞𝐢𝐭𝐡𝐞𝐫 𝐞𝐚𝐫𝐧 𝐨𝐫 𝐥𝐨𝐬𝐞 𝐯𝐨𝐝𝐤𝐚 𝐛𝐨𝐭𝐭𝐥𝐞𝐬.
''')
        input("Press enter to continue")
    elif option == "story":
        screen_refresh()
        print(f'''𝐘𝐨𝐮'𝐫𝐞 𝐭𝐡𝐞 𝐩𝐚𝐫𝐥𝐢𝐚𝐦𝐞𝐧𝐭𝐚𝐫𝐢𝐚𝐧 𝐰𝐡𝐨 𝐬𝐭𝐨𝐥𝐞 𝐦𝐨𝐧𝐞𝐲 𝐟𝐫𝐨𝐦 𝐚 𝐠𝐨𝐯𝐞𝐫𝐧𝐦𝐞𝐧𝐭 𝐜𝐨𝐧𝐭𝐫𝐚𝐜𝐭 𝐚𝐧𝐝 𝐠𝐨𝐭 𝐜𝐚𝐮𝐠𝐡𝐭. 
𝐓𝐡𝐞 𝐏𝐫𝐞𝐬𝐢𝐝𝐞𝐧𝐭 𝐡𝐚𝐬 𝐝𝐞𝐜𝐥𝐚𝐫𝐞𝐝 𝐲𝐨𝐮 𝐚𝐬 𝐚𝐧 𝐞𝐧𝐞𝐦𝐲 𝐨𝐟 𝐭𝐡𝐞 𝐩𝐞𝐨𝐩𝐥𝐞. 𝐓𝐡𝐞 𝐰𝐡𝐨𝐥𝐞 𝐜𝐨𝐮𝐧𝐭𝐫𝐲 𝐢𝐬 𝐥𝐨𝐨𝐤𝐢𝐧𝐠 𝐟𝐨𝐫 𝐲𝐨𝐮. 𝐘𝐨𝐮 𝐦𝐮𝐬𝐭 
𝐭𝐨 𝐡𝐢𝐝𝐞 𝐥𝐢𝐤𝐞 𝐚 𝐛𝐮𝐦. 𝐀𝐬 𝐬𝐨𝐨𝐧 𝐚𝐬 𝐲𝐨𝐮 𝐬𝐨𝐛𝐞𝐫 𝐮𝐩, 𝐭𝐡𝐞 𝐛𝐮𝐦𝐬 𝐰𝐢𝐥𝐥 𝐤𝐢𝐜𝐤 𝐲𝐨𝐮 𝐨𝐮𝐭 𝐨𝐟 𝐭𝐡𝐞𝐢𝐫 𝐩𝐚𝐫𝐭𝐲. 
𝐘𝐨𝐮 𝐡𝐚𝐝 𝐚 𝐬𝐩𝐚𝐫𝐞 𝐩𝐥𝐚𝐧𝐞, 𝐛𝐮𝐭 𝐲𝐨𝐮 𝐝𝐨𝐧'𝐭 𝐫𝐞𝐦𝐞𝐦𝐛𝐞𝐫 𝐰𝐡𝐞𝐫𝐞 𝐲𝐨𝐮 𝐥𝐞𝐟𝐭 𝐢𝐭.
''')
        input("Press enter to continue")
    elif option == "gameover":
        print(f"::::::::::::::::::::::\nTHE TRAIN RAN OVER YOU\n::::::::::::::::::::::\n\n")
        input("Press enter to continue")
    elif option == "chuh-chuh":
        print("... ... ... ... ... ... ... ...\n      Chuh-Chuh Chuh-Chuh\n... ... ... ... ... ... ... ...\n\n\n\n")
    elif option == "map":
        print("""
        Murmansk												                            Nizhny Bestyakh	     Sovetskaya Gavan
	     |													            		    	 	        |                 |
Belomorsk - Arkhangelsk 	Pechora---Vorkuta----Salekhard								           Tommot	Urgal---Komsomolsk-on-Amur
	|	     |	     		|							                                                 |   /         /          
	|	Konosha - Kotlas----|					Nadym---Novy Urengoy				      Nizhneangarsk---Tynda  	  /+Khabarovsk--Vladivostok
	|	| 						                            |  			   	   	                          |   |    Birobidzhan    
	|	Vologda - Yaroslavl - Kirov--------Perm	            Surgut-------Nizhnevartovsk	  Ust-Ilimsk      |   |   /
	|	|    	  |		|	   |		      |			     	 |	                              |       |   Never----
 Saint Petersburg - Moscow--"Nizhny Novgorod" Yekaterinburg------Tyumen		Lesosibirsk    Bratsk-+-Ust-Kut           |
                     |  |     | |		 	  /	 |      		   |		       |			  |                 /Chita
Smolensk-------------/	|-----/ |		 	 /   |---Kurgan--Omsk-----Novosibirsk--+--Krasnoyarsk-+--Irkutsk---Ulan-Ude
	         | 			|	 	|	        |	 |			   |			                     /
Bryanks------/	   /----+-------+-------Kazan	Chelyabinsk    ---Barbaul---Abakan--------------/
  |      /         |            |		 |			     |           |
Oryol--------Voronezh---------Saratov---Samara-----Ufa---+-----------/
		        |			  |	   	 |                  /
		        |------Volgograd	Orenburg    /------/
	    Rostov-on-Don          |	     	|  /	
		        |	      Astrakhan---------Orsk
Novorossiysk---Krasnodar
        """)


def menu():
    chosen = 0
    while chosen != "1":
        print_text("menu")
        chosen = input("Choose: ")
        if chosen == "2":
            print_text("story")
        elif chosen == "3":
            print_text("manual")
        elif chosen == "4":
            print('\nДо свидания! Goodbye!\n')
            sys.exit()


def difficulty():
    chosen = True
    while chosen:
        print("Choose your difficulty: 1, 2 or 3.")
        print("1. младенец (15 vodkas)")
        print("2. подросток (10 vodkas)")
        print("3. мужчина (5 vodkas)")

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
            print("сука блять! Please try again.")
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

    for i, event_id in enumerate(events_list):
        sql = f"INSERT INTO events_location (game, station, event)" \
              f" VALUES ({g_id}, '{t_stations[i]['StationName']}', {event_id});"
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql)

    return g_id


def create_game():
    vodka_balance = difficulty()
    screen_name = str(input("Choose your name: "))
    print('\n\n... Loading ...\n\n')
    if screen_name == 'Putin':
        vodka_balance = 100000

    all_stations = get_stations()
    current_station = all_stations[0]['StationID']
    game_id = start(vodka_balance, current_station, screen_name, all_stations)

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

def get_airplane(game_id):
    sql = f"SELECT station FROM events_location WHERE event = 1 AND game = {game_id}"
    cursor = connection.cursor()
    cursor.execute(sql)
    airplane_stationname = cursor.fetchone()
    return airplane_stationname[0]


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
    menu()
    while True:
        screen_refresh()

        ##################### Start #########################

        current_station, game_id = create_game()
        airplane_location = get_airplane(game_id)
        while True:
            screen_refresh()
            moveto(current_station)
            update_balance(-1, game_id)




            ################### STATION MENU ################

            station_name = get_current_station_name(current_station)
            if airplane_location == station_name[0]:
                print("YOU WON!")
                input("...")
                menu()
            balance = get_balance(game_id)
            if balance < 0:
                print_text("gameover")
                break
            print_text("map")
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
            print(f"\nYour balance is {balance} bottles of vodka.")
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

        menu()


main()
