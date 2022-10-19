email_to_name = {}
email = input("Email: ")
while email != "":
    confirmation = input(f"Is your name {email}?(Y/n) ")
    email_to_name[email] = email
    email = input("Email: ")

for email in email_to_name:
    print(f"{email_to_name.get(email)} ({email})")
