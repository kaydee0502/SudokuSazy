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
        
    def check_edge(self,x,y,w,h):
        if x == 0 or y == 0 or x+w == 28 or y+h == 28:
            return False
        return True
        
    def chop(self,doProc = False):
        
        cells = []
        sud = self.image
        #print(type(sud))
        sud = cv2.cvtColor(sud,cv2.COLOR_BGR2GRAY)
        #plt.imshow(sud)
        (thresh, sud) = cv2.threshold(sud, 127, 255, cv2.THRESH_BINARY_INV)

        

        cells = []
        doProc = True
        for r in range(0,252,28):
            for c in range(0,252,28):
                im = sud[r:r+28][:,c:c+28]
                
                if doProc:
                    #pad = np.zeros(im.shape)
                    centroid = sud[r+5:r+20][:,c+5:c+20]
                    #plt.imshow(centroid)
                    
                    contours, hierarchy = cv2.findContours(im,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
                    #cv2.drawContours(im, contours, -1, (0,255,0), 3)

                    
                    
                    for cnt in contours:
                        print("f")
                        x,y,w,h = cv2.boundingRect(cnt)
                        print(x,y,w,h)
                        if self.check_edge(x,y,w,h):
                            cnt_mask = np.zeros_like(im)
                            cnt_mask[y:y+h,x:x+w] = 1
                            
                            # Draw the rectangle
                            #cv2.rectangle(im,(x,y),(x+w,y+h),(255,255,0),1)
                            print(im.dtype,cnt_mask.dtype)
                            assert im.dtype == cnt_mask.dtype 
                            im = cv2.bitwise_and(im,cnt_mask)
                        
                                
                            
                            break
                    else:
                        im*=0
                        
                cells.append(im)
                
        
        
        cells = np.array(cells)

        cells = cells.reshape((-1,28,28,1))

                
        return cells
        
    def predict(self,cells):
        return self.model.predict(cells,verbose = 1)