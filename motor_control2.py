#######################################
# Copyright (c) 2021 Maker Portal LLC
# Author: Joshua Hrisko
#######################################
#
# NEMA 17 (17HS4023) Raspberry Pi Tests
# --- rotating the NEMA 17 to test
# --- wiring and motor functionality
#
#
#######################################
#
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time
import sys

################################
# RPi and Motor Pre-allocations
################################
#
#define GPIO pins
direction= 20 # Direction (DIR) GPIO Pin
step = 21 # Step GPIO Pin
EN_pin = 24 # enable pin (LOW to enable)
ms = (14,15,18)

# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction, step, ms, "A4988")
GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output

###########################
# Actual motor control
###########################
#
GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor
mymotortest.motor_go(True, # True=Clockwise, False=Counter-Clockwise
                     "1/16" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                     int(sys.argv[1]), # number of steps
                     .00001, # step delay [sec]
                     False, # True = print verbose output 
                     .05) # initial delay [sec]
print(int(sys.argv[1]))
GPIO.cleanup() # clear GPIO allocations after run
