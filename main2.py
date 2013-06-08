"""Main File"""

import sfml as sf
import random
from datetime import datetime
#import entity

WINDOW = sf.RenderWindow(sf.VideoMode(310, 610), "lol")

FRAMECOUNT = 0
WINDOWONCOUNT = 50
SPEEDINCREMENT = 100
KILLCOUNT = 0

font = sf.Font.from_file("Ubuntu-R.ttf")

LASTDATE = datetime.now()

windowlist = [[False for y in range(10)] for x in range(5)]

#ent1 = entity.entity(sf.Color.RED, sf.Vector2(100, 100), sf.Vector2(100, 100))

while WINDOW.is_open:

    for event in WINDOW.events:
       # request for closing the window
        if type(event) is sf.CloseEvent:
            WINDOW.close()

       # the escape key was pressed
        if type(event) is sf.KeyEvent and event.code is sf.Keyboard.ESCAPE:
            WINDOW.close()

        if type(event) is sf.MouseButtonEvent and event.pressed is True and event.button is sf.Mouse.LEFT:
            for x in range (5):
                for y in range (10):
                    if event.position.x > x*60+10 and event.position.x < x*60+60 and event.position.y > y*60+10 and event.position.y < y*60+60:
                        KILLCOUNT = KILLCOUNT + 1 if windowlist[x][y] else KILLCOUNT
                        windowlist[x][y] = False
                        


    d = datetime.now() - LASTDATE
    secs = 1000000 / d.microseconds

    fps = sf.Text(str(secs))
    fps.character_size = 40
    fps.color = sf.Color.RED
    fps.style = sf.Text.BOLD
    fps.font = font

    kills = sf.Text(str(KILLCOUNT), font)

    kills.position = sf.Vector2(10, 650)

    LASTDATE = datetime.now()
    

    if (FRAMECOUNT % WINDOWONCOUNT == 0):
        OffWindows = []
        for x in range (0, 5):
            for y in range (0, 10):
                if not windowlist[x][y]:
                    OffWindows.append([x, y])
        print len(OffWindows)
        target = OffWindows.pop(random.randint(0, len(OffWindows) - 1))
        print target
        windowlist[target[0]][target[1]] = True


    if (FRAMECOUNT % SPEEDINCREMENT == 0):
        WINDOWONCOUNT = WINDOWONCOUNT - 1 if WINDOWONCOUNT > 1 else 1

    FRAMECOUNT = FRAMECOUNT + 1

    

    WINDOW.clear(sf.Color.BLACK)

    #sf.Mouse.set_position(sf.Vector2(100,100))

    house = sf.RectangleShape()
    house.size = sf.Vector2(310, 610)
    house.fill_color = sf.Color.GREEN
    WINDOW.draw(house)

    for x in range (0, 5):
        for y in range (0, 10):
            rect = sf.RectangleShape()
            rect.size = sf.Vector2(50, 50)
            rect.fill_color = sf.Color.YELLOW if windowlist[x][y] else sf.Color.BLACK
            rect.position = sf.Vector2(x*60 + 10, y*60 + 10)
            WINDOW.draw(rect)

    #ent1.draw(WINDOW)
    
    WINDOW.draw(fps) 
    WINDOW.draw(kills)

    WINDOW.display()

    end = True

    for x in range (5):
        for y in range (10):
            end = end and windowlist[x][y]


    if end == True:
        break;




while WINDOW.is_open:

    for event in WINDOW.events:
       # request for closing the window
        if type(event) is sf.CloseEvent:
            WINDOW.close()

       # the escape key was pressed
        if type(event) is sf.KeyEvent and event.code is sf.Keyboard.ESCAPE:
            WINDOW.close()

    WINDOW.clear(sf.Color.BLACK)
    WON = sf.Text("YOU LOST! SCORE: " + str(KILLCOUNT), font)
    WINDOW.draw(WON)
    WINDOW.display()
