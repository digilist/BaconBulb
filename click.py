#! /usr/bin/python2.7
import sfml as sf

window = sf.RenderWindow(sf.VideoMode(800, 600), "BaconBulb")

rec = sf.RectangleShape()
rec.size = (50,50)
rec.fill_color = sf.Color(100,100,100)
rec.outline_color = sf.Color(50,50,50)
rec.outline_thickness = 5
rec.position = (250,50)

rec2 = sf.Rectangle(sf.Vector2(250,50), sf.Vector2(50,50))


# start the game loop
while window.is_open:
   # process events
   for event in window.events:
      # close window: exit
      if type(event) is sf.CloseEvent:
         window.close()

   if sf.Mouse.is_button_pressed(sf.Mouse.LEFT):
   	mouse_pos = sf.Mouse.get_position(window)
   	if rec2.contains(mouse_pos):
   		rec.fill_color = sf.Color.RED
  	
   

   window.clear() # clear screen
   #window.draw(text)
   window.draw(rec)
   window.display() # update the window