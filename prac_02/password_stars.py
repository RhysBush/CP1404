minimum_password_length = 10
is_password_strong = "false"
user_password = input("Your new password: ")
while is_password_strong == "false":
    if len(user_password) >= minimum_password_length:
        is_password_strong = "true"
    else:
        print(f"Password does not meet length requirement (> {minimum_password_length} characters)")
        user_password = input("Your new password: ")
print("*" * len(user_password))
