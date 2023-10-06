'''
option a
Point(x=479, y=631)

option b
Point(x=474, y=767)

option c
Point(x=482, y=910)

screenshot

ques
start Point(x=241, y=399)
end Point(x=531, y=550)

ans
a

b

c

'''

##Collecting the question
import pyautogui as pag
import cv2
from PIL import Image
import pytesseract
import time
X=99

pytesseract.pytesseract.tesseract_cmd=r"C:\Users\shekh\AppData\Local\Tesseract-OCR\tesseract.exe"
pag.click(x=482, y=910, button="left")
while X<=100:

    X+=1
    im = pag.screenshot("qu.png",region=(241,399,290,160))
    ima = pag.screenshot("a.jpg",region=(353,591,185,86))
    imb = pag.screenshot("b.png",region=(353,730,185,86))
    imc = pag.screenshot("c.png",region=(353,869,185,86))

    # Reading image
    img = cv2.imread("qu.png")
    ima = cv2.imread("a.jpg")
    imb = cv2.imread("b.png")
    imc = cv2.imread("c.png")

    # Convert to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ima = cv2.cvtColor(ima, cv2.COLOR_BGR2GRAY)
    imb = cv2.cvtColor(imb, cv2.COLOR_BGR2GRAY)
    imc = cv2.cvtColor(imc, cv2.COLOR_BGR2GRAY)

    ques = pytesseract.image_to_string(img)

    cv2.putText(ima,"00",(70,50),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
    cv2.putText(imb,"00",(70,50),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
    cv2.putText(imc,"00",(70,50),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)

    a = str(pytesseract.image_to_string(ima))
    b = str(pytesseract.image_to_string(imb))
    c = str(pytesseract.image_to_string(imc))

##    print(ques[:-1])
##    print(a)
##    print(b)
##    print(c)
    a=str(a[:-2])
    b=str(b[:-2])
    c=str(c[:-2])

    if a[-2]=="0":
        a = int(a[-1])
    elif a[-2]=='-':
        a = int(a[-2:])
    elif a[-2]=="1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9":
        a = int(a[-2:])
    
    if b[-2]=="0":
        b = int(b[-1])
    elif b[-2]=='-':
        b = int(b[-2:])
    elif b[-2]=="1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9":
        b = int(b[-2:])
        
    if c[-2]=="0":
        c = int(c[-1])
    elif str(c[-2])=='-':
        c = int(c[-2:])    
    elif c[-2]=="1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9":
        c = int(c[-2:])

    ##calculating the answer
    x= int(ques[0])
    y= int(ques[2])
    op = ques[1]

    if op == "+":
        z = x + y
    elif op == "x":
        z = x * y
    elif op == '-'or'—':
        z = x - y
        
    ##clicking the answer
    if z == int(a):
        pag.click(x=479, y=631, button="left")
    elif z == int(b):
        pag.click(x=474, y=767, button="left")
    elif z == int(c):
        pag.click(x=482, y=910, button="left")
    time.sleep(0.5)
