"""Structured Wordle"""
__author__ = "730599859"

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

def contains_char(multi_chr: str, single_chr: str ) -> bool:
    """this function searches a multi charachter string to see if a letter matches with a single character"""
    assert len(single_chr) == 1
    indx: int = 0
    contained_word: bool = False
    while len(multi_chr) > indx:
        if multi_chr[indx] == single_chr:
            contained_word = True 
            indx += 1
        else: 
            indx += 1    
    return contained_word







def emojified(guess: str, secret: str) -> str:
    """this function will take the contains_chr function and gies eaach index a colored box."""
    assert len(guess) == len(secret)
    display: str = ""
    indx: int = 0
    while len(guess) > indx:
        if contains_char(secret, guess[indx]) is True and secret[indx] == guess[indx]:
            display = display + green_box
        elif contains_char(secret, guess[indx]) is True and secret[indx] != guess[indx]:
            display = display + yellow_box
        elif contains_char(secret, guess[indx]) is False:
            display = display + white_box
        indx += 1
    return display


def input_guess(exp_len: int) -> str:
    """this function will make sure that the inputted guess is equal to the expected length, which is the secret word"""
    guess = input(f"Enter a {exp_len} character word: ")
    while len(guess) != exp_len:
        print(f"That was not {exp_len} letters! Try again: ")
        guess = input(f"what is your {exp_len} letter guess: ")
    return guess

def main() -> None: 
    """The entrypoint of the program and main game loop."""
    playing = True
    secret: str = "codes"
    n = 1
    while n <= (len(secret) + 1) and playing == True:
        print(f"=== Turn {n}/6 ===") 
        guess = input_guess(len(secret))
        print(emojified(guess, secret))

        if guess == secret:
            print(f"You won in {n}/6 turns!")
            playing = False
        else:
            n += 1
        if n > 6:
            print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()
    



