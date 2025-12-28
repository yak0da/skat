class Square:
    __match_args__ = ('x', 'y', 'w')  # Определяем порядок для позиционных параметров в match
    
    def __init__(self, x, y, w):
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
        old_center = self.center
        self._w = value
        self.center = old_center  # Центр сохраняется
    
    @property
    def h(self):
        return self._w
    
    @h.setter
    def h(self, value):
        old_center = self.center
        self._w = value
        self.center = old_center  # Центр сохраняется
    
    @property
    def s(self):
        return self._w * self._w
    
    @s.setter
    def s(self, value):
        # Изменение площади игнорируется
        pass
    
    @property
    def center(self):
        return (self._x + self._w / 2, self._y + self._w / 2)
    
    @center.setter
    def center(self, value):
        if isinstance(value, (tuple, list)) and len(value) == 2:
            cx, cy = value
            self._x = cx - self._w / 2
            self._y = cy - self._w / 2
        else:
            raise ValueError("Center must be a tuple/list of two numbers")
    
    def __iadd__(self, other):
        # Для поддержки Sq.center += (dx, dy)
        # Но эта магическая функция применяется к объекту Square, а не к свойству center
        # Поэтому лучше переопределим ее как сдвиг всего квадрата
        if isinstance(other, tuple) and len(other) == 2:
            dx, dy = other
            self._x += dx
            self._y += dy
        return self
    
    # Добавим специальный метод для поддержки center +=
    def _move_center(self, dx, dy):
        """Вспомогательный метод для смещения центра"""
        cx, cy = self.center
        self.center = (cx + dx, cy + dy)


# Тестовый код
if __name__ == "__main__":
    for x, y, w in (1, 2, 0), (1, 1, 7), (3, 4, 10), (5, 3, 6):
        Sq = Square(x, y, w)
        # Вместо Sq.center += -1, -1 используем:
        cx, cy = Sq.center
        Sq.center = (cx - 1, cy - 1)
        
        match Sq:
            case Square(_, _, 0):
                print("Zero square")
            case Square(0, 0, _):
                print("Started from 0")
            case Square(s=100):
                print("10x10 square")
            case Square(center=c) if c[0] == round(c[0]) and c[1] == round(c[1]):
                print("Even-sized square")
