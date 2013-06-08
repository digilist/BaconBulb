import sfml as sf
import settings

class Animation(sf.Drawable):
    def __init__(self, loop = 0):
        sf.Drawable.__init__(self)

        self._loop = loop
        self._frames = []

        self._current_frame = 0
        self._timer = 0

    def addFrame(self, timer, canvas):
        self._frames.append({
            "timer": timer,
            "canvas": canvas
        })

    def draw(self, target, states):
        current_frame = self._frames[self._current_frame];

        test = sf.Text("BaconBulb", settings.font, 50)
        target.draw(current_frame["canvas"], states)
        #print target
        #target.draw(test, stages)
        print("lol")       
       # print current_frame["canvas"]

        self._timer += 1
        if(self._timer >= current_frame.timer):
            self.timer = 0
            self._current_frame += 1

        if(self._current_frame >= len(self._frames)):
            if(self._loop):
                self._current_frame = 0
            else:
                self._current_frame = len(self._frames) - 1