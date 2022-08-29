from math import sqrt

class Tetraedron:
    def __init__(self, edge: float):
        self.edge = edge

    @property
    def edge(self) -> float:
        return self.edge

    def volume(self) ->float:
        return self.edge**3 * sqrt(2) / 12

    def surface(self):
        return self.edge**2 * sqrt(3)

Tetraedron(5)
