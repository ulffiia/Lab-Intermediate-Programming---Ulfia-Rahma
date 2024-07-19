class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("The numerator and denominator must be integers.")
        
        if numerator == 0:
            self._numerator = 0
            self._denominator = 1
        else:
            if (numerator < 0 and denominator >= 0) or (numerator >= 0 and denominator < 0):
                sign = -1
            else:
                sign = 1
            a = abs(numerator)
            b = abs(denominator)
            while a % b != 0:
                a, b = b, a % b
            self._numerator = sign * abs(numerator) // b
            self._denominator = abs(denominator) // b
    
    def __add__(self, other):
        if isinstance(other, Fraction):
            numerator = self._numerator * other._denominator + other._numerator * self._denominator
            denominator = self._denominator * other._denominator
            return Fraction(numerator, denominator)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Fraction):
            numerator = self._numerator * other._denominator - other._numerator * self._denominator
            denominator = self._denominator * other._denominator
            return Fraction(numerator, denominator)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, Fraction):
            numerator = self._numerator * other._numerator
            denominator = self._denominator * other._denominator
            return Fraction(numerator, denominator)
        return NotImplemented
    
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            numerator = self._numerator * other._denominator
            denominator = self._denominator * other._numerator
            if denominator == 0:
                raise ZeroDivisionError("Denominator cannot be zero.")
            return Fraction(numerator, denominator)
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self._numerator == other._numerator and self._denominator == other._denominator
        return NotImplemented
    
    def __str__(self):
        return f"{self._numerator}/{self._denominator}"
    
    def __repr__(self):
        return f"Fraction({self._numerator}, {self._denominator})"
    
    def __int__(self):
        return self._numerator // self._denominator
    
    def __float__(self):
        return self._numerator / self._denominator
