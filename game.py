import sfml as sf
import random
import settings
from animations import Animation
from datetime import datetime
from drawable_container import DrawableContainer
from powerbar import Powerbar

class Game():

    def __init__(self, window, game_menu):
        self._window = window
        self._game_menu = game_menu
        self._game_engine = GameEngine(window)

    def loop(self):
        self._game_engine.loop()

        if self._game_engine._check_end():
            self._game_menu.show_gameover(self._game_engine._points) # later show highscore
            self._game_engine.reset()

    def listen_for_event(self, event):
        self._escape_listener(event);
        self._game_engine._click_listener(event);
    
    def _escape_listener(self, event):
        if type(event) is sf.KeyEvent and event.pressed and event.code is sf.Keyboard.ESCAPE:
            self._game_menu.show_splash()

class GameEngine():

    def __init__(self, window):
        self._window = window
        self._columns = 15
        self._rows = 10
        self._windowWidth = 30
        self._windowHeight = 30
        self._borderWeight = 2;
        self._houseColor = sf.Color(50, 50, 50)

        house_size = self._get_house_size()

        self._house_position = ((settings.windowWidth - house_size[0]) / 2, (settings.windowHeight - house_size[1]) / 2)

        self.reset()
        
    def reset(self):
        self._meter_view = MeterView(self._window)
        self._points = 0
        self._acceleration = True

        self._powerbar_view = PowerbarView(self._window)
        self._energy = 100
        self._energy_cmp = self._energy
        self._dt = datetime.now()
        self._dt2 = datetime.now()
        self._dt3 = datetime.now()
        self._dt_cmp = self._dt
        self._dt_cmp2= self._dt
        self._dt_cmp3 = self._dt

        self._frame_count = 0
        self._window_on_count = 50

        self._monster_texture = settings.monsterTexture
        self._monster_sprite = sf.Sprite(self._monster_texture)

        self._windows = {} # contains all windows with their current status
        for x in range (0, self._columns):
            self._windows[x] = {}
            for y in range (0, self._rows):
                self._create_window(x, y)


    def loop(self):
        self._turn_on_light()
        self._turn_off_lights()
        self._display_house()
        # self._display_main_monster()
        self._display_meter()
        self._dt_cmp = datetime.now()
        self._dt_cmp3 = datetime.now()
        if((self._dt_cmp-self._dt).microseconds >= 1/40):
            self._dt = self._dt_cmp
            self._energy_cmp = self._energy
            self._display_powerbar()
        if((self._dt_cmp3-self._dt3).microseconds >= 600000):
            self._dt3 = self._dt_cmp3
            self._spawn_rnd_monster()
            

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
            self._windows[x][y]["status"] = True
            self._windows[x][y]["window"].fill_color = sf.Color.WHITE
            self._windows[x][y]["create_time"] = datetime.now()
            self._windows[x][y]["energyConsumption"] = 0.01
            animWin = Animation(self._windows[x][y]["window"])
            self._windows[x][y]["animating"] = animWin
            self._windows[x][y]["a_creation_time"] = datetime.now()

        if (self._frame_count % settings.speedIncrement == 0 and self._acceleration):
            self._window_on_count = self._window_on_count - 1 if self._window_on_count > 1 else 1

        self._frame_count += 1

    """ Turn off bulbs that were on for too long """
    def _turn_off_lights(self):
        for x in range (0, self._columns):
            for y in range (0, self._rows):
                if (self._windows[x][y]["status"] and (datetime.now()-self._windows[x][y]["create_time"]).seconds >= 9):
                    self._windows[x][y]["status"] = False
                    self._windows[x][y]["hasBread"] = False
                    self._windows[x][y]["window"].fill_color = self._houseColor

    def _display_house(self):
        totalConsumption = 0

        self._dt_cmp2 = datetime.now()
        if((self._dt2-self._dt_cmp2).microseconds >= 1/40):
            for x in range (0, self._columns):
                for y in range (0, self._rows):
                    if(self._windows[x][y]["status"]):
                        self._window.draw(self._windows[x][y]["animating"])
                        if(self._windows[x][y]["hasBread"] == True):
                            self._monster_sprite.position = self._windows[x][y]["window"].position
                            self._window.draw(self._monster_sprite)
                        totalConsumption += self._windows[x][y]["energyConsumption"]
                    elif(not self._windows[x][y]["isDrawn"]):
                        self._window.draw(self._windows[x][y]["window"])
                        self._windows[x][y]["isDrawn"] = True

        self._energy -= totalConsumption



    """ Display the meter, which shows the counter """
    def _display_meter(self):
        self._meter_view.draw(self._points)

    def _display_powerbar(self):
        self._powerbar_view.draw(self._energy)

    def _display_main_monster(self):
        monster = sf.Sprite(self._monster_texture)
        monster.texture_rectangle = sf.Rectangle((0, 0), (self._monster_texture.width, self._monster_texture.height))
        monster.position = ((settings.windowWidth - self._monster_texture.width) / 2, (settings.windowHeight - self._monster_texture.height) / 2)

    """ Check, whether the game is over """
    def _check_end(self):

        end = True

        if(not self._energy < 0.5):
            for x in range (0, self._columns):
                for y in range (0, self._rows):
                    end = end and self._windows[x][y]["status"]

        return end

    def _keyboard_listener(self, event):
        movementSpeed = 10
        if sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
            self._house_position = (self._house_position[0], self._house_position[1] + movementSpeed)
        if sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
            self._house_position = (self._house_position[0], self._house_position[1] - movementSpeed)
        if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT):
            self._house_position = (self._house_position[0] + movementSpeed, self._house_position[1])
        if sf.Keyboard.is_key_pressed(sf.Keyboard.LEFT):
            self._house_position = (self._house_position[0] - movementSpeed, self._house_position[1])

        if type(event) is sf.KeyEvent and event.pressed and event.code is sf.Keyboard.SPACE:
            self._acceleration = not self._acceleration

    """ Listen for the clicks on windows """
    def _click_listener(self, event):
        if type(event) is sf.MouseButtonEvent and event.pressed is True and event.button is sf.Mouse.LEFT:
            for x in range (0, self._columns):
                for y in range (0, self._rows):
                    if self._are_coordinates_in_window(event.position.x, event.position.y, x, y) and self._windows[x][y]["status"]:
                            self._lightbulb_clicked(x, y)

    def _lightbulb_clicked(self, x, y):
        diff = datetime.now() -self._windows[x][y]["create_time"]
        diff = round(((diff.seconds * 1000) + (diff.microseconds/1000))/100)

        points = max(5, 50-diff)
        if(self._energy+1 > 100):
            self._energy = 100
        else:
            self._energy += 1

        if(self._windows[x][y]["hasBread"]):
            if(self._energy+2 > 100):
                self._energy = 100
            else:
                self._energy += 2
                self._points += 10
        self._points += points
        self._windows[x][y]["status"] = False
        self._windows[x][y]["window"].fill_color = self._houseColor
        self._windows[x][y]["hasBread"] = False
        self._windows[x][y]["animating"] = None

    """ create a new Window on the given coordinates """
    def _create_window(self, x, y):
        pX = x * (self._windowWidth + self._borderWeight) + self._borderWeight
        pY = y * (self._windowHeight + self._borderWeight) + self._borderWeight

        window = sf.RectangleShape(sf.Vector2(self._windowWidth, self._windowHeight))
        window.fill_color = self._houseColor

        window.position = sf.Vector2(pX, pY) + self._house_position
        

        self._windows[x][y] = {
            "window": window,
            "status": False,
            "create_time": datetime.now(),
            "energyConsumption": 0,
            "animating": None,
            "a_creation_time": datetime.now(),
            "isDrawn": False,
            "hasBread": False
        }

    def _spawn_rnd_monster(self):
        rnd = random.random()*100
        if(rnd < 10):
            OnWindows = []
            for x in range (0, self._columns):
                for y in range (0, self._rows):
                    if self._windows[x][y]["status"]:
                        OnWindows.append([x, y])
            target = OnWindows.pop(random.randint(0, len(OnWindows) - 1))
            x, y = target[0], target[1]
            self._windows[x][y]["hasBread"] = True


    # """ creates a animated window, which appears when the light was turned on """
    # def _create_animated_window(self):
    #     animation = Animation()

    #     for i in range(255, 5, -10):
    #         w = sf.RectangleShape()
    #         w.size = sf.Vector2(self._windowWidth, self._windowHeight)
    #         w.fill_color = sf.Color(255, 255, i)
            
    #         animation.add_frame(200, w)

    #     last_frame = animation.get_frame(animation.get_number_of_frames() - 1)
    #     last_frame["timer"] = 2000
        
    #     rand = random.random() * 100
    #     if(rand < 30): # in 30% of windows show the monster

    #         monster = sf.Sprite(self._monster_texture)
    #         monster.texture_rectangle = sf.Rectangle((0, 0), (self._monster_texture.width, self._monster_texture.height))

    #         container = DrawableContainer()
    #         container.add_element(last_frame["canvas"])
    #         container.add_element(monster, (8, 10))

    #         animation.add_frame(round(500 + random.random() * 1500), container)
    #         animation.add_frame(1000, last_frame["canvas"]) # and disappear

    #     return animation

    def _are_coordinates_in_window(self, positionX, positionY, windowX, windowY):
        result = positionX > self._house_position[0] + windowX * (self._windowWidth + self._borderWeight) + self._borderWeight
        result = result and positionX < self._house_position[0] + (windowX + 1) * (self._windowWidth + self._borderWeight)
        result = result and positionY > self._house_position[1] + windowY * (self._windowHeight + self._borderWeight) + self._borderWeight
        result = result and positionY < self._house_position[1] + (windowY + 1) * (self._windowHeight + self._borderWeight)

        return result

    def _get_house_size(self):
        width = self._columns * (self._windowWidth + self._borderWeight) + self._borderWeight
        height = self._rows * (self._windowHeight + self._borderWeight) + self._borderWeight

        return (width, height)

class MeterView():

    def __init__(self, window):
        self._box = sf.RectangleShape()
        self._box.size = (92, 38)
        self._box.fill_color = sf.Color.WHITE

        self._text = sf.Text("00000", settings.monospaceFont, 30)
        self._text.color = sf.Color.BLACK

        self._window = window

    def draw(self, counter):
        counter %= 100000;
        self._text.string = str(counter).zfill(5)

        self._box.position = (0,0)
        self._text.position = (0,0)

        self._window.draw(self._box)
        self._window.draw(self._text)

class PowerbarView():

    def __init__(self, window):
        self._bar = sf.RectangleShape()
        self._bar.position = (92,0)
        self._orig_size = (settings.windowWidth-self._bar.position[0],38)
        self._bar.size = (settings.windowWidth-self._bar.position[0],38)
        self._bar.fill_color = sf.Color.GREEN

        self._window = window

    def draw(self, energy):
        if energy > 50.0:
            self._bar.fill_color = sf.Color(255*(100-energy)*2/100, 255, 0, 255)
        else:
            self._bar.fill_color = sf.Color(255, 255*energy/50, 0, 255)
        self._bar.size = (energy/100*self._orig_size[0],self._orig_size[1])
        self._window.draw(self._bar)