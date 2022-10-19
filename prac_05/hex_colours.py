COLOUR_CODES = {"AliceBlue": "#f0f8ff"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print(f"{colour_name} has a hexadecimal value of {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ")
