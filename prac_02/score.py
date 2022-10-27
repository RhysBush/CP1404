"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

from random import randint


def main():
    user_score = float(input("Enter score: "))
    random_score = randint(0, 100)
    user_result = grade_user_score(user_score)
    random_result = grade_user_score(random_score)
    # Print user and random results on separate lines
    print(f"{user_result}\n{random_result}")


def grade_user_score(score):
    if 0 <= score <= 100:
        if score >= 90:
            result = "Excellent"
        elif score >= 50:
            result = "Passable"
        else:
            result = "Bad"
    else:
        result = "Invalid score"
    return result


main()
