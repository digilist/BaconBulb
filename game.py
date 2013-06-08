import sfml as sf
import random
import settings

class Game():

    def __init__(self, window, game_menu):
        self._window = window
        self._game_menu = game_menu
        self._game_engine = GameEngine(window)

    def loop(self):
        self._game_engine.loop()

        if self._game_engine._check_end():
            self._game_menu.show_splash() # later show highscore

    def listen_for_event(self, event):
        self._escape_listener(event);
        self._game_engine._click_listener(event);
    
    def _escape_listener(self, event):
        if type(event) is sf.KeyEvent and event.pressed and event.code is sf.Keyboard.ESCAPE:
            self._game_menu.show_splash()

class GameEngine():

    def __init__(self, window):
        self._window = window
        self._meter_view = MeterView(window)
        self._points = 0

        self._frame_count = 0
        self._window_on_count = 50

        self._window_list = [[False for y in range(10)] for x in range(5)]

    def loop(self):
        self._turn_on_lights()
        self._display_house()
        self._display_meter()

    def _turn_on_lights(self):
        if (self._frame_count % self._window_on_count == 0):
            OffWindows = []
            for x in range (0, 5):
                for y in range (0, 10):
                    if not self._window_list[x][y]:
                        OffWindows.append([x, y])
           # print len(OffWindows)
            target = OffWindows.pop(random.randint(0, len(OffWindows) - 1))
            #rint target
            self._window_list[target[0]][target[1]] = True


        if (self._frame_count % settings.speedIncrement == 0):
            self._window_on_count = self._window_on_count - 1 if self._window_on_count > 1 else 1

        self._frame_count += 1

    def _display_house(self):
        house = sf.RectangleShape()
        house.size = sf.Vector2(310, 610)
        house.fill_color = sf.Color.GREEN
        self._window.draw(house)

        for x in range (0, 5):
            for y in range (0, 10):
                rect = sf.RectangleShape()
                rect.size = sf.Vector2(50, 50)
                rect.fill_color = sf.Color.YELLOW if self._window_list[x][y] else sf.Color.BLACK
                rect.position = sf.Vector2(x*60 + 10, y*60 + 10)
                self._window.draw(rect)

    def _display_meter(self):
        self._meter_view.draw(self._points)

    def _check_end(self):
        end = True
        for x in range (5):
            for y in range (10):
                end = end and self._window_list[x][y]

        return end

    def _click_listener(self, event):
        if type(event) is sf.MouseButtonEvent and event.pressed is True and event.button is sf.Mouse.LEFT:
            for x in range (5):
                for y in range (10):
                    if event.position.x > x*60+10 and event.position.x < x*60+60 and event.position.y > y*60+10 and event.position.y < y*60+60:
                        if self._window_list[x][y]:
                            self._points += 1
                            self._window_list[x][y] = False


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