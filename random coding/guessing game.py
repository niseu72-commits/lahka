import random

print("Yoo hoo welcome to the guessing game!")
print("I have selected a number between 1 and 100. Can you guess what it is?")
print("You have 5 attempts to guess the number. Good luck!")

number = random.randint(1, 100)
attempts = 5

while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("Higher pa idol! Try again.")
    elif guess > number:
        print("Lower pa idol! Try again.")
    else:
        print(f"Pucha galing! You guessed the number {number} correctly!")
        break

    attempts -= 1
    if attempts > 0:
        print(f"You only have {attempts} attempts left.")
else:
    print(f"Sorry, you ran out of attempts. The number was {number}.")