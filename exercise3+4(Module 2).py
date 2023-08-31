#Exercise 3.1:

zanderLength = int(input("What is the length of a zander in centimeters?\n"))
requiredLength = 42

if (zanderLength < requiredLength):
    zanderDif = requiredLength-zanderLength
    print(f"Please put release the fish back into the lake. The fish you caught is {zanderDif} centimeter(s) below the size limit.\n")

#Exercise 3.2:
cabinClass = input("Please enter the cabin class\n")

if (cabinClass == "LUX"):
    print("upper-deck cabin with a balcony.\n")
elif(cabinClass == "A"):
    print("above the car deck, equipped with a window.\n")
elif(cabinClass == "B"):
    print("windowless cabin above the car deck.\n")
elif(cabinClass == "C"):
    print("windowless cabin below the car deck.\n")
else:
    print("Invalid cabin class\n")

#Exercise 3.3:
gender = input("What is your gender (male or female)?\n")
hemoglobinValue = float(input("What is your hemoglobin value?\n"))

if((gender == "male" and hemoglobinValue > 167) or (gender == "female" and hemoglobinValue > 155)):
    print("Your hemoglobin value is high.\n")
elif((gender =="male" and hemoglobinValue >= 134) or (gender == "female" and hemoglobinValue > 117)):
    print("Your hemoglobin value is in the normal range.\n")
else:
    print("Your hemoglobin value is low.\n")

#Exercise 3.4:
year = int(input("Enter a year:\n"))

if(year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
    print("The year you inserted is not a leap year.\n")
else:
    print("The year you inserted is a leap year.\n")

#Exercise 4.1:
numbers = 1
while (numbers<=1000):
    if (numbers % 3 == 0):
        print(numbers)
    numbers = numbers + 1

#Exercise 4.2:
value = float(input("Please insert a number in inch(es): \n"))
while(value >= 0):
    print(f"{value} inch(es) is equal to {value*2.54} cm(s)\n")
    value = float(input("Please insert a number in inch(es): \n"))

#Exercise 4.3:
insertNumber = input("Please enter a number. Enter empty sting to quit.")
smallestNumber = largestNumber = insertNumber

while(insertNumber!= str()):
    if (float(smallestNumber) > float(insertNumber)):
        smallestNumber = insertNumber
    if(float(largestNumber) < float(insertNumber)):
        largestNumber = insertNumber
    insertNumber = input("Please enter a number. Enter empty sting to quit.")

if(smallestNumber != str()):
    print(f"The smallest number you inserted was {smallestNumber} and the largest number you inserted was {largestNumber}.\n")

#Exercise 4.4:
import random
randomNumber = random.randint(1,10)
userGuess = int(input("Take a guess of what is the random number between 1-10: \n"))

while(userGuess != randomNumber):
    if(userGuess > randomNumber):
        print("Too high.\n")
    else:
        print("Too low.\n")
    userGuess = int(input("Take another guess: \n"))

print("Correct!\n")

#Exercise 4.5
correctUserName = "python"
correctPassword = "rules"

username = input("Please enter your username: ")
password = input("Please enter your password: ")
count = 0

while((username != correctUserName or password != correctPassword)):
    count= count + 1
    if(count>=5):
        print("Access denied.")
        break
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
else:
    print("Login information is correct. Successful login.\n")

#Exercise 4.6
import random
totalRandomPoints = int(input("How many random points to generate? "))
pointsCounted = 0
numbersInCircle = 0

while(pointsCounted < totalRandomPoints):
    randomX = random.uniform(-1,1)
    randomY = random.uniform(-1,1)
    if(randomX ** 2 + randomY ** 2 < 1):
        numbersInCircle = numbersInCircle + 1
    pointsCounted = pointsCounted + 1

print(f"The approximation of the value pi is: {4*numbersInCircle/pointsCounted}.")