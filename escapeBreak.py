import time
def breakFunction():
    j = 0
    for i in range(6):
        j = j + 2
        print("i = ", i, "j = ", j)
        if j == 10:
            break
breakFunction()

def continueFunction():
    s = 0
    for i in range(5):
        s = s + 2
        print("\ni = ", i, "s = ", s)
        if s == 8:
            continue
        print ("this line will be skipped if s = 8")

continueFunction()

def errorFunction():
    try:
        answer = 12/0
        print (answer)
    except:
        print("\n\ner error occurred")
errorFunction()

def finalCode():
    s = 1
    for i in range(10000):
        s = (s *2)
        print (s)
        
finalCode()

