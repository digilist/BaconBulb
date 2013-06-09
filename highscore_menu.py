import sfml as sf
import settings
from button import Button
from highscore import Highscore
from drawable_container import DrawableContainer

class Highscore_menu():

    def __init__(self, window, game_menu):
        self._window = window
        self._game_menu = game_menu
        self._font = settings.defaultFont
        self._score = Highscore().getScore()
        
        

        #background
        self._haus = sf.RectangleShape()
        self._hausplace = 300
        self._haus.size = (150,400)
        self._haus.fill_color = sf.Color.GREEN

        

        #backbutton
        self._backbutton = Button(sf.Vector2(20,(self._window.size[1]-50)), #position
                                  sf.Vector2(150,20),  #size
                                  sf.Color.GREEN,      #background color
                                  sf.Color.BLACK,      #text color
                                  sf.Color.RED,        #outline color
                                  2,                   #outline thickness
                                  "Back",              #lable
                                  self._font,          #font
                                  17)                  #text size

    def scorelist(self):
        self._highcontainer = DrawableContainer()
        self._score = Highscore().getScore()
        self._highcontainer.position = ((self._window.size[0]-200)/2,0)
        self._titletext = sf.Text("Highscore", self._font, 50)
        self._highcontainer.add_element(self._titletext)
        for x in range(10):
            name = self._score[x]['name']
            score = self._score[x]['score']
            linename = sf.Text(name, self._font, 40)
            linescore = sf.Text(str(score), self._font, 40)
            self._highcontainer.add_element(linename,sf.Vector2(-200,(50*x)+50))
            self._highcontainer.add_element(linescore,sf.Vector2(250,(50*x+50)))


    def loop(self):
        self._haus.position = (self._hausplace,200)
        self._hausplace += 1
        self._hausplace = self._hausplace % 800
        self._window.draw(self._haus)
        self._window.draw(self._highcontainer)
        self._window.draw(self._backbutton)
            #for b in self._menubuttons:
            #   self._window.draw(b)

        
    def listen_for_event(self, event):
        self.esc_listener(event)
        self.mouse_listener(event)

    def esc_listener(self, event):
        if type(event) is sf.KeyEvent and event.pressed and event.code is sf.Keyboard.ESCAPE:
            self._game_menu.show_splash()

    def mouse_listener(self, event):
        if type(event) is sf.MouseButtonEvent and event.pressed and sf.Mouse.is_button_pressed(sf.Mouse.LEFT):
            mouse_pos = sf.Mouse.get_position(self._window)
            if self._backbutton.contains(mouse_pos):
                self._backbutton.bgcolor(sf.Color.RED)
        
        if type(event) is sf.MouseButtonEvent and event.released and event.button == sf.Mouse.LEFT:
            mouse_pos = sf.Mouse.get_position(self._window)
            #startbutton
            if self._backbutton.contains(mouse_pos):
              self._game_menu.show_splash()   
        if type(event) is sf.MouseButtonEvent and event.released:
            self._backbutton.bgcolor(sf.Color.GREEN)