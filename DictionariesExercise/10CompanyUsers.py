company_users = {}

while True:
    command = input()
    if command == "End":
        break
    company_name, employee_id = command.split("->")

    if company_name not in company_users:
        company_users[company_name] = [employee_id]
    else:
        if employee_id not in company_users[company_name]:
            company_users[company_name].append(employee_id)

for company in company_users:
    print(f"{company}")
    for user_id in company_users[company]:
        print(f"--{user_id}")
