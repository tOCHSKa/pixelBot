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
        self.KEY_SIT = ''


    def forward_start(self):
        pyautogui.keyDown(self.KEY_FORWARD)

    def forward_stop(self):
        pyautogui.keyUp(self.KEY_FORWARD)

    def backward_start(self):
        pyautogui.keyDown(self.KEY_BACKWARD)

    def backward_stop(self):
        pyautogui.keyUp(self.KEY_BACKWARD)

    def left_start(self, timer):
        pyautogui.keyDown(self.KEY_LEFT)
        print('Start turn left')
        time.sleep(timer)
        print('Stop turn left')
        pyautogui.keyUp(self.KEY_LEFT)

    def left_stop(self):
        pyautogui.keyUp(self.KEY_LEFT)

    def right_start(self,timer):
        pyautogui.keyDown(self.KEY_RIGHT)
        time.sleep(timer)
        pyautogui.keyUp(self.KEY_RIGHT)

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
        time.sleep(0.01)
        pyautogui.keyUp(self.KEY_LEFT)

    def bump_right(self):
        pyautogui.keyDown(self.KEY_RIGHT)
        time.sleep(0.01)
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



#Zone with [X,Y,Rad,Boolean]
# northShire = [[0,0,0,False],[1,1],[1,2],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

rotateTime = 2
current_angle = None
next_angle = 6.1

from Capture import *
player = Move()
local = ScreenCapture()

# if player.get_facingRadian() > next_angle and player.get_facingRadian() - next_angle < 3.14:
#     while player.get_facingRadian() != next_angle:
#         player.right_start()
#     else:
#         player.left_start()

# print(player.get_facingRadian())
# print(player.get_Xpos())
# print(player.get_Ypos())



position = []
firstPos = [local.get_Xpos(),local.get_Ypos(),local.get_facingRadian()]
secondPos = [local.get_Xpos(), local.get_Ypos(), math.pi]
position=[firstPos,secondPos]
print(position)

def timeToRotate(firstPos, secondPos):
    totalTimeToRotate = 2
    angle = firstPos - secondPos
    timeToTurn = (totalTimeToRotate * angle)/(2 * math.pi)
    return timeToTurn

def rotatePlayer(timer):
    print(timer)
    if timer > 0 and timer <= 1:
        # print('tourne a droite')
        player.bump_right()
    else:
        # print('tourne a gauche')
        player.bump_left()


# nextAngle = timeToRotate(firstPos[2],secondPos[2])

# time.sleep(3)
# timer = rotatePlayer(nextAngle)


