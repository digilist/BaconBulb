import sfml as sf

class Splash():

    def __init__(self, window, game_menu):
        self._window = window
        self._game_menu = game_menu

    def loop(self):
        font = sf.Font.from_file("Ubuntu-R.ttf")
        text = sf.Text("Press Space to Start the Game", font, 50)

        self._window.draw(text)
        self.space_listener()

    def space_listener(self):
        for event in self._window.events:
            if type(event) is sf.KeyEvent and event.pressed and event.code is sf.Keyboard.SPACE:
                self._game_menu.start_game()