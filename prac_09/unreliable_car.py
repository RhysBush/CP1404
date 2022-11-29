"""
CP1404 UnreliableCar class.
Rhys Bush
"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Represent a Car object."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(0, 101)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
