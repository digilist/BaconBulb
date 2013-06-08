import sfml as sf

class DrawableContainer(sf.Drawable):
    def __init__(self):
        sf.Drawable.__init__(self)
        self._container = []
        self.position = (0, 0)

    def add_element(self, element, position = None):
        if(position == None):
            position = element.position

        self._container.append({
            "element": element,
            "position": position
        })

    def draw(self, target, states):
        for e in self._container:
            element = e["element"]

            old_position = element.position
            element.position = self.position
            element.position += e["position"]

            target.draw(element, states)

            element.position = old_position