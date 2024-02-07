import unittest
from points import Point

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.A = Point(3, 4)
        self.B = Point(-1 / 2, -2)
        self.C = Point(0, 0)
    
    def test_str(self):
        self.assertEqual(str(self.A), "(3, 4)")
        self.assertEqual(str(self.B), "(-0.5, -2)")
        self.assertEqual(str(self.C), "(0, 0)")
    
    def test_repr(self):
        self.assertEqual(repr(self.A), "Point(3, 4)")
        self.assertEqual(repr(self.B), "Point(-0.5, -2)")
        self.assertEqual(repr(self.C), "Point(0, 0)")
    
    def test_eq(self):
        self.assertTrue(self.A == self.A)
        self.assertTrue(self.A == Point(3, 4))
        self.assertFalse(self.A == Point(-3, -4))
    
    def test_ne(self):
        self.assertFalse(self.A != self.A)
        self.assertFalse(self.A != Point(3, 4))
        self.assertTrue(self.A != Point(-3, -4))
    
    def test_add(self):
        self.assertTrue(self.A + self.B == Point(2.5, 2))
        self.assertTrue(self.B + self.A == Point(2.5, 2))
        self.assertTrue(self.A + self.C == self.A)
    
    def test_sub(self):
        self.assertTrue(self.A - self.B == Point(3.5, 6))
        self.assertTrue(self.B - self.A == Point(-3.5, -6))
        self.assertTrue(self.B - self.C == self.B)
    
    def test_mul(self):
        self.assertTrue(self.A * self.B == -9.5)
        self.assertTrue(self.B * self.A == -9.5)
        self.assertTrue(self.A * self.C == 0)
    
    def test_cross(self):
        self.assertTrue(self.A.cross(self.B) == -4)
        self.assertTrue(self.B.cross(self.A) == 4)
        self.assertTrue(self.C.cross(self.B) == 0)
    
    def test_length(self):
        self.assertTrue(self.A.length() == 5)
        self.assertTrue(self.B.length() == (4.25 ** (1 / 2)))
        self.assertTrue(self.C.length() == 0)
    
    def test_hash(self):
        self.assertTrue(hash(self.A) == hash(Point(3, 4)))
        self.assertTrue(hash(self.B) == hash(Point(-0.5, -100 / 50)))
        self.assertTrue(hash(self.C) == hash(Point(0, 0)))

if __name__ == "__main__":
    unittest.main()
