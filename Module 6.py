#Exercise 6.1
import random
diceNumber1 = 0
def randomDiceRoll1():
    randomResult1 = random.randint(1,6)
    return randomResult1

while (diceNumber1!= 6):
    diceNumber1 = randomDiceRoll1()
    print(diceNumber1)

#Exercise 6.2
import random
maximumDiceSides = int(input("what is the number of sides on the dice do you want to have? "))
diceNumber2 = 0
def randomDiceRoll2(diceSides):
    randomResult2 = random.randint(1,diceSides)
    return randomResult2

while (diceNumber2!= maximumDiceSides):
    diceNumber2 = randomDiceRoll2(maximumDiceSides)
    print(diceNumber2)

#Exercise 6.3
inputGallon = float(input("What is the volume of American gallon that you want to convert? Stop by putting a negative value: \n"))
def usGallonToLiter (input):
    result = input * 3.785
    return result

while(inputGallon >= 0):
    print(f"{inputGallon} American gallon(s) are {usGallonToLiter(inputGallon):.2f} liter(s).")
    inputGallon = float(input("What is the volume of American gallon that you want to convert? Stop by putting a negative value: \n"))

#Exercise 6.4
def sumOfNumbers1(integerNumbers):
    sum1 = 0
    for integerNumber1 in integerNumbers:
        sum1 = sum1 + integerNumber1
    return sum1

list1 = [6,5,4,8,9,7,3]
print(sumOfNumbers1(list1))

#Exercise 6.5
def newListCreated (integerNumbers2):
    newList = []
    for integerNumber2 in integerNumbers2:
        if(integerNumber2 % 2 == 0 and integerNumber2 != 0):
            newList.append(integerNumber2)
    return newList

list2 = [0,6,5,4,8,9,7,3]
print(list2)
print(newListCreated(list2))

#Exercise 6.6
import math
diameterOfPizza1 = float(input("Insert the diameter of the first pizza: \n"))
priceOfPizza1 = float(input("Insert the price of the first pizza: \n"))
diameterOfPizza2 = float(input("Insert the diameter of the second pizza: \n"))
priceOfPizza2 = float(input("Insert the price of the second pizza: \n"))

def avePrice (diameterOfPizza,priceOfPizza):
    result = priceOfPizza/ math.pi * (diameterOfPizza/2)**2
    return result
pizza1Ave = avePrice(diameterOfPizza1,priceOfPizza1)
pizza2Ave = avePrice(diameterOfPizza2,priceOfPizza2)

if(pizza1Ave > pizza2Ave):
    print("The first pizza provides better value for money.")
if(pizza2Ave > pizza1Ave):
    print("The second pizza provides better value for money.")
else:
    print("They have the same value for money.")
