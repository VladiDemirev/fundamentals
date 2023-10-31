def list_manipulator(input_list):
    even_list = [x for x in input_list if x % 2 == 0]
    odd_list = [x for x in input_list if x % 2 != 0]
    reversed_list = list(reversed(input_list))
    while True:
        command = input()
        if command == "end":
            break
        action, *params = command.split()

        if action == "exchange":
            index = int(params[0])
            if index in range(len(input_list)):
                input_list = input_list[(index + 1):] + input_list[:(index + 1)]
                reversed_list = list(reversed(input_list))
            else:
                print("Invalid index")

        elif action == "max":
            if params[0] == "even":
                if even_list:
                    max_even = max(even_list)
                    max_even_index = reversed_list.index(max_even)
                    max_even_reverse_index = (len(input_list) - 1) - max_even_index
                    print(max_even_reverse_index)
                else:
                    print("No matches")
            elif params[0] == "odd":
                if odd_list:
                    max_odd = max(odd_list)
                    max_odd_index = reversed_list.index(max_odd)
                    max_odd_reverse_index = (len(input_list) - 1) - max_odd_index
                    print(max_odd_reverse_index)
                else:
                    print("No matches")

        elif action == "min":
            if params[0] == "even":
                if even_list:
                    min_even = min(even_list)
                    min_even_index = reversed_list.index(min_even)
                    min_even_reverse_index = (len(input_list) - 1) - min_even_index
                    print(min_even_reverse_index)
                else:
                    print("No matches")
            elif params[0] == "odd":
                if odd_list:
                    min_odd = min(odd_list)
                    min_odd_index = reversed_list.index(min_odd)
                    min_odd_reverse_index = (len(input_list) - 1) - min_odd_index
                    print(min_odd_reverse_index)
                else:
                    print("No matches")

        elif action == "first":
            first_even = []
            first_odd = []
            count = int(params[0])
            if count > len(input_list):
                print("Invalid count")
            elif params[1] == "even":
                counter = 0
                for number in input_list:
                    if number % 2 == 0:
                        first_even.append(number)
                        counter += 1
                        if counter == count:
                            break
                print(first_even)
            elif params[1] == "odd":
                counter = 0
                for number in input_list:
                    if number % 2 != 0:
                        first_odd.append(number)
                        counter += 1
                        if counter == count:
                            break
                print(first_odd)

        elif action == "last":
            last_even = []
            last_odd = []
            count = int(params[0])
            if count > len(input_list):
                print("Invalid count")
            elif params[1] == "even":
                counter = 0
                for number in reversed_list:
                    if number % 2 == 0:
                        last_even.append(number)
                        counter += 1
                        if counter == count:
                            break
                print(list(reversed(last_even)))
            elif params[1] == "odd":
                counter = 0
                for number in reversed_list:
                    if number % 2 != 0:
                        last_odd.append(number)
                        counter += 1
                        if counter == count:
                            break
                print(list(reversed(last_odd)))
    return input_list


integer_list = [int(x) for x in input().split()]
print(list_manipulator(integer_list))
