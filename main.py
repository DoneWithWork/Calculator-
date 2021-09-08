# Simple console based calculator in Python
print("Welcome to simple console-based calculator")

number1 = 0
number2 = 0


def restart():
    global number1, number2
    replay = str(input("Do you want to restart the programme? (y/n): "))
    if replay == "y":
        number1 = 0
        number2 = 0
        main()
    elif replay == "n":
        print("Goodbye")
        quit()
    else:
        print("Please enter a correct answer!!")
        restart()


def Add():
    print("You have chosen addition")
    print("Your answer is:", number1 + number2)
    restart()


def Minus():
    print("You have chosen minus")
    print("Your answer is:", number1 - number2)
    restart()


def Times():
    print("You have chosen Times")
    print("Your answer is:", number1 * number2)
    restart()


def Divide():
    print("You have chosen divide")
    print("Your answer is:", number1 / number2)
    restart()


def GetInput():
    print("Pick one of the following operators.")
    print("Times = *")
    print("Divide = /")
    print("Plus = +")
    print("Minus = -")
    operator = str(input("Which operator do you want to pick?: "))
    if operator == "*":
        Times()
    elif operator == "/":
        Divide()
    elif operator == "+":
        Add()
    elif operator == "-":
        Minus()
    else:
        print("Please enter a correct operator!!")
        GetInput()


def main():
    global number1, number2
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    number1 = num1
    number2 = num2
    GetInput()


if __name__ == "__main__":
    main()
