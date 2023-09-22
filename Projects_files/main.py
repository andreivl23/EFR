import random
import mysql.connector

connection = mysql.connector.connect(
         host='172.232.129.9',
         port= 3306,
         database='escaperussia_test',
         user='escapee',
         password='123456789',
         autocommit=True
         )

def getcurrentstationname(GameID):
    sql = f"SELECT StationName FROM Stations, Game WHERE StationID = Location AND GameID ='{GameID}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def getstationid(StationName):
    sql = f"SELECT StationID from Stations WHERE StationName = '{StationName}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    neighbor = cursor.fetchall()
    return neighbor

def start(GameID, ScreenName, Balance):
    Location = str(random.randint(1,61))
    #print(ScreenName,Location,Balance)
    sql = "INSERT INTO Game (GameID, ScreenName, Location, Balance) VALUES ("
    sql += f"{GameID},'{ScreenName}'," + f"{Location}," + f"'{Balance}')"
    cursor = connection.cursor()
    cursor.execute(sql)
    return Location


def getneighbors(Location):
    sql = f"SELECT StationName, StationID from Stations, Connections WHERE StationID2 = StationID AND StationID1 = '{Location}'"
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
    GameID = random.randint(1, 999999)
    ScreenName = input("Choose your name: ")
    Balance = str(random.randint(20, 100))
    Location = start(GameID, ScreenName, Balance)
    chosed = 0

    while chosed != "stop":
        StationName = getcurrentstationname(GameID)
        StationID = getstationid(StationName[0][0])
        neighbors = getneighbors(StationID[0][0])
        print(f"...\n{ScreenName}, you are at station {StationName[0][0]}\nYour balance is {Balance} rubles")
        print("Connected stations: ")
        for station in neighbors:
            print(f"{station[0]} (ID: {station[1]})")

            #StationID = station[1]
            #options = []
            #options.append(StationID)

        chosed = input("Where to?: ")
        moveto(chosed)
        #StationName = getcurrentstationname(GameID)
        #print(StationName[0][0])
main()
cleartable()