import cv2
import numpy as np
from PIL import Image
import wx

"""
An example class of how to implement openCV and how it can communicate with the
wxPython layer.
"""
global frame

class WebcamFeed(object):
    """ Starts a webcam feed """

    def __init__(self):
        self.webcam = cv2.VideoCapture(0)

    """ Determines if the webcam is available """

    def has_webcam(self):
        _, frame = self.webcam.read()
        if (isinstance(frame, np.ndarray)):
            return True
        return False

    """ Retrieves a frame from the webcam and converts it to an RGB - Image """

    def get_image(self, w=None, h=None):
        _, frame = self.webcam.read()
        if w != None and h != None:
            frame = cv2.resize(frame, (w, h))
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    def get_imageHSV(self,frame1, w=None, h=None,hmin=None,smin=None,vmin=None,hmax=None,smax=None,vmax=None):
        if w != None and h != None:
            frame1 = cv2.resize(frame1, (w, h))
        #frame2=Image.new("RGB",(w,h),(255,255,255))

        hsv=cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask=cv2.inRange(hsv, np.array([hmin, smin, vmin]), np.array([hmax, smax, vmax]))
        res = cv2.bitwise_and(frame1,frame1,mask=mask)
        return mask,res


    def get_imageEro(self,original,binarizada,valorEro, w=None, h=None,value=None):
        if w != None and h != None:
            original = cv2.resize(original, (w, h))
            binarizada = cv2.resize(binarizada, (w, h))
        kernel = np.ones((valorEro,valorEro),np.uint8)
        erosion = cv2.erode(binarizada, kernel, iterations=1)
        eroShow=cv2.bitwise_and(original,original, mask= erosion)
        return erosion,eroShow

    def get_imageDila(self,original,binarizada,valorDila, w=None, h=None,value=None):
        if w != None and h != None:
            original = cv2.resize(original, (w, h))
            binarizada = cv2.resize(binarizada, (w, h))
        kernel = np.ones((valorDila,valorDila),np.uint8)
        dilatacion = cv2.dilate(binarizada, kernel, iterations=1)
        dilaShow=cv2.bitwise_and(original,original, mask= dilatacion)
        return dilatacion,dilaShow

    def get_centroMasa(self, original, binarizada, w=None, h=None):
        if w != None and h != None:
            original = cv2.resize(original, (w, h))
            binarizada = cv2.resize(binarizada, (w, h))
        moments = cv2.moments(binarizada)
        area = moments['m00']
        if area == 0:
            return original, 0, 0, 0
        else:
            x = int(moments['m10'] / moments['m00'])
            y = int(moments['m01'] / moments['m00'])
            cv2.rectangle(original, (x - 20, y - 20), (x + 20, y + 20), (255, 255, 255), 2)
            return original, x, y, area

    def contornos(self,imagenO,mask):
        label = 'nada'
        edges = cv2.Canny(mask, 1, 2)
        contours, hier = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        areas = [cv2.contourArea(c) for c in contours]
        i=0
        for extension in areas:
            if extension > 200:
                actual = contours[0]

                approx = cv2.approxPolyDP(actual, 0.05 * cv2.arcLength(actual, True), True)
                if len(approx) == 3:
                    cv2.drawContours(imagenO, [actual], 0, (0, 0, 255), 2)
                    cv2.drawContours(mask, [actual], 0, (0, 0, 255), 2)
                    label= 'triangulo'
                if len(approx) == 4:
                    cv2.drawContours(imagenO, [actual], 0, (0, 0, 255), 2)
                    cv2.drawContours(mask, [actual], 0, (0, 0, 255), 2)
                    label='cuadrado'

                i = i + 1
            print
        return imagenO,label
    """ Retrieves a frame to get the size """

    def size(self):
        _, frame = self.webcam.read()
        return frame.shape[:2]