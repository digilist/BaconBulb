import sfml as sf

class Game():

    def __init__(self, window, game_menu):
        self._window = window
        self._game_menu = game_menu

    def loop(self):
        for event in self._window.events:
            if type(event) is sf.KeyEvent and event.pressed and event.code is sf.Keyboard.ESCAPE:
                self._game_menu.show_splash()