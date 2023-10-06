'''
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r"C:\Users\shekh\AppData\Local\Tesseract-OCR\tesseract.exe"

# Reading image
img = cv2.imread("nono.png")

# Convert to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show the Output
cv2.imshow("Output", img)
cv2.waitKey(1)

# Detect texts from image
texts = pytesseract.image_to_string(img)

print(texts)

'''

 


