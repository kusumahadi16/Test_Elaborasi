num1 = 0
num2 = 1

prnt = str(num1) + " " + str(num2)
for i in range(9):
    print(prnt)
    inc = num1 + num2
    num1 = num2
    num2 = inc
    prnt += " " + str(num2)