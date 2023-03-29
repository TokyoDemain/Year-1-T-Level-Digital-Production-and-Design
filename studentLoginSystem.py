import csv
import time

def Login():
    username = input("Username : ")
    time.sleep(0.5)
    password = input("Password : ")
    time.sleep(0.5)
    with open("C:/Users/M2202787/OneDrive - Middlesbrough College/Documents/GitHub/Year-1-T-Level-MbroColl/Student Login System/studentLoginSystem.csv" , "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if username and password in row:
                time.sleep(0.5)
                print("access granted\n")
                Menu()
            else:
                time.sleep(0.5)
                print("Login Failed")
                Login()

def Menu():
    choice = input("Menu:\n1: Search For Students\n2: Add Student Database\n3: Logout")
    if choice == "1":
        time.sleep(0.5)
        Search()
    elif choice == "2":
        time.sleep(0.5)
        AddStudent()
    elif choice == "3":
        Logout()
    else:
        print("please enter 1, 2 or 3")
        time.sleep(0.5)
        Menu()

def AddStudent():
    print("Welcome to the Add Student Function!")
    studentFirstName = input("What is the student you want to add's first name: ")
    time.sleep(0.1)
    studentLastName = input("What is the student you want to add's last name: ")
    time.sleep(0.1)
    studentTutorGroup = input("What is the student's Tutor group: ")
    time.sleep(0.1)
    studentID = input("What is the student's ID: ")
    time.sleep(0.1)
    studentEmail = input("What is the student's school email: ")
    time.sleep(0.1)
    studentDOB = input("What is the student's Date Of Birth: ")
    time.sleep(0.1)
    studentAddress = input("What is the student's Address: ")
    time.sleep(0.1)
    studentHomeNumber = input("What is the student's Home Phone Number: ")
    time.sleep(0.1)
    studentGender = input("What is the student's Gender: ")
    time.sleep(0.1)
    with open("C:/Users/M2202787/OneDrive - Middlesbrough College/Documents/GitHub/Year-1-T-Level-MbroColl/Student Login System/studentInfo.csv", "a") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow([studentFirstName, studentLastName, studentID, studentTutorGroup, studentEmail, studentDOB, studentAddress, studentHomeNumber, studentGender])
        time.sleep(0.1)
        print("Items have been added to the csv file")
        time.sleep(0.5)
        logoutChoice = input("Would you like to \n1: logout or \n2: go back to the menu? \n1 or 2: \n")
    if logoutChoice == "1":
        Logout()
    elif logoutChoice == "2":
        Menu()
            

def Search():
    print("Welcome to the Search Function")
    time.sleep(0.5)
    field = input("input what student info you want to search for")
    time.sleep(0.5)
    with open("C:/Users/M2202787/OneDrive - Middlesbrough College/Documents/GitHub/Year-1-T-Level-MbroColl/Student Login System/studentInfo.csv", "r") as file:
        csvreader = csv.reader(file)
        a = int(0)
        for row in csvreader:
            if field in row:
                a = a + 1
                print(row)
        if a == 0:
            print("There is no student on record with this information")
        else:
            next
        
    time.sleep(0.5)
    logoutChoice = input("Would you like to \n1: logout \nor \n2: go back to the menu? \n1 or 2: \n")
    if logoutChoice == "1":
        Logout()
    elif logoutChoice == "2":
        Menu()

def Logout():
    choice = input("\n\nAre you sure you would you like to logout? Y or N\n")
    if choice == "Y" or "y":
        time.sleep(0.5)
        print("You are now logged out")
        time.sleep(0.5)
        Login()
    elif choice == "N" or "n":
        time.sleep(0.5)
        print("OK, you will now be sent back to the menu.\n")
        time.sleep(0.5)
        Menu()
    else:
        print("Please enter Y or N.\n")
        
    
Login()
