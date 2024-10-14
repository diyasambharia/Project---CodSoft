def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero."

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operations = {
        '1': ('+', add),
        '2': ('-', subtract),
        '3': ('*', multiply),
        '4': ('/', divide)
    }

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in operations:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            operator, operation = operations[choice]
            result = operation(num1, num2)
            print(f"{num1} {operator} {num2} = {result}")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != "yes":
                print("Thank you for using the calculator!")
                break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
