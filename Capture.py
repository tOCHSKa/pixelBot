import mss
import numpy as np
import pyautogui
import cv2 as cv
import time
import math
import multiprocessing
import pygetwindow as gw


class ScreenCapture:

    def __init__(self,monitor=None):
        self.monitor = monitor
        self.w, self.h = pyautogui.size()
        print("Screen Resolution: " + "w: " + str(self.w) + " h: " + str(self.h))
        if monitor is None:
            self.monitor = {"top": 0, "left": 0, "width": self.w, "height": self.h}
        self.Xpos = None
        self.Ypos = None
        self.healthPercent  = None
        self.manaPercent = None
        self.facingDegrees = None
        self.facingRadian = None
        self.isCombat = False
        self.capture_process = None
        self.img = None

    
    def grab_screen(self):

        with mss.mss() as sct:

            while True:
                self.img = np.array(sct.grab(self.monitor))
                small = cv.resize(self.img, (0, 0), fx=0.5, fy=0.5)
                pixelSquareIsCombat = self.img[0,0]
                pixelSquarePosX = self.img[0,1]
                pixelSquarePosY = self.img[0,2]
                pixelSquareHealth = self.img[0,3]
                pixelSquareMana = self.img[0,4]
                pixelSquareFacing = self.img[0,5]
                pixelCheck=[pixelSquareIsCombat,pixelSquarePosX,pixelSquarePosY,pixelSquareHealth,pixelSquareMana,pixelSquareFacing] 

                
                if pixelCheck[0][2] == 255:
                    self.isCombat = False
                    # Show the Combat Status on screen
                    cv.putText(
                            small,
                            f'Combat : False',
                            (25, 50),
                            cv.FONT_HERSHEY_COMPLEX,
                            1,
                            (0, 0, 255),
                            1,
                            cv.LINE_AA, False
                        )
                else:
                    self.isCombat = True
                    # Show the Combat Status on screen
                    cv.putText(
                            small,
                            f'Combat : True',
                            (25, 50),
                            cv.FONT_HERSHEY_COMPLEX,
                            1,
                            (0, 0, 255),
                            1,
                            cv.LINE_AA, False
                        )
                    
                # Formatting the result to have XPOS and YPOS in coordinates
                self.Xpos = "{:.2f}".format(((pixelCheck[1][2])/255)*100)
                self.Ypos = "{:.2f}".format(((pixelCheck[2][1])/255)*100)

                # Convert to integer to ensure the value is in the range 0 to 255
                XposColor = int(pixelCheck[1][2])
                YposColor = int(pixelCheck[2][1])
                
                # Show the XPos on screen
                cv.putText(
                        small,
                        f'X pos: {str(self.Xpos)}',
                        (25, 75),
                        cv.FONT_HERSHEY_COMPLEX,
                        1,
                        (0, 0, XposColor),
                        1,
                        cv.LINE_AA, False
                    )
                
                # Show the YPos on screen
                cv.putText(
                        small,
                        f'Y pos: {str(self.Ypos)}',
                        (25, 100),
                        cv.FONT_HERSHEY_COMPLEX,
                        1,
                        (0, YposColor, 0),
                        1,
                        cv.LINE_AA, False
                    )
                
                # Formatting the result to have %health
                self.healthPercent = "{:.2f}".format(((pixelCheck[3][1])/255)*100)

                # Convert to integer to ensure the value is in the range 0 to 255
                self.healthPercentColor = int(pixelCheck[3][1])


                # print(healthPercentRed)
                # Show the %Health on screen
                cv.putText(
                        small,
                        f'Health: {str(self.healthPercent)} %',
                        (25, 125),
                        cv.FONT_HERSHEY_COMPLEX,
                        1,
                        (0, self.healthPercentColor, 0),
                        1,
                        cv.LINE_AA, False
                    )
                
                            # Formatting the result to have %health
                self.manaPercent = "{:.2f}".format(((pixelCheck[4][0])/255)*100)

                # Convert to integer to ensure the value is in the range 0 to 255
                self.manaPercentColor = int(pixelCheck[4][0])


                # print(ManaPercent)
                # Show the %Health on screen
                cv.putText(
                        small,
                        f'Mana: {str(self.manaPercent)} %',
                        (25, 150),
                        cv.FONT_HERSHEY_COMPLEX,
                        1,
                        (self.manaPercentColor, 0, 0),
                        1,
                        cv.LINE_AA, False
                    )
                
                # Formatting the result to have Facing in degrees
                # self.facingDegrees = "{:.2f}".format(((pixelCheck[5][0])/255)*360)
                self.facingRadian = "{:.2f}".format(math.radians((pixelCheck[5][0])/255*360))
                
                # Convert to integer to ensure the value is in the range 0 to 255
                facingDegreesColor = int(pixelCheck[5][0])

                # Show the Angle on screen
                cv.putText(
                        small,
                        f'Angle: {str(self.facingRadian)}',
                        (25, 175),
                        cv.FONT_HERSHEY_COMPLEX,
                        1,
                        (facingDegreesColor, 0, 0),
                        1,
                        cv.LINE_AA, False
                    )

                # Draw Image
                cv.imshow("Computer Vision", small)
                cv.waitKey(1)

    def pixelSearch(self):
        with mss.mss() as sct:

            
                self.img = np.array(sct.grab(self.monitor))
                
                pixelSquareIsCombat = self.img[0,0]
                pixelSquarePosX = self.img[0,1]
                pixelSquarePosY = self.img[0,2]
                pixelSquareHealth = self.img[0,3]
                pixelSquareMana = self.img[0,4]
                pixelSquareFacing = self.img[0,5]
                pixelCheck=[pixelSquareIsCombat,pixelSquarePosX,pixelSquarePosY,pixelSquareHealth,pixelSquareMana,pixelSquareFacing] 

                
                if pixelCheck[0][2] == 255:
                    self.isCombat = False

                else:
                    self.isCombat = True
                    
                # Formatting the result to have XPOS and YPOS in coordinates
                self.Xpos = "{:.2f}".format(((pixelCheck[1][2])/255)*100)
                self.Ypos = "{:.2f}".format(((pixelCheck[2][1])/255)*100)

                # Formatting the result to have %health
                self.healthPercent = "{:.2f}".format(((pixelCheck[3][1])/255)*100)

                
                # Formatting the result to have %health
                self.manaPercent = "{:.2f}".format(((pixelCheck[4][0])/255)*100)

                # Formatting the result to have Facing in degrees
                # self.facingDegrees = "{:.2f}".format(((pixelCheck[5][0])/255)*360)
                self.facingRadian = "{:.2f}".format(math.radians((pixelCheck[5][0])/255*360))

                # Return important values
                return self.img, pixelCheck, self.isCombat, self.Xpos, self.Ypos, self.healthPercent, self.facingRadian, self.manaPercent
                        
    def get_isCombat(self):
        with mss.mss() as sct: 
            self.img = np.array(sct.grab(self.monitor))
            pixelSquareIsCombat = self.img[0,0]
            if pixelSquareIsCombat[0] == 255:
                    self.isCombat = False
            else:
                    self.isCombat = True
            return self.isCombat
       
    def get_Xpos(self):
        with mss.mss() as sct: 
            self.img = np.array(sct.grab(self.monitor))
            pixelSquarePosX = self.img[0,1]
            # Formatting the result to have XPOS  in coordinates
            self.Xpos = "{:.2f}".format(((pixelSquarePosX[2])/255)*100)
        return self.Xpos  
       
    def get_Ypos(self):
        with mss.mss() as sct: 
            self.img = np.array(sct.grab(self.monitor))
            pixelSquarePosY = self.img[0,2]
            # Formatting the result to have  YPOS in coordinates
            self.Ypos = "{:.2f}".format(((pixelSquarePosY[1])/255)*100)  
        return self.Ypos   

    def get_healthPercent(self):
        with mss.mss() as sct: 
            self.img = np.array(sct.grab(self.monitor))
            pixelSquareHealth = self.img[0,3]
            # Formatting the result to have %health
            self.healthPercent = "{:.2f}".format(((pixelSquareHealth[1])/255)*100)
        return self.healthPercent 
    
    def get_healthPercent(self):
        with mss.mss() as sct: 
            self.img = np.array(sct.grab(self.monitor))
            pixelSquareMana = self.img[0,4]
            # Formatting the result to have %mana
            self.manaPercent = "{:.2f}".format(((pixelSquareMana[0])/255)*100)
        return self.manaPercent

    def get_facingRadian(self):
        with mss.mss() as sct: 
            self.img = np.array(sct.grab(self.monitor))
            pixelSquareFacing = self.img[0,5]
            # Formatting the result to have Facing in degrees
            # self.facingDegrees = "{:.2f}".format(((pixelCheck[5][0])/255)*360)
            self.facingRadian = "{:.2f}".format(math.radians((pixelSquareFacing[0])/255*360))
        return self.facingRadian

class bcolors:
    PINK = '\033[95m'
    CYAN = '\033[96m'
    BLEU = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'

def print_menu():
    print(f'{bcolors.CYAN}Command Menu{bcolors.ENDC}')
    print(f'\t{bcolors.GREEN}r - Run{bcolors.ENDC}\t\tStart screen capture')
    print(f'\t{bcolors.RED}s - Stop{bcolors.ENDC}\tStop screen capture')
    print(f'\tq - Quit\tQuit screen capture')


    
