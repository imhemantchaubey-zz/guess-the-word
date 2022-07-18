import random

words = ['apple', 'ball', 'computer', 'drive', 'elegant']
guess_word = random.choice(words)
hint = guess_word[0] + " " + guess_word[-1]
store_guessed_letters = []
no_of_try = 5
print("Hello! This is Hemant's Word Guessing Game...")
name = input("What's your good name dear: ")
print("Hello " + name + "!\nWelcome to the game...!\nYou get 5 attempts to guess the word")
for guess in range(no_of_try):
    while True:
        letter = input("Guess the letter: ")
        if len(letter) == 1:
            break
        else:
            print("Oops...! Please guess a letter...")

    if letter in guess_word:
        store_guessed_letters.append(letter)
        print("Yah!!! You got it right...!")
    else:
        print("Ahh!!! Sorry try again...")

    if guess == 2:
        cluerequest = input("Would you like to have a clue: ")
        if cluerequest.lower().startswith('y'):
            print("CLUE: The first and last letter of the word is: ", hint)
        else:
            print("Great...! Looks like you are very confident...")

print("Now, let's see what you have guessed so far...")
print("You have guessed ", len(store_guessed_letters), " letters correctly...")
print("Those letters are: ", store_guessed_letters)

word_guess = input("Try guessing the whole word: ")
if word_guess.lower() == guess_word:
    print("Yah...! Congrats...You got it right...")
else:
    print("Sorry! The answer was, ", guess_word)
