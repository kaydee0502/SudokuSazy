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
        self.model = keras.models.load_model("drec")
        cells = self.chop()
        self.predictions = self.predict(cells)
        
        
        
    def chop(self):
        cells = []
        sud = self.image
        sud = cv2.cvtColor(sud,cv2.COLOR_BGR2GRAY)
        #plt.imshow(sud)
        (thresh, sud) = cv2.threshold(sud, 150, 255, cv2.THRESH_BINARY_INV)

        for r in range(0,252,28):
            for c in range(0,252,28):
                im = sud[r:r+28][:,c:c+28]
                #pad = np.zeros(im.shape)
                #pad[3:-3][:,3:-3] = sud[r+3:r+25][:,c+3:c+25]
                cells.append(im)
        cells = np.array(cells)

        cells = cells.reshape((-1,28,28,1))

                
        return cells
        
    def predict(self,cells):
        return self.model.predict_classes(cells,verbose = 1)