"""
CP1404 Prac 09
Silver Service Taxi
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, reliability, fanciness):
        super().__init__(name, fuel)
        self.reliability = reliability
        self.price_per_km *= fanciness

    def get_fare(self):
        return super().get_fare() + self.flagfall

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"
