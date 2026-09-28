# Jasmine McCray
# September 28, 2026
# P1HW2_McCrayJasmine.py
# This program will calculate travel expenses for a trip

#----- Get user input -----
Budget = float(input("Enter your budget for the trip: "))
Travel_destination = input("Enter your travel destination: ")

#----- Get estimated expenses -----
gas = float(input("How much will you spend on gas? "))
hotel = float(input("How much will you spend on hotel accommodations? "))
food = float(input("How much will you spend on food? "))

#----- Calculate remaining balance -----
remaining_balance = Budget - (gas + hotel + food)


#----- Display results -----
print ("--------Trip finance Summary--------")
print()
print(f"Location: {Travel_destination}")
print(f"Budget: ${Budget:.2f}")
print(f"Fuel: ${gas:.2f}")
print(f"Hotel: ${hotel:.2f}")
print(f"Food: ${food:.2f}")
print()
print("--------------------------------------------")

print(f"Remaining Balance: ${remaining_balance:.2f}")