import unittest
import fracs

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.undefined1 = [0, 0]
        self.undefined2 = [1, 0]
        self.zero = [0, 99]
        self.quarter = [25, 100]
        self.eigth = [-2, -16]
        self.negative_half = [-1, 2]
        self.negative_two = [500, -250]

    def test_canonical_form(self):
        self.assertEqual(fracs.canonical_form([1, 2]), [1, 2])
        self.assertEqual(fracs.canonical_form([-3, 4]), [-3, 4])
        self.assertEqual(fracs.canonical_form([5, -6]), [-5, 6])
        self.assertEqual(fracs.canonical_form([-7, -8]), [7, 8])

    def test_simplify_frac(self):
        self.assertEqual(fracs.simplify_frac(self.eigth), [1, 8])
        self.assertEqual(fracs.simplify_frac(self.negative_two), [-2, 1])
        self.assertEqual(fracs.simplify_frac(self.zero), [0, 1])

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac(self.quarter, self.eigth), [3, 8])
        self.assertEqual(fracs.add_frac(self.zero, [-36, 6]), [-6, 1])
        self.assertRaises(ValueError, fracs.add_frac, [8, 2], self.undefined1)

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac(self.negative_half, self.negative_two), [3, 2])
        self.assertEqual(fracs.sub_frac(self.zero, [100, -10]), [10, 1])
        self.assertRaises(ValueError, fracs.sub_frac, self.undefined2, [1, 1])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac(self.eigth, self.negative_two), [-1, 4])
        self.assertEqual(fracs.mul_frac(self.quarter, [16, 1]), [4, 1])
        self.assertRaises(ValueError, fracs.mul_frac, self.zero, self.undefined1)

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac(self.quarter, self.eigth), [2, 1])
        self.assertEqual(fracs.div_frac(self.negative_half, [1, 16]), [-8, 1])
        self.assertRaises(ZeroDivisionError, fracs.div_frac, [5, 1], self.zero)
        self.assertRaises(ValueError, fracs.div_frac, [24, 1], self.undefined2)

    def test_is_positive(self):
        self.assertTrue(fracs.is_positive(self.quarter))
        self.assertFalse(fracs.is_positive(self.zero))
        self.assertFalse(fracs.is_positive(self.negative_half))
        self.assertFalse(fracs.is_positive(self.undefined1))

    def test_is_zero(self):
        self.assertTrue(fracs.is_zero(self.zero))
        self.assertFalse(fracs.is_zero(self.eigth))
        self.assertFalse(fracs.is_zero(self.negative_two))
        self.assertFalse(fracs.is_zero(self.undefined2))

    def test_is_undefined(self):
        self.assertTrue(fracs.is_undefined(self.undefined1))
        self.assertTrue(fracs.is_undefined(self.undefined2))
        self.assertFalse(fracs.is_undefined(self.zero))
        self.assertFalse(fracs.is_undefined([4224, 1]))

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac(self.eigth, [-8, -64]), 0)
        self.assertEqual(fracs.cmp_frac(self.negative_two, [-7, 4]), -1)
        self.assertEqual(fracs.cmp_frac([101, 10], [100, 10]), 1)
        self.assertRaises(ValueError, fracs.cmp_frac, [31, 4], self.undefined1)

    def test_frac2float(self):
        self.assertEqual(fracs.frac2float(self.quarter), 0.25)
        self.assertEqual(fracs.frac2float(self.negative_half), -0.5)
        self.assertAlmostEqual(fracs.frac2float([1, 3]), 0.333, places=3)
        self.assertRaises(ValueError, fracs.frac2float, self.undefined2)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
