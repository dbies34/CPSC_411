# motion_sensor_test.py
# team1

import RPi.GPIO as gpio
import time 
from email import email

gpio.setmode(gpio.BCM)
pir_pin = 37 # pin for motion sensor
gpio.setup(pir_pin, gpio.IN)
e = email()
kp = keypad(columnCount = 3)
armed = True

def MOTION(pir_pin):
    if armed == True
        print ("motion detected!")
        e.send_email("your code is 1234", "your code is 5678")
        user_1 = [1, 2, 3, 4, '#']
        user_2 = [5, 6, 7, 8, '#']

        ###### 4 Digit wait ######
        seq = []
        for i in range(4):
            digit = None
            while digit == None:
                digit = kp.getKey()
            seq.append(digit)
            time.sleep(0.4)

        # Check digit code
        print(seq)
        if seq == user_1:
            print "User 1 accepted"
            armed = False
        elif seq == user2:
            print "User 2 accepted"
            armed = False
        else:
            print "User not authorized. [set off alarm here]"
            armed = True



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