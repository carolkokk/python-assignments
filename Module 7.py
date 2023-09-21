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


