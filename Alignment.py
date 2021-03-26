import cv2
import numpy as np
import matplotlib.pyplot as plt




class ChangePerspective():
    def prepro(self, img):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        mask = np.zeros((gray.shape),np.uint8)
        kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))
    
        close = cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel1)
        div = np.float32(gray)/(close)
        res = np.uint8(cv2.normalize(div,div,0,255,cv2.NORM_MINMAX))
        res2 = cv2.cvtColor(res,cv2.COLOR_GRAY2BGR)
        #plt.imshow(res2)
        return res2, res, mask
    

    def readim(self, path,name=None):
        if isinstance(path, str):
            m = cv2.imread(path)
        else:
            m = path

        mo, mg, mask = self.prepro(m)
        r,mask = self.get_cnt(mg, mask)
        corners = self.get_corners(mask)
        mH = m.shape[0]
        mW = m.shape[1]
        
        pA = corners[self.closest_node([0,0],corners)]
        pB = corners[self.closest_node([0,mH-1],corners)]
        pC = corners[self.closest_node([mW-1,mH-1],corners)]
        pD = corners[self.closest_node([mW-1,0],corners)]
        H = W = 252
        output_pts = np.float32([[0, 0],
                        [0, H - 1],
                        [W - 1, H - 1],
                        [W - 1, 0]])
        
        input_pts = np.float32([pA, pB, pC, pD])
        M = cv2.getPerspectiveTransform(input_pts,output_pts)
        out = cv2.warpPerspective(mo,M,(W, H),flags=cv2.INTER_LINEAR)
        
        #save img
        if isinstance(path, str):
            fpath = "static/images/"
            fname = "edited_" + name
            print(fpath+fname)
            self.save_img(fpath,fname,out)
        return out
    
    def save_img(self,fpath,fname,out):
        cv2.imwrite(fpath+fname,out)

    def get_cnt(self,mg,mask):
        thresh = cv2.adaptiveThreshold(mg,255,0,1,19,2)
        contour,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        plt.imshow(thresh)
        max_area = 0
        best_cnt = None
        for cnt in contour:
            area = cv2.contourArea(cnt)
            if area > 1000:
                if area > max_area:
                    max_area = area
                    best_cnt = cnt
        
        t1 = cv2.drawContours(mask,[best_cnt],0,255,-1)
        
        t2 = cv2.drawContours(mask,[best_cnt],0,0,2)
        
        
        res = cv2.bitwise_and(mg,mask)
            
        return res,mask
    
    def get_corners(self,mask):
        canny = cv2.Canny(mask, 120, 255, 1)
        corners = cv2.goodFeaturesToTrack(canny,4,0.5,50)
        return corners


    def closest_node(self, node, nodes):
        nodes = np.asarray(nodes)
        dist_2 = (nodes - node)**2
        
        n = np.sum(dist_2.astype("int"),axis=-1)
    
        return np.argmin(n)






