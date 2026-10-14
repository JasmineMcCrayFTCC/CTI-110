# Jasmine McCray
# P3HW2
# October 14, 2026
# This program calculates salary

# Get employee info from user
name = input("Enter employee name: ")
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

# Get overtime infor
if hours > 40:
    #Calculate overtime
    overtime_hours = hours - 40
    #Calculate over pay
    overtime_pay = overtime_hours * (rate * 1.5)
    #Calculate regular pay
    regular_pay = 40 * rate
    #Calculate total pay
    total_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    regular_pay = hours * rate
    total_pay = hours * rate

# Display results
print("-------------------------------")
print("Employee Name:", name)
print("Hours Worked:", hours)
print(f'{"Hours worked":<15}{"Rate":<12}{"Overtime pay":<15}{"Regular pay":<12}{"Total pay":<12}')
print("-----------------------------------------------")
print(f'{hours:<15}{rate:<12.2f}{overtime_pay:<15.2f}{regular_pay:<12.2f}{total_pay:<12.2f}')