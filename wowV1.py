
from Capture import *
from Move import *
import time
import threading

def focusWow(windowTitle):
        window = gw.getWindowsWithTitle(windowTitle)
        try:
            time.sleep(2)
            window[0].activate()
        except:
            window[0].minimize()
            window[0].maximize()

#Combat State
Fighting = False

#Try before reach the target (l）
MoveRecord = 0
MoveMaxTry = 50

#Number of monsterKilled
KillMonster = 0

#Verify if we have a target , Return True if yes
def hasTargetEnemy():
    return pyautogui.pixelMatchesColor(1018, 717, (209, 206, 0))

#Verify if we are in combat
def isFightOver():
    print("Is the battle over?")
    return Fighting

#Verify if we are in melee range
def checkAttackDistance():
    print("Verify Attack Distance")
    return pyautogui.pixelMatchesColor(1, 1, (0, 251, 255))

#Start Attack
def attack():
    print("Attack The Target")
    pyautogui.press('l')
    if pyautogui.pixelMatchesColor(1223, 925, (229, 78, 79)) : 
        pyautogui.press('3')
    else:
        pyautogui.press('r')


#Move to the Target
def moveToTarget():
    global MoveRecord
    global MoveMaxTry
    if MoveRecord < MoveMaxTry:
        MoveRecord = MoveRecord + 1
        print("Moving to Target")
        pyautogui.press('l')
    else:
        moveFaild()

#Movement failed
def moveFaild():
    print("Cannot reach the target")
    print('\7')

#Loot the mob
def pickupTreasure():
    print("LOOT")
    pyautogui.rightClick(959,525)

#Search for target
def searchTarget():
    global Fighting
    print("Search for target")
    pyautogui.press('f5')
    if hasTargetEnemy():
        Fighting = True

#We need regen?
def rest():
    global KillMonster
    if KillMonster > 2:
        KillMonster = 0
        pyautogui.press('v')
        pyautogui.sleep(20)

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



#Robot AI (Execute only one action at a time).            
def botSequence():
    global Fighting
    global MoveRecord
    global KillMonster
    if hasTargetEnemy():
        if checkAttackDistance():
            attack()
        else:
            moveToTarget()
    else:
        if isFightOver() :
            KillMonster = KillMonster + 1
            Fighting = False
            MoveRecord = 0
            pickupTreasure()
            rest()
        else:
            searchTarget()

#Start
while True:
    targetWow = "World of Warcraft"  # Titre de la fenêtre du jeu
    target = focusWow(targetWow)
    if target:
        botSequence()
    else:
        print("Game not in First Plan")
    
    #Pause after each action
    pyautogui.sleep(0.3)

