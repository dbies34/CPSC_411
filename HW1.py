#HW1
# team1

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

while True:
    for event in sense.stick.get_events():
        printIntructions()
        if event.action == "pressed":
            if event.direction == "up":
                pressure = sense.get_pressure()
                pressure = round(pressure, 0)
                sense.show_message("pressure {0} mbr".format(str(pressure)))
            elif event.direction == "down":
                temp = sense.get_temperature()
                temp = round(temp, 0)
                sense.show_message("temp {0} C".format(str(temp)))   
            elif event.direction == "left":
                hum = sense.get_humidity()
                hum = round(hum, 0)
                sense.show_message("humidity {0} %".format(str(hum)))
            elif event.direction == "right":  
                o = sense.get_orientation()
                pitch = o["pitch"]
                roll = o["roll"]
                yaw = o["yaw"]

                pitch=round(pitch, 0)
                roll=round(roll, 0)
                yaw=round(yaw, 0)
                sense.show_message("pitch {0} roll {1} yaw {2}".format(str(pitch), str(roll), str(yaw)))
            elif event.action == "pressed":        
                printIntructions()
        

def printIntructions():
    sense.show_message("up: pressure | down: temp | left: humidity | right: orientation")
    