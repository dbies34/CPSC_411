# motion_sensor_test.py
# team1

import RPi.GPIO as gpio
import time 

gpio.setmode(gpio.BCM)
pir_pin = 37 # pin for motion sensor
gpio.setup(pir_pin, gpio.IN)

def MOTION(pir_pin):
    print ("motion detected!")


print ("motion sensor test")
time.sleep(2)
print ("starting now")

try:
    gpio.add_event_detect(pir_pin, gpio.RISING, callback=MOTION)
    while True:
        time.sleep(100)

except KeyboardInterrupt:
    print ("\nexiting\n")
    gpio.cleanup()