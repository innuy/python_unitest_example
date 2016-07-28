from unittest import TestCase, main


class TestBasicArithmeticMethods(TestCase):

    def test_add(self):
        self.assertEqual(2 + 2, 4)

    def test_subtract(self):
        self.assertEqual(3 - 2, 1)

    def test_multiply(self):
        self.assertEqual(3 * 3, 9)

    def test_equal(self):
        self.assertTrue(3 == 3)
        self.assertFalse(2 == 9)

if __name__ == '__main__':
    main()
