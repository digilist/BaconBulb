#!/usr/bin/env python2.7

""" Main File"""

import sfml as sf
from game_menu import GameMenu
import settings;

class Startup():

    def __init__(self):
        self._window = sf.RenderWindow(sf.VideoMode(settings.windowWidth, settings.windowHeight), "pySFML Window")
        self._game_menu = GameMenu(self._window)

    def run(self):
        while self._window.is_open:
            self.loop()

    def loop(self):
        self._window.clear(sf.Color.BLACK)
        self._game_menu.dispatch()
        self._window.display()

Startup().run()