from math import sqrt


class Tetrahedron:
    def __init__(self, edge: float):
        self.edge = edge

    @property
    def edge(self) -> float:
        return self.edge

    @edge.setter
    def edge(self, value):
        self._edge = value

    def volume(self) -> float:
        return self.edge**3 * sqrt(2) / 12

    def surface(self):
        return self.edge**2 * sqrt(3)


tet = Tetrahedron(5)
print(f'{tet.edge = :.2f}\t{tet.volume = :.2f}')


# ДОБАВИТЬ: примеры выполнения скрипта в закомментированном виде под меткой tests
# tests:
