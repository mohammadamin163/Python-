secret_number = 7

print("Welcome to Number Guessing Game!")
print("You have 3 chances to guess the number.")

for i in range(3):
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("You Win!")
    else:
        print("Wrong Guess!")

print("Game Over!")
