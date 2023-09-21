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

