#Jasmine McCray
#October 27, 2026
#P4HW2
#This program will use loops for salary calculations

# Get employee info from user
name = input("Enter employee name or done to exit: ")

# Calculate pays
overtime_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while name != "done":
    # Add employee count plus one
    employee_count += 1
    #Get employee info
    hours = float(input("How many hours did " + name + " work? "))
    rate = float(input("What is "+ name + "'s hourly rate? "))

    # Evaluate overtime
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours * rate
        gross_pay = regular_pay 


    # Accumulator variables
    overtime_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay

    # Display results
    print("------------------------")
    print("Employee Name: " + name)
    print(f'{"hours worked":<15}{"Pay Rate":<12}{"Overtime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<15}')
    print("------------------------")
    print(f'{hours:<15}{rate:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<15}')


    # Get next employee name
    name = input("Enter employee name or done to exit: ")

 # Display totals
print("Total numbers of employees: " , employee_count)
print("Total amount of overtime pay: $" + format(overtime_total, ",.2f"))
print("Total amount of regular pay: $" + format(regularpay_total, ",.2f"))
print("Total amount of gross pay: $" + format(grosspay_total, ",.2f"))

    