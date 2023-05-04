while True:
    string = input()
    if string == "End":
        break
    result = [(char + char) for char in string]
    if string != "SoftUni":
        print(*result, sep="")
