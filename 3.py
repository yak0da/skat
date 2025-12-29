class _Center(tuple):
    def __new__(cls, x, y):
        return super().__new__(cls, (x, y))
    
    def __add__(self, other):
        # if not hasattr(other, '__iter__') or len(other) != 2:
        #     return NotImplemented
        return _Center(self[0] + other[0], self[1] + other[1])
    
    __radd__ = __add__


class Square:
    __match_args__ = ("x", "y", "w")
    
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w

    @property
    def h(self):
        return self.w

    @h.setter
    def h(self, value):
        self.w = value

    @property
    def s(self):
        return self.w * self.w

    @s.setter
    def s(self, value):
        pass

    @property
    def center(self):
        half = self.w / 2
        return _Center(self.x + half, self.y + half)

    @center.setter
    def center(self, value):
        cx, cy = value
        half = self.w / 2
        self.x = cx - half
        self.y = cy - half

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