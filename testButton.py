#! /usr/bin/python2.7

import sfml as sf


# create the main window
size = sf.Vector2(100,50)
pos = sf.Vector2(0,0)
rec = sf.RectangleShape()
rec.size = size
rec.fill_color = sf.Color.GREEN
rec.position = pos


window = sf.RenderWindow(sf.VideoMode(640, 480), "BaconBulb")
font = sf.Font.from_file("DroidSansMono.ttf")
text = sf.Text("GJjgLqe",font,20)
text.color = sf.Color.RED

textpos = (size - text.local_bounds.size)/2 + pos
textpos = sf.Vector2(textpos[0],(textpos[1]-(text.local_bounds.size[1]/4)))
text.position = textpos



# start the game loop
while window.is_open:
   # process events
   for event in window.events:
      # close window: exit
      if type(event) is sf.CloseEvent:
         window.close()

   window.clear() # clear screen
   window.draw(rec) # draw the sprite
   window.draw(text) # draw the string
   window.display() # update the window
   print(text.local_bounds.size)
   print(textpos)