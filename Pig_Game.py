import random
from tkinter import *
from tkinter import messagebox

# Creates The Window for the user to interact with the GUI
windowRoot = Tk()
windowRoot.geometry("250x210")  # (width x height)
windowRoot.resizable(0, 0)
windowRoot.title("Pig Game")


def scoreBoard():
    global playerScoreLabel, computerScoreLabel, currentRoundLabel
    
    if playerScoreLabel:
        playerScoreLabel.config(text="Your Score: " + str(playerScore))
    if computerScoreLabel:
        computerScoreLabel.config(text="Computer Score: " + str(computerScore))
    if currentRoundLabel:
        currentRoundLabel.config(text="Current Round: " + str(currentRound))
        
def userTurn():
    global playerScore, currentRound

    dice = random.randint(1, 6)
    if dice == 1:
        currentRound = 0
        scoreBoard()
        computerTurn()
    else:
        currentRound += dice
        scoreBoard()

def bank():
    global playerScore, currentRound

    playerScore += currentRound
    currentRound = 0
    scoreBoard()
    computerTurn()
    scoreBoard()

def computerTurn():
    global computerScore

    currentRound = 0
    while True:
        dice = random.randint(1, 6)
        if dice == 1:
            break
        currentRound += dice
        if currentRound > 15:
            computerScore += currentRound
            break

def endGame():
    global playerScore, computerScore, currentRound
    
    if playerScore > computerScore:
        play_again = messagebox.askyesno("Game Over", "The player won!\n" "Would you like to play again?")
    elif computerScore > playerScore:
        play_again = messagebox.askyesno("Game Over", "The player lost!\n" " Would you like to play again?")
    elif playerScore == computerScore:
        play_again = messagebox.askyesno("Game Over", "It's a draw!\n" " Would you like to play again?")

    if play_again:
        # Reset game variables
        playerScore = 0
        computerScore = 0
        currentRound = 0
        scoreBoard()
    else:
        windowRoot.quit()
    
# Initialize game variables
playerScore = 0
computerScore = 0
currentRound = 0

# Frame for the Score Board
frameScore = Frame(windowRoot)
frameScore.pack(side = BOTTOM)
frameScore.place(x = 75, y = 0)

# Frame to Roll  
frameRoll = Frame(windowRoot)
frameRoll.pack(side = LEFT)

# Frame to Bank 
frameBank = Frame(windowRoot)
frameBank.pack(side = RIGHT)

playerScoreLabel = None
computerScoreLabel = None
currentRoundLabel = None

# Buttons for the User to Interact With
rollButton = Button(frameRoll, text = "Roll", font = ("Arial", 15, "bold"), width = 10, height = 2, bg = "#FFD700", bd = 5, command = userTurn)
rollButton.pack(side = LEFT, anchor = 'n')
bankButton = Button(frameBank, text = "Bank", font = ("Arial", 15, "bold"), width = 10, height = 2, bg = "#FFD700", bd = 5, command = bank)
bankButton.pack(side = RIGHT, anchor = 'n')
endGameButton = Button(windowRoot, text = "End Game", font = ("Arial", 15, "bold"), width = 20, height = 2, bg = "#FFD700", bd = 5, command = endGame)
endGameButton.pack(side = BOTTOM)
endGameButton.place(y = 136.5)

# Keeping Track of Score
playerScoreLabel = Label(frameScore, text = "Your Score: " + str(playerScore))
if playerScoreLabel:
    playerScoreLabel.pack()
computerScoreLabel = Label(frameScore, text = "Computer Score: " + str(computerScore))
if computerScoreLabel:
    computerScoreLabel.pack()
currentRoundLabel = Label(frameScore, text = "Current Round: " + str(currentRound))
if currentRoundLabel:
    currentRoundLabel.pack()

# Calling the Function(s)
windowRoot.mainloop()
