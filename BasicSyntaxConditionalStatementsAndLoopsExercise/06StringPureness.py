number_n = int(input())
unpure_string = [",", ".", "_"]

for _ in range(number_n):
    string = input()
    if "," in string or "." in string or "_" in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
