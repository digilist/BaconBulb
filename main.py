#! /usr/bin/env python3

""" Main File"""

import sfml as sf
from game_menu import GameMenu
from animations import Animation
import settings
import time

class Startup():

    def __init__(self):
        self._window = sf.RenderWindow(sf.VideoMode(settings.windowWidth, settings.windowHeight), "BaconBulb")
        self._game_menu = GameMenu(self._window)

        test = sf.Text("BaconBulb", settings.font, 50)
        test2 = sf.Text("Blub", settings.font, 50)

        self._animation = Animation()
        self._animation.addFrame(1000, test)
        self._animation.addFrame(1000, test2)

    def run(self):
        while self._window.is_open:
            self.loop()

    def loop(self):
        self._window.clear(sf.Color.BLACK)
        #self._window.draw(self._animation)
        self._game_menu.dispatch()
        self._game_menu.handle_events()
        self._window.display()

Startup().run()
