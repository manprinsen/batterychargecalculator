from ._anvil_designer import Form2Template
from anvil import *

class Form2(Form2Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def button_calc_click(self, **event_args):
        if self.text_box_hours.text == None:
            alert("Please enter charge time")
            return
        if self.text_box_power.text == None:
            alert("Please enter charge speed")
            return
        power = float(self.text_box_power.text)
        hours = float(self.text_box_hours.text)
        energy_raw = power * hours
        energy = round(energy_raw, 2)
        self.label_energy.text = f"""After {hours} hours, the battery will be charged with {energy} kWh"""