# build a hangman game with python
import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# testing code
print(f"Psst, the solution is {chosen_word}")

# create empty list. for each letter in the chosen word, add "_". So if the word is apple, it should show 5 "_" representing each letter to guess.

display = []
for _ in range(word_length):
    display += "_"
print(display)

# using a while loop to let the user guess again. the loop only stops once the user has guessed all the letters in the chosen word, and display has no more blanks. then we'll give a winning message.

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # loop thru each position in the chosen word. if the letter in that position matches the guess, then reveal that letter in the display at that position.
    # example, if user guessed "p" and the chosen word was apple, then display should be ["_", "p", "p", "_", "_"]

    for position in range(word_length):
        letter = chosen_word[position]
        print(
            f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}"
        )
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game == True
        print("You win.")
