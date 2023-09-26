import random
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='',
         user='',
         password='',
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


def main():
    game_on = True

    screen_name = str(input("Choose your name: "))
    vodka_balance = 10
    all_stations = get_stations()
    current_station = all_stations[0]['StationID']

    game_id = start(vodka_balance, current_station, screen_name, all_stations)

    while game_on:

        stationname = getcurrentstationname(current_station)
        stationid = getstationid(stationname[0])
        neighbors = getneighbors(stationid[0])

        print(f"...\n{screen_name}, you are at station {stationname[0]}\n"
              f"Your balance is {vodka_balance} bottles of vodka.")
        print("Connected stations: ")
        for station in neighbors:
            print(f"{station[0]} (ID: {station[1]})")

        chosed = input("Where to?: ")
        moveto(chosed)
        current_station = chosed


main()
cleartable()