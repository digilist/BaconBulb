import sfml as sf

window = sf.RenderWindow(sf.VideoMode(640, 480), "BaconBulb")

font = sf.Font.from_file("DroidSansMono.ttf")
text = sf.Text()
text.string = "1234567"
text.font = font


while window.is_open:
   # process events
   for event in window.events:
      # close window: exit
      if type(event) is sf.CloseEvent:
         window.close()

   window.clear() # clear screen
   window.draw(text) # draw the string
   window.display() # update the window