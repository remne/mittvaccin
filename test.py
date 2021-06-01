"""

import requests
import pprint
import time

class ExampleSensor():

    def __init__(self):
        self._state = None
        self.lowestMinAge = 100
        self.next_update = 0

    def doRequestToMittVaccin(self):
        r = requests.get("https://booking-api.mittvaccin.se/clinique/1013/appointmentTypes")
        j = r.json()
        for entry in j:
            min_age = int(entry["min_age"])
            if entry["id"] != '17310' and min_age < self.lowestMinAge:
                self.lowestMinAge = int(entry["min_age"])

    @property
    def name(self):
        return 'Example Temperature'

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return TEMP_CELSIUS

    def update(self):
        if self.next_update < time.time():
            self.doRequestToMittVaccin()
            self.next_update = time.time() + 3600  # schedule next update in 1 hour
            print("do update!")
        self._state = self.lowestMinAge


def main():
    sensor = ExampleSensor()
    sensor.update()
    while True:
        time.sleep(1)
        sensor.update()


if __name__ == "__main__":
    main()
"""