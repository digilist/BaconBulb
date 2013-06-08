#! /usr/bin/env python3

""" Main File"""

import sfml as sf
from game_menu import GameMenu
from cursor import Cursor
import settings
import copy
import time

class Startup():

    def __init__(self):
        self._window = sf.RenderWindow(sf.VideoMode(settings.windowWidth, settings.windowHeight), "BaconBulb")
        self._window.mouse_cursor_visible = False
        self._cursor = Cursor(self._window)
        self._game_menu = GameMenu(self._window)

    def run(self):
        while self._window.is_open:
            self.loop()

    def loop(self):
        self._window.clear(sf.Color(50, 50, 50))
        self._cursor.setPosition(sf.Mouse.get_position(self._window))
        self._cursor.rotate(2)
        self._game_menu.dispatch()
        self._game_menu.handle_events()
        self._window.draw(self._cursor)
        self._window.display()

Startup().run()
