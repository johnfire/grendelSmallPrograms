#!/usr/bin/python3
import json

from picamera import PiCamera
from time import sleep
from datetime import datetime

def cameraZeroTakePhotos(cameraRunTime = 60, pauseTime =10):
    
    print("hello world from the zero cam function")

    camera1Run=True
    camera = PiCamera()
    
    while(camera1Run==True):
        print("taking pic cam2 now")
        foto = 'zero' + str(datetime.now()) +'.jpg'
        camera.capture('/media/grendelData102/GrendelData/grendelFotos/'+str(datetime.now())+'.jpg')
        #camera.capture('/home/pi/Desktop/ZeroImages/' + foto)
        message = [ 'newfoto', foto , str(datetime.now()) , 'zero' ] 
        with open('/media/grendelData102/GrendelData/grendelMsgs/'+ str(datetime.now()) + '.msg', 'w') as outfile:
            json.dump(message, outfile)
        sleep(pauseTime)
        cameraRunTime-=pauseTime
        if (cameraRunTime <= 0):
            camera1Run = False


if __name__ == '__main__':

    cameraZeroTakePhotos(10,1)

    



