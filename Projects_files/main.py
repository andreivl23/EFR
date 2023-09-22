import random
import mysql.connector

connection = mysql.connector.connect(
         host='172.232.129.9',
         port=3306,
         database='escaperussia_test',
         user='escapee',
         password='123456789',
         autocommit=True
         )


def getcurrentstationname(gameid):
    sql = f"SELECT StationName FROM Stations, Game WHERE StationID = Location AND GameID ='{gameid}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def getstationid(stationname):
    sql = f"SELECT StationID from Stations WHERE StationName = '{stationname}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    neighbor = cursor.fetchall()
    return neighbor


def start(gameid, screenname, balance):
    location = str(random.randint(1, 61))
    # print(screenname,Location,balance)
    sql = "INSERT INTO Game (GameID, ScreenName, Location, Balance) VALUES ("
    sql += f"{gameid},'{screenname}'," + f"{location}," + f"'{balance}')"
    cursor = connection.cursor()
    cursor.execute(sql)
    return location


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
    gameid = random.randint(1, 999999)
    screenname = input("Choose your name: ")
    balance = str(random.randint(20, 100))
    location = start(gameid, screenname, balance)
    chosed = location

    while chosed != "stop":
        moveto(chosed)

        stationname = getcurrentstationname(gameid)
        stationid = getstationid(stationname[0][0])
        neighbors = getneighbors(stationid[0][0])

        print(f"...\n{screenname}, you are at station {stationname[0][0]}\nYour balance is {balance} rubles")
        print("Connected stations: ")
        for station in neighbors:
            print(f"{station[0]} (ID: {station[1]})")

        chosed = input("Where to?: ")


main()
cleartable()
