import random
import mysql.connector
import time

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


def moveto(station):
    sql = f"UPDATE Game SET Location = '{station}' "
    cursor = connection.cursor()
    cursor.execute(sql)
    return


def screen_refresh():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    return


def slowprint(text, speed):
    for char in text:
        print(char, end='', flush=True)  # Print a character without a newline
        time.sleep(speed)
    return


def updatebalance(balance, amount):
    sql = f"UPDATE `efr_test`.`game` SET `Balance`={int(balance)+amount}"
    cursor = connection.cursor()
    cursor.execute(sql)
    return


def getbalance():
    sql = "SELECT balance FROM game"
    cursor = connection.cursor()
    cursor.execute(sql)
    balance = cursor.fetchone()
    return balance[0]


def main():


    chosed = 0
    while chosed != "3":
        cleartable()
        screen_refresh()
        print("""\n::::::::::::::::::
ESCAPE FROM RUSSIA\n
1) Start the game
2) Read manual
3) Exit\n""")
        chosed = input("Choose: ")
        #time.sleep(1)
        if chosed == "2":
            screen_refresh()
            print("\nWhen you are at station, you can move only to stations next to the current station.\n\
Each travel costs one bottle of vodka. You have limited amount of vodka. \n\
Your goal is to find an airplane, that is hidden in a random city.\n\
During your travel between stations, there is a chance something will happen.\n\
In those events, you can either earn get or lose vodka bottles. \n")
            input("Press enter to continue")

        elif chosed == "1":
            screen_refresh()
            screen_name = str(input("Choose your name: "))
            vodka_balance = 3
            all_stations = get_stations()
            current_station = all_stations[0]['StationID']
            game_id = start(vodka_balance, current_station, screen_name, all_stations)
            chosed = current_station
            while chosed != "":
                screen_refresh()
                moveto(chosed)
                balance = getbalance()
                updatebalance(balance,-1)
                balance = getbalance()
                if balance < 1:
                    print(f"::::::::::::::::::::::\nTHE TRAIN RAN OVER YOU\n::::::::::::::::::::::\n\n")
                    input("Press enter to continue")
                    break
                current_station = chosed
                screen_refresh()
                print("... ... ... ... ... ... ... ...\n      Chuh-Chuh Chuh-Chuh\n... ... ... ... ... ... ... ...")
                print("\n\n\n\n")
                screen_refresh()
                stationname = getcurrentstationname(current_station)
                stationid = getstationid(stationname[0])
                neighbors = getneighbors(stationid[0])
                print(f"\n{screen_name}, arriving at {stationname[0]}\n" \
                       f"Your balance is {balance} bottles of vodka.")
                print("Connected stations:\n...")
                for station in neighbors:
                    print(f"{station[0]} (ID: {station[1]})")
                print("...")
                chosed = input("Where to: ")


main()

