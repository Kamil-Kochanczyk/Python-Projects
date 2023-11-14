import unittest
from points import Point
from triangles import Triangle

class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.t1 = Triangle(0, 0, 0, 3, 4, 0)
        self.t2 = Triangle(4, 0, 0, 3, 0, 0)
        self.t3 = Triangle(-8, -3, 3, 2, -5, 4)
        self.deltaX = -2
        self.deltaY = 1
    
    def test_str(self):
        self.assertEqual(str(self.t1), "[(0, 0), (0, 3), (4, 0)]")
        self.assertEqual(str(self.t2), "[(4, 0), (0, 3), (0, 0)]")
        self.assertEqual(str(self.t3), "[(-8, -3), (3, 2), (-5, 4)]")

    def test_repr(self):
        self.assertEqual(repr(self.t1), "Triangle(0, 0, 0, 3, 4, 0)")
        self.assertEqual(repr(self.t2), "Triangle(4, 0, 0, 3, 0, 0)")
        self.assertEqual(repr(self.t3), "Triangle(-8, -3, 3, 2, -5, 4)")

    def test_eq(self):
        self.assertTrue(self.t1 == Triangle(0, 3, 0, 0, 4, 0))
        self.assertTrue(self.t1 == self.t2)
        self.assertFalse(self.t1 == self.t3)

    def test_ne(self):
        self.assertFalse(self.t2 != Triangle(0, 3, 4, 0, 0, 0))
        self.assertFalse(self.t2 != self.t1)
        self.assertTrue(self.t2 != self.t3)

    def test_center(self):
        self.assertTrue(self.t1.center() == Point(4 / 3, 1))
        self.assertTrue(self.t2.center() == Point(4 / 3, 1))
        self.assertTrue(self.t3.center() == Point(-10 / 3, 1))

    def test_area(self):
        self.assertTrue(self.t1.area() == 6)
        self.assertTrue(self.t2.area() == 6)
        self.assertTrue(round(self.t3.area()) == 31)    # analitical result = 31, numerical result = 30.999...

    def test_move(self):
        self.t1.move(self.deltaX, self.deltaY)
        self.t2.move(self.deltaX, self.deltaY)
        self.t3.move(self.deltaX, self.deltaY)

        self.assertTrue(self.t1 == Triangle(-2, 1, -2, 4, 2, 1))
        self.assertTrue(self.t2 == Triangle(-2, 1, -2, 4, 2, 1))
        self.assertTrue(self.t3 == Triangle(-10, -2, 1, 3, -7, 5))

if __name__ == "__main__":
    unittest.main()
