import cv2
import numpy as np
import os



def image_match(image_name,path,path2):
    img_rgb = cv2.imread(image_name,1)
    result=[]
    if not img_rgb is None:
        
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        os.chdir(path2)
        files= os.listdir(path2)
        #print files
        
        for f in files:
            #print f
                
            template = cv2.imread(f,0)
            #print template
            w, h = template.shape[::-1]

            res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where( res >= threshold)
            
            for e in loc:
               
                if any(e):
                    result.append(True)
                    break
                    
                else:
                    result.append(False)
    
            
    os.chdir(path)
    if True in result:
        return True
    else:
        return False

