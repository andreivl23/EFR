import random
import mysql.connector
import time
import sys

connection = mysql.connector.connect(
         host='172.232.129.9',
         port=3306,
         database='efr_test',
         user='root',
         password='123321',
         autocommit=True
         )


def get_stations():
    sql = """SELECT StationID, StationName
    FROM stations
    ORDER by RAND()"""
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def getcurrentstationname(gameid):
    sql = f"SELECT StationName FROM Stations WHERE StationID = {gameid}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result


def getstationid(stationname):
    sql = f"SELECT StationID from Stations WHERE StationName = '{stationname}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    neighbor = cursor.fetchone()
    return neighbor


def get_goals():
    sql = "SELECT * FROM goal;"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def start(resource, current_station, player, stations):
    sql = f"INSERT INTO game (ScreenName, Location, Balance) VALUES ('{player}', '{current_station}', {resource});"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    g_id = cursor.lastrowid

    goals = get_goals()
    goal_list = []
    for goal in goals:
        for i in range(0, goal['probability'], 1):
            goal_list.append(goal['id'])

    t_stations = stations[1:].copy()
    random.shuffle(t_stations)

    for i, goal_id in enumerate(goal_list):
        sql = f"INSERT INTO ports (game, station, goal) VALUES ({g_id}, '{t_stations[i]['StationName']}', {goal_id});"
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql)

    return g_id


def getneighbors(stationid):
    sql = f"SELECT StationName, StationID from Stations, Connections WHERE StationID2 = StationID AND StationID1 = '"
    sql += f"{stationid}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    neighborsname = cursor.fetchall()
    return neighborsname


def cleartable():
    sql = "DELETE FROM Game"
    cursor = connection.cursor()
    cursor.execute(sql)
    return


def screen_refresh():
    print("\n"*30)
    return


def slowprint(text, speed):
    for char in text:
        print(char, end='', flush=True)  # Print a character without a newline
        time.sleep(speed)
    return


def updatebalance(amount, game_id):
    sql = f"UPDATE game SET Balance = Balance+({amount}) WHERE GameID = '{game_id}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    return


def getbalance(game_id):
    sql = f"SELECT balance FROM game WHERE GameID = '{game_id}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    balance = cursor.fetchone()
    return balance[0]


def moveto(station,game_id):
    updatebalance(-1, game_id)
    sql = f"UPDATE Game SET Location = '{station}' "
    cursor = connection.cursor()
    cursor.execute(sql)
    return

def menu():
    chosed = 0
    while chosed != "1":
        cleartable()
        printtext("menu")
        chosed = input("Choose: ")
        if chosed == "2":
            printtext("story")
        elif chosed == "3":
            printtext("manual")
        elif chosed == "4":
            print('\nWelcome again!!!\n')
            sys.exit()
    main()

def main():

    ##################### Start #########################

    screen_refresh()
    screen_name = str(input("Choose your name: "))
    print('\n\n... Loading ...\n\n')

    ###################### Sys ##########################

    vodka_balance = 3
    all_stations = get_stations()
    current_station = all_stations[0]['StationID']
    game_id = start(vodka_balance, current_station, screen_name, all_stations)
    chosed = current_station

    while chosed != "x":
        screen_refresh()
        moveto(chosed,game_id)                               # смена локации

        balance = getbalance(game_id)
        if balance < 1:
            printtext("gameover")
            break

        ################ to work with ###########

        current_station = chosed
        stationname = getcurrentstationname(current_station) # надо объединять
        stationid = getstationid(stationname[0])
        neighbors = getneighbors(stationid[0]) # соседние станции

        ################### STATION MENU ################

        print(f"\n{screen_name}, arriving at {stationname[0]}\n" \
               f"Your balance is {balance} bottles of vodka.")
        print("Connected stations:\n...")
        for station in neighbors:
            print(f"{station[0]} (ID: {station[1]})")
        print("...")
        chosed = input("Where to: ")

    menu()

def printtext(option):
    if option == "menu":
        screen_refresh()
        print("""\n::::::::::::::::::
ESCAPE FROM RUSSIA\n
1) Start the game
2) Game story
3) Read manual 
4) Exit\n""")

    elif option == "manual":
        screen_refresh()
        print("\nWhen you are at station, you can move only to stations next to the current station.\n\
Each travel costs one bottle of vodka. You have limited amount of vodka. \n\
Your goal is to find an airplane, that is hidden in a random city.\n\
During your travel between stations, there is a chance something will happen.\n\
In those events, you can either earn get or lose vodka bottles. \n")
        input("Press enter to continue")
    elif option == "story":
        screen_refresh()
        print(f'''Olet kansanedustaja, joka varasti rahaa hallituksen sopimuksesta ja jäi kiinni. 
Presidentti on julistanut sinut kansan viholliseksi. Koko maa etsii sinua. Sinun on pakko 
piiloutua pummiksi. Heti kun raitistut, pummit potkaisevat sinut ulos puolueestaan. 
Sinulla oli varakone, mutta et muista, mihin jätit sen.
''')
        input("Press enter to continue")
    elif option == "gameover":
        print(f"::::::::::::::::::::::\nTHE TRAIN RAN OVER YOU\n::::::::::::::::::::::\n\n")
        input("Press enter to continue")
    elif option == "chuh-chuh":
        print("... ... ... ... ... ... ... ...\n      Chuh-Chuh Chuh-Chuh\n... ... ... ... ... ... ... ...\n\n\n\n")

menu()

