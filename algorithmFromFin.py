import time
email = "Mark101gmail.com"
pw = "RETRY123"

log = input("Welcome user, what is your email:  ")

if log == email:
    log2 = input("what is your password?:  ")
    if log2 == pw:
        time.sleep(3)
        print("login authorized")
    else:
        print ("Try again")
else:
    print("Try again")
