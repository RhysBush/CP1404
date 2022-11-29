"""
CP1404 Practical 09 - Taxi Simulator
Rhys Bush - 29/11/2022
Note: This file looks similar to the solution...because I leaned heavily on it to get this file done.
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_06.car import Car

MENU = "(Q)uit, (C)hoose taxi, (D)rive"


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    print("We go vroom vroom.")
    print(MENU)
    menu_choice = input(">>> ").upper()

    while menu_choice != "Q":
        if menu_choice == "C":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")

        elif menu_choice == "D":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("Distance to drive (km): "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost

            else:
                print("Get a taxi. Can't drive without one.")

        else:
            print("Invalid option.")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        menu_choice = input(">>> ").upper()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
