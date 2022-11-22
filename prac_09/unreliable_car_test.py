"""
Tests for the "unreliable car" program.
"""

from prac_09.unreliable_car import UnreliableCar


def run_tests():
    """Test various unreliable cars."""
    perfect_car = UnreliableCar("Perfecto", 100, 101)
    average_car = UnreliableCar("Ford Ranger", 100, 50)
    bad_car = UnreliableCar("Tesla Model X", 100, 5)

    print(f"{perfect_car} drove {perfect_car.drive(5)}km")
    print(f"{average_car} drove {average_car.drive(5)}km")
    print(f"{bad_car} drove {bad_car.drive(5)}km")

    print(perfect_car)
    print(average_car)
    print(bad_car)


if __name__ == "__main__":
    run_tests()
