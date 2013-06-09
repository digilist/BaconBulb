import sfml as sf
import random
import math

class Background():
    def __init__(self,window):
        self._window = window
        self._background = []
        self._radius = {}
        for x in range(40):
            self._background.append(sf.CircleShape())
            self._radius[self._background[x]] = random.randint(0,20)
            self._background[x].radius = self._radius[self._background[x]]
            self._background[x].position = (random.randint(0,self._window.size[0]),random.randint(0,self._window.size[1]))
            self._background[x].fill_color = sf.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def draw(self, target):
        for background in self._background:
            background.position = ((background.position[0] + random.randint(-1,1))%self._window.size[0], 
                                   (background.position[1] + random.randint(-1,1))%self._window.size[1])
            #background.radius = (background.radius + random.randint(-1,1))%20
            self._radius[background] = self._radius[background]+random.randint(-1,1)/10
            background.radius = math.fabs(math.sin(self._radius[background])*20)
            target.draw(background)