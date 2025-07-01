# Simple Calculator

def main():
    print("Simple Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Enter choice (1/2/3/4 or +, -, *, /): ")

    if choice in ('1', '+'):
        result = num1 + num2
        op = '+'
    elif choice in ('2', '-'):
        result = num1 - num2
        op = '-'
    elif choice in ('3', '*'):
        result = num1 * num2
        op = '*'
    elif choice in ('4', '/'):
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        op = '/'
    else:
        print("Invalid input. Please select a valid operation.")
        return

    print(f"{num1} {op} {num2} = {result}")

if __name__ == "__main__":
    main()
