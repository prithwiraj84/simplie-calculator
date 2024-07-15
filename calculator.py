def sum(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    opp = input("Enter the operator(+,-,*,/):")
    if opp == "+":
        print(sum(a,b))
    elif opp == "-":
        print(subtract(a,b))
    elif opp == "*":
        print(multiply(a,b))
    elif opp == "/":
        print(divide(a,b))
    else:
        print("Invalid input!!!")
    choice = input("Enter your choice whether you want to continue (Y/N):")
    if choice == "n" or choice == "N":
        break
