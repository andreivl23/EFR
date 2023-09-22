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

def getcurrentstationname(id):
    sql = "SELECT StationName FROM Stations, Game WHERE StationID = Location AND Game.location ='" + id + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def getstationname(i):
    sql = f"SELECT StationName from Stations WHERE StationID = '{i}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    neighbor = cursor.fetchall()
    return neighbor


def start(ScreenName, Balance):
    id = str(random.randint(1,3))
    #print(ScreenName,id,Balance)
    sql = "INSERT INTO Game (ScreenName, Location, Balance) VALUES ("
    sql += f"'{ScreenName}'," + f"{id}," + f"'{Balance}')"
    cursor = connection.cursor()
    cursor.execute(sql)

    return id


def getneighbors(id):
    sql = f"SELECT StationName from Stations, Connections WHERE StationID2 = StationID AND StationID1 = '{id}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    neighborsID = cursor.fetchall()
    return neighborsID

def getcoordinates(station):
    sql = "SELECT latitude, longitude FROM Stations"
    sql += " WHERE StationID='" + station + "'" +" OR StationName ='" + station + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def cleartable():
    sql = "DELETE FROM Game"
    cursor = connection.cursor()
    cursor.execute(sql)
    return
def main():
    ScreenName = input("Choose your name: ")
    Balance = str(random.randint(20,100))
    id = start(ScreenName, Balance)
    StationName = getcurrentstationname(id)
    neighbors = getneighbors(id)
    print(f"{ScreenName}, you are at station {StationName[0][0]}\nYour balance is {Balance} rubles")
    for station in neighbors:
        print(f"You can travel to {station[0]}")

main()
cleartable()