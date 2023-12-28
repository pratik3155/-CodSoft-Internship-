'''
Task 2
Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.
'''
print("________Calculator_______")

num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number: "))

print("Press 1 for Addition\nPress 2 for Subtraction\nPress 3 for Multiplication\nPress 4 for Division")

choice = int(input("Enter your choice from 1-4: "))

if choice == 1:
    result = num1 + num2
    print(f"The Addition of given Numbers is: {result}")
elif choice == 2:
    result = num1 - num2
    print(f"The Subtraction of given Numbers is: {result}")
elif choice == 3:
    result = num1 * num2
    print(f"The Multiplication of given Numbers is: {result}")
elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print(f"The Division of given Numbers is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid Choice")
