# task 1
print("hello world")

# task 2
n = input("enter a number:")
print(n)

# task 3
num1 = input("enter first number:")
num2 = input("enter second number:")

print("sum is :",int(num1)+int(num2))

# task 4
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))

sum = num1 + num2 + num3
print("average is :",sum/3)

# task 5
a = 20
b= 30

b,a = a,b
print("values:", a,b)

# task 6
num1 = int(input("enter a number:"))

if(num1 < 0):
    print("value is negative")
else:
    print("value is positive")

# task 7
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))

if(num1 > num2):
    print("first number is greater than second number")
elif(num2 > num1):
    print("second number is greater than first number")
else:
    print("both are equal")

# Day 2

# task 1
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
print("1 for Addition \n2 for Subtraction \n3 for Multiplication \n4 for Division")
choice = int(input("enter your choice:"))
result = 0

if(choice == 1):
    result = num1 + num2
elif(choice == 2):
    result = num1 - num2
elif(choice == 3):
    result = num1 * num2
elif(choice == 4):
    result = num1 * num2
else:
    print("enter a valid choice")

print("the result is:",result)

# task 2
print("1 for Porotta \n2 for Biriyani \n3 for Fried Rice \n4 for Mandhi")
choice = int(input("enter your choice:"))

match choice:
    case 1:
        print("Porotta")
    case 2:
        print("Biriyani")
    case 3:
        print("Fried Rice")
    case 4:
        print("Mandhi")
    case _:
        print("Fool")

# task 3
num1 = int(input("enter a Number:"))
sum = 0
for i in range(1,num1):
    sum += num1
print("average:",sum/num1)

# task 4
num1 = int(input("enter a Number:"))

for i in range(1,num1):
    if (i % 2 == 0):
        print(i)

# task 5 prime number
num1 = int(input("enter a Number:"))
flag = 0
for i in range(2,num1//2):
    if (num1 % i == 0):
        flag = 1
        break
if (flag==0):
    print("prime number")
else:
    print("not prime number")

# task 6 pattern
n = int(input("enter a Number:"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")

# task 7
for i in range(6):
    print("hi")
    if(i==3):
        break
    print("hello")
print("finished")

# task 8
for i in range(6):
    print("hi")
    if(i==3):
        continue
    print("hello")
print("finished")
