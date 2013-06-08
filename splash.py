import sfml as sf

class Splash():

    def __init__(self, window, game_menu):
        self._window = window
        self._game_menu = game_menu
        self._startposition = sf.system.Vector2(350,200)
        self._startsize = sf.system.Vector2(100,20)
        self._start = sf.RectangleShape()
        self._start.size = self._startsize
        self._start.fill_color = sf.Color.GREEN
        self._start.outline_color = sf.Color.RED
        self._start.outline_thickness = 2
        self._start.position = self._startposition
        self._startfield = sf.Rectangle(self._startposition, self._startsize)
        
        self._font = sf.Font.from_file("Ubuntu-R.ttf")

        self._starttext = sf.Text("Start Game", self._font, 17)
        self._starttext.position = self._startposition
        self._starttext.color = sf.Color.BLACK
        self._starttext.style =sf.Text.BOLD

        self._titel = sf.Text("BaconBulb", self._font, 50)

    def loop(self):

        self._window.draw(self._titel)
        self._window.draw(self._start)
        self._window.draw(self._starttext)
        

    def listen_for_event(self, event):
        self.space_listener(event)
        self.mouse_listener(event)

    def space_listener(self, event):
        if type(event) is sf.KeyEvent and event.pressed and event.code is sf.Keyboard.SPACE:
            self._game_menu.start_game()

    def mouse_listener(self, event):
        if type(event) is sf.MouseButtonEvent and event.pressed and sf.Mouse.is_button_pressed(sf.Mouse.LEFT):
            mouse_pos = sf.Mouse.get_position(self._window)
            if self._startfield.contains(mouse_pos):
                self._start.fill_color = sf.Color.RED
        if type(event) is sf.MouseButtonEvent and event.released:
            mouse_pos = sf.Mouse.get_position(self._window)
            if self._startfield.contains(mouse_pos):
                self._start.fill_color = sf.Color.GREEN
                self._game_menu.start_game()
        if type(event) is sf.MouseButtonEvent and event.released:
                self._start.fill_color = sf.Color.GREEN