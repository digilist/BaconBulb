import sfml as sf
import settings
from button import Button

class Splash():

    def __init__(self, window, game_menu):
        self._window = window
        self._game_menu = game_menu
        self._font = settings.defaultFont
        self._titel = sf.Text("BaconBulb", self._font, 50)
        self._titel.position = ((self._window.size[0]-self._titel.local_bounds.size[0])/2,40)
        self._titel_left = sf.Text("BaconBulb", self._font, 50)
        self._titel_left.position = ((self._window.size[0]-self._titel.local_bounds.size[0])/2-1.5,40)
        self._titel_left.color = sf.Color.BLACK
        self._titel_up = sf.Text("BaconBulb", self._font, 50)
        self._titel_up.position = ((self._window.size[0]-self._titel.local_bounds.size[0])/2,40-1.5)
        self._titel_up.color = sf.Color.BLACK
        self._titel_right = sf.Text("BaconBulb", self._font, 50)
        self._titel_right.position = ((self._window.size[0]-self._titel.local_bounds.size[0])/2+1.5,40)
        self._titel_right.color = sf.Color.BLACK
        self._titel_down = sf.Text("BaconBulb", self._font, 50)
        self._titel_down.position = ((self._window.size[0]-self._titel.local_bounds.size[0])/2,40+1.5)
        self._titel_down.color = sf.Color.BLACK

        self._menubuttons = []
        #startbutton
        self._startbutton = Button(sf.Vector2((self._window.size[0]-150)/2,200), #position
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
        self._highscorebutton = Button(sf.Vector2((self._window.size[0]-150)/2,250), #position
                                       sf.Vector2(150,20),  #size
                                       sf.Color.GREEN,      #background color
                                       sf.Color.BLACK,      #text color
                                       sf.Color.RED,        #outline color
                                       2,                   #outline thickness
                                       "Highscore",         #lable
                                       self._font,          #font
                                       17)                  #text size
        self._menubuttons.append(self._highscorebutton)

        #helpbutton
        self._helpbutton = Button(sf.Vector2((self._window.size[0]-150)/2,300),
                                  sf.Vector2(150,20),
                                  sf.Color.GREEN,
                                  sf.Color.BLACK,
                                  sf.Color.RED,
                                  2,
                                  "Help",
                                  self._font,
                                  17)
        self._menubuttons.append(self._helpbutton)

        #quitbutton
        self._quitbutton = Button(sf.Vector2((self._window.size[0]-150)/2,350), #position
                                  sf.Vector2(150,20),  #size
                                  sf.Color.GREEN,      #background color
                                  sf.Color.BLACK,      #text color
                                  sf.Color.RED,        #outline color
                                  2,                   #outline thickness
                                  "Quit",              #lable
                                  self._font,          #font
                                  17)                  #text size
        self._menubuttons.append(self._quitbutton)

    def loop(self, background):
        background.draw(self._window)
        self._window.draw(self._titel_left)
        self._window.draw(self._titel_up)
        self._window.draw(self._titel_right)
        self._window.draw(self._titel_down)
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
            #helpbutton
            if self._helpbutton.contains(mouse_pos):
                self._game_menu.show_help()
            #quitbutton
            if self._quitbutton.contains(mouse_pos):
                self._game_menu.close()    
        if type(event) is sf.MouseButtonEvent and event.released:
            for b in self._menubuttons:
                b.bgcolor(sf.Color.GREEN)
