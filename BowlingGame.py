class BowlingGame():

    def __init__(self):
        self.frames = [['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', '', '']]
        self.scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.frame = 0 # The current frame
        self.subFrame = 0 # The current sub frame
        self.gameOver = False

    def getScoreSheet(self):
        print("| Frame |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10  |")
        print("|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|")
        
        subFrameOne, subFrameTwo, subFrameThree = "", "", ""

        # Build the input string
        inputString = "|         "
        for i in range(0, self.frame + 1):
            # Sub Frame 1
            if self.frames[i][0] == "": 
                subFrameOne = " "
            else: subFrameOne = self.frames[i][0]

            # Sub Frame 2
            if self.frames[i][1] == "": 
                subFrameTwo = " "
            else: subFrameTwo = self.frames[i][1]

            #Sub Frame 3 (10th Frame)
            if i == 9:
                if self.frames[i][2] == "": 
                    subFrameThree = " "
                else: subFrameThree = self.frames[i][2]

            inputString += subFrameOne + "|" + subFrameTwo + subFrameThree + "   "

        print(inputString)
        print("|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|")
        #print(scoreString)

        #Debugging print statements
        #print("frame: ", self.frame + 1, ", subFrame: ", self.subFrame + 1)
        #print("\n")
        #print("frames: ", self.frames)
        #print("score: ", self.scores)

    def strike(self):
        if self.subFrame == 1:  
            self.frames[self.frame][1] = "-"
            self.frame += 1
            self.frames[self.frame][0] = "X"
            self.frame += 1
            self.subFrame = 0  
        else:
            self.frames[self.frame][self.subFrame] = "X"
            self.frame += 1

    def spare(self):
        if self.subFrame == 0:
            self.frames[self.frame][0] = "-"
            self.frames[self.frame][1] = "/"
            self.frame += 1
            self.subFrame = 0
        else:
            self.frames[self.frame][self.subFrame] = "/"
            self.frame += 1
            self.subFrame = 0

    def miss(self):
        self.frames[self.frame][self.subFrame] = "-"
        if self.subFrame == 0:
            self.subFrame = 1
        else:
            self.subFrame = 0
            self.frame += 1
    
    # Any roll that is a valid and is NOT a spare, strike, or miss
    def defaultRoll(self, userInput):
        if self.subFrame == 1 and self.frames[self.frame][0] == "-":
            self.frames[self.frame][self.subFrame] = userInput

            if self.subFrame == 0: 
                self.subFrame = 1
            else:
                self.subFrame = 0
                self.frame += 1

        # If the two sub frames add to 10, it's a spare
        elif self.subFrame == 1 and (int(userInput) + int(self.frames[self.frame][0])) == 10 :
            self.frames[self.frame][self.subFrame] = "/"
            self.frame += 1
            self.subFrame = 0

        # If 2 values add up to over 9, go to the next frame
        elif self.subFrame == 1 and (int(userInput) + int(self.frames[self.frame][0])) > 10:
            self.frames[self.frame][1] = "-"
            self.frame += 1
            self.frames[self.frame][0] = userInput
            self.subFrame = 1
            
        else:
            self.frames[self.frame][self.subFrame] = userInput
            self.scores[self.frame] += int(userInput)
            if self.subFrame == 0: 
                self.subFrame = 1
            else:
                self.subFrame = 0
                self.frame += 1

    # Last frame functions
    def strikeLastFrame(self):
        if self.subFrame == 0:  
            self.frames[self.frame][0] = "X"
            self.subFrame = 1
        elif self.subFrame == 1:
            self.frames[self.frame][1] = "X"
            self.subFrame = 2 
        else:
            self.frames[self.frame][2] = "X"
            self.gameOver = True

    def spareLastFrame(self):
        if self.subFrame == 0:
            self.frames[self.frame][0] = "-"
            self.frames[self.frame][1] = "/"
            self.subFrame = 2
        elif self.subFrame == 1:
            self.frames[self.frame][1] = "/"
            self.subFrame = 2
        else:
            self.frames[self.frame][2] = "/"
            self.gameOver = True

    def missLastFrame(self):
        self.frames[self.frame][self.subFrame] = "-"
        if self.subFrame == 0:
            self.subFrame = 1
        elif self.subFrame == 1 or self.subFrame == 2:
            self.gameOver = True

    # Any roll that is a valid and is NOT a spare, strike, or miss
    def lastFrameDefault(self, userInput):
        if self.subFrame == 0:
            self.frames[self.frame][0] = userInput
            self.subFrame = 1

        elif self.frames[self.frame][1] == "/" or self.frames[self.frame][1] == "X" or self.frames[self.frame][1] == "-":
            self.frames[self.frame][2] = userInput
            self.gameOver = True

        elif self.subFrame == 1 and (int(self.frames[self.frame][0]) + int(userInput)) > 9:
            print("Invalid roll. Pins knocked over cannot exceed remaining pin count on the last frame.") #Because we can't skip to an 11th frame

        else:
            self.frames[self.frame][1] = userInput
            self.gameOver = True

    # Receive the input roll from the user
    def getInput(self):
        validInputs = ["-", "/", "x", "X", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "strike", "spare", "miss"]
        userInput, userScore = "", 0

        userInput = str(input("Roll: "))

        # Exit command
        if userInput.lower() == "c":
            print("Thank you for playing!")
            quit()

        # Sanitize input
        if userInput not in validInputs:
            print("Invalid input. Please try again.")
            return False

        # 10th frame can have up to 3 parts, logic will be different
        if self.frame < 9:
            # Spare
            if (userInput == "spare" or userInput == "/"):
                self.spare()
            # Miss
            elif userInput == "miss" or userInput == "0" or userInput == "-":
                self.miss()
            # Strike
            elif userInput == "strike" or userInput.lower() == "x" or userInput == "10":
                self.strike()
            else:
                self.defaultRoll(userInput)

        # 10th frame
        elif self.subFrame <= 2:
            # Spare
            if (userInput == "spare" or userInput == "/"):
                self.spareLastFrame() 
            # Miss
            elif userInput == "miss" or userInput == "0" or userInput == "-":
                self.missLastFrame()
            # Strike
            elif userInput == "strike" or userInput.lower() == "x" or userInput == "10":
                self.strikeLastFrame()
            else:
                self.lastFrameDefault(userInput)
        else:
            self.gameOver = True





        

        