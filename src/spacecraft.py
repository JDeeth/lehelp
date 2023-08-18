from component import parse_components


class Spacecraft:
    def __init__(self):
        self.components = []

    @staticmethod
    def from_str(s):
        result = Spacecraft()
        result.components = parse_components(s)
        return result

    @property
    def mass(self):
        return sum(c.mass for c in self.components)

    @property
    def cost(self):
        return sum(c.cost for c in self.components)
