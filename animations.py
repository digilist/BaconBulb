# import sfml as sf
# from datetime import datetime

# class Animation(sf.Drawable):
#     def __init__(self, loop = False):
#         sf.Drawable.__init__(self)

#         self._loop = loop
#         self._frames = []

#         self._current_frame = 0
#         self._timer = None # contains last frame time

#     def add_frame(self, timer, canvas):
#         self._frames.append({
#             "timer": timer,
#             "canvas": canvas
#         })

#     def get_current_frame(self):
#         return self._current_frame

#     def get_number_of_frames(self):
#         return len(self._frames)

#     def get_frame(self, frame):
#         return self._frames[frame]

#     def draw(self, target, states):
#         current_frame = self.get_frame(self._current_frame)
#         current_frame["canvas"].position = self.position

#         target.draw(current_frame["canvas"], states)

#         if(self._timer == None):
#             self._timer = datetime.now()
        
#         diff =  datetime.now() - self._timer
#         diff = (diff.seconds * 1000) + (diff.microseconds / 1000)
        
#         if(diff >= current_frame["timer"]):
#             self._timer = None
#             self._current_frame += 1

#         if(self._current_frame >= len(self._frames)):
#             if(self._loop):
#                 self._current_frame = 0
#             else:
#                 self._current_frame = len(self._frames) - 1

import sfml as sf
from datetime import datetime
import settings

class Animation(sf.Drawable):
    def __init__(self, hwindow):
        sf.Drawable.__init__(self)

        self._hwindow = hwindow

        self._dt = datetime.now()
        self._dt_cmp = self._dt


    def draw(self, target, states):
        self._dt_cmp = datetime.now()
        r, g, b, a = self._hwindow.fill_color

        if (self._dt_cmp-self._dt).microseconds >= 200000 and b >= 10:
            self._hwindow.fill_color = sf.Color(r,g,b-10,a)
            self._dt = self._dt_cmp
            target.draw(self._hwindow, states)
        else:
            target.draw(self._hwindow)