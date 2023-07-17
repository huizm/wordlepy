import pathlib
import random

LETTERS = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
# TODO: hint unused letters


class Wordle:
    """
    Prototype of the game.
    """
    def __init__(self, len: int, guesses: int):
        self.len = len
        self.guesses = guesses
        return

    def create(self):
        """
        Main loop of the game. Implicitly takes variable len, guesses and constant LETTERS.
        """


        # TODO: should i nest these funcions?
        def random_target(len: int) -> str:
            """
            Choose a random target word from word list according to len.
            """
            tlist = pathlib.Path("targets_" + str(len) + ".txt").read_text(encoding="utf-8").strip().upper().split("\n")
            target = random.choice(tlist)
            return target
        

        # TODO: this func is not like a python func and must be rewritten
        # TODO: fix doctest
        def print_feedback(guess: str, target: str, len: int):
            """
            Compare guess word with target and give feedback.

            >>> print_feedback("CRANE", "RAINY", 5)
            C R A N E
            ⬛🟨🟨🟩⬛
            
            >>> print_feedback("LEMMA", "MOUNT", 5)
            L E M M A
            ⬛⬛🟨⬛⬛
            
            """
            for char in guess[:-1:]:
                print(char, end=" ")
            print(guess[-1])
            
            target_chars = list(target)
            for j in range(0, len):
                if guess[j] == target_chars[j]:
                    print("🟩", end="")
                    target_chars[j] = 0
                elif guess[j] in target_chars:
                    print("🟨", end="")

                    # find first non-matching letter and remove it in target_chars
                    for k in range(0, len):
                        if target_chars[k] == guess[j] and target_chars[k] != guess[k]:
                            target_chars[k] = 0
                else:
                    print("⬛", end="")

            print()
            return


        # list of all valid words
        wlist = pathlib.Path("words_" + str(self.len) + ".txt").read_text(encoding="utf-8").strip().upper().split("\n")
        target = random_target(self.len)

        prompt = " (valid try: all caps with no spaces in between)\n"

        guess_count = 0
        while guess_count < self.guesses:
            guess = input("_ " * (self.len - 1) + "_" + prompt).strip().upper()

            if guess not in wlist:
                print(guess, "not in word list.")
            else:
                print("Guess", guess_count+1)

                if guess == target:
                    print_feedback(guess, target, self.len)
                    print("Correct!")
                    break
                else:
                    print_feedback(guess, target, self.len)
                    print("Wrong...")
                guess_count += 1

            prompt = "\n" # not show valid try from second try
        else:
            if guess_count >= self.guesses:
                print(F"Barge. The target was {target}.")
        return


if __name__ == "__main__":
    game = Wordle(5, 6)
    game.create()
