import sfml as sf
from splash import Splash
from game import Game
from highscore_menu import Highscore_menu

class GameMenu():

    def __init__(self, window):
        self._window = window

        self._splash = Splash(window, self)
        self._game = Game(window, self)
        self._highscore = Highscore_menu(window, self)

        self.show_splash()

    def dispatch(self):
        self.handle_events();

        if(self._current_screen == "splash"): #splash = menu
            self._splash.loop()
        elif(self._current_screen == "game"):
            self._game.loop()
        elif(self._current_screen == "highscore"):
            self._highscore.loop()

    def handle_events(self):
        for event in self._window.events:
            self._event_listener.listen_for_event(event)
            self._close_listener(event)

    def show_splash(self):
        self._current_screen = "splash"
        self._event_listener = self._splash

    def start_game(self):
        self._current_screen = "game"
        self._event_listener = self._game

    def show_highscore(self):
        self._current_screen = "highscore"
        self._event_listener = self._highscore

    def close(self):
        self._window.close()

    def _close_listener(self, event):
        if type(event) is sf.CloseEvent:
            self.close()
