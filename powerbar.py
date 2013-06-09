#! /usr/bin/python3

import sfml as sf
import settings

class Powerbar(sf.Drawable):
    def __init__(self, window):
        self._window = window
        self._bar = sf.RectangleShape()
        self._position = (93,0)
        self._size = (settings.windowWidth-self._position[0],38)