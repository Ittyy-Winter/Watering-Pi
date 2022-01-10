from classes import Hardware
from classes import TimeKeeper as TK
import schedule
import smtplib
import time
import ssl

# WATERING_TIME must be in "00:00:00 PM" format
WATERING_TIME = '11:59:50 AM'
SECONDS_TO_WATER = 10
RELAY = Hardware.Relay(12, False)
EMAIL_MESSAGES = {
    'last_watered': {
        'subject': 'Raspberry Pi: Plant Watering Time',
        'message': 'Your plant was last watered at'
    },
    'check_water_level': {
        'subject': 'Raspberry Pi: Check Water Level',
        'message': 'Check your water level!',
    }
}

def send_last_watered_email(time_last_watered):
    message = EMAIL_MESSAGES['last_watered']['message']
    subject = EMAIL_MESSAGES['last_watered']['subject']

def send_check_water_level_email():
    message = EMAIL_MESSAGES['check_water_level']['message']
    subject = EMAIL_MESSAGES['check_water_level']['subject']

def water_plant(relay, seconds):
    relay.on()
    print("Plant is being watered!")
    time.sleep(seconds)
    print("Watering is finished!")
    relay.off()

def main():
    time_keeper = TK.TimeKeeper(TK.TimeKeeper.get_current_time())
    if(time_keeper.current_time == WATERING_TIME):
        water_plant(RELAY, SECONDS_TO_WATER)
        time_keeper.set_time_last_watered(TK.TimeKeeper.get_current_time())
        print("\nPlant was last watered at {}".format(time_keeper.time_last_watered))
        # send_last_watered_email(time_keeper.time_last_watered)

# schedule.every().friday.at("12:00").do(send_check_water_level_email)

while True:
    # schedule.run_pending()
    time.sleep(1)
    main()