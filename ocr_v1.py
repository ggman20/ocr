# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 08:38:32 2022

@author: Gokhan Arman
"""

import pytesseract
import cv2
import os
import sys
import comtypes.client

path = "abraham.jpg"
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# load the input image and convert it from BGR to RGB channel
# ordering}
image = cv2.imread(path, 0)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# use Tesseract to OCR the image
text = pytesseract.image_to_string(image)
print(text)

filename = ("ocr_abraham.doc")
open(filename, "w").write(text)

wdFormatPDF = 17

in_file = os.path.abspath("ocr_abraham.doc")
out_file = os.path.abspath("ocr_abraham.pdf")

word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()

cv2.imshow("image", image)
cv2.waitKey(0)
