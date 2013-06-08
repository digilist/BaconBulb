import sfml as sf

class Splash():

    def __init__(self, window, game_menu):
        self._window = window
        self._game_menu = game_menu

    def loop(self):
        font = sf.Font.from_file("Ubuntu-R.ttf")
        text = sf.Text("Press Space to Start the Game", font, 50)

        self._window.draw(text)


    def listen_for_event(self, event):
        self.space_listener(event)

    def space_listener(self, event):
            if type(event) is sf.KeyEvent and event.pressed and event.code is sf.Keyboard.SPACE:
                self._game_menu.start_game()