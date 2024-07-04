## Employee Names/Salaries Program
## v1.20
## Author: Shannon Wetnight
##
## This program is designed to take and store the names of employees and their rounded user input salaries in two separate arrays until the user enters a sentinel value, at which point the program will calculate and store the average salary
## from the list of salaries, output the names and salaries stored in the list, output the average salary, and output any of the employees from the list who are within $5000 of the average salary.
## I did not try to over-complicate the program like I did with M07's final project. No input validation or unnecessary defined functions this time.

## Declare two arrays to be used to store employee names and salaries
employeeNamesList = []
employeeSalariesList = []

## Declare sentinel value so we can change it later if needed
SENTINEL_VALUE = "XXX"

## Declare variables and initialize them to avoid storing garbage data
employeeName = None
employeeSalary = 0
roundedSalary = 0
averageSalary = 0
roundedAverageSalary = 0
## This variable represents $5000 used in the average comparison later in the program, stored as 5 because the list values are all inputs divided by 1000, so $5000 needs to be divided in the same fashion
RANGE_VALUE = 5

## Start a while loop to ask user for names and salaries
while employeeName != SENTINEL_VALUE:
    employeeName = input(f"Please enter the employee's first and last name or {SENTINEL_VALUE} to quit: ")
    ## Check for sentinel value to exit loop
    if employeeName.upper() == "XXX":
        break
    ## Add employee name to name list
    employeeNamesList.append(employeeName)
    ## Take user input as a float data type
    employeeSalary = float(input(f"Please enter {employeeName}'s salary: "))
    ## Round user input before storing in the list
    roundedSalary = round(employeeSalary, -2) / 1000
    ## Add rounded input to salary list
    employeeSalariesList.append(roundedSalary)

## Calculate average salary
averageSalary = sum(employeeSalariesList) / len(employeeSalariesList)
## Round average salary before calling
roundedAverageSalary = round(averageSalary, 1)

## Employee names and salaries print loop
print("\n\nEmployee Names and Salaries")
## Iterates through loop to print names and salaries
for i in range(len(employeeNamesList)):

    ## Prints both "For example, a salary of 36,510 should be input as 36.5 (according to assignment)" and longer form of number (was confused which was wanted specifically so I opted for having both)
    print(f"{employeeNamesList[i]:20} {employeeSalariesList[i]}", "($" + str(employeeSalariesList[i] * 1000) + ")")
## Output average rounded salary from earlier calculation
print(f"\n\nThe average salary is {roundedAverageSalary}", "($" + str(roundedAverageSalary * 1000) + ").")

## Define a minimum and maximum range to compare salaries from list to
maxRange = averageSalary + RANGE_VALUE
minRange = averageSalary - RANGE_VALUE

## Start loop to compare salaries to minimum and maximum ranges, output findings
print(f"\n\nEmployees who are within $5,000 of the average salary:")
## Flag used if no employees were found within the average salary
foundIt = False
## Iterates through comparison loop
for i in range(len(employeeSalariesList)):
    if employeeSalariesList[i] <= maxRange and employeeSalariesList[i] >= minRange:
        ## Prints both "For example, a salary of 36,510 should be input as 36.5 (according to assignment)" and longer form of number (was confused which was wanted specifically so I opted for having both)
        print(f"{employeeNamesList[i]:20} {employeeSalariesList[i]}", "($" + str(employeeSalariesList[i] * 1000) + ")")
        foundIt = True
if not foundIt:
    print(f"No employees within the average salary (${roundedAverageSalary * 1000}) were found in the list.")