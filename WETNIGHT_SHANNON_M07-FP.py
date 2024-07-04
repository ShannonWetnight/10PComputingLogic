## Trainers/enrollees program
## v1.61
## Author: Shannon Wetnight
##
## This program is designed to take and store the names of 15 trainers and the number of new members they have
## enrolled in the gym. The program then outputs 3 different categories, 0-5, 6-10, and 11-15, with the total amount
## of trainers for each applicable category. Additionally, I have added some cosmetic things using os and time libraries
## to add some "flare" to be more human-relatable (delays between prompts, color changing for errors, etc.).#

# Imports the os and time libraries so we can use some good ol' fashioned terminal commands for visual cleanup.
import os, time

## Getting more familiar with Python by adding unnecessary complexity to the program via defined functions.
def clearScreen():
     
     os.system('cls')
     return

def programExit():
     
     os.system('color 04')
     clearScreen()
     print("Program will exit in 10 seconds.")
     time.sleep(10)
     os.system('exit')
     return

def inputValidation(prompt):

    ## Added input validation to make sure the user is entering appropriate data types.
    ## Added a way to control the entry values to keep them within range of the assignment.
    ## If the user enters a value that is outside of the range 5 times it will assign the value 0 and ask for the next name.
    attemptsRemaining = 5
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            os.system('color 04')
            if attemptsRemaining == 0:
                clearScreen()
                print(f"You reached the maximum attempts and your input was saved as 0.")
                value = 0
                time.sleep(3)
                break
            clearScreen()
            print(f"That is not a valid entry for NEW MEMBERS. If you reach 5 invalid attempts your input will be saved as 0.\n\n{attemptsRemaining} attempt(s) remaining.")

            attemptsRemaining = attemptsRemaining - 1
            continue
        if value < 0 or value > 15:
            os.system('color 04')
            if attemptsRemaining == 0:
                print((f"You reach the maximum attempts and your input was saved as 0."))
                value = 0
                time.sleep(3)
                break
            clearScreen()
            print(f"Your number must be no less than 0 and no greater than 15. If you reach 5 invalid attempts your input will be saved as 0.\n\n{attemptsRemaining} attempt(s) remaining.")
            time.sleep(1)
            attemptsRemaining = attemptsRemaining - 1
            continue
        else:
            break
    return value

def welcomeMessage():
     
    os.system('color 06')
    print("##################################################################")
    print("########################     v1.61     ###########################")
    print("#########    Wally's Gym Trainer and Enrollee Tracker   ##########")
    print("#####################    Let's get fit.   ########################")
    print("##################################################################\n\n")
    time.sleep(2)
    return

def userPrompts():

    ## Declare and initialize a counter variable to be used as the exit condition for the while loop.
    ## Declare a constant to be used as the maximum number of entries before the end of the loop.
    counter = 1
    MAX_ENTRIES = 15
    while counter <= MAX_ENTRIES:
        os.system('color 06')
        trainerLastName = input(f"(Name Counter: {counter}) Please enter the LAST NAME of the TRAINER or -1 to stop the program and calculate the categories: ")
        if trainerLastName == "-1":
            break
        trainerLastNameList.append(trainerLastName)
        newMemberCount = inputValidation("Please enter how many NEW MEMBERS the trainer has enrolled: ")
        newMemberCountList.append(newMemberCount)
        counter += 1
        time.sleep(1)
        clearScreen()
    return

def calculateAndOutputCategories():

    ## Declare and initialize 3 variables for the categories mentioned in the assignment.
    firstCategoryOfTrainers = 0
    secondCategoryOfTrainers = 0
    thirdCategoryOfTrainers = 0

    ## For loop that compares the member and trainer counts in the array (list) and sums the trainer totals acording to the assignment.
    ## Iterates through both arrays to keep track of the applicable totals.
    for members in newMemberCountList:
        if 0 <= members <= 5:
                firstCategoryOfTrainers += 1
        elif 6 <= members <= 10:
                secondCategoryOfTrainers += 1
        elif 11 <= members <= 15:
                thirdCategoryOfTrainers += 1

    ## Prints the totals according to the assignment in 3 lines.
    clearScreen()
    ## Fake calculating output to simulate computation.
    print("Calculating totals. Please wait...")
    time.sleep(2)
    clearScreen()
    print("Results based on the information provided:\n")
    print(f"Trainers with 0-5 new members: {firstCategoryOfTrainers}")
    print(f"Trainers with 6-10 new members: {secondCategoryOfTrainers}")
    print(f"Trainers with 11-15 new members: {thirdCategoryOfTrainers}")
    time.sleep(3)
    return

def optionalTrainerOutput():
    
    trainerHeader = "TRAINER"
    newMemberHeader = "NEW MEMBERS"
    answer = input("\nWould you like to list the trainers and totals together (YES/NO)? ")
    if answer.upper() == "YES" or answer.upper() == "Y":
        if not trainerLastNameList or not newMemberCountList:
            clearScreen()
            print("Nothing was entered into the lists to display.\n")
            time.sleep(1)
        else:
            clearScreen()
            print(f"{trainerHeader:20}{newMemberHeader:20}")
            print(f"_______________________________")
            for index in range(len(trainerLastNameList)):
                print(f"{trainerLastNameList[index]:20}{newMemberCountList[index]}")
        print(f"\nInformation will be cleared in 5 seconds.")
        time.sleep(5)
        programExit()
    else:
         clearScreen()
         programExit()
    return

## Welcome message for the program.
welcomeMessage()

## Declare our arrays (lists) to store the prompted input data that will be used later in the program.
## Lists are declared here so that all of my functions can access them.
trainerLastNameList = []
newMemberCountList = []

## Asks the user of the program to enter the last name of the trainer. Mentions you can enter -1 to calculate the categories.
## Follow-up prompt asks the user of the program to enter the number of enrollees.
## This information will be stored in the two arrays (lists) that were declared earlier.
userPrompts()

## Calculates the information we provided in the userPrompts() function and outputs the information per the assignment.
calculateAndOutputCategories()

## Added an optional trainer output with a shutdown feature and some prompts so I could verify the trainer list was being written
## to in a fun way. This also provides some additional functionality.
optionalTrainerOutput()