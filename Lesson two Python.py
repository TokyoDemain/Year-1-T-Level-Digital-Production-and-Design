def welcome():
    Name = (str)(input("what is your name"))
    print("hello " , Name , "!")

#welcome()
def Addition():
    num1 = 0
    num2 = 0
    num1 = (int)(input("what number do you want to start with?  "))
    num2 = (int)(input("what number do you want to add to the first number?  "))
    print("when two numbers added together is " , num1 + num2 , ". ")

#Addition()
def fizzBuzz():
    for i in range(51):
        string = ""
        print(i)
        if i % 3 == 0:
            string += "Fizz"
        if i % 5 == 0:
            string += "Buzz"
        if string:
            print(string)

#fizzBuzz()

def largestNumber():
    greatestNum = 0
    num1 = int(input("What number do you want to have as number one\n"))
    num2 = int(input("What number do you want to have as number two\n"))
    num3 = int(input("What number do you want to have as number three\n"))
    if num1 > num2:
        greatestNum = num1
    else:
        greatestNum = num2

    if num3 > greatestNum:
        greatestNum = num3
    else:
        greatestNum = greatestNum

    print(greatestNum)

#largestNumber()


    
array = [1, 2, 3, 4, 5]

def print_first_three():
    for i in range(3):
        print(array[i])

def reverse():
    array.reverse()
    print(array)

def get_occurrences():
    char = int(input("What number do you want to be your first number\n "))
    array.append(char)
    occur = 0
    for el in array:
        if el == char:
            occur += 1
    print("There are", occur, "mentions of", char)

def remove_index():
    index = int(input("Enter a index to remove"))
    del array[index]
    print(array)

print_first_three()
reverse()
get_occurrences()
remove_index()
