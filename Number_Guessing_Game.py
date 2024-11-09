import random

def check_answer(number):
    if number > answer:
        print("Too high.")
    elif number < answer:
        print("Too low.")

def attempts_number(attempts):
    attempts -= 1
    print(f"You have {attempts} attempts ramaining to guess the number.")
    return attempts

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

gamemode_choose = input("Choose a difficulty. Type 'easy' or 'hard': ")

answer = random.randint(1, 100)


if gamemode_choose == "easy":
    attempts = 10
elif gamemode_choose == "hard":
    attempts = 5


if gamemode_choose == "easy":
    print("You have 10 attempts remaining to guess the number.")    
    while True:
        guess_number = int(input("Make a guess: "))
        check_answer(guess_number)
        if guess_number == answer:
            print(f"You got it! The answer is {answer}.")
            break
        if attempts == 1:
            print("You've run out of guesses, you lose.")
            break
        print("Guess again.")
        attempts = attempts_number(attempts)
elif gamemode_choose == "hard":
    print("You have 5 attempts remaining to guess the number.")  
    while True:
        guess_number = int(input("Make a guess: "))
        check_answer(guess_number)
        if guess_number == answer:
            print(f"You got it! The answer is {answer}.")
            break
        if attempts == 1:
            print("You've run out of guesses, you lose.")
            break
        print("Guess again.")
        attempts = attempts_number(attempts)

