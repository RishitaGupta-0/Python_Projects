#PYTHON PROGRAM FOR DICE ROLL GAME.

import random

def dice(n):  # Define function once, outside the loop
    for i in range(n):
        die = random.randint(1, 6)
        print(die)  # Print each die roll separately

while True:
    choice = input("Do you want to roll again? (y/n): ").lower()
    
    if choice == 'y':
        n = int(input("Enter the number of dice: "))  # Ask only when rolling
        dice(n)  # Call function with user input
    
    elif choice == 'n':
        print("Thank you 😊")
        break  # Exit the loop when user says 'n'
    
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")
