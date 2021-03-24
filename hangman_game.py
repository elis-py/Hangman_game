# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:20:25 2021

"""

import random

def check_input():
    global letter
    print("\n", "".join(hidden_word))
    letter = input("Input a letter: ")
    if letter in letters_input:
        print("You've already guessed this letter")
        check_input()
    elif len(letter) != 1 or letter == "":
        print("You should input a single letter")
        check_input()
    elif letter == letter.upper() or letter == "":
        print("Please enter a lowercase English letter")
        check_input()


words_choice = ('python', 'java', 'kotlin', 'javascript')
random_word = random.choice(words_choice)
hidden_word = list(len(random_word) * "-")
tries = 8
letters_input = set()

print("H A N G M A N\n")

while tries != 0:
    check_input()
    if letter in random_word:
        for k in range(len(random_word)):
            if random_word[k] == letter:
                hidden_word[k] = letter
        if "-" not in hidden_word:
            print(f'You guessed the word {"".join(hidden_word)}!\nYou survived!')
            break                 
    else:
        print("That letter doesn't appear in the word")
        tries -= 1
    letters_input.add(letter)
     
if "-" in hidden_word:
    print('You lost!')

print("\nThanks for playing!")