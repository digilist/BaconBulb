#! /usr/bin/python3

import sfml as sf

class Cursor(sf.Drawable):
    def __init__(self, window):
        # load cursor icon
        texture = sf.Texture.from_file("assets/cursor.png")
        
        self._window = window
        self._icon = sf.Sprite(texture)

    def setPosition(self,pos):
        self._icon.position = pos

    def rotate(self, angle):
        self._icon.origin = (12,16)
        self._icon.rotate(angle)

    def draw(self, target, states):
        target.draw(self._icon, states)