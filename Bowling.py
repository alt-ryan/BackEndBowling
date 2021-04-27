from BowlingGame import BowlingGame

def main():

    """
    Hi CardFlight devs! Thanks for reviewing my code. I didn't want to go over the 6 hour mark too much,
        so I stopped before implementing much of the scoring system, but the input logic and display is here
    I tried to cover as many cases as I could with the input. Hopefully they're as you expect

    X, "strike", or 10 will result in a strike (strings are set to lower case, so strike/STRIKE/sTrIkE are accepted)
    /, "spare", or two frames that add up to 10 (unless the first frame is a miss) will result in a spare
    -, or 0, or "miss" will result in a miss
    """

    print("\nWelcome to Backend Bowling!\n")

    print("| Frame |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10  |")
    print("|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|\n")
    

    game = BowlingGame()

    while game.gameOver == False:
        game.getInput()
        game.getScoreSheet()

    print("Game over")
        

if __name__ == "__main__":
    main()