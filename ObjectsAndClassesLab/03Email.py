class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


email_list = []

command = input()

while command != "Stop":
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    email_list.append(email)

    command = input()

indices = [int(x) for x in input().split(", ")]

for index, email in enumerate(email_list):
    if index in indices:
        email_list[index].send()
    print(email.get_info())
