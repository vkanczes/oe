
# Veronica Kanczes
# Assignment 3

#PartI

# set up intitial variables
number = 10
numAttempts = 0

# request user's name
name = input("Hello! What is your name?\n"  )
print ("Well,", name, ",", "I am thinking of a number between 1 and 20.\n")

# give the user 3 tries to guess the correct number
for counter in range(3):
    guess = int(input("Take a guess.\n"))
    numAttempts = numAttempts + 1

    # determine if they chose the correct number
    if (guess == number):
        print ("Good job,", name, "! You guessed my number in", numAttempts, "guesses!")
        break
    elif (guess < number):
        print ("Your guess is too low.")
    elif (guess > number):
        print ("Your guess is too high.")

    # keep track of number of attempts and if too many then exit
    if numAttempts == 3:
        print ("Your three guesses are over, the number I was thinking of was", number)

# Part II

def checkInput(player):
    '''Check for valid input and continue to ask until valid input received'''

    choice = 0;

    while choice == 0:
        print ("\n", player)
        choice = input("Please enter either (R)ock, (P)aper, or (S)cissors:\n")
    
        # check for valid choice
        if choice.lower() == 'p' or choice.lower() == 'r' or choice.lower() == 's':

            # return valid choice
            return choice

        # have them choose again
        else:
            print ("Invalid choice..")
            choice = 0


def game(a, b):
    '''A game of rock-paper-scissors takes 2 string parameters, one for each player's choice and returns to represent who won'''


    # Rules:
    # Paper beats rock
    # Rock beats scissors
    # Scissors beat paper
    if a == b:
        return 0
    elif a == 'r' and b == 's':
        return 1
    elif a == 's' and b == 'p':
        return 1
    elif a == 'p' and b == 'r':
        return 1
    elif b == 'r' and a == 's':
        return 2
    elif b == 's' and a == 'p':
        return 2
    elif b == 'p' and a == 'r':
        return 2

# set up all scores to be zero                                                
p1score = 0
p2score = 0
tieScore = 0
counter = 0


# set to have the game be played multiple times
while counter in range(5):
    '''Play multiple games and keep score of who wins, 1 - player1 wins, 2 - player2 wins 0-tie'''

    # get player 1 choice and make sure within guidelines
    player = "Player1"
    p1 = checkInput(player)
    player1 = p1.lower()

    # get player 2 choice and make sure within guidlines
    player = "Player2"
    p2 = checkInput(player)
    player2 = p2.lower()

    result = game(p1,p2)

    # display who won the game
    if result == 1:
        print ("\nPlayer 1 wins.")
        p1score = p1score + 1
    elif result == 2:
        print ("\nPlayer 2 wins.")
        p2score = p2score + 1
    else:
        tieScore = tieScore + 1
        print ("\nIt's a tie...")

    # keep track of games played
    counter = counter + 1

    # print correct header based on amount of games played
    if counter < 5:
        # provide readout of final scores
        print ("\nScores after game:", counter, )
    else:
        print ("\nFINAL SCORE:\n")

    # show tallied scores after each game
    print ("Player1:  ", p1score)
    print ("Player2:  ", p2score)
    print ("Ties:  ", tieScore)
    


