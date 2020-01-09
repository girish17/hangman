#!/usr/bin/env python2
from random import *

player_score = 0
computer_score = 0
word_list = ["namespace", "cardinality", "string", "python", "tuple", "dictionary", "list", "set"]

def hangedman(hangman):
    graphic = [
    """
        +-------+
        |
        |
        |
        |
        |
    ==============
    """,
    """
        +-------+
        |       |
        |       O
        |            
        |
        |
    ===============
    """,
    """
        +-------+
        |       |
        |       O
        |       |     
        |
        |
    ===============
    """,
    """
        +-------+
        |       |
        |       O
        |     - |    
        |
        |
    ===============
    """,
    """
        +-------+
        |       |
        |       O
        |     - | -    
        |
        |
    ===============
    """,
    """
        +-------+
        |       |
        |       O
        |     - | -     
        |      /
        |
    ===============
    """,
    """
        +-------+
        |       |
        |       O            
        |     - | -
        |      / \ 
        |
    ===============
    """]

    print(graphic[hangman])
    return


def start():
    print("Let's play a game of Python Hangman.")
    while game():
        pass
    scores()


def game():
    global word_list, word, computer_score, player_score
    if len(word_list) == 0:
        return False
    word = choice(word_list)
    word_length = len(word)
    clue = word_length * ["_"]
    tries = 6
    letters_tried = ""
    letters_wrong = 0

    while (letters_wrong != tries) and ("".join(clue) != word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print("You've already picked", letter)
            else:
                letters_tried = letters_tried + letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print("Sorry,", letter, "isn't what we're looking for .")
                else:
                    print("Congratulations,", letter, " is correct.")
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print("Choose another.")

        hangedman(letters_wrong)
        print(" ".join(clue))
        print("Guesses: ", letters_tried)

        if letters_wrong == tries:
            print("Game Over.")
            print("The word was", word)
            computer_score += 1
            break
        if "".join(clue) == word:
            print("You Win!")
            print("The word was", word)
            player_score += 1
            break
    return play_again()


def guess_letter():
    print()
    letter = raw_input("Take a guess at our mystery word:")
    letter.strip()
    letter.lower()
    print()
    return letter


def play_again():
    answer = raw_input("Would you like to play again? y/n: ")
    if answer in ("y", "Y", "yes", "Yes", "Of course!"):
        word_list.remove(word)
        return answer
    else:
        print("Thank you very much for playing our game.See you next time!")


def scores():
    global player_score, computer_score
    if len(word_list) == 0:
        print("You've exhausted the words in our word bank")
    print("HIGH SCORES")
    print("Player: ", player_score)
    print("Computer: ", computer_score)


if __name__ == '__main__':
    start()
