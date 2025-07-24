def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def main():
    print("Welcome to the Calculator!")
    while True:
        operation = input("Enter operation (add, subtract, multiply, divide) or 'exit' to quit: ").strip().lower()
        if operation == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        if operation in ['add', 'subtract', 'multiply', 'divide']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if operation == 'add':
                    result = add(num1, num2)
                elif operation == 'subtract':
                    result = subtract(num1, num2)
                elif operation == 'multiply':
                    result = multiply(num1, num2)
                elif operation == 'divide':
                    result = divide(num1, num2)
                print(f"The result is: {result}")
            except ValueError as e:
                print(f"Invalid input: {e}")
        else:
            print("Invalid operation. Please try again.")

if __name__ == "__main__":
    main()