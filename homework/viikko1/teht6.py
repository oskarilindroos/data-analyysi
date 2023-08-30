class Murtoluku:
    def __init__(self, os, nim):
        self.os = os
        self.nim = nim

    def tulosta(self):
        print(f'{self.os} / {self.nim}')
        
    def gcd(self,a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
        
    def sievenna(self):
        gcd = self.gcd(self.os, self.nim)
        self.nim //= gcd
        self.os //= gcd
        
ml = Murtoluku(34562, 311058)

ml.tulosta()

ml.sievenna()

ml.tulosta()