import sfml as sf
from splash import Splash
from game import Game
from highscore_menu import Highscore_menu
from gameover_menu import Gameover_menu
from background import Background

class GameMenu():

    def __init__(self, window):
        self._window = window
        self._points = 0
        self._splash = Splash(window, self)
        self._game = Game(window, self)
        self._highscore = Highscore_menu(window, self)
        self._gameover = Gameover_menu(window, self)
        self._background = Background(window)
        

        self.show_splash()

    def dispatch(self):
        self.handle_events();
        
        if(self._current_screen == "splash"): #splash = menu
            self._splash.loop(self._background)
        elif(self._current_screen == "game"):
            self._game.loop()
        elif(self._current_screen == "highscore"):
            self._highscore.loop(self._background)
        elif(self._current_screen == "gameover"):
            self._gameover.loop(self._background)

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

    def show_gameover(self,points):
        self._current_screen = "gameover"
        self._event_listener =  self._gameover
        self._points = points

    def close(self):
        self._window.close()

    def _close_listener(self, event):
        if type(event) is sf.CloseEvent:
            self.close()
