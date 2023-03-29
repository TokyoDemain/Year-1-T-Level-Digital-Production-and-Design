minutes = int(input("what numbeer of minutes do you want to convert into seconds? "))
seconds = minutes * 60
print (seconds)


number1 = int(input("what number do you want as you first number? "))
number2 = int(input("what number do you want to add to the first number? "))
total = (number1 + number2)
print(total)


years = int(input("what numbeer of years do you want to convert into days? "))
days = years * 360
print (days)


alphabet_short = ["s" , "j" , "f" , "g"]

if input("what letter do you want to search for? ")in alphabet_short:
    print("it is in there")
else:
    print("it is not in there")
