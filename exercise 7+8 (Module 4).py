#Exercise 7.1:
spring = (3,4,5)
summer = (6,7,8)
autumn = (9,10,11)
winter = (12,1,2)

month = int(input("Insert a month 1-12 to be converted to season: "))

if month in spring:
    print("Spring")
elif month in summer:
    print("Summer")
elif month in autumn:
    print("Autumn")
elif month in winter:
    print("Winter")
else:
    print("Invalid number")

#Exercise 7.2:
names = set()
newName = True
inputName = input("Enter a name or quit by entering an empty string: ")

while (inputName != ""):
    for name in names:
        if(inputName == name):
            newName = False
    if(newName == True):
        names.add(inputName)
        print("New Name")
    else:
        print("Existing Name")
    inputName = input("Enter a name or quit by entering an empty string: ")

for name in names:
    print(name)

#Exercise 7.3:
userChoice = int(input("Do you want to 1.enter a new airport, 2. fetch the information of an existing airport or 3. quit? Answer by 1/2/3: "))
airportData = {}

while (userChoice != 3):
    if (userChoice == 1):
        iCAO = input("Enter the ICAO code: ")
        airport = input("Enter the airport name: ")
        airportData[iCAO] = airport
    elif(userChoice == 2):
        fetchICAO = input("What is the ICAO code of the airport? ")
        if(fetchICAO in airportData):
            print(airportData[fetchICAO])
        else:
            print("ICAO code not found.")
    else:
        print("Insert a valid number! ")
    userChoice =  int(input("Do you want to 1.enter a new airport, 2. fetch the information of an existing airport or 3. quit? Answer by 1/2/3: "))

#Exercise 8.1:
import mysql.connector

connection = mysql.connector.connect(
    host= '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '0528',
    autocommit = True
)

def airportNameAndLocation(inputCode):
    sql = "SELECT Name, Municipality fROM Airport WHERE ident = '"+ inputCode +"'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The airport name is {row[0]} and it is located in {row[1]}")
    else:
        print("Invalid ICAO code")
    return

inputICAO = input("Please enter the ICAO of the airport")
airportNameAndLocation(inputICAO)

#Exercise 8.2:
import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '0528',
    autocommit = True
)

def allAirportsInACountry(selectedCountry):
    closedAirport = 0
    heliport = 0
    largeAirport = 0
    mediumAirport = 0
    smallAirport = 0
    country = ""

    sql = "SELECT AIRPORT.TYPE, COUNTRY.NAME FROM AIRPORT,COUNTRY WHERE AIRPORT.ISO_COUNTRY = COUNTRY.ISO_COUNTRY AND AIRPORT.ISO_COUNTRY = '"+selectedCountry+"' ORDER BY TYPE ASC"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if (cursor.rowcount > 0):
        for row in result:
            country = row[1]
            if(row[0]=="closed"):
                closedAirport = closedAirport + 1
            elif(row[0]=="heliport"):
                heliport = heliport +1
            elif(row[0]=="large_airport"):
                largeAirport = largeAirport +1
            elif(row[0]=="medium_airport"):
                mediumAirport = mediumAirport +1
            else:
                smallAirport = smallAirport +1
        print(f"{row[1]} has {closedAirport} closed airports, {heliport} heliports, {largeAirport} large airports, {mediumAirport} medium airports, and {smallAirport} small airports.")
    else:
        print("Invalid country code")


enteredAreaCode = input("Enter the area code: ")
allAirportsInACountry(enteredAreaCode)

#Exercise 8.3:
import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '0528',
    autocommit = True
)
def latitudeLongitudeInfo(code):
    sql = "SELECT Latitude_deg, Longitude_deg FROM AIRPORT WHERE ident = '"+code+"'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if (cursor.rowcount > 0):
        for row in result:
            locationInformation = (row[0],row[1])
        return locationInformation
    else:
        print("Invalid country code")

first = input("Enter the first ICAO code:")
second = input("Enter the second ICAO code: ")
firstLocation = latitudeLongitudeInfo(first)
secondLocation = latitudeLongitudeInfo(second)
distanceOfAirports = distance.distance(firstLocation,secondLocation).km
print(f"The distance of two airports is: {distanceOfAirports:.2f}km.")
