# Jasmine McCray
# September 11, 2026
# P1HW2_McCrayJasmine.py
# This program will calculate travel expenses for a trip

# Get budget and destination from user
Budget = float(input("Enter your budget for the trip: "))
Travel_destination = input("Enter your travel destination: ")

#Get estimated expenses 
gas = float(input("How much will you spend on gas? "))
hotel = float(input("How much will you spend on hotel accommodations? "))
food = float(input("How much will you spend on food? "))

# Calculate remaining balance

remaining_balance = Budget - (gas + hotel + food)


# Display results
print ("--------Trip finance Summary--------")
print()
print("Location:", Travel_destination)
print("Budget:" + str(Budget))
print() 
print("Fuel: $" + str(gas))
print("Hotel: $" + str(hotel))
print("Food: $" + str(food))
print()
print("Remaining Balance: $", remaining_balance)