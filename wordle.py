import pathlib
import random


def print_feedback():
    for char in guess[:-1:]:
        print(char, end=" ")
    print(guess[-1])
    
    for j in range(0, LEN):
        if guess[j] == target[j]:
            print("🟩", end="")
        elif guess[j] in set(target):
            print("🟨", end="")
        else:
            print("⬛", end="")

    return


LEN = 5
GUESSES = 6

# choose target word from word list according to LEN
wlist = pathlib.Path("words_" + str(LEN) + ".txt").read_text(encoding="utf-8").strip().upper().split("\n")
tlist = pathlib.Path("targets_" + str(LEN) + ".txt").read_text(encoding="utf-8").strip().upper().split(" ")
target = random.choice(tlist)

prompt = " (valid try: all caps with no spaces in between)\n"

guess_count = 0
while guess_count < GUESSES:
    guess = input("_ " * (LEN - 1) + "_" + prompt).strip().upper()

    if guess not in wlist:
        print(guess, "not in word list.")
    else:
        print("Guess", guess_count+1)

        if guess == target:
            print_feedback()
            print("\nCorrect!")
            break
        else:
            print_feedback()
            print("\nWrong...")
        guess_count += 1

    prompt = "\n" # not show valid try from second try
else:
    if guess_count >= GUESSES:
        print("Barge. The target was", target)