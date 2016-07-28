class Complex:
    __version__ = (1, 1)

    def __init__(self, real=0, imaginary=0):
        self.r = real
        self.i = imaginary

    def __add__(self, other):
        real_result = self.r + other.r
        imaginary_result = self.i + other.i
        return Complex(real_result, imaginary_result)

    def __sub__(self, other):
        real_result = self.r - other.r
        imaginary_result = self.i - other.i
        return Complex(real_result, imaginary_result)

    def __eq__(self, other):
        return self.r == other.r and self.i == other.i