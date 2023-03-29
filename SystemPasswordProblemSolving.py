import time
import sys
#these import the time and the exit function
print("Password must include \n- 6 - 12 characters, atleast \n- One number and \n- One capital letter, \nand is suggested to use a symbol too\n")
#Tells the user what the password peramiters are
def systemPassword():
    password = str(input("What do you want as your password\n"))
    #askes the user what their password is
    if len(password) < 6:
        passwordshort = str("1")
        passwordlong = str("0")
    elif len(password) > 12:
        passwordlong = str("1")
        passwordshort = str("0")
    else:
        passwordlong = str("0")
        passwordshort = str("0")
    #creates variables to see if the password is too short or long

    res1 = any(chr.isdigit() for chr in password)
    res2 = any(ele.isupper() for ele in password)
    #checks if the password has numbers and letters in
    if res2 == False:
        noCapital = str("1")
    else:
        noCapital = str("0")
    if res1 == True:
        noNum = str("0")
    else:
        noNum = str("1")
    #creates a variable as a check to be used later to store if the password has numbers and letters
    
    if passwordshort == "1":
        print("Your password must be more that 5 characters long\n")
        time.sleep(0.2)
    #if statement to print that the password needs to be longer if the variables created before are true or not and print the problem if needed

    if passwordlong == "1":
        print("Your password must be less that 13 characters long\n")
        time.sleep(0.2)
    #if statement to print that the password needs to be shorter if the variables created before are true or not and print the problem if needed

    if noCapital == "1":
        print("Your password requires a capital letter\n")
        time.sleep(0.2)
    #if statement to print that the password needs to have capital letters in if the variables created before are true or not and print the problem if needed
    
    if noNum == "1":
        print("Your password requires a number\n")
        time.sleep(0.2)
    #if statement to print that the password needs to have numbers in if the variables created before are true or not and print the problem if needed

    if passwordshort == "0" and passwordlong == "0" and noCapital == "0" and noNum == "0":
        print("This password is strong\n")
        time.sleep(1)
        goAgain()
    #if statement that prints that there are no errors if all of the forementioned variables are false

    systemPassword()
    #loops the function if there are any errors

def goAgain():
    again = input("Do you want to go again? Y or N...\n")
    #asks if the user wants to try again
    if again == "Y" or again == "y":
        systemPassword()
    elif again == "N" or again == "n":
        sys.exit()
    else:
        print("please enter Y or N")
        goAgain()
    #if statement to check if the user wants to go again

    
systemPassword()
#starts the beggining function
