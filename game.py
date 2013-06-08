import sfml as sf
from meter import Meter

class Game():

    def __init__(self, window, game_menu):
        self._window = window
        self._game_menu = game_menu
        self._meter = Meter(window)

    def loop(self):
        self._meter.incr()

    def listen_for_event(self, event):
        self.escape_listener(event);
    
    def escape_listener(self, event):
            if type(event) is sf.KeyEvent and event.pressed and event.code is sf.Keyboard.ESCAPE:
                self._game_menu.show_splash()