from art import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations_dict = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))

    continue_calculation = True

    for operations in operations_dict:
        print(f"{operations}")

    while continue_calculation:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the next number?: "))
        perform_operation = operations_dict[operation_symbol](num1, num2)
        answer = perform_operation
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} & 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            continue_calculation = False
            calculator()


calculator()
 