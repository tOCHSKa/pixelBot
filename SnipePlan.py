import pyautogui
import time

time.sleep(3)
try:
    while True:
        # Clic sur la touche "L"
        pyautogui.press('l')
        time.sleep(0.5)  # Attendre 1.5 secondes

        # Clic sur la touche "1"
        pyautogui.press('v')
        time.sleep(0.5)  # Attendre 1.5 secondes

        # Clic sur la touche "Échap" (Escape)
        pyautogui.press('esc')
        time.sleep(0.5)  # Attendre 1.5 secondesLV

except KeyboardInterrupt:
    print("Programme interrompu par l'utilisateur.")