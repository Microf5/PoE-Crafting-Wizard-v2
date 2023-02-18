import pyautogui as pyag
import time
import cv2, numpy
def print_hi(name):


   screenWidth, screenHeight = pyag.size()
   time.sleep(2)
   r = pyag.locateOnScreen('kekw.png',region=(0, 0, screenWidth, screenHeight),confidence = (0.8),grayscale = True)
   print(r)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   print_hi('PyCharm')
