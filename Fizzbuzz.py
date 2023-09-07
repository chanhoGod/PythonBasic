inputnum = int(input("숫자는?"));
intarr = []
for i in range(1, inputnum + 1):
    if ((i % 3 == 0) & (i % 5 == 0)):
        intarr.append("FizzBuzz")
    elif (i % 3 == 0):
        intarr.append("Fizz")
    elif (i % 5 == 0):
        intarr.append("Buzz")
    else:
        intarr.append(str(i))

print(intarr)