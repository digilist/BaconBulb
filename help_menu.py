import sfml as sf
import settings
from button import Button

class Help_Menu():

    def __init__(self, window, game_menu):
        self._window = window
        self._game_menu = game_menu
        self._font = settings.defaultFont
        self._name = ""
        
        self._titletext = sf.Text("Help", self._font, 50)
        self._titletext_left = sf.Text("Help", self._font, 50)
        self._titletext_up = sf.Text("Help", self._font, 50)
        self._titletext_right = sf.Text("Help", self._font, 50)
        self._titletext_down = sf.Text("Help", self._font, 50)

        self._titletext.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,20)
        self._titletext_left.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2-1.5,20)
        self._titletext_up.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,20-1.5)
        self._titletext_right.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2+1.5,20)
        self._titletext_down.position = ((self._window.size[0]-self._titletext.local_bounds.size[0])/2,20+1.5)
        self._titletext_left.color = sf.Color.BLACK
        self._titletext_up.color = sf.Color.BLACK
        self._titletext_right.color = sf.Color.BLACK
        self._titletext_down.color = sf.Color.BLACK

        self._helptext = sf.Text("The goal of this game is to light-off as many bulbs with your\nbacon as possible. The brighter/whiter the light is,"+
                                 "the more\npoints you will get for lighting it off...\n"+
                                 "Occasionally some bread slices will appear on top of lighted\n"+
                                 "windows. Lighting off windows with these slices will give you\n"+
                                 "some extra points.\n"+
                                 "Additionally at the top corner you will find a points-counter\n"+
                                 "and a bar representing your remaining energy. Lighting off\n"+
                                 "windows will replenish some of your energy and those with a\n"+
                                 "bread slice will replenish even a bit more.\n"+
                                 "But beware! Every window is consuming some of your energy\n"+
                                 "and so the more windows are lighted, the faster your energy\n"+
                                 "will be consumed. The further you are into the game, the\n"+
                                 "faster new windows will be lighted.\n"
                                 "Once your energy reaches 0 it\'s \"Game Over\" for you.", self._font, 25)
        self._helptext_left = sf.Text("The goal of this game is to light-off as many bulbs with your\nbacon as possible. The brighter/whiter the light is,"+
                                 "the more\npoints you will get for lighting it off...\n"+
                                 "Occasionally some bread slices will appear on top of lighted\n"+
                                 "windows. Lighting off windows with these slices will give you\n"+
                                 "some extra points.\n"+
                                 "Additionally at the top corner you will find a points-counter\n"+
                                 "and a bar representing your remaining energy. Lighting off\n"+
                                 "windows will replenish some of your energy and those with a\n"+
                                 "bread slice will replenish even a bit more.\n"+
                                 "But beware! Every window is consuming some of your energy\n"+
                                 "and so the more windows are lighted, the faster your energy\n"+
                                 "will be consumed. The further you are into the game, the\n"+
                                 "faster new windows will be lighted.\n"
                                 "Once your energy reaches 0 it\'s \"Game Over\" for you.", self._font, 25)
        self._helptext_up = sf.Text("The goal of this game is to light-off as many bulbs with your\nbacon as possible. The brighter/whiter the light is,"+
                                 "the more\npoints you will get for lighting it off...\n"+
                                 "Occasionally some bread slices will appear on top of lighted\n"+
                                 "windows. Lighting off windows with these slices will give you\n"+
                                 "some extra points.\n"+
                                 "Additionally at the top corner you will find a points-counter\n"+
                                 "and a bar representing your remaining energy. Lighting off\n"+
                                 "windows will replenish some of your energy and those with a\n"+
                                 "bread slice will replenish even a bit more.\n"+
                                 "But beware! Every window is consuming some of your energy\n"+
                                 "and so the more windows are lighted, the faster your energy\n"+
                                 "will be consumed. The further you are into the game, the\n"+
                                 "faster new windows will be lighted.\n"
                                 "Once your energy reaches 0 it\'s \"Game Over\" for you.", self._font, 25)
        self._helptext_right = sf.Text("The goal of this game is to light-off as many bulbs with your\nbacon as possible. The brighter/whiter the light is,"+
                                 "the more\npoints you will get for lighting it off...\n"+
                                 "Occasionally some bread slices will appear on top of lighted\n"+
                                 "windows. Lighting off windows with these slices will give you\n"+
                                 "some extra points.\n"+
                                 "Additionally at the top corner you will find a points-counter\n"+
                                 "and a bar representing your remaining energy. Lighting off\n"+
                                 "windows will replenish some of your energy and those with a\n"+
                                 "bread slice will replenish even a bit more.\n"+
                                 "But beware! Every window is consuming some of your energy\n"+
                                 "and so the more windows are lighted, the faster your energy\n"+
                                 "will be consumed. The further you are into the game, the\n"+
                                 "faster new windows will be lighted.\n"
                                 "Once your energy reaches 0 it\'s \"Game Over\" for you.", self._font, 25)
        self._helptext_down = sf.Text("The goal of this game is to light-off as many bulbs with your\nbacon as possible. The brighter/whiter the light is,"+
                                 "the more\npoints you will get for lighting it off...\n"+
                                 "Occasionally some bread slices will appear on top of lighted\n"+
                                 "windows. Lighting off windows with these slices will give you\n"+
                                 "some extra points.\n"+
                                 "Additionally at the top corner you will find a points-counter\n"+
                                 "and a bar representing your remaining energy. Lighting off\n"+
                                 "windows will replenish some of your energy and those with a\n"+
                                 "bread slice will replenish even a bit more.\n"+
                                 "But beware! Every window is consuming some of your energy\n"+
                                 "and so the more windows are lighted, the faster your energy\n"+
                                 "will be consumed. The further you are into the game, the\n"+
                                 "faster new windows will be lighted.\n"
                                 "Once your energy reaches 0 it\'s \"Game Over\" for you.", self._font, 25)

        self._helptext.position = ((self._window.size[0]-self._helptext.local_bounds.size[0])/2,100)
        self._helptext_left.position = ((self._window.size[0]-self._helptext.local_bounds.size[0])/2-1.5,100)
        self._helptext_up.position = ((self._window.size[0]-self._helptext.local_bounds.size[0])/2,100-1.5)
        self._helptext_right.position = ((self._window.size[0]-self._helptext.local_bounds.size[0])/2+1.5,100)
        self._helptext_down.position = ((self._window.size[0]-self._helptext.local_bounds.size[0])/2,100+1.5)
        self._helptext_left.color = sf.Color.BLACK
        self._helptext_up.color = sf.Color.BLACK
        self._helptext_right.color = sf.Color.BLACK
        self._helptext_down.color = sf.Color.BLACK

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




    def loop(self, background):
        background.draw(self._window)
        self._window.draw(self._titletext_left)
        self._window.draw(self._titletext_right)
        self._window.draw(self._titletext_up)
        self._window.draw(self._titletext_down)
        self._window.draw(self._titletext)
        self._window.draw(self._helptext_left)
        self._window.draw(self._helptext_up)
        self._window.draw(self._helptext_right)
        self._window.draw(self._helptext_down)
        self._window.draw(self._helptext)
        self._window.draw(self._backbutton)

        
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