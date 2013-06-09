import sfml as sf
import settings
from button import Button
from highscore import Highscore

class Gameover_menu():

    def __init__(self, window, game_menu):
        self._window = window
        self._game_menu = game_menu
        self._font = settings.defaultFont
        self._highscore = Highscore()
        self._name = ""
        

        #background
        self._haus = sf.RectangleShape()
        self._hausplace = 300
        self._haus.size = (150,400)
        self._haus.fill_color = sf.Color.GREEN
        self._titletext = sf.Text("Game Over", self._font, 50)
        self._titletext.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,50)
        self._scoretext = sf.Text("Points "+str(self._game_menu._points), self._font, 50)
        self._scoretext.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,150)
        self._nametext = sf.Text(self._name, self._font, 50)
        self._nametext.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,250)

        #backbutton
        self._okbutton = Button(sf.Vector2((self._window.size[0]-150)/2,(self._window.size[1]-50)), #position
                                  sf.Vector2(150,20),  #size
                                  sf.Color.GREEN,      #background color
                                  sf.Color.BLACK,      #text color
                                  sf.Color.RED,        #outline color
                                  2,                   #outline thickness
                                  "OK",              #lable
                                  self._font,          #font
                                  17)                  #text size




    def loop(self):
        self._haus.position = (self._hausplace,200)
        self._hausplace += 1
        self._hausplace = self._hausplace % 800
        self._scoretext.string = "Points " + str(self._game_menu._points)
        self._window.draw(self._haus)
        self._window.draw(self._titletext)
        self._window.draw(self._scoretext)
        self._window.draw(self._nametext)
        self._window.draw(self._okbutton)
            #for b in self._menubuttons:
            #   self._window.draw(b)

        
    def listen_for_event(self, event):
        self.mouse_listener(event)
        self.text_listener(event)
        self.enter_listener(event)

    def enter_listener(self, event):
        if type(event) is sf.KeyEvent and event.pressed and event.code is sf.Keyboard.RETURN:
            self._highscore.addScore(self._name,self._game_menu._points)
            self._game_menu._highscore.scorelist()
            self._game_menu.show_highscore() 

    def mouse_listener(self, event):
        if type(event) is sf.MouseButtonEvent and event.pressed and sf.Mouse.is_button_pressed(sf.Mouse.LEFT):
            mouse_pos = sf.Mouse.get_position(self._window)
            if self._okbutton.contains(mouse_pos):
                self._okbutton.bgcolor(sf.Color.RED)
        
        if type(event) is sf.MouseButtonEvent and event.released and event.button == sf.Mouse.LEFT:
            mouse_pos = sf.Mouse.get_position(self._window)
            #startbutton
            if self._okbutton.contains(mouse_pos):
                self._highscore.addScore(self._name,self._game_menu._points)
                self._game_menu._highscore.scorelist()
                self._game_menu.show_highscore()   
        if type(event) is sf.MouseButtonEvent and event.released:
            self._okbutton.bgcolor(sf.Color.GREEN)

    def text_listener(self, event):
        if type(event) is sf.TextEvent:
            if(48 <= event.unicode <= 57 or 65 <= event.unicode <= 90 or 97 <= event.unicode <= 122):
                self._name += chr(event.unicode)
                self._nametext.string = self._name
