a = [1, 2, 3, 4, 5]

findNum = int(input("what numben do you want to find\n"))


if findNum in a:
    print("your number is in there\n")
else:
    print("not in list\n")



largest = max(a)
print(largest , "is the largest number\n")


sum = 0
for i in a:
    sum = sum + i


print(sum , "is the sum of all numbers\n")
