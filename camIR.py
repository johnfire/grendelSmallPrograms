#!/usr/bin/python3
import sys
from time import sleep
from datetime import datetime

from picamera import PiCamera

def cameraTakePhotos(numberOfFotos=5, pauseTime=2):
    print("hello world from the IR  cam function")

    camera1Run=True

    camera = PiCamera()

    while(camera1Run==True):
        print("taking pic IR cam now")
        #camera.capture('/media/grendelData102/GrendelData/grendelFotos/'+str(datetime.now())+'.jpg')
        camera.capture('/media/grendelData102/GrendelData/grendelFotos/'+"N"+str(datetime.now())+'.jpg')
        sleep(pauseTime)
        numberOfFotos -= 1
        #cameraRunTime-=pauseTime
        #if cameraRunTime < 0:
        if numberOfFotos == 0:
            camera1Run = False

if __name__ == "__main__":
    arglist = sys.argv
    if len(arglist) == 3:
        cameraTakePhotos(float(arglist[1]),float(arglist[2]))
    else:
        cameraTakePhotos(3,1)



