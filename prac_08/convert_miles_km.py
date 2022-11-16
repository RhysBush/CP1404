"""
Rhys Bush - Miles to Kilometres Converter
Expected time: 20 minutes.
Actual time: 40 minutes.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_TO_KM_FACTOR = 1.609


class MilesToKilometresConverter(App):
    output_km = StringProperty()

    def build(self):
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self, text):
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        self.output_km = str(miles * MILES_TO_KM_FACTOR)

    @staticmethod  # Taken from solution - removes static error
    def convert_to_number(text):
        try:
            return float(text)
        except ValueError:
            return 1.0


MilesToKilometresConverter().run()
