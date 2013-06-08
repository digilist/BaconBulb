import sfml as sf
import random
import settings
from animations import Animation
from datetime import datetime
from drawable_container import DrawableContainer

class Game():

    def __init__(self, window, game_menu):
        self._window = window
        self._game_menu = game_menu
        self._game_engine = GameEngine(window)

    def loop(self):
        self._game_engine.loop()

        if self._game_engine._check_end():
            self._game_engine.reset()
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
        self._columns = 10
        self._rows = 10
        self._windowWidth = 50
        self._windowHeight = 50
        self._borderWeight = 10;

        self.reset()
        
    def reset(self):
        self._meter_view = MeterView(self._window)
        self._points = 0

        self._frame_count = 0
        self._window_on_count = 50

        self._monster_texture = sf.Texture.from_file("assets/monster.png")

        self._windows = {} # contains all windows with their current status
        for x in range (0, self._columns):
            self._windows[x] = {}
            for y in range (0, self._rows):
                self._create_window(x, y, False)

    def loop(self):
        self._turn_on_light()
        self._display_house()
        self._display_meter()

    """ Turn on the next bulb """
    def _turn_on_light(self):
        if (self._frame_count % self._window_on_count == 0):
            OffWindows = []
            for x in range (0, self._columns):
                for y in range (0, self._rows):
                    if not self._windows[x][y]["status"]:
                        OffWindows.append([x, y])
            target = OffWindows.pop(random.randint(0, len(OffWindows) - 1))
            x, y = target[0], target[1]
            self._create_window(x, y, True)

        if (self._frame_count % settings.speedIncrement == 0):
            self._window_on_count = self._window_on_count - 1 if self._window_on_count > 1 else 1

        self._frame_count += 1

    """ Display the House with all Windows """
    def _display_house(self):
        houseWidth = self._columns * (self._windowWidth + self._borderWeight) + self._borderWeight
        houseHeight = self._rows * (self._windowHeight + self._borderWeight) + self._borderWeight

        house = sf.RectangleShape()
        house.size = sf.Vector2(houseWidth, houseHeight)
        house.fill_color = sf.Color.GREEN
        self._window.draw(house)

        for x in range (0, self._columns):
            for y in range (0, self._rows):
                self._window.draw(self._windows[x][y]["window"])

    """ Display the meter, which shows the counter """
    def _display_meter(self):
        self._meter_view.draw(self._points)

    """ Check, whether the game is over """
    def _check_end(self):
        end = True
        for x in range (0, self._columns):
            for y in range (0, self._rows):
                end = end and self._windows[x][y]["status"]

        return end
    """ Listen for the clicks on windows """
    def _click_listener(self, event):
        if type(event) is sf.MouseButtonEvent and event.pressed is True and event.button is sf.Mouse.LEFT:
            for x in range (0, self._columns):
                for y in range (0, self._rows):
                    if self._is_mouse_in_window(event, x, y) and self._windows[x][y]["status"]:
                            self._lightblub_clicked(x, y)

    """ is called, when die lighbulb on the given coordinates is clicked """
    def _lightblub_clicked(self, x, y):
        # calculate points
        diff =  datetime.now() - self._windows[x][y]["create_time"]
        diff = round(((diff.seconds * 1000) + (diff.microseconds / 1000)) / 100) # in microseconds

        points = max(5, 50 - diff) # between 10 and 50 points

        self._points += points
        self._create_window(x, y, False)

    """ create a new Window on the given coordinates """
    def _create_window(self, x, y, turnedOn):
        if turnedOn:
            window = self._create_animated_window()
        else:
            window = sf.RectangleShape()
            window.size = sf.Vector2(self._windowWidth, self._windowHeight)
            window.fill_color = sf.Color.BLACK
            turnedOn = False

        pX = x * (self._windowWidth + self._borderWeight) + self._borderWeight
        pY = y * (self._windowHeight + self._borderWeight) + self._borderWeight
        window.position = sf.Vector2(pX, pY)

        self._windows[x][y] = {
            "window": window,
            "status": turnedOn,
            "create_time": datetime.now()
        }

    """ creates a animated window, which appears when the light was turned on """
    def _create_animated_window(self):
        animation = Animation()

        for i in range(255, 0, -50):
            w = sf.RectangleShape()
            w.size = sf.Vector2(self._windowWidth, self._windowHeight)
            w.fill_color = sf.Color(255, 255, i)
            
            animation.add_frame(100, w)

        last_frame = animation.get_frame(animation.get_number_of_frames() - 1)
        last_frame["timer"] = 2000
        
        rand = random.random() * 100
        if(rand < 30): # in 30% of windows show the monster

            monster = sf.Sprite(self._monster_texture)
            monster.texture_rectangle = sf.Rectangle((0, 0), (self._monster_texture.width, self._monster_texture.height))

            container = DrawableContainer()
            container.add_element(last_frame["canvas"])
            container.add_element(monster, (8, 10))

            animation.add_frame(round(500 + random.random() * 1500), container)
            animation.add_frame(1000, last_frame["canvas"]) # and disappear

        return animation

        #event.position.x > x *60+10 and event.position.x < x*60+60 and event.position.y > y*60+10 and event.position.y < y*60+60:

    def _is_mouse_in_window(self, event, x, y):
        result = event.position.x > x * (self._windowWidth + self._borderWeight) + self._borderWeight
        result = result and event.position.x < (x+1) * (self._windowWidth + self._borderWeight)
        result = result and event.position.y > y * (self._windowHeight + self._borderWeight) + self._borderWeight
        result = result and event.position.y < (y+1) * (self._windowHeight + self._borderWeight)

        return result

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