# build a hangman game with python
import random

word_list = ['ardvark', 'baboon', 'camel']


chosen_word = random.choice(word_list)

# 
print(f'Psst, the word is {chosen_word}')

# create empty list. for each letter in the chosen word, add "_". So if the word is apple, it should show 5 "_" representing each letter to guess.

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()


# loop thru each position in the chosen word. if the letter in that position matches the guess, then reveal that letter in the display at that position. 
# example, if user guessed "p" and the chosen word was apple, then display should be ["_", "p", "p", "_", "_"]

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)




