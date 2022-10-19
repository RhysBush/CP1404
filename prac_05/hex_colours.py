COLOUR_CODES = {"Brick Red": "#cb4154", "Burnt Orange": "#cc5500", "Lemon Yellow": "#fff44f", "Mint Green": "98ff98",
                "Alice Blue": "#f0f8ff", "Indigo": "#4b0082", "Violet": "#d02090", "Dutch White": "#efdfbb",
                "Black Coffee": "#3b2f2f", "Ash Grey": "#b2beb5"}

colour_name = input("Enter a colour name: ").title()
while colour_name != "":
    print(f"{colour_name} has a hexadecimal value of {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ").title()
