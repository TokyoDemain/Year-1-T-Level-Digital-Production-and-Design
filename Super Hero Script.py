play = "Y"

while play == "Y":
    print("\n\nChoose one of the super heroes between: \nBatman\nWonder Woman\nThe Flash\nSuper Man\n\n")
    Superpowers = input("\nDo they have superpowers? Y or N\n")
    if Superpowers == "Y":
        Male = input("\nAre they male? Y or N\n")
        if Male == "Y":
            Fly = input("\nCan they fly? Y or N\n")
            if Fly == "Y":
                print("Your hero is Super Man\n")
            elif Fly == "N":
                print("Your hero is The Flash\n")
            else:
                print("You can only enter Y or N ")
        elif Male == "N":
            print("Your hero is Wonder Woman\n")
        else:
            print("You can only enter Y or N ")
    elif Superpowers == "N":
        print("Your hero is batman\n")
    else:
        print("You can only enter Y or N ")

        
    enjoy = input("\nDid you enjoy your game? Y or N ")
    if enjoy == "Y":
        print("I am glad to hear that")
    elif enjoy == "N":
        print("I am sorry to hear that")
    else:
        print("You can only enter Y or N ")
        

    playCheck = input("\nSDo you want to play again? Y or N ")
    if playCheck == "Y":
        play = "Y"
    elif playCheck == "N":
        play = "N"
    else:
        print("you can only enter Y or N ")
