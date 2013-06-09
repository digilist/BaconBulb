import sfml as sf
import settings
from button import Button

class Splash():

    def __init__(self, window, game_menu):
        self._window = window
        self._game_menu = game_menu
        self._font = settings.defaultFont
        self._titel = sf.Text("BaconBulb", self._font, 50)

        self._menubuttons = []
        #startbutton
        self._startbutton = Button(sf.Vector2((self._window.size[0]-200)/2,200), #position
                                   sf.Vector2(150,20),  #size
                                   sf.Color.GREEN,      #background color
                                   sf.Color.BLACK,      #text color
                                   sf.Color.RED,        #outline color
                                   2,                   #outline thickness
                                   "Start Game",        #lable
                                   self._font,          #font
                                   17)                  #text size
        self._menubuttons.append(self._startbutton)

        #highscorebutton
        self._highscorebutton = Button(sf.Vector2((self._window.size[0]-200)/2,250), #position
                                       sf.Vector2(150,20),  #size
                                       sf.Color.GREEN,      #background color
                                       sf.Color.BLACK,      #text color
                                       sf.Color.RED,        #outline color
                                       2,                   #outline thickness
                                       "Highscore",         #lable
                                       self._font,          #font
                                       17)                  #text size
        self._menubuttons.append(self._highscorebutton)

        #quitbutton
        self._quitbutton = Button(sf.Vector2((self._window.size[0]-200)/2,300), #position
                                  sf.Vector2(150,20),  #size
                                  sf.Color.GREEN,      #background color
                                  sf.Color.BLACK,      #text color
                                  sf.Color.RED,        #outline color
                                  2,                   #outline thickness
                                  "Quit",              #lable
                                  self._font,          #font
                                  17)                  #text size
        self._menubuttons.append(self._quitbutton)



        #background
        self._haus = sf.RectangleShape()
        self._hausplace = 300
        self._haus.size = (150,400)
        self._haus.fill_color = sf.Color.GREEN
        self._haus2 = sf.RectangleShape()
        self._haus2place = 300
        self._haus2.size = (400,150)
        self._haus2.fill_color = sf.Color.RED
        

    def loop(self):
        self._haus.position = (self._hausplace,200)
        self._hausplace += 1
        self._hausplace = self._hausplace % 800
        self._haus2.position = (self._haus2place,450)
        self._haus2place -= 1
        self._haus2place = self._haus2place % 800
        self._window.draw(self._haus)
        self._window.draw(self._haus2)
        self._window.draw(self._titel)
        for b in self._menubuttons:
            self._window.draw(b)

        
    def listen_for_event(self, event):
        self.space_listener(event)
        self.mouse_listener(event)

    def space_listener(self, event):
        if type(event) is sf.KeyEvent and event.pressed and event.code is sf.Keyboard.SPACE:
            self._game_menu.start_game()

    def mouse_listener(self, event):
        if type(event) is sf.MouseButtonEvent and event.pressed and sf.Mouse.is_button_pressed(sf.Mouse.LEFT):
            mouse_pos = sf.Mouse.get_position(self._window)
            for b in self._menubuttons:
              if b.contains(mouse_pos):
                b.bgcolor(sf.Color.RED)
        
        if type(event) is sf.MouseButtonEvent and event.released and event.button == sf.Mouse.LEFT:
            mouse_pos = sf.Mouse.get_position(self._window)
            #startbutton
            if self._startbutton.contains(mouse_pos):
              self._game_menu.start_game()
            #higscorebutton
            if self._highscorebutton.contains(mouse_pos):
              self._game_menu._highscore.scorelist()
              self._game_menu.show_highscore()
            #quitbutton
            if self._quitbutton.contains(mouse_pos):
              self._game_menu.close()    
        if type(event) is sf.MouseButtonEvent and event.released:
            for b in self._menubuttons:
              b.bgcolor(sf.Color.GREEN)
