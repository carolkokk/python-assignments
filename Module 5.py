# Exercise 5.1
import random
times = int(input("How many dices to roll?"))
diceNumbers = []
sum = 0

for i in range(0,times):
    randomNumber = random.randint(1,6)
    diceNumbers.append(randomNumber)
    sum = sum + randomNumber

print(sum)

#Exercise 5.2
number = input("Enter the first number, put empty string to quit.")
numbers = []

while (number != ""):
    numbers.append(int(number))
    number = input("Enter the next number, put empty string to quit.")

numbers.sort(reverse=True)

for i in range(0,5):
    print(numbers[i])

# Exercise 5.3
number = int(input("Type in a positive integer: \n"))
primeInteger = True

for i in range(2,number):
    if(number % i == 0):
        primeInteger = False

if(primeInteger == True):
    print("The number is a prime number.")
else:
    print("The number is not a prime number.")

#Exercise 5.4
cityNames = []
name = input("Enter the names of five cities one by one:")
cityNames.append(name)

for n in range(0,4):
    name = input()
    cityNames.append(name)
    n= n+1

for i in range(0,5):
    print(cityNames[i])

