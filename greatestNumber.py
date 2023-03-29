def game():
    num1 = float(input("what is your first number"))
    num2 = float(input("what is your second number"))
    num3 = float(input("what is your third number"))

    if num1 > num2:
        if num1 > num3:
            print(num1, " is the largest")
        else:
            print(num2, " is the largest")
    elif num2 > num1:
        if num2 > num3:
            print(num2, "is the largest")
        else:
            print(num3, "is the largest")
    elif num3 > num1:
        if num3 > num2:
            print(num3, "is the largest")
        else:
            print(num2, "is the largest")
    
game()
