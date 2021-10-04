class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = f'{a} + {b} * i'

    def __add__(self, other):
        new_z = ComplexNumber(self.a + other.a, self.b + other.b)
        return new_z

    def __mul__(self, other):
        new_z = ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)
        return new_z

    def __str__(self):
        return self.z


z1 = ComplexNumber(2, 6)
z2 = ComplexNumber(1, 8)
print(z1)
print(z1 + z2)
print(z1 * z2)