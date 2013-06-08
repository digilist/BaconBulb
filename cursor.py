#! /usr/bin/python3

import sfml as sf

# load cursor icon
texture = sf.Texture.from_file("assets/cursor.png")
cursorIcon = sf.Sprite(texture)

class Cursor(sf.Drawable):
	def __init__(self, window):
		self._window = window
		self._icon = cursorIcon

	def setPosition(self,pos):
		self._icon.position = pos -(14,16)

	def draw(self, target, states):
		target.draw(self._icon, states)