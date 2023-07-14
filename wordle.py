import pathlib
import random


# TODO: this func is not like a python func and must be rewritten
def print_feedback(guess, target): # pass LEN as param
    """
    Compare guess word with target and give feedback.

    >>> print_feedback("CRANE", "RAINY")
    C R A N E
    ⬛🟨🟨🟩⬛
    
    """
    for char in guess[:-1:]:
        print(char, end=" ")
    print(guess[-1])
    
    target_chars = list(target)
    for j in range(0, LEN):
        if guess[j] == target_chars[j]:
            print("🟩", end="")
            target_chars[j] = 0
        elif guess[j] in target_chars:
            print("🟨", end="")

            # find first non-matching letter and remove it in target_chars
            for k in range(0, LEN):
                if target_chars[k] == guess[j] and target_chars[k] != guess[k]:
                    target_chars[k] = 0
        else:
            print("⬛", end="")

    print()
    return


def random_target(LEN: int) -> str:
    tlist = pathlib.Path("targets_" + str(LEN) + ".txt").read_text(encoding="utf-8").strip().upper().split(" ")
    target = random.choice(tlist)
    return target


LEN = 5
GUESSES = 6
LETTERS = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

# main loop

# list of all valid words
wlist = pathlib.Path("words_" + str(LEN) + ".txt").read_text(encoding="utf-8").strip().upper().split("\n")
target = random_target(LEN)

prompt = " (valid try: all caps with no spaces in between)\n"

guess_count = 0
while guess_count < GUESSES:
    guess = input("_ " * (LEN - 1) + "_" + prompt).strip().upper()

    if guess not in wlist:
        print(guess, "not in word list.")
    else:
        print("Guess", guess_count+1)

        if guess == target:
            print_feedback(guess, target)
            print("Correct!")
            break
        else:
            print_feedback(guess, target)
            print("Wrong...")
        guess_count += 1

    prompt = "\n" # not show valid try from second try
else:
    if guess_count >= GUESSES:
        print(F"Barge. The target was {target}.")
