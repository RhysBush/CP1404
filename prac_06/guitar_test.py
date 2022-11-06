from guitar import Guitar


def run_tests():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    another = Guitar("Another Guitar", 2013, 100)

    print(f"{guitar.name} get_age() - Expected 100. Got {guitar.get_age()}")
    print(f"{another.name} get_age() - Expected 9. Got {another.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")


if __name__ == "__main__":
    run_tests()
