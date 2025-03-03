import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def square_root(x):
    if x < 0:
        return "Error! Square root of a negative number is not defined."
    return math.sqrt(x)
def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")

    while True:
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")

        elif choice == '5':
            try:
                num = float(input("Enter a number for square root: "))
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
                continue

            print(f"Result: {square_root(num)}")
        else:
            print("Invalid choice! Please select a valid operation.")

        next_calc = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if next_calc != 'yes':
            print("Thank you for using the calculator!")
            break

# Run the calculator function
calculator()