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
