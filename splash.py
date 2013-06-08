import sfml as sf

class Splash():

    def __init__(self, window, game_menu):
        self._window = window
        self._game_menu = game_menu
        self._font = sf.Font.from_file("DroidSansMono.ttf")
        self._titel = sf.Text("BaconBulb", self._font, 50)

        #startbutton
        self._startposition = sf.system.Vector2(350,200)
        self._startsize = sf.system.Vector2(100,20)
        self._start = sf.RectangleShape()
        self._start.size = self._startsize
        self._start.fill_color = sf.Color.GREEN
        self._start.outline_color = sf.Color.RED
        self._start.outline_thickness = 2
        self._start.position = self._startposition
        self._startfield = sf.Rectangle(self._startposition, self._startsize)
        self._starttext = sf.Text("Start Game", self._font, 17)
        self._starttext.position = self._startposition
        self._starttext.color = sf.Color.BLACK
        self._starttext.style =sf.Text.BOLD

        #highscorebutton
        self._highposition = sf.system.Vector2(350,250)
        self._highsize = sf.system.Vector2(100,20)
        self._high = sf.RectangleShape()
        self._high.size = self._highsize
        self._high.fill_color = sf.Color.GREEN
        self._high.outline_color = sf.Color.RED
        self._high.outline_thickness = 2
        self._high.position = self._highposition
        self._highfield = sf.Rectangle(self._highposition, self._highsize)
        self._hightext = sf.Text("Highscore", self._font, 17)
        self._hightext.position = self._highposition
        self._hightext.color = sf.Color.BLACK
        self._hightext.style =sf.Text.BOLD


        #background
        self._haus = sf.RectangleShape()
        self._hausplace = 300
        self._haus.size = (150,400)
        self._haus.fill_color = sf.Color.GREEN
        

    def loop(self):
        self._haus.position = (self._hausplace,200)
        self._hausplace += 1
        self._hausplace = self._hausplace % 800
        self._window.draw(self._haus)
        self._window.draw(self._titel)
        self._window.draw(self._start)
        self._window.draw(self._starttext)
        self._window.draw(self._high)
        self._window.draw(self._hightext)
        

    def listen_for_event(self, event):
        self.space_listener(event)
        self.mouse_listener(event)

    def space_listener(self, event):
        if type(event) is sf.KeyEvent and event.pressed and event.code is sf.Keyboard.SPACE:
            self._game_menu.start_game()

    def mouse_listener(self, event):
        if type(event) is sf.MouseButtonEvent and event.pressed and sf.Mouse.is_button_pressed(sf.Mouse.LEFT):
            mouse_pos = sf.Mouse.get_position(self._window)
            #startbutton
            if self._startfield.contains(mouse_pos):
                self._start.fill_color = sf.Color.RED
            #highscorebutton
            if self._highfield.contains(mouse_pos):
                self._high.fill_color = sf.Color.RED
        if type(event) is sf.MouseButtonEvent and event.released:
            mouse_pos = sf.Mouse.get_position(self._window)
            #startbutton
            if self._startfield.contains(mouse_pos):
                self._start.fill_color = sf.Color.GREEN
                self._game_menu.start_game()
            #highscorebutton
            if self._highfield.contains(mouse_pos):
                self._high.fill_color = sf.Color.GREEN
                
        if type(event) is sf.MouseButtonEvent and event.released:
                self._start.fill_color = sf.Color.GREEN
                self._high.fill_color = sf.Color.GREEN