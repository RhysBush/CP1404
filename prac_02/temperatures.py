"""Convert between Celsius and Fahrenheit."""


def main():
    menu_choice = input("(F)ahrenheit to Celsius\n"
                        "(C)elsius to Fahrenheit\n"
                        " >> ").upper()
    while menu_choice != "Q":
        if menu_choice == "F":
            fahrenheit_input = float(input("Fahrenheit: "))
            celsius_output = convert_fahrenheit_to_celsius(fahrenheit_input)
            print(f"{fahrenheit_input:.2f}f is {celsius_output:.2f}c.")
        elif menu_choice == "C":
            celsius_input = float(input("Celsius: "))
            fahrenheit_output = convert_celsius_to_fahrenheit(celsius_input)
            print(f"{celsius_input:.2f}c is {fahrenheit_output:.2f}f.")
        else:
            print("Invalid choice, please try again.")
        menu_choice = input("(F)ahrenheit to Celsius\n"
                            "(C)elsius to Fahrenheit\n"
                            " > ").upper()


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius_output = 5 / 9 * (fahrenheit - 32)
    return celsius_output


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit_output = celsius * 9.0 / 5 + 32
    return fahrenheit_output


main()
