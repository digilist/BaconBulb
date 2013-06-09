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
        self._titletext = sf.Text("Game Over", self._font, 50)
        self._titletext_left = sf.Text("Game Over", self._font, 50)
        self._titletext_up = sf.Text("Game Over", self._font, 50)
        self._titletext_right = sf.Text("Game Over", self._font, 50)
        self._titletext_down = sf.Text("Game Over", self._font, 50)
        self._titletext_left.color = sf.Color.BLACK
        self._titletext_up.color = sf.Color.BLACK
        self._titletext_right.color = sf.Color.BLACK
        self._titletext_down.color = sf.Color.BLACK
        self._titletext.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,50)
        self._titletext_left.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2-1.5,50)
        self._titletext_up.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,50-1.5)
        self._titletext_right.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2+1.5,50)
        self._titletext_down.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,50+1.5)
        self._scoretext = sf.Text("Points "+str(self._game_menu._points), self._font, 50)
        self._enternametext = sf.Text("Enter Name!", self._font, 50)
        self._enternametext_left = sf.Text("Enter Name!", self._font, 50)
        self._enternametext_up = sf.Text("Enter Name!", self._font, 50)
        self._enternametext_right = sf.Text("Enter Name!", self._font, 50)
        self._enternametext_down = sf.Text("Enter Name!", self._font, 50)
        self._enternametext.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,250)
        self._enternametext_left.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2-1.5,250)
        self._enternametext_up.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,250-1.5)
        self._enternametext_right.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2+1.5,250)
        self._enternametext_down.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,250+1.5)
        self._enternametext_left.color = sf.Color.BLACK
        self._enternametext_up.color = sf.Color.BLACK
        self._enternametext_right.color = sf.Color.BLACK
        self._enternametext_down.color = sf.Color.BLACK
        self._nametext = sf.Text(self._name, self._font, 50)
        self._nametext_left = sf.Text(self._name, self._font, 50)
        self._nametext_up = sf.Text(self._name, self._font, 50)
        self._nametext_right = sf.Text(self._name, self._font, 50)
        self._nametext_down = sf.Text(self._name, self._font, 50)
        self._nametext.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,350)
        self._nametext_left.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2-1.5,350)
        self._nametext_up.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,350-1.5)
        self._nametext_right.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2+1.5,350)
        self._nametext_down.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,350+1.5)
        self._nametext_left.color = sf.Color.BLACK
        self._nametext_up.color = sf.Color.BLACK
        self._nametext_right.color = sf.Color.BLACK
        self._nametext_down.color = sf.Color.BLACK

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




    def loop(self, background):
        self._scoretext.string = "Points " + str(self._game_menu._points)
        self._scoretext_left = sf.Text("Points "+str(self._game_menu._points), self._font, 50)
        self._scoretext_up = sf.Text("Points "+str(self._game_menu._points), self._font, 50)
        self._scoretext_right = sf.Text("Points "+str(self._game_menu._points), self._font, 50)
        self._scoretext_down = sf.Text("Points "+str(self._game_menu._points), self._font, 50)
        self._scoretext.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,150)
        self._scoretext_left.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2-1.5,150)
        self._scoretext_up.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,150-1.5)
        self._scoretext_right.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2+1.5,150)
        self._scoretext_down.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,150+1.5)
        self._scoretext_left.color = sf.Color.BLACK
        self._scoretext_up.color = sf.Color.BLACK
        self._scoretext_right.color = sf.Color.BLACK
        self._scoretext_down.color = sf.Color.BLACK
        background.draw(self._window)
        self._window.draw(self._titletext_left)
        self._window.draw(self._titletext_up)
        self._window.draw(self._titletext_right)
        self._window.draw(self._titletext_down)
        self._window.draw(self._titletext)
        self._window.draw(self._enternametext_left)
        self._window.draw(self._enternametext_up)
        self._window.draw(self._enternametext_right)
        self._window.draw(self._enternametext_down)
        self._window.draw(self._enternametext)
        self._window.draw(self._scoretext_left)
        self._window.draw(self._scoretext_up)
        self._window.draw(self._scoretext_right)
        self._window.draw(self._scoretext_down)
        self._window.draw(self._scoretext)
        self._window.draw(self._nametext_left)
        self._window.draw(self._nametext_up)
        self._window.draw(self._nametext_right)
        self._window.draw(self._nametext_down)
        self._window.draw(self._nametext)
        self._window.draw(self._okbutton)



        
    def listen_for_event(self, event):
        self.mouse_listener(event)
        self.text_listener(event)
        self.key_listener(event)

    def key_listener(self, event):
        if type(event) is sf.KeyEvent and event.pressed and event.code is sf.Keyboard.RETURN:
            self._highscore.addScore(self._name,self._game_menu._points)
            self._name = ""
            self._nametext.string = ""
            self._game_menu._highscore.scorelist()
            self._game_menu.show_highscore()
        try:
            if type(event) is sf.KeyEvent and event.pressed and event.code is sf.Keyboard.BACK_SPACE:
                if not (len(self._name)==0):
                    self._name = self._name[:-1]
                    self._nametext.string = self._name
                    self._nametext_left.string = self._name
                    self._nametext_up.string = self._name
                    self._nametext_right.string = self._name
                    self._nametext_down.string = self._name
        except AttributeError: 
            if type(event) is sf.KeyEvent and event.pressed and event.code is sf.Keyboard.BACK:
                if not (len(self._name)==0):
                    self._name = self._name[:-1]
                    self._nametext.string = self._name
                    self._nametext_left.string = self._name
                    self._nametext_up.string = self._name
                    self._nametext_right.string = self._name
                    self._nametext_down.string = self._name


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
                self._name = ""
                self._nametext.string = ""
                self._game_menu._highscore.scorelist()
                self._game_menu.show_highscore()   
        if type(event) is sf.MouseButtonEvent and event.released:
            self._okbutton.bgcolor(sf.Color.GREEN)

    def text_listener(self, event):
        if type(event) is sf.TextEvent:
            if(48 <= event.unicode <= 57 or 65 <= event.unicode <= 90 or 97 <= event.unicode <= 122):
                self._name += chr(event.unicode)
                self._nametext.string = self._name
                self._nametext_left.string = self._name
                self._nametext_up.string = self._name
                self._nametext_right.string = self._name
                self._nametext_down.string = self._name
