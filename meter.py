import sfml as sf

class Meter():
    def __init__(self, window):
        self._counter = 0
        self._meter_view = MeterView(window)

    def incr(self):
        self._counter += 1
        print self._counter

        self._meter_view.draw()


class MeterView():

    def __init__(self, window):
        box = sf.RectangleShape()
        box.size = (200, 50)
        box.fill_color = sf.Color.WHITE

        self._box = box
        self._window = window

    def draw(self):
        self._window.draw(self._box)