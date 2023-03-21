# define set of functions
def add(a, b):
    """returns sum of two numbers"""
    return a + b


def multiply(a, b):
    """returns product of two numbers"""
    return a * b


def sub(a, b):
    """returns subtraction of two numbers"""
    return a - b


def Div(a, b):
    """returns division of two numbers"""
    return a / b


# ask user for inputs
a = int(input("Enter first number: "))
b = int(input("Enter next number: "))


def calculator_opr():
    # ask for type of operation
    operators = {
        '*': multiply,
        '-': sub,
        '+': add,
        '/': Div
    }

    # show user list of operators
    print("list of operators available are following: ")
    for key, value in operators.items():
        print(key)

    # ask user to opt an operator
    operator = input("Please type of operation: ")

    # execute operation
    return operators[operator](a, b)


# store output of output function
output = calculator_opr()

# flagging
is_continue = True
# ask user whether he wants to continue or not
while is_continue:
    ask_user = input("Do you want to continue with output,type Y or N: ").lower()
    if ask_user == "y":
        a = output
        b = int(input("Enter next number: "))
        output = calculator_opr()

    else:
        is_continue = False
print(f"Output = {output}")
