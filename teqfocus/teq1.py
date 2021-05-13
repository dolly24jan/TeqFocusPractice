num = list(range(10))           #List of numbers
num1 = 0                             #Previous Number
for i in num:                       # i for current Number
    sum = num1 + i               #Sum of numbers
    print("Current Number "+ str(i) + " Previous Number "+" "+ str(num1) + "Sum :" +" " + str(sum))
    num1=i
