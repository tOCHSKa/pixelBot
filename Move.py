import pyautogui
import time
import pygetwindow as gw

class Move:
    def __init__(self):
        self.KEY_RUN = 'numlock'
        self.KEY_JUMP = 'space'
        self.KEY_LEFT = 'left'
        self.KEY_RIGHT = 'right'
        self.KEY_FORWARD = 'z'
        self.KEY_BACKWARD = 's'
        self.KEY_STRAFE_LEFT = 'q'
        self.KEY_STRAFE_RIGHT = 'd'
        self.KEY_SHEATHE = ''
        self.KEY_SIT = 'w'
        self.KEY_TARGET = 'tab'

    def target(self):
        pyautogui.keyDown(self.KEY_TARGET)

    def forward_start(self):
        pyautogui.keyDown(self.KEY_FORWARD)

    def forward_stop(self):
        pyautogui.keyUp(self.KEY_FORWARD)

    def backward_start(self):
        pyautogui.keyDown(self.KEY_BACKWARD)

    def backward_stop(self):
        pyautogui.keyUp(self.KEY_BACKWARD)

    def left_start(self):
        pyautogui.keyDown(self.KEY_LEFT)

    def left_stop(self):
        pyautogui.keyUp(self.KEY_LEFT)

    def right_start(self):
        pyautogui.keyDown(self.KEY_RIGHT)
        print("DROITE")

    def right_stop(self):
        pyautogui.keyUp(self.KEY_RIGHT)

    def left_strafe_start(self):
        pyautogui.keyDown(self.KEY_STRAFE_LEFT)

    def left_strafe_stop(self):
        pyautogui.keyUp(self.KEY_STRAFE_LEFT)

    def right_strafe_start(self):
        pyautogui.keyDown(self.KEY_STRAFE_RIGHT)

    def right_strafe_stop(self):
        pyautogui.keyUp(self.KEY_STRAFE_RIGHT)

    def jump(self):
        pyautogui.press(self.KEY_JUMP)

    def bump_forward(self, t=0.05):
        pyautogui.keyDown(self.KEY_FORWARD)
        time.sleep(t)
        pyautogui.keyUp(self.KEY_FORWARD)

    def bump_backward(self):
        pyautogui.keyDown(self.KEY_BACKWARD)
        time.sleep(0.05)
        pyautogui.keyUp(self.KEY_BACKWARD)

    def bump_left(self):
        pyautogui.keyDown(self.KEY_LEFT)
        time.sleep(0.0001)
        pyautogui.keyUp(self.KEY_LEFT)

    def bump_right(self):
        pyautogui.keyDown(self.KEY_RIGHT)
        time.sleep(0.001)
        pyautogui.keyUp(self.KEY_RIGHT)

    def bump_strafe_left(self):
        pyautogui.keyDown(self.KEY_STRAFE_LEFT)
        time.sleep(0.05)
        pyautogui.keyUp(self.KEY_STRAFE_LEFT)
  
    def bump_strafe_right(self):
        pyautogui.keyDown(self.KEY_STRAFE_RIGHT)
        time.sleep(0.05)
        pyautogui.keyUp(self.KEY_STRAFE_RIGHT)

    def sheathe_toggle(self):
        pyautogui.press(self.KEY_SHEATHE)

    def sit(self):
        pyautogui.press(self.KEY_SIT)


