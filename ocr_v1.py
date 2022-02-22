# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 08:38:32 2022

@author: proje7
"""

import pytesseract
import cv2

path = "abraham.jpg"
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# load the input image and convert it from BGR to RGB channel
# ordering}
image = cv2.imread(path, 0)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# use Tesseract to OCR the image
text = pytesseract.image_to_string(image)
print(text)

cv2.imshow("image", image)
cv2.waitKey(0)