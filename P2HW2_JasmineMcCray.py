#Jasmine McCray
#9/28/2026
#P2HW2
#This program will calculate and manage test grades

# Get module grade from user
module_grade = float(input("Enter your module 1 grade: "))
module_grade2 = float(input("Enter your module 2 grade: "))
module_grade3 = float(input("Enter your module 3 grade: "))
module_grade4 = float(input("Enter your module 4 grade: "))
module_grade5 = float(input("Enter your module 5 grade: "))
module_grade6 = float(input("Enter your module 6 grade: "))

# Put grades into a list
module_grades = [module_grade, module_grade2, module_grade3, module_grade4, module_grade5, module_grade6]

#Sort grades in order
module_grades.sort()

#calculate results
lowest_grade = module_grades[0]
highest_grade = module_grades[5]
total_grade = sum(module_grades)
average_grade = total_grade / len(module_grades)

#Display results
print ("--------Grade Summary--------")
print (f"Lowest Grade: {lowest_grade}")
print (f"Highest Grade: {highest_grade}")
print (f"Total Grade: {total_grade}")
print (f"Average Grade: {average_grade}")
print("---------------------")