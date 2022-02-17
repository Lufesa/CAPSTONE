#######################################
# Copyright (c) 2022 Luis Sanchez
# Author: Luis Sanchez
#######################################
#
# Code used for the extruder
#
#
#######################################
#

#import RPi.GPIO as GPIO
#from RpiMotorLib import RpiMotorLib
import time
import sys



RESOLUTION = {'Full': 200,
              'Half': 400,
              '1/4': 800,
              '1/8': 1600,
              '1/16': 3200,
              '1/32': 6400}


def convert_to_steps(turns, resolution = "1/16"):
    return int(turns*RESOLUTION.get(resolution))


step = [21, 26, 19, 13, 6, 5, 7, 8] # Step GPIO Pin

direction= 20 # Direction (DIR) GPIO Pin

EN_pin = 24 # enable pin (LOW to enable)

ms = (14,15,18)

# Initilialisation of motors

# Motor classes
motors = []

# Enable Switch to turn on or off motors
# GPIO.setup(EN_pin,GPIO.OUT)

for i in range (len(step)):
    motors.append(RpiMotorLib.A4988Nema(direction, step[i], ms, "A4988"))
    #motors.append(step[i])
    print (motors)


motors[0].motor_go(True, # True=Clockwise, False=Counter-Clockwise
                     "1/16" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                     convert_to_steps(float(sys.argv[1])), # number of steps
                     .00001, # step delay [sec]
                     False, # True = print verbose output 
                     .05) # initial delay [sec]
print ("Did ", (convert_to_steps(0.5)), "turns")


