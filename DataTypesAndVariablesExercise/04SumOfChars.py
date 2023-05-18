num_lines = int(input())

total_sum = [ord(input()) for x in range(num_lines)]

print(f"The sum equals: {sum(total_sum)}")

#   OPTION 2
# num_lines = int(input())
# total_sum = 0
#
# for _ in range(num_lines):
#   letter = input()
#   number = ord(letter)
#   total_sum += number
#
# print(f"The sum equals: {total_sum}")

