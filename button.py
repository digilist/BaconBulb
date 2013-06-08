import sfml as sf

class Button(sf.Drawable):
	def __init__(self,position,size,bgcolor,fgcolor,linecolor,linesize,lable,font,fontsize):
		self._position = position
		self._size = size
		self._bgcolor = bgcolor
		self._fgcolor = fgcolor
		self._linecolor = linecolor
		self._linesize = linesize
		self._lable = lable
		self._font = font
		self._fontsize = fontsize

	#def RecShape():
		#RectangleShape
		self._recShape = sf.RectangleShape()
		self._recShape.position = self._position
		self._recShape.size = self._size
		self._recShape.fill_color = self._bgcolor
		self._recShape.outline_color = self._linecolor
		self._recShape.outline_thickness = self._linesize

	#def Rec():
		#Rectangle
		self._rec = sf.Rectangle(self._position, self._size)

	#def Text():
		#text
		self._text = sf.Text()
		self._text.string = self._lable
		self._text.font = self._font
		self._text.character_size = self._fontsize
		textpos = (self._size - self._text.local_bounds.size)/2 + self._position
		textpos = sf.Vector2(textpos[0],(textpos[1]-(self._text.local_bounds.size[1]/4)))
		self._text.position = textpos
		self._text.color = self._fgcolor

	def draw(self, target, states):
		target.draw(self._recShape, states)
		target.draw(self._text, states)

	def contains(self, point):
		return self._rec.contains(point)

	# change backgroundcolor
	def bgcolor(self, color):
		self._recShape.fill_color = color

	# change text color
	def fgcolor(self, color):
		self._text.color

	#change position
	def position(self, position):
		self._recShape.position = position
		self._rec.position = position
		textpos = (self._size - self._text.local_bounds.size)/2 + self._position
		textpos = sf.Vector2(textpos[0],(textpos[1]-(self._text.local_bounds.size[1]/4)))
		self._text.position = textpos

