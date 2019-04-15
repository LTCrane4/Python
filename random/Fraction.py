class Fraction:
    """Class representing a fraction"""
    
    def __init__(self, newnum: int, newden: int):
        self.num = newnum
        if newden != 0:
            self.den = newden
        else:
            self.den = 1
    
    def gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
    
    def reduce(self) -> None:
        denom: int = self.gcd(self.num, self.den)
        self.num /= denom
        self.den = denom
    
    def add(self, other) -> bool:
        if isinstance(other, Fraction):
            self.num *= other.den
            self.num += other.num * self.den
            self.den *= other.den
            self.reduce()
            return True
        return False
    
    def subtract(self, other) -> bool:
        if isinstance(other, Fraction):
            temp = Fraction(0 - other.num, other.den)
            self.add(temp)
            self.reduce()
            return True
        return False
    
    def multiply(self, other) -> bool:
        if isinstance(other, Fraction):
            self.num *= other.num
            self.den *= other.den
            self.reduce()
            return True
        return False
    
    def divide(self, other) -> bool:
        if isinstance(other, Fraction):
            self.num *= other.den
            self.den *= other.num
            self.reduce()
            return True
        return False
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Fraction):
            self.reduce()
            other.reduce()
            return self.num == other.num and self.den == other.den
        return False
    
    def __str__(self) -> str:
        return str(self.num) + "/" + str(self.den)
    
    def __repr__(self) -> str:
        return self.__str__()

