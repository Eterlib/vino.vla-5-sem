class Rectangle:
    rectcnt = 0

    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        Rectangle.rectcnt += 1
        self.num = Rectangle.rectcnt
        setattr(self, f"rect_{self.num}", self.num)

    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1}) [{Rectangle.rectcnt}]"

    def _area(self):
        return abs(self.x2 - self.x1) * abs(self.y2 - self.y1)

    def __lt__(self, other):  return self._area() < other._area()
    def __eq__(self, other):  return self._area() == other._area()

    def __mul__(self, k):     return Rectangle(self.x1*k, self.y1*k, self.x2*k, self.y2*k)
    def __rmul__(self, k):    return self.__mul__(k)

    def __getitem__(self, i):
        v = [(self.x1,self.y1),(self.x1,self.y2),(self.x2,self.y2),(self.x2,self.y1)]
        if i < 0 or i > 3: raise IndexError
        return v[i]

    def __iter__(self):
        for v in [(self.x1,self.y1),(self.x1,self.y2),(self.x2,self.y2),(self.x2,self.y1)]:
            yield v

    def __bool__(self):  return self._area() != 0

    def __del__(self):
        Rectangle.rectcnt -= 1
        print(Rectangle.rectcnt)
