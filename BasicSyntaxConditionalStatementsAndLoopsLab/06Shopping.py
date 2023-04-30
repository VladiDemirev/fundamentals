budget = int(input())

while True:
    user_input = input()
    if user_input == "End":
        print("You bought everything needed.")
        break
    else:
        user_input = int(user_input)

    if user_input > budget:
        print("You went in overdraft!")
        break

    budget -= user_input




