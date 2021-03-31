#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:36:48 2021

@author: kaydee
"""

from tensorflow import keras
import cv2
import numpy as np

class Model:
    def __init__(self,path):
        if isinstance(path,str):
            self.image = cv2.imread(path)
        else:
            self.image = path

        
        self.model = keras.models.load_model("drecv3.h5")
        cells = self.chop(True)
        self.predictions = self.predict(cells)
        
        
    def check_corner(self, im):
        '''
        Check pixel values at the corners of the image.

        Parameters
        -----------
        im : image represented in 2darray form.

        Return
        ------
        Array of pixel values at all 4 corners.
        '''
    
        return [im[0][0],im[0][-1],im[-1][0],im[-1][-1]]
        
    def chop(self,doProc = False):
        
        cells = []
        sud = self.image
        print(type(sud))
        sud = cv2.cvtColor(sud,cv2.COLOR_BGR2GRAY)
        #plt.imshow(sud)
        (thresh, sud) = cv2.threshold(sud, 150, 255, cv2.THRESH_BINARY_INV)

        cells = []

        for r in range(0,252,28):
            for c in range(0,252,28):
                im = sud[r:r+28][:,c:c+28]
                #pad = np.zeros(im.shape)
                centroid = sud[r+5:r+20][:,c+5:c+20]
                #plt.imshow(centroid)
                
                if doProc:    
                
                    contours, hierarchy = cv2.findContours(im,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                    #cv2.drawContours(im, contours, -1, (0,255,0), 3)
                    
                    if sum(centroid.ravel()) == 0:
                        print(im.shape)
                        im = im * 0
                    else:
                        t = im.copy()
                        t2 = im.copy() * 0
                        maxc = max(contours, key = cv2.contourArea)
                        
                        cv2.drawContours(t2, [maxc], -1, 255, 2)
            
                        
                        
                        cv2.fillPoly(t2, pts =[maxc], color=255)
                        im = cv2.bitwise_and(t,t2)
                    
                    if sum(self.check_corner(im)) != 0:
                        im *= 0
               
                cells.append(im)
                #plt.imshow(im)
                #print(sud[r:r+28][:,c:c+28])
               
        
        
        cells = np.array(cells)

        cells = cells.reshape((-1,28,28,1))

                
        return cells
        
    def predict(self,cells):
        return self.model.predict(cells,verbose = 1)