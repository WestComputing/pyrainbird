import os
from pyrainbird import RainbirdController
import logging

logging.basicConfig(filename='pypython.log', level=logging.DEBUG)

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
_LOGGER.addHandler(ch)

controller = RainbirdController(os.getenv("RAINBIRD_SERVER"),
                                os.getenv("RAINBIRD_PASSWORD"))
model = controller.get_model_and_version()
print(model)
zone_count = controller.zones.count
print(f"Zone count: {zone_count}"
      f" • {controller.get_available_stations(0)}")
print(f"Raining: {controller.get_rain_sensor_state()}"
      f" • Rain delay: {controller.get_rain_delay()}"
      f" • Current Irrigation: {controller.get_current_irrigation()}")
zone_states = dict()
for zone in range(zone_count):
    zone_states[zone + 1] = controller.get_zone_state(zone)
zone_text = ""
for zone, state in zone_states.items():
    zone_text += f"Zone {zone:02d} {'ON' if state else '--'}"
    if zone % 4 == 0:
        zone_text += '\n'
    else:
        zone_text += ' | '
print(zone_text[:-1])

# print(controller.stop_irrigation())
