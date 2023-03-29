import time
import random

def menu():
    choice = input("Do you want to\n1: Read the rules\nor\n2: Play the game\n")
    if choice == "1":
        time.sleep(0.5)
        print("You will have to pick between five colours\n1: Red\n2: Blue\n3: Yellow\n4: Green\n5: Purple")
        time.sleep(0.5)
        print("The computer will pick one of the 5 colours too")
        time.sleep(0.5)
        print("If the colour is the same as the computer, then the computer gets a point")
        time.sleep(0.5)
        print("If the colour is not the same as the computer, then you get a point")
        time.sleep(0.5)
        print("Whoever gets 5 points first, wins the game")
        time.sleep(0.5)
        menu()
    elif choice == "2":
        game(0, 0)
    else:
        print("please enter 1 or 2")
        menu()

def game(playerScore, computerScore):
    if playerScore != 5 and computerScore != 5:
        playerColour = int(input("What colour do you want to pick?\n1: Red\n2: Blue\n3: Yellow\n4: Green\n5: Purple\n"))
        computerColour = (random.randint(1,5))
        time.sleep(0.2)
        print("the computer's choice was ", computerColour)
        time.sleep(0.5)
        if playerColour == computerColour and playerColour in [1, 2, 3, 4, 5]:
            computerScore = (computerScore + 1)
            print("the computer has won the round. The computer's score is ", computerScore, " and the player's score is ", playerScore)
            time.sleep(0.5)
            game(playerScore, computerScore)
        elif playerColour != computerColour and playerColour in [1, 2, 3, 4, 5]:
            playerScore = (playerScore + 1)
            print("the player has won the round. The computer's score is ", computerScore, " and the player's score is ", playerScore)
            time.sleep(0.5)
            game(playerScore, computerScore)
        else:
            print("please enter a valid number between 1 and 5")
            time.sleep(0.5)
            game(playerScore, computerScore)
    else:
        if playerScore == 5:
            again = input("The player has won! Well done! \nWould you like to play again? Y or N:\n")
            time.sleep(0.5)
            if again == "Y" or again == "y":
                time.sleep(0.5)
                game(0, 0)
            elif again == "N" or again == "n":
                print("Thanks for playing, come again later")
                time.sleep(0.5)
                next
            else:
                print ("Please enter Y or N")
                time.sleep(0.5)
                game(playerScore, computerScore)
        elif computerScore == 5:
            again = input("The computer has won! Well done! \nWould you like to play again? Y or N:\n")
            time.sleep(0.5)
            if again == "Y" or again == "y":
                time.sleep(0.5)
                game(0, 0)
            elif again == "N" or again == "n":
                print("Thanks for playing, come again later")
                time.sleep(0.5)
                next
            else:
                print ("Please enter Y or N")
                time.sleep(0.5)
                game(playerScore, computerScore)
        
        

        
    

menu()
