
from Capture import *

class Character: 
    def __init__(self) -> None:
        self.player = ScreenCapture()

    #we are in combat
    def isCombatLocal(self):
        return self.player.get_isCombat()
    #we are not in combat
    #we need to rest

    def needRegen(self):
        health_percent = int(self.player.get_healthPercent())
        if health_percent < 30:
            return True
        else:
            return False

#we have target


player = Character()

test = player.isCombatLocal()
needMana = player.needRegen()

print(needMana)
