"""ask user for number, give hints about number if wrong"""

secret: int = 10
guess: int = int(input("guess a number "))

playing: bool = True

while playing:
    if guess == secret:
        print("correct ")
        playing = False
    else:
        if guess % 2 == 1:
            print("your guess is odd. the answer is even ")
        
        if guess < secret:
            print("Too low ")
        
        else:
            print("too high")
        guess = int(input("wrong guess try again"))
        

    





    








