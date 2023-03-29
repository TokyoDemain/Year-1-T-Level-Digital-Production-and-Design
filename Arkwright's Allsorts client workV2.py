import time
import datetime
import ProductIDModule

def menu():
    run = str(input("what would you like to do, \n1: Make an entry and change stock amount \nor \n2:search"))
    if run == "1":
        EnterproductID()
    elif run == "2":
        search()
    else:
        print("Enter one of the two options")
        time.sleep(2)
        menu()

def EnterproductID():
    global productID
    productID = str(input("what is the 7 digit product ID: "))
    ProductIDModule.IDCheck(productID)
    productName = str(input("what is the product name: "))
    department = str(input("what department is the product in: "))
    warehouseLocation = str(input("Where is the product stored in the warehouse: "))
    stockAmount = str(input("How much is in stock before entry: "))
    priceExcVATTemp = float(input("What is the price excluding VAT: "))
    priceIncVATTemp = float(priceExcVATTemp * 1.20)
    priceExcVAT = str(priceExcVATTemp)
    priceIncVAT = str(priceIncVATTemp)
    e = datetime.datetime.now()
    date2 = (e.strftime("%d/%m/%Y"))
    time2 = (time.strftime("%H:%M"))
    date = (date2 , time2)
    date = str(date)

    changeStockOrAddProduct = input("Do you want to change to 1: stock numbers or 2: add an entry: ")
    if changeStockOrAddProduct == "1":
        stockAmount = int(stockAmount)
        stockIncrease = int(input("How much stock would you like to add: "))
        stockAmount = (stockAmount + stockIncrease)
        stockAmount = str(stockAmount)
        f = open("Database.txt" , "a")
        f.write("| ID: ")
        f.write(productID)
        f.write(" | Name: ")
        f.write(productName)
        f.write(" | Department: ")
        f.write(department)
        f.write(" | Warehouse Location: ")
        f.write(warehouseLocation)
        f.write(" | Stock Amount: ")
        f.write(stockAmount)
        f.write(" | Price Ex VAT: ")
        f.write(priceExcVAT)
        f.write(" | Price Inc VAT: ")
        f.write(priceIncVAT)
        f.write(" | Date and time of entry: ")
        f.write(date)
        f.write(" | \n")
        f.close()
    else:
        f = open("Database.txt" , "a")
        f.write("| ID: ")
        f.write(productID)
        f.write(" | Name: ")
        f.write(productName)
        f.write(" | Department: ")
        f.write(department)
        f.write(" | Warehouse Location: ")
        f.write(warehouseLocation)
        f.write(" | Stock Amount: ")
        f.write(stockAmount)
        f.write(" | Price Ex VAT: £")
        f.write(priceExcVAT)
        f.write(" | Price Inc VAT: £")
        f.write(priceIncVAT)
        f.write(" | Date and time of entry: ")
        f.write(date)
        f.write(" | \n")
        f.close()
            
        
        


def search():
    f = open("Database.txt" , "r")
    whichType = input("would you like to search for \n1:Product ID \n    or \n2:Product Name \n")
    if whichType == "1":
        word = str(input("what ID do you want to search for:  "))
        with open("Database.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.find(word) != -1:
                    print(line)
                else:
                    print("This item could not be found")
    elif whichType == "2":
        word = str(input("what name do you want to search for:  "))
        with open("Database.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.find(word) != -1:
                   print(line)
                else:
                    print("This item could not be found")
    else:
        print("Please enter 1 or 2")
        time.sleep(2)
        search()
menu()
