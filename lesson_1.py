# 1️⃣ Write a program to check positive / negative / zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is possitive")
elif num <0:
    print("The number is negative")
else:
    print("the number is zero")
# 2️⃣ Write a program to find largest of 3 numbers
a= int(input("Enter a number:"))
b= int(input("Enter a number:"))
c= int(input("Enter a number:"))
if a>b and a>c:
    print(f"{a}is the lastest number")
elif b>a and b>c:
    print(f"{b} is the Lastest number")
else:
    print(f"{c} is the lastest number")
# 3️⃣ Create a simple calculator using if-elif
cal1 = int(input("Enter a number"))
cal2 = int(input("Enter a number"))
operation = input("enter operation(+,-,*,/)")
if operation == "+":
    print(cal1 + cal2)
elif operation == "-":
    print(cal1-cal2)
elif operation == "*":
    print(cal1*cal2)
elif operation == "/":
    print(cal1/cal2)
# 4️⃣ Take user details and print in formatted way
name = input("Enter your name:")
age = int(input("Enter your age:"))
course = input("enter your course:")
print("My name is",name)
print("My age is",age)
print("My course is",course)

