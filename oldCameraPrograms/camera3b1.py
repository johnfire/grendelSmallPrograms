#!/usr/bin/python3
from picamera import PiCamera
from time import sleep
from datetime import datetime

def camera2b1TakePhotos(cameraRunTime =60, pauseTime=10):
    print("hello world from the 2b1 cam function")

    camera1Run=True

    camera = PiCamera()

    while(camera1Run==True):
        print("taking pic cam1 now")
        #camera.capture('/media/grendelData102/GrendelData/grendelFotos/'+str(datetime.now())+'.jpg')
        camera.capture('/media/grendelData102/GrendelData/grendelFotos/'+str(datetime.now())+'.jpg')
        sleep(pauseTime)
        cameraRunTime-=pauseTime
        if (cameraRunTime < 0):
            camera1Run = False

if __name__ == "__main__":
    camera2b1TakePhotos(15,3)
    



