"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur when an invalid entry is input (anything other than an integer). For example: "a", "0.1", " "
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur when the program attempts to divide by zero, which is undefined.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, you can by using an "if" statement to check if the denominator is 0. If so, print "Undefined" and exit.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        fraction = "Undefined."
    else:
        fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
