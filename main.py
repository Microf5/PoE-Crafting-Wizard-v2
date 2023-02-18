import pyautogui as pyag
import time
import cv2, numpy


def print_hi(name):
    screenWidth, screenHeight = pyautogui.size()
    time.sleep(1)
    altLocation = pyag.locateCenterOnScreen('alteration.png', region=(0, 0, screenWidth, screenHeight),
                                                 confidence=(.65))
    # prob need to find a better way to locate this, it like - only works depending on how many alts u have
    print(altLocation)
    pyag.moveTo(altLocation)
    craftLocation = pyag.locateCenterOnScreen('wherecraft.png', region=(0, 0, screenWidth, screenHeight),
                                                   confidence=(.9))
    print(craftLocation)
    pyag.moveTo(craftLocation)
    searchLocation = pyg.locateCenterOnScreen('searchbox.png', region=(0, 0, screenWidth, screenHeight),
                                                    confidence=(.9))
    print(searchLocation)
    pyag.moveTo(searchLocation)


if __name__ == '__main__':
    print_hi('PyCharm')

# TODO:
# MAKE STUFF WORK, THEN ADD ALT REGAL SPAM
# MAY NEED TO GET THE GRAYSCALED(ones that dont fit search) IMAGES OF SOME ITEMS
# STUFF EVERYTHING INTO A MAP/DICTIONARY?
# IMPLEMENT FAILSAFES -> NOT ON RIGHT STASHTAB OR RUN OUT OF A MATERIAL OR SOMETHING WRONG


# ALT REGAL SPAM STUFF


# regalLocation = pyautogui.locateCenterOnScreen('regal.png', region=(0, 0, screenWidth, screenHeight),confidence=(.6))
# print(regalLocation)
# pyautogui.moveTo(regalLocation)
# scourLocation = pyautogui.locateCenterOnScreen('scour.png', region=(0, 0, screenWidth, screenHeight),confidence=(.6))
# print(scourLocation)
# pyautogui.moveTo(scourLocation)
# transmuteLocation = pyautogui.locateCenterOnScreen('transmute.png', region=(0, 0, screenWidth, screenHeight),confidence=(.6))
# print(transmuteLocation)
# pyautogui.moveTo(transmuteLocation)

