def print_feedback():
    for char in guess[:-1:]:
        print(char, end=" ")
    print(guess[-1])
    
    for j in range(0, LEN-1):
        if guess[j] == target[j]:
            print("🟩 ", end="")
        elif guess[j] in set(target):
            print("🟨 ", end="")
        else:
            print("⬛ ", end="")
    
    if guess[-1] == target[-1]:
        print("🟩 ")
    elif guess[-1] in set(target):
        print("🟨 ")
    else:
        print("⬛ ")

    return


LEN = 5
GUESSES = 6
target = "WHIRL" # choose word list according to LEN

prompt = "_ " * (LEN - 1) + "_"
guess = input(prompt + " (valid try: all caps with no spaces in between)\n").strip()

for i in range(0, GUESSES):
    print("Guess", i+1)

    if guess == target:
        print_feedback()
        print("correct!")
        break
    else:
        print_feedback()
        print("false...")
        guess = input(prompt + "\n").strip()
