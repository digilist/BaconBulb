#! /usr/bin/python3

import sfml as sf
import settings

class Cursor(sf.Drawable):
    def __init__(self, window):
        self._window = window
        self._icon = sf.Sprite(settings.cursorTexture)
        self._icon.origin = (12,16)

    def setPosition(self,pos):
        self._icon.position = pos

    def rotate(self, angle):
        self._icon.rotate(angle)

    def draw(self, target, states):
        target.draw(self._icon, states)
