usernames = {}
submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break
    action = command.split("-")

    if len(action) == 3:
        user, language, score = action[0], action[1], int(action[2])

        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

        if user not in usernames:
            usernames[user] = {language: score}
        else:
            if language not in usernames[user]:
                usernames[user][language] = score

            if usernames[user][language] < score:
                usernames[user][language] = score

    elif len(action) == 2:
        user = action[0]
        # usernames.pop(user)
        del usernames[user]

print("Results:")
for name in usernames:
    for results in usernames[name].values():
        print(f"{name} | {results}")

print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")
