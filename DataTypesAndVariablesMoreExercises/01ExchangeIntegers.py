def exchange_integers(a, b):
    temp_number = a
    # print("Before:")
    # print(f"a = {a}")
    # print("a =", a) - OPTION 2
    # print(f"b = {b}")
    print("Before:\na =", a, "\n b =", b)
    a = b
    b = temp_number
    print("After:")
    print(f"a = {a}")
    print(f"b = {temp_number}")


integer1 = int(input())
integer2 = int(input())
exchange_integers(integer1, integer2)
