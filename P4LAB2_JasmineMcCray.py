# Jasmine McCray
# October 27, 2026
# P4LAB2
# This program will use while loop and for loops

# Get integer from user
run_again = "yes"
while run_again != "no":

    user_num = int(input("Enter an integer: "))
    if user_num >= 0:

        # display multiplication for what value and range (1-12)
        for item in range (1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("No negative numbers allowed")

 #If user enters no
    run_again = input("Would you like to run again? (yes/no): ")

#Response if user enters no
print("Exiting program...")