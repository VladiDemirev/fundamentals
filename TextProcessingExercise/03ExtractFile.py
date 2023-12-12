# path_to_file = input().split("\\")

# file_name, extension = path_to_file[-1].split(".")

# print(f"File name: {file_name}")
# print(f"File extension: {extension}")


#  OPTION 2

path_to_file = input().split("\\")

file_args = path_to_file[-1].split(".")

extension = file_args.pop()
file_name = file_args

print(f"File name: {''.join(file_name)}")
print(f"File extension: {extension}")
