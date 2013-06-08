from splash import Splash
from game import Game

class GameMenu():

    def __init__(self, window):
        self._window = window
        self._current_screen = "splash"

        self._splash = Splash(window, self)
        self._game = Game(window, self)

    def dispatch(self):
        if(self._current_screen == "splash"): #splash = menu
            self._splash.loop()
        elif(self._current_screen == "game"):
            self._game.loop()

    def show_splash(self):
        self._current_screen = "splash"

    def start_game(self):
        self._current_screen = "game"