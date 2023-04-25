user_input = float(input())

if user_input == 0:
    print("zero")
elif 1 <= user_input <= 1000000:
    print("positive")
elif -1000000 <= user_input <= -1:
    print("negative")
elif 0 < user_input < 1:
    print("small positive")
elif -1 < user_input < 0:
    print("small negative")
elif user_input > 1000000:
    print("large positive")
else:
    print("large negative")
