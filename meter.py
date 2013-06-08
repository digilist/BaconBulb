import sfml as sf
import settings

class Meter():
    def __init__(self, window):
        self._counter = 0
        self._meter_view = MeterView(window)

    def incr(self):
        self._counter += 1

        self._meter_view.draw(self._counter)


class MeterView():

    def __init__(self, window):
        box = sf.RectangleShape()
        box.size = (75, 38)
        box.fill_color = sf.Color.WHITE

        self._text = sf.Text("0000", settings.monospaceFont, 30)
        self._text.color = sf.Color.BLACK

        self._box = box
        self._window = window

    def draw(self, counter):
        counter %= 10000;
        self._text.string = str(counter).zfill(4)

        self._box.position = (0,0)
        self._text.position = (0,0)

        self._window.draw(self._box)
        self._window.draw(self._text)