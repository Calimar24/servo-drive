#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Libraries
import time    #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
import sys
#Constants
#Channel=1
ANG_PRESS=[0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #Winkel wenn Taste gedrückt
ANG_RELEASE=[90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90] # Winkel wenn Tate losgelassen
arg = sys.argv[1] #Kanal aus Paramter übernhemen (python3 MulitKanal.py 1)
Channel = int(arg) #Kanal in Integer 
Pause = 0.3
#Objects
pca = ServoKit(channels=16) #Angabe wieviel Kanäle Platine hat
# function init  
def init():
     pca.servo[Channel].set_pulse_width_range(500 , 2500) #Setze minmale (0°) und maximale (180°) Pulsbreite der Servomotoren
# function main 
def main():
    pcaScenario();
# function pcaScenario 
def pcaScenario():
    """Scenario to test servo"""
    print("Kanal {} Winkel {}".format(Channel,ANG_PRESS[Channel]))
    pca.servo[Channel].angle = ANG_PRESS[Channel]
    time.sleep(Pause)
    print("Kanal {} Winkel {}".format(Channel,ANG_RELEASE[Channel]))
    pca.servo[Channel].angle = ANG_RELEASE[Channel]
    time.sleep(Pause)
    pca.servo[Channel].angle=None #disable channel     
if __name__ == '__main__':
    init()
    main()
