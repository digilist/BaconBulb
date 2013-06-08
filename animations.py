import sfml as sf
import settings
from datetime import datetime

class Animation(sf.Drawable):
    def __init__(self, loop = False):
        sf.Drawable.__init__(self)

        self._loop = loop
        self._frames = []

        self._current_frame = 0
        self._timer = None # contains last frame time

    def addFrame(self, timer, canvas):
        self._frames.append({
            "timer": timer,
            "canvas": canvas
        })

    def draw(self, target, states):
        current_frame = self._frames[self._current_frame];
        current_frame["canvas"].position = self.position

        test = sf.Text("BaconBulb", settings.font, 50)
        target.draw(current_frame["canvas"], states)

        if(self._timer == None):
            self._timer = datetime.now()
        
        diff =  datetime.now() - self._timer
        diff = (diff.seconds * 1000) + (diff.microseconds / 1000)
        
        if(diff >= current_frame["timer"]):
            self._timer = None
            self._current_frame += 1

        if(self._current_frame >= len(self._frames)):
            if(self._loop):
                self._current_frame = 0
            else:
                self._current_frame = len(self._frames) - 1