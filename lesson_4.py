try:
    num1 = int(input("enter fisrt number:"))
    num2 = int(input("enter Second number:"))
    result = num1 / num2
    print("the result is : " ,result)
except ZeroDivisionError:
    print("Enter a non zero number ")
except ValueError:
    print("Error: Please enter valid numbers")
else:
    print("Calculation successful")
finally:
    print("Program ended")