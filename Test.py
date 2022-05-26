import re
import cv2
import argparse
import imutils
import numpy as np
from crop_licence_plate import LicencePlate
from segment_letter_lp import SegmentChar
from flask import Flask,render_template

lp = LicencePlate()
image = cv2.imread(r'.\static\uploads\49810384_2160862904232003_7663659804388229120_n.jpg')
image = cv2.resize(image,(620,480))

lp.load_image(image)

plate,cnt = lp.crop_plate()

result = 'Khong the nhan dang'

if plate is not None:

    segchar = SegmentChar()
    segchar.loadplate(plate)
    
    suc = segchar.segmentPlate()
    if suc:
        numPlate = segchar.ReadCharPlate()
        #segchar.showplate()
        result = 'Bien so: '+ ''.join(numPlate)
if result != 'Khong the nhan dang':
    cv2.drawContours(image, [cnt], -1, (0,255,0), 3)
cv2.putText(image, result,(20,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
segchar.showplate()
cv2.imshow('Car', image)
cv2.waitKey(0)
cv2.destroyAllWindows()