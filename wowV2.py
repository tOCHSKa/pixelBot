
from Capture import *
from Move import *
import time
import threading
player = Move()
pixelInfo = WowCapture()

def timeToRotate(angle):
    x = (2 * abs(angle))/(2 * math.pi)
    print("X = " , x)
    print('Angle = ' , abs(angle))
    return x

def rotationByTime(rotation_time, rotation):
    if rotation < 0 and abs(rotation) < math.pi:
        pyautogui.keyDown('left')
        time.sleep(rotation_time)
        pyautogui.keyUp('left')
    elif rotation < 0 and abs(rotation) > math.pi:
        timer = 2 - rotation_time
        pyautogui.keyDown('right')
        time.sleep(timer)
        pyautogui.keyUp('right')
    elif rotation > 0 and abs(rotation) < math.pi:
        pyautogui.keyDown('right')
        time.sleep(rotation_time)
        pyautogui.keyUp('right')
    elif rotation > 0 and abs(rotation) > math.pi:
        timer = 2 - rotation_time
        pyautogui.keyDown('left')
        time.sleep(timer)
        pyautogui.keyUp('left')
    else:
        pyautogui.keyDown('left')
        time.sleep(1)
        pyautogui.keyUp('left')


def isRanged():
    color = pyautogui.pixel(1, 1)  # Obtenir la couleur du pixel à la position (0, 0)
    #RGB
    red = (255, 0 ,0)
    orange = (255,126,0)
    yellow =  (255, 251, 0)
    green = (0, 251, 0)
    cyan = (0, 251 , 255)

    if color == cyan:
        print("Nearest Range")
        return 1
    elif color == green:
        return 2
    elif color == yellow:
        return 3
    elif color == orange:
        return 4
    elif color == red:
        print("Out of Range")
        return 5
    else:
        print("No Target")
        return 0

def loot():
    # Ajouter un clic droit au milieu de l'écran
    screen_width, screen_height = pyautogui.size()  # Obtenir la taille de l'écran
    middle_x = screen_width // 2  # Calculer la position x du milieu de l'écran
    middle_y = 570  # Calculer la position y du milieu de l'écran
    pyautogui.moveTo(middle_x, middle_y)
    pyautogui.leftClick()  # Effectuer un clic gauche
    time.sleep(1)


def interactWithTarget():
            pyautogui.press('l')  # Autre action
            time.sleep(1)


#target special enemy
def targetBySlashTar():
    pyautogui.press('enter')
    pyautogui.write('/tar young')
    time.sleep(0.5)
    pyautogui.press('enter')


#Spell to active in combat
def castSequence():
        pyautogui.press('r')  # Premier sort


#Regeneration 
def regenerate():
    hp = pixelInfo.get_healthPercent()
    mana = pixelInfo.get_manaPercent()
    if hp < 80:
        pyautogui.keyDown('v')
        time.sleep(25)

#Return level of the target
def targetUnitLevel():
    level = pixelInfo.get_unitLevel()
    return level

def classPlayer():
    classP = pixelInfo.get_classPlayer()
    return classP


def focusWow(windowTitle):
        window = gw.getWindowsWithTitle(windowTitle)
        try:
            time.sleep(2)
            window[0].activate()
            return window[0]
        except:
            window[0].minimize()
            window[0].maximize()
            return None

# DEFINE THE DIRECTION TO TAKE TO GO TO THE NEXT WAYPOINT
def mapDirection(x, y):
    # Calcul des différences entre les coordonnées x et y
    dx = y[0] - x[0]
    dy = y[1] - x[1]
    
     # Calcul de l'angle entre les deux points en radians
    angle = math.atan2(dy, dx)
        # Ajustement de l'angle pour que 0 radian soit orienté vers le haut
    angle += math.pi / 2
    
    # Ajustement de l'angle pour qu'il reste dans l'intervalle [0, 2*pi]
    if angle < 0:
        angle += 2 * math.pi
    angle -= (2 * math.pi)

    
    return round(abs(angle),2)

# DEFINE THE MARGIN ROTATION BETWEEN THE CURRENT ANGLE AND THE TARGET ANGLE
def rotation(current_angle, target_angle):

    rotation = round(current_angle - target_angle,2)  
    print("rotation : ", rotation)
    return rotation, target_angle

# ROTATE THE CHAR WITH ROTATION PARAMETER
def rotate_to(rotation):

        minValue = round(target_angle - 0.04,2)
        if minValue < 0:
            minValue = 0
        print("min Value of TargetAngle ", minValue)
        maxValue = round(target_angle + 0.04,2)
        if maxValue > 6.28:
            maxValue = 6.28
        print("max Value of TargetAngle ", maxValue)

        if rotation < 0:
            print("Starting left rotation")
            player.left_start()
            player.left_start()
            while True:
                current_angle = round(pixelInfo.get_facingRadian(), 2)
                print("current : ",current_angle)
                if minValue < current_angle < maxValue:
                    player.left_stop()
                    print("Current Angle", current_angle)
                    # if current_angle > angle:
                    #     player.bump_right()
                    # else:
                    #     player.bump_left()
                    break 
        elif rotation > 0:
            print("Starting right rotation")
            player.right_start()
            while True:
                current_angle = round(pixelInfo.get_facingRadian(), 2)
                print(current_angle)
                if minValue < current_angle < maxValue:
                    player.right_stop()
                    #player.sit()
                    print("Current Angle", current_angle)
                    # if current_angle > angle:
                    #     player.bump_right()
                    # else:
                    #     player.bump_left()
                    break 

def moveTo(a,b):

    # minValueZeroB = b[0] - 0.5
    # maxValueBZeroB = b[0] + 0.5
    # print(minValueZeroB)
    # print(maxValueBZeroB)

    # minValueOneB = b[1] - 0.5
    # maxValueBOneB = b[1] + 0.5
    # print(minValueOneB)
    # print(maxValueBOneB)

    player.forward_start()
    if a[0] > b[0] and a[1] > b[1]:
        print("a[0] > b[0] and a[1] > b[1]")
        while True:
            a = (round(pixelInfo.get_Xpos(), 2), round(pixelInfo.get_Ypos(), 2))
            if a[0] <= b[0] and a[1] <= b[1]:
                player.forward_stop()
                break
    
    elif a[0] > b[0] and a[1] < b[1]:
        print("a[0] > b[0] and a[1] < b[1]")
        while True:
            a = (round(pixelInfo.get_Xpos(), 2), round(pixelInfo.get_Ypos(), 2))
            if a[0] <= b[0] and a[1] >= b[1]:
                player.forward_stop()
                break
    
    elif a[0] < b[0] and a[1] > b[1]:
        print("a[0] < b[0] and a[1] > b[1]")
        while True:
            a = (round(pixelInfo.get_Xpos(), 2), round(pixelInfo.get_Ypos(), 2))
            if a[0] >= b[0] and a[1] <= b[1]:
                player.forward_stop()
                break
    
    elif a[0] < b[0] and a[1] < b[1]:
        print("a[0] < b[0] and a[1] < b[1]")
        while True:
            a = (round(pixelInfo.get_Xpos(), 2), round(pixelInfo.get_Ypos(), 2))
            if a[0] >= b[0] and a[1] >= b[1]:
                player.forward_stop()
                break
    
    elif a[0] > b[0] and a[1] == b[1]:
        print("a[0] > b[0] and a[1] == b[1]")
        while True:
            a = (round(pixelInfo.get_Xpos(), 2), round(pixelInfo.get_Ypos(), 2))
            if a[0] <= b[0]:
                player.forward_stop()
                break
    
    elif a[0] < b[0] and a[1] == b[1]:
        print("a[0] < b[0] and a[1] == b[1]")
        while True:
            a = (round(pixelInfo.get_Xpos(), 2), round(pixelInfo.get_Ypos(), 2))
            if a[0] >= b[0]:
                player.forward_stop()
                break
    
    elif a[0] == b[0] and a[1] > b[1]:
        print("a[0] == b[0] and a[1] > b[1]")
        while True:
            a = (round(pixelInfo.get_Xpos(), 2), round(pixelInfo.get_Ypos(), 2))
            if a[1] <= b[1]:
                player.forward_stop()
                break
    
    elif a[0] == b[0] and a[1] < b[1]:
        print("a[0] == b[0] and a[1] < b[1]")
        while True:
            a = (round(pixelInfo.get_Xpos(), 2), round(pixelInfo.get_Ypos(), 2))
            if a[1] >= b[1]:
                player.forward_stop()
                break
    
    elif a[0] == b[0] and a[1] == b[1]:
        print("a[0] == b[0] and a[1] == b[1]")
        player.forward_stop()
    # while True:
    #     a = (round(pixelInfo.get_Xpos(),0),round(pixelInfo.get_Ypos(),0))
    #     print("position actuelle : " ,a)
    #     print("position a atteindre : " ,b)

            # break

time.sleep(3)

# print("Position finale :", current_position)
first = (round(pixelInfo.get_Xpos(),2),round(pixelInfo.get_Ypos(),2))
second = (80,80)

print("Position actuelle (x, y) : ", first)
print("Position d'arrivée (x, y) : ", second)


current_angle = round(pixelInfo.get_facingRadian(),2)
print("Angle actuelle du personnage: ", current_angle)

target_angle = mapDirection(first, second)
print("Direction vers le prochain Waypoint:", target_angle)


# targetWow = "World of Warcraft"  # Titre de la fenêtre du jeu
# target = focusWow(targetWow)


rotation, angle = rotation(current_angle,target_angle)
rotate_to(rotation)
# moveTo(first,second)



# current_position = (100, 200)
# current_angle = 0  # Angle initial

# print("Position initiale :", current_position)

# # Liste des waypoints
# waypoints = [(100, 250), (200, 250), (100, 350)]  # Ajoutez autant de waypoints que nécessaire

# # Parcourir chaque waypoint
# for idx, waypoint in enumerate(waypoints):
#     target_angle = mapDirection(current_position, waypoint)
#     print(f"Angle vers waypoint {idx + 1} (position {waypoint}) : {target_angle:.2f} radians")

#     # Rotation
#     current_angle = rotate_to(current_angle, target_angle)
    
#     # Avancement
#     current_position = move_to(current_position, waypoint)

