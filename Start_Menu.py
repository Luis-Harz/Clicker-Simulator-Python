from ursina import *
import os
import sys
import time


class MainMenu(Entity):
    def __init__(self):
        super().__init__()
        self.title = Text(text="Main Menu", position=(0, 0.4), scale=2)

        self.start_button = Button(text='Start Game', color=color.azure, position=(0, 0.1), scale=(0.3, 0.1),
                                   on_click=self.start_game)
        self.exit_button = Button(text='Exit Game', color=color.red, position=(0, -0.1), scale=(0.3, 0.1),
                                  on_click=self.exit_game)

    def start_game(self):
        # Start the game by running game.py
        os.system(f'{sys.executable} game.py')
        time.sleep(0.5)
        application.quit()

    def exit_game(self):
        application.quit()


if __name__ == '__main__':
    app = Ursina()
    main_menu = MainMenu()
    app.run()
