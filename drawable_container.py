import sfml as sf

class DrawableContainer(sf.Drawable):
    def __init__(self):
        sf.Drawable.__init__(self)
        self._container = []

    def add_element(self, element, position = None):
        if(position == None):
            position = (0, 0)

        self._container.append({
            "element": element,
            "position": position
        })

    def draw(self, target, states):
        for e in self._container:
            element = e["element"]
            element.position = self.position
            element.position += e["position"]

            target.draw(element, states)