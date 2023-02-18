import pyautogui
import time
import cv2, numpy
def print_hi(name):


   screenWidth, screenHeight = pyautogui.size()
   time.sleep(2)
   r = pyautogui.locateOnScreen('kekw.png',region=(0, 0, screenWidth, screenHeight),confidence = (0.8),grayscale = True)
   print(r)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   print_hi('PyCharm')
