"""Functions to test knowledge of reading lines from files."""

# Question 1:
out_file = open("name.txt", "w")
user_name = input("Please enter your name: ")
print(user_name, file=out_file)
out_file.close()

# Question 2:
in_file = open("name.txt", "r")
user_name = in_file.read().strip()
print(f"Your name is {user_name}")
in_file.close()

# Question 3:
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
total = number1 + number2
print(total)
in_file.close()

# Question 4:
total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()
