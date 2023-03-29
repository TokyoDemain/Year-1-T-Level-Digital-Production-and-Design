def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(n = int(input("what number do you want to double")))

print(mydoubler(11))
