# usernames = input().split(", ")

# for username in usernames:
#   if (
#     (3 <= len(username) <= 16) and
#     (username.isalnum() or (("_" in username) or ("-" in username)))
#   ):
#     print(username)


#  OPTION 2

from string import ascii_letters, digits

usernames = input().split(", ")
valid_chars = ascii_letters + digits + "-" + "_"

for username in usernames:
    if len(username) < 3 or len(username) > 16:
        continue
    for char in username:
        if char not in valid_chars:
            break
    else:
        print(username)
