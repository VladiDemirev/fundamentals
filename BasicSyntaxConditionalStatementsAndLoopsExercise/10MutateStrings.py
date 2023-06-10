string1 = input()
string2 = input()
list1 = [*string1]
list2 = [*string2]
mutant_string = []

for index1, letter1 in enumerate(list1):
    for index2, letter2 in enumerate(list2):

        if index1 == index2 and letter1 != letter2:
            list1[index1] = list2[index2]
            print(*list1, sep="")
