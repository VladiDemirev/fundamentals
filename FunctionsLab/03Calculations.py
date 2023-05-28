operator = input()
integer1 = int(input())
integer2 = int(input())


def calculate():
    if operator == "multiply":
        return integer1 * integer2
    elif operator == "divide":
        return integer1 // integer2
    elif operator == "add":
        return integer1 + integer2
    elif operator == "subtract":
        return integer1 - integer2


print(calculate())
