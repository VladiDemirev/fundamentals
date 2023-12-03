# sequence = input().split()

# result = [(word * len(word)) for word in sequence]
# print(''.join(result))


#  OPTION 2

# result = [(word * len(word)) for word in input().split()]
# print(''.join(result))


#  OPTION 3

print(''.join([(word * len(word)) for word in input().split()]))