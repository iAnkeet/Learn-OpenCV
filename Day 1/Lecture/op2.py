import cv2 as cv
import numpy as np
img=np.zeros((512,512,3),np.uint8)
cv.line(img,(0,0),(511,511),(255,255,255),10)
cv.rectangle(img,(384,0),(510,128),(255,0,0),3)
cv.circle(img,(200,60),20,(0,100,255),3)
cv.ellipse(img,(250,250),(100,50),90,0,180,(255,0,255),3)
font=cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500),font,4,(255,0,255),3)

cv.imshow('d1',img)
cv.waitKey(0)

