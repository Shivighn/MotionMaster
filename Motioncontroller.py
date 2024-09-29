import numpy as np
import cv2
import time 
import pynput
from pynput.keyboard import Key, Controller

''' Varables'''
noseCascade = cv2.CascadeClassifier ("C:/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml")
keyboard = Controller()

'''functions'''
def gamevideo():
    windowName = "Live Video Feed"
    cv2.namedWindow(windowName)
    cap=cv2.VideoCapture(0)
     
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    #da ctangl range
    #cv2.rectangle(frame,(415,190) , (225,290) , (157,0,0) , 3 )

    while ret:
        ret,frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        nose = noseCascade.detectMultiScale(gray, 1.3, 5)

        #da ctangl range
        #cv2.rectangle(frame,(370,290) , (270,190) , (157,0,0) , 3 )

        for (x, y, w, h) in nose:
         center_coordinatesx = x + w // 2 
         center_coordinatesy = y + h // 2
         center_coordinates = center_coordinatesx,center_coordinatesy
         radius = w // 14 # or can be h / 2 or can be anything based on your requirements
         cv2.circle(frame, center_coordinates, radius, (0, 255, 0), 2)


        flip = cv2.flip(frame,1)
        cv2.imshow(windowName,flip)

        #print(center_coordinates)

        if(center_coordinatesx > 375):
            print("Move left")
            keyboard.press(Key.left)
            #keyboard.release(Key.left)

        if(center_coordinatesx < 255):
            print("move right")
            keyboard.press(Key.right)
            #keyboard.release(Key.right)

        if(center_coordinatesy < 190):
            print("move up")
            keyboard.press(Key.up)
            #keyboard.release(Key.up)

        if(center_coordinatesy > 285):
            print("mov doownw")
            keyboard.press(Key.down)
            #keyboard.release(Key.down)

        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyWindow(windowName)

    cap.release()
        
    
if __name__ == "__main__":
   gamevideo()
