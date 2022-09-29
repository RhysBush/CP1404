"""Score grading stars"""


def main():
    user_score = float(input("Your score: "))
    menu_choice = input(f"(G)rading:\n"
                        "(S)tars:\n"
                        "(Q)uit:\n"
                        " > ").upper()
    while menu_choice != "Q":
        if menu_choice == "G":
            result = grade_user_score(user_score)
            print(result)
        elif menu_choice == "S":
            result = print_stars(user_score)
            print(result)
        else:
            print("Incorrect input.")
        menu_choice = input(f"(G)rading:\n"
                            "(S)tars:\n"
                            "(Q)uit:\n"
                            " > ").upper()


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


def print_stars(score):
    result = "*" * int(score)
    return result


main()
