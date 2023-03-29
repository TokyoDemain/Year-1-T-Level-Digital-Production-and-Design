def dictionaryMoment():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    
    print(dict(zip(keys, values)))
    
    sampleDict = {
        "class":{
            "student":{
                "name":"Mike",
                "marks":{
                    "physics":70,
                    "history":80
                }
            }
        }
    }


def dictionaryMoment():
    print(str(sampleDict["class"]["student"]["marks"]["history"]))



    deleteChallangeDict = {
        "name": "Kelly",
        "age":25,
        "salary": 8000,
        "city": "new york"

    }
    keysToRemove = ["name", "salary"]


    print(dict(deleteChallangeDict.items() - keysToRemove.items()))


data = "some data to save"

def read():
    with open("data.txt", "r") as file:
        file.close()

def write():
    with open("data.txt", "w") as file:
        file.write(data + "\n")
        file.close

def append():
    with open("data.txt", "a") as file:
        file.write(data + "\n")
        file.close()

#read()
#write()
#append()

def fileTaskOne():
    with open("file1.txt", "r") as file:
        file.write(data + "\n")
        file.close

fileTaskOne()

def fileTaskTwo():
    with open("file2.txt", "r") as file:
        file.write(file2 + "\n")
        file.close
        
