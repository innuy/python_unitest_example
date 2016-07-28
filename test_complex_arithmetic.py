from unittest import TestCase, skip, skipIf

from complex import Complex


class TestComplexArithmetic(TestCase):

    def setUp(self):
        self.zero = Complex()

    @skip("Sure that this is correct, and will never change")
    def test_default_complex_value(self):
        self.assertEqual(self.zero.r, 0)
        self.assertEqual(self.zero.i, 0)

    def test_add_complex(self):
        one_onei = Complex(1, 1)
        result = one_onei + self.zero
        self.assertEqual(result.r, 1)
        self.assertEqual(result.i, 1)

    def test_sub_complex(self):
        one_onei = Complex(1, 1)
        result = self.zero - one_onei
        self.assertEqual(result.r, -1)
        self.assertEqual(result.i, -1)

    @skipIf(Complex.__version__ < (1, 1), "Not supported by this library")
    def test_equal_complex(self):
        zero = Complex()
        one = Complex(1)
        self.assertTrue(zero == self.zero)
        self.assertFalse(self.zero == one)

    def tearDown(self):
        del self.zero
