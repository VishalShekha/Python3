import pyautogui as pag
import time


time.sleep(5)


print(pag.position())

'''
##Give the python file some time before continuing
time.sleep(10)
x=555, y=660
##Mouse func

##prints the resolution of the screen
print(pag.size())

##print the current position of the mouse
print(pag.position())
'''


##ima = pag.screenshot("a.png",region=(430,606,150,55))

'''
##moves the cursor over three seconds
pag.moveTo(100,100,3)


##Moves the mouse relative to its current position
pag.moveRel(100,100,3)
'''

'''
##click
pag.click(500,500, 3, 3, button="left")
pag.leftClick()
'''

'''
##scorll
time.sleep(3)
pag.scroll(500)
'''

##mouse up and down
##pag.mouseUp(100,100, button="left")


##screenshot
##im = pag.screenshot("scree.png",region=(241,399,290,160))