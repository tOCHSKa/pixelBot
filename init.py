from Capture import *
from Move import *
import time


def focusWow(windowTitle):
        window = gw.getWindowsWithTitle(windowTitle)
        try:
            time.sleep(2)
            window[0].activate()
        except:
            window[0].minimize()
            window[0].maximize()


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



if __name__ == "__main__":

    screen_agent = ScreenCapture()
    player = Move()
    
    # Print Menu
    while True:

        print_menu()
        user_input = input().strip().lower()
        if user_input == 'quit' or user_input == 'q':
            if screen_agent.capture_process is not None:
                screen_agent.capture_process.terminate()
            break
        elif user_input == 'run' or user_input == 'r':
            if screen_agent.capture_process is not None:

                print(f'{bcolors.YELLOW}WARNING:{bcolors.ENDC} Capture process already running.')
                continue
            screen_agent.capture_process = multiprocessing.Process(
                target=screen_agent.grab_screen,
                args=(),
                name="screen capture process"
            )

            screen_agent.capture_process.start()

            targetWow = "World of Warcraft"  # Titre de la fenêtre du jeu
            target = focusWow(targetWow)


        elif user_input == 'stop' or user_input == 's':
            if screen_agent.capture_process is None:
                print(f'{bcolors.RED}ERROR:{bcolors.ENDC} Capture process is not running.')
                continue
            screen_agent.capture_process.terminate()
            screen_agent.capture_process = None
        else:
            print(f'{bcolors.RED}ERROR:{bcolors.ENDC} Invalid selection.')

print("Done.")

