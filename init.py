from Capture import *
from Move import *

class FocusWindow:
    def __init__(self):
        self.windowTitle = None

    def focusWow(self, windowTitle):
        window = gw.getWindowsWithTitle(windowTitle)
        try:
            window[0].activate()
        except:
            window[0].minimize()
            window[0].maximize()


if __name__ == "__main__":


    screen_agent = ScreenCapture()
    
    # Print Menu
    while True:
        # screen_agent.grab_screen()
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
            target = FocusWindow()
            # if target.focusWow(targetWow):
            #     print("La fenêtre du jeu a été focalisée avec succès.")
            # else:
            #     print("Impossible de trouver la fenêtre du jeu.")

        elif user_input == 'stop' or user_input == 's':
            if screen_agent.capture_process is None:
                print(f'{bcolors.RED}ERROR:{bcolors.ENDC} Capture process is not running.')
                continue
            screen_agent.capture_process.terminate()
            screen_agent.capture_process = None
        else:
            print(f'{bcolors.RED}ERROR:{bcolors.ENDC} Invalid selection.')

print("Done.")