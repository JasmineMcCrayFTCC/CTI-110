#Jasmine McCray
#9/28/2026
#P2LAB2
#This program will create a dictionary where the key and value pairs as follows:

cars = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}

#Get keys from dict
cars_keys = cars.keys()

print(cars_keys)

print(*cars_keys, sep = ", ")

#Get car from user
car_name = input("What car would you like to look up? ")

#Get mpg for given car
car_mpg = cars[car_name]

print(f"The {car_name} gets {car_mpg} miles per gallon.")

#Get miles from user
miles_driven = float(input(f"How many miles will you be driving your {car_name}? "))

#Calculate
gallons_needed = miles_driven / car_mpg

#Display results
print(f"You will need {gallons_needed} gallon(s) of gas to drive your {car_name} {miles_driven} miles.")