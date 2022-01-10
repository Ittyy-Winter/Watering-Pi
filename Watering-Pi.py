from classes import Hardware
from classes import TimeKeeper as TK
from parinya import LINE
import time

# WATERING_TIME must be in "00:00:00 PM" format
WATERING_TIME = '3:03:00 PM'
SECONDS_TO_WATER = 10
RELAY = Hardware.Relay(16, False)
line = LINE('mjTkdeP1Zx4OJF8XH469iha0dpzMbBRDea05AIIMO1J')

def water_plant(relay, seconds):
    relay.on()
    line.sendtext("Plant is being watered!")
    time.sleep(seconds)
    line.sendtext("Watering is finished!")
    relay.off()

def main():
    time_keeper = TK.TimeKeeper(TK.TimeKeeper.get_current_time())
    if(time_keeper.current_time == WATERING_TIME):
        water_plant(RELAY, SECONDS_TO_WATER)
        time_keeper.set_time_last_watered(TK.TimeKeeper.get_current_time())

while True:
    time.sleep(1)
    main()