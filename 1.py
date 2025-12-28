from dataclasses import dataclass, field

@dataclass
class Square:
    _x: float
    _y: float
    _w: float
    
    def __init__(self, x: float, y: float, w: float):
        self._x = x
        self._y = y
        self._w = w
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value
    
    @property
    def w(self):
        return self._w
    
    @w.setter
    def w(self, value):
        self._w = value
        # Высота всегда равна ширине
        self._h = value
    
    @property
    def h(self):
        return self._w
    
    @h.setter
    def h(self, value):
        self.w = value  # Используем сеттер ширины, который обновит и высоту
    
    @property
    def s(self):
        return self._w * self._w
    
    @s.setter
    def s(self, value):
        # Изменение площади ничего не делает
        pass
    
    @property
    def center(self):
        return (self._x + self._w / 2, self._y + self._w / 2)
    
    @center.setter
    def center(self, value):
        # При изменении центра координаты вершины сдвигаются, ширина остается прежней
        cx, cy = value
        self._x = cx - self._w / 2
        self._y = cy - self._w / 2
    
    def __iadd__(self, other):
        # Для поддержки Sq.center += (-1, -1)
        if isinstance(other, tuple) and len(other) == 2:
            cx, cy = self.center
            dx, dy = other
            self.center = (cx + dx, cy + dy)
            return self
        return NotImplemented
    
    # Методы для поддержки match/case
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.w
        raise IndexError("Square index out of range")
    
    # Специальный метод для pattern matching
    def __match_args__(self):
        return ("x", "y", "w")

# Тестовый код
if __name__ == "__main__":
    for x, y, w in (1, 2, 0), (1, 1, 7), (3, 4, 10), (5, 3, 6):
        Sq = Square(x, y, w)
        Sq.center += -1, -1
        match Sq:
            case Square(_, _, 0):
                print("Zero square")
            case Square(0, 0, _):
                print("Started from 0")
            case Square(s=100):
                print("10x10 square")
            case Square(center=c) if c[0] == round(c[0]) and c[1] == round(c[1]):
                print("Even-sized square")
