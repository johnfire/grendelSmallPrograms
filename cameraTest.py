#!/usr/bin/python3
from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/2b1images/'+str(datetime.now())+'2b1.jpg')
camera.stop_preview()
