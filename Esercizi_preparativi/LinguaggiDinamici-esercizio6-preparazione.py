'''
   Definire una classe salvadanaio che, di regola,rappresenta
   una quantità di denaro espressa in euro. Il suo "contenuto"
   può però essere anche riferito alla valuta "dollari".
   La classe può essere usata nel modo seguente
   >> E = salvadanaio(10)  # Valuta in Euro
   >> E
   10
   >> print(E)
   10.0€
   >> D = salvadanaio.dollari(20)  # Valuta in dollari
   >> D
   20
   >> print(D)
   20$
'''

class salvadanaio(float):
    def __init__(self, m):
        self.valuta = '\u20ac'

    @classmethod
    def dollari(cls, m):
        self = cls(m)
        self.valuta = '$'
        return self

    def __str__(self) -> str:
        return f'{super().__str__()}' + self.valuta

s = salvadanaio(10)
print(s)

s = salvadanaio.dollari(10)
print(s)