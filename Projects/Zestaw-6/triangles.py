from points import Point

class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.A = Point(x1, y1)
        self.B = Point(x2, y2)
        self.C = Point(x3, y3)

    def __str__(self):
        return f"[{str(self.A)}, {str(self.B)}, {str(self.C)}]"

    def __repr__(self):
        return f"Triangle({self.A.x}, {self.A.y}, {self.B.x}, {self.B.y}, {self.C.x}, {self.C.y})"

    def __eq__(self, other):
        return {self.A, self.B, self.C} == {other.A, other.B, other.C}

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.A.x + self.B.x + self.C.x) / 3, (self.A.y + self.B.y + self.C.y) / 3)

    def area(self):
        import numpy as np
        CA = self.A - self.C
        CB = self.B - self.C
        matrix = np.array([[CA.x, CA.y], [CB.x, CB.y]])
        return np.abs(np.linalg.det(matrix)) / 2

    def move(self, x, y):
        delta = Point(x, y)
        self.A = self.A + delta
        self.B = self.B + delta
        self.C = self.C + delta
