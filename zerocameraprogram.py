#!/usr/bin/python3
from picamera import PiCamera
from time import sleep
from datetime import datetime

def cameraZeroTakePhotos(cameraRunTime = 60, pauseTime =10):
    
    print("hello world from the zero cam function")

    camera1Run=True
    camera = PiCamera()

    while(camera1Run==True):
        print("taking pic cam2 now")
        #camera.capture('/media/grendelData102/testworkspace/imagesPiCam2/'+str(datetime.now())+'.jpg')
        camera.capture('/home/pi/Desktop/ZeroImages/'+str(datetime.now())+'.jpg')
        sleep(pauseTime)
        cameraRunTime-=pauseTime
        if (cameraRunTime <= 0):
            camera1Run = False


if __name__ == '__main__':

    cameraZeroTakePhotos(30,5)

    



