import time

def addition(firstNumber, secondNumber):
    print(firstNumber + secondNumber)
#addition(int (input("what is the first number")), int(input("what is the second number")))

global_message = "Its a global variable"

def myFunction():
    print("\nthis is inside of a function")
    print(global_message)
    local_message = "Its a local variable"
    print(local_message)
#myFunction()
#print(global_message)
#print(local_message)

def checkIfPrime(number):
    for x in range(2, number):
        if (number%x==0):
            print ("False")
        print("True")
    
#checkIfPrime(2)

def name(firstname, age):
    print("Your name is " + firstname + " and you are " + age + " years old.")

#name(firstname = "tokyo", age = "16")

def numbers():
    n = 0
    while n <= 5000:
        print(n)
        n = n + 1
#numbers()

def equal0():
    time.sleep(1)
    n = 0
    while 0 == 0:
        while n <= 5:
            print(n)
            n = n + 1
        time.sleep(1)
        n = 0
    
#equal0()

def forloop():
    #nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #for i in nums:
        #print(i)
    for i = 1 to 10
        print (i)
    
#forloop()

