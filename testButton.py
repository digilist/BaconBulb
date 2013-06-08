#! /usr/bin/python2.7

import sfml as sf
from button import Button


# create the main window
#size = sf.Vector2(100,50)
#pos = sf.Vector2(0,0)
#rec = sf.RectangleShape()
#rec.size = size
#rec.fill_color = sf.Color.GREEN
#rec.position = pos


window = sf.RenderWindow(sf.VideoMode(640, 480), "BaconBulb")
font = sf.Font.from_file("DroidSansMono.ttf")
#text = sf.Text("GJjgLqe",font,20)
#text.color = sf.Color.RED

#textpos = (size - text.local_bounds.size)/2 + pos
#textpos = sf.Vector2(textpos[0],(textpos[1]-(text.local_bounds.size[1]/4)))
#text.position = textpos

newbutton = Button(sf.Vector2(100,100),sf.Vector2(80,80),sf.Color.GREEN,sf.Color.RED,sf.Color.BLUE,2,"wurst",font,15)


def handle_events(self):
   for event in self.window.events:
      self.listen_for_event(event)
      self.close_listener(event)

def listen_for_event(self, event):
      self.space_listener(event)
      self.mouse_listener(event)

def mouse_listener(self, event):
   if type(event) is sf.MouseButtonEvent and event.pressed and sf.Mouse.is_button_pressed(sf.Mouse.LEFT):
      mouse_pos = sf.Mouse.get_position(self._window)
      
      if self.newbutton.contains(mouse_pos):
         self.newbutton.bgcolor= sf.Color.RED
      
                
      if type(event) is sf.MouseButtonEvent and event.released:
         self.newbutton.bgcolor = sf.Color.GREEN

   def window_listener(self, event):
      if type(event) is sf.CloseEvent:
         window.close()


# start the game loop
while window.is_open:
   # process events
   handle_events()
      

   window.clear() # clear screen
   #window.draw(rec) # draw the sprite
   #window.draw(text) # draw the string
   window.draw(newbutton)
   window.display() # update the window