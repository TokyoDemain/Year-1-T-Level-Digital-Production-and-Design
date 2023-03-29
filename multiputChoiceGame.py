print("welcome to the game")


def choice1():
    choice = input("your at a party and your friends are going home. \n1. Get a taxi\n or\n2. Walk home")
    if choice == "1":
        print("You have no money, you'll have to walk")
        choice2()
    elif choice == "2":
        choice2()
        
def choice2():
    choice = input("would you like to walk throught the \n1. woods \nor \n2. the road")
    if choice == "1":
        print("the woods are quiet tonight, you should be fine")
        choice3()
    elif choice == "2":
        print ("you begin to walk through the woods")
        choice4()

def choice3():
    choice = input("there are two paths, \n1. Left or \n 2. Right")
    



choice1()
