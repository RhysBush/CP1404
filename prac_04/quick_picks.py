"""
CP1404 Practical
Quick Pick Program
"""

from random import randint
NUMBER_OF_COLUMNS = 6
MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 45
number_of_quick_picks = int(input("Number of quick picks to generate: "))
for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(NUMBER_OF_COLUMNS):
        number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        while number in quick_pick:
            number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick))
