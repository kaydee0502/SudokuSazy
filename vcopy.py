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
        self.image = cv2.imread(path)
        self.model = keras.models.load_model("drecv2")
        cells = self.chop()
        self.predictions = self.predict(cells)
        
        
        
    def chop(self):
        cells = []
        sud = self.image
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
               
                cells.append(im)
                #plt.imshow(im)
                #print(sud[r:r+28][:,c:c+28])
               
        
        
        cells = np.array(cells)

        cells = cells.reshape((-1,28,28,1))

                
        return cells
        
    def predict(self,cells):
        return self.model.predict_classes(cells,verbose = 1)