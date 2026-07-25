def calculate():

    print("\n===== Calculator =====")

    try:
        num1 = float(input("Enter First Number: "))
        operator = input("Enter Operator (+, -, *, /): ")
        num2 = float(input("Enter Second Number: "))

        if operator == "+":
            print("Result =", num1 + num2)

        elif operator == "-":
            print("Result =", num1 - num2)

        elif operator == "*":
            print("Result =", num1 * num2)

        elif operator == "/":
            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("Division by zero is not allowed.")

        else:
            print("Invalid Operator!")

    except ValueError:
        print("Please enter valid numbers.")