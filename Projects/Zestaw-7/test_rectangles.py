import unittest
from points import Point
from rectangles import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rect1 = Rectangle(1, 2, 3, 4)
        self.rect2 = Rectangle(3, 1, 5, 5)

    def test_init(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 0, -5, 5)
        with self.assertRaises(ValueError):
            Rectangle(0, 0, 10, -10)

    def test_str(self):
        self.assertEqual(str(self.rect1), "[(1, 2), (3, 4)]")
        self.assertEqual(str(self.rect2), "[(3, 1), (5, 5)]")

    def test_repr(self):
        self.assertEqual(repr(self.rect1), "Rectangle(1, 2, 3, 4)")
        self.assertEqual(repr(self.rect2), "Rectangle(3, 1, 5, 5)")

    def test_eq(self):
        self.assertEqual(self.rect1, Rectangle(1, 2, 3, 4))
        self.assertEqual(self.rect1, self.rect1)

    def test_ne(self):
        self.assertNotEqual(self.rect1, Rectangle(0, 1, 2, 3))
        self.assertNotEqual(self.rect1, Rectangle(0, 0, 5, 5))

    def test_center(self):
        self.assertEqual(self.rect1.center(), Point(2.0, 3.0))
        self.assertEqual(self.rect2.center(), Point(4.0, 3.0))

    def test_area(self):
        self.assertEqual(self.rect1.area(), 4)
        self.assertEqual(self.rect2.area(), 8)

    def test_move(self):
        self.rect1.move(1, 1)
        self.rect2.move(-2, -3)

        self.assertEqual(self.rect1, Rectangle(2, 3, 4, 5))
        self.assertEqual(self.rect2, Rectangle(1, -2, 3, 2))

    def test_intersection(self):
        intersected_rect1 = self.rect1.intersection(self.rect2)
        self.assertIsNone(intersected_rect1)  # in this case intersection is a line segment

        intersected_rect2 = self.rect1.intersection(Rectangle(1.5, 1, 2.5, 2.5))
        self.assertEqual(intersected_rect2, Rectangle(1.5, 2, 2.5, 2.5))

        intersected_rect3 = self.rect1.intersection(Rectangle(-100, -100, 0, 0))
        self.assertIsNone(intersected_rect3)

    def test_cover(self):
        covering_rect1 = self.rect1.cover(self.rect2)
        self.assertEqual(covering_rect1, Rectangle(1, 1, 5, 5))

        covering_rect2 = self.rect1.cover(Rectangle(1.5, 1, 2.5, 2.5))
        self.assertEqual(covering_rect2, Rectangle(1, 1, 3, 4))

        covering_rect3 = self.rect1.cover(Rectangle(-100, -100, 0, 0))
        self.assertEqual(covering_rect3, Rectangle(-100, -100, 3, 4))

    def test_make4(self):
        rect1, rect2, rect3, rect4 = self.rect1.make4()
        self.assertEqual(rect1, Rectangle(1, 2, 2, 3))
        self.assertEqual(rect2, Rectangle(2, 2, 3, 3))
        self.assertEqual(rect3, Rectangle(1, 3, 2, 4))
        self.assertEqual(rect4, Rectangle(2, 3, 3, 4))

        rect1, rect2, rect3, rect4 = self.rect2.make4()
        self.assertEqual(rect1, Rectangle(3, 1, 4, 3))
        self.assertEqual(rect2, Rectangle(4, 1, 5, 3))
        self.assertEqual(rect3, Rectangle(3, 3, 4, 5))
        self.assertEqual(rect4, Rectangle(4, 3, 5, 5))

if __name__ == '__main__':
    unittest.main()
