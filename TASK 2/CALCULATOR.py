while True:
    print("Options:")
    print("Enter '+', '-', '*', or '/' to perform the corresponding operation")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break

    if user_input in ("+", "-", "*", "/"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = {
                '+': num1 + num2,
                '-': num1 - num2,
                '*': num1 * num2,
                '/': num1 / num2 if num2 != 0 else "Cannot divide by zero",
            }.get(user_input, "Invalid operator")
            print("Result:", result)
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    else:
        print("Invalid input. Please enter a valid operation.")
