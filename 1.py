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
        return (self.x + half, self.y + half)

    @center.setter
    def center(self, value):
        cx, cy = value
        half = self.w / 2
        self.x = cx - half
        self.y = cy - half
