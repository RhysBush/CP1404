"""
CP1404 Band exercise
Estimated time: 30 minutes.
Actual time:
Rhys Bush
"""


class Band():

    def __init__(self, name=""):
        self.name = name
        self.band = []

    def __str__(self):
        """Return a string representation of a Musician."""
        return f"{self.name} ({self.band})"

    def __repr__(self):
        return str(self.__str__())

    def add(self, musician):
        self.band.append(musician)

    def play(self):
        if not self.band:
            return f"{self.name} needs an instrument!"
        return f"{self.name} is playing: {self.band[0]}"
