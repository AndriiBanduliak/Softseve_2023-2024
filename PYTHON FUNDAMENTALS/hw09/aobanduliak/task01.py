from random import randint as r

def guess_number():
    number_to_guess = r(1, 100)
    attempts = 10

    for i in range(attempts):
        user_guess = int(input("Enter your guess: "))
        
        if user_guess < number_to_guess:
            print("Your guess is less than the number.")
        elif user_guess > number_to_guess:
            print("Your guess is greater than the number.")
        else:
            print("Congratulations! You've guessed the number.")
            return

    print("Sorry, you didn't guess the number in 10 attempts.")

guess_number()
