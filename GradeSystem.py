def grade():
    name = str(input("What is the student's name: "))
    score = int(input("What is " + name + "'s score: "))
    date = input("What date was the test taken: ")
    test = input("What was the test on: ")
    
    if score < 40:
        print("Fail")
        grade = ("F")
    elif score < 50:
        print(name + "'s grade is a D")
        grade = ("D")
    elif score < 60:
        print(name + "'s grade is a C")
        grade = ("C")
    elif score < 70:
        print(name + "'s grade is a B")
        grade = ("B")
    elif score < 80:
        print(name + "'s grade is an A")
        grade = ("A")
    else:
        print(name + "'s grade is an A*")
        grade = ("A*")

    score = str(score)


    def saveToFile():
        f = open("scores.txt", "a")
        f.write(name)
        f.write(": ")
        f.write(score)
        f.write(" | Grade: ")
        f.write(grade)
        f.write(" | Date: ")
        f.write(date)
        f.write(" | Subject: ")
        f.write(test)
        f.write(" |")
        f.write("\n")
        f.close()

    saveToFile()

grade()
