from ._anvil_designer import Form2Template
from anvil import *

class Form2(Form2Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def button_calc_click(self, **event_args):
        if self.slider_minutes.value == None:
            alert("Please enter charge time")
            return
        if self.slider_power.value == None:
            alert("Please enter charge speed")
            return
        power = float(self.slider_power.value)
        minutes = int(self.slider_minutes.value)
        hours = float(self.slider_minutes.value) / 60
        energy_raw = power * hours
        energy = round(energy_raw, 2)
        self.label_energy.text = f"""After {minutes} minutes, the battery will be charged with {energy} kWh"""