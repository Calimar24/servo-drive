#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Libraries
import time    #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
import sys
#Constants
Channel=1
ANG_PRESS=0
ANG_RELEASE=90
#Objects
pca = ServoKit(channels=16)
# function init 
def init():
     pca.servo[Channel].set_pulse_width_range(500 , 2500)
# function main 
def main():
    pcaScenario();
# function pcaScenario 
def pcaScenario():
    print("Kanal {} Winkel {}".format(Channel,ANG_PRESS))
    pca.servo[Channel].angle = ANG_PRESS
    time.sleep(1)
    print("Kanal {} Winkel {}".format(Channel,ANG_RELEASE))
    pca.servo[Channel].angle = ANG_RELEASE
    time.sleep(0.5)
    pca.servo[Channel].angle=None #disable channel     
if __name__ == '__main__':
    init()
    main()
