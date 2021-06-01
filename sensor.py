"""Platform for sensor integration."""
from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.entity import Entity
import requests
import time

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    add_entities([MittVaccinSensor()])


class MittVaccinSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None
        self.lowest_min_age = 100
        self.next_update = 0

    def poll_mitt_vaccin(self):
        r = requests.get("https://booking-api.mittvaccin.se/clinique/1013/appointmentTypes")
        j = r.json()
        for entry in j:
            min_age = int(entry["min_age"])
            if entry["id"] != '17310' and min_age < self.lowest_min_age:
                self.lowest_min_age = int(entry["min_age"])

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Mitt Vaccin'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return "years"

    def update(self):
        """Fetch new state data for the sensor."""
        if self.next_update < time.time():
            self.poll_mitt_vaccin()
            self.next_update = time.time() + 3600  # schedule next update in 1 hour

        self._state = self.lowest_min_age
