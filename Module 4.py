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
