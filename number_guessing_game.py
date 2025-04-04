import random
number_to_guess = random.randint(1,100)

while True:
    
    try:
        guess = int(input("Enter the number from 1 to 100: "))

        if guess > number_to_guess:
            print("Too High")
        elif guess < number_to_guess:
            print ("Too Low")
        else: 
            print("Congratulations!! You have guessed the right number.🥳")
            break

    except ValueError:
        print("Please enter the valid value")
    

    