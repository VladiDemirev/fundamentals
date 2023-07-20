# def loading_bar(integer):
#     loading_list = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
#     index = 0
#     for num in range(0, integer, 10):
#         loading_list[index] = "%"
#         index += 1
#     if integer < 100:
#         return f"{integer}% [{''.join(loading_list)}] \nStill loading..."
#     return f"{integer}% Complete! \n[{''.join(loading_list)}]"
#
#
# number = int(input())
#
# print(loading_bar(number))


#   OPTION 2

def loading_bar(integer):
    if integer == 100:
        return "100% Complete! \n[%%%%%%%%%%]"
    return f"{integer}% [{'%' * (integer // 10)}{'.' * (10 - (integer // 10))}] \nStill loading..."


number = int(input())

print(loading_bar(number))
