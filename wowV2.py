player = Move()
pixelInfo = WowCapture()

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

