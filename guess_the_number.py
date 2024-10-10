guess = 0
count = 0
right_value = 55

while right_value != guess:
    guess = int(input("Enter a guess: "))
    count += 1
    if guess > right_value:
        print("Your guess is too high.")
    elif guess < right_value:
        print("Your guess is too low.")
    else:
        print(f"Correct! It took you {count} guesses.")
        break