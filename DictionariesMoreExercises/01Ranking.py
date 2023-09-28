# def contest_data(text):
#     contest_password = {}
#     while True:
#         if text == "end of contests":
#             break
#         contest, password = text.split(":")
#         contest_password[contest] = password
#         text = input()
#     return contest_password
#
#
# string = input()
# print(contest_data(string))

contest_password = {}
username_points = {}

while True:
    string = input()
    if string == "end of contests":
        break
    contest, password = string.split(":")
    contest_password[contest] = password

while True:
    string = input()
    if string == "end of submissions":
        break
    contest, password, username, points = string.split("=>")
    if contest in contest_password.keys() and contest_password[contest] == password:
        username_points[contest] = {username: points}
        # if username in username_points:
        #     if points > username_points[username][contest]:
        #         username_points[username][contest] = points


print(username_points)