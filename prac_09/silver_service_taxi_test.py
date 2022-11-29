"""
CP1404 - Prac 09
Tests for silver service taxi program.
Rhys Bush
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def run_tests():
    cool_silver_service_taxi = SilverServiceTaxi("Coolio Mobilio", 100, 100, 2)

    cool_silver_service_taxi.drive(18)
    print(cool_silver_service_taxi)
    print(cool_silver_service_taxi.get_fare())


if __name__ == "__main__":
    run_tests()
