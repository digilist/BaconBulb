#! /usr/bin/python3

import sfml as sf

class Cursor(sf.Drawable):
    def __init__(self, window):
        self._window = window
        self._icon = cursorIcon

    def setPosition(self,pos):
        self._icon.position = pos -(14,16)

    def rotate(self, angle):
        self._icon.rotate(angle)

    def draw(self, target, states):
        target.draw(self._icon, states)

