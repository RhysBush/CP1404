username = input("Enter name: ")
print("(H)ello\n"
      "(G)oodbye\n"
      "(Q)uit")
user_choice = input(">>> ")
while user_choice != "Q":
    if user_choice == "H":
        print(f"Hello, {username}")
    elif user_choice == "G":
        print(f"Goodbye, {username}")
    else:
        print("Invalid input, try again.")
    print("(H)ello\n"
          "(G)oodbye\n"
          "(Q)uit")
    user_choice = input(">>> ")
print("Finished.")
