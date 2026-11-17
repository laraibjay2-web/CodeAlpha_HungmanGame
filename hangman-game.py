import random

words = ["python" , "apple" ,  "school" , "computer" , "coding"]

secret_word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("===========================")
print("         WELCOME TO HANGMAN        ")
print("===========================")


while incorrect_guesses < max_attempts:

    display_word = ""

    for letter in secret_word:

        if letter in guessed_letters:
            display_word = display_word + letter + " "

        else:
            display_word = display_word + "_"

    print("\nword:", display_word)

    print("Incorrect guesses:" , incorrect_guesses)
    print("Remaining attempts:", max_attempts - incorrect_guesses)

    guess = input("Guess a letter:")

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    guess = guess.lower()

    if guess in guessed_letters:
        print("you already guessed this letter. try another!")
        continue
    
    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")

    else:
        incorrect_guesses = incorrect_guesses + 1
        print("Wrong guess!")

    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        print("The secret word was:", secret_word)
        break

if incorrect_guesses == max_attempts:
    print("\nGame Over! You lost!")
    print("The secret word was:", secret_word)

print("\nThank you for playing Hangman!")