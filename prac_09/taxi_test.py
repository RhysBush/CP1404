"""
Rhys Bush - Test Taxi...tests!
Expected time:  minutes.
Actual time:   minutes.
"""

from taxi import Taxi


def run_tests():
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(f"{my_taxi.__str__()}. Current fare: ${my_taxi.get_fare()}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi.__str__()}. Current fare: ${my_taxi.get_fare()}")


if __name__ == '__main__':
    run_tests()
