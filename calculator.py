import numpy


# takes 2 positional arguments but 3 were given
class Calculator:
    def add(self, n, m, key=10):
        return n + m

    def substract(self, n, m):
        return n - m

    def mulitply(self, n, m):
        return n * m

    def division(self, n, m):
        if m == 0:
            return "Invalid"
        return n / m

    def expoent(self, n, m):
        return n**m
