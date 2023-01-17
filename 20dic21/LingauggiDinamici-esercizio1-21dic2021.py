
'''
    Definire una classe gradi che memorizza ampiezze
    angolari misurate in gradi.
    Inizializzazione:
    >> v = gradi(g,p,s)
    dove g,p,s indicano rispettivamente i gradi, i primi e i secondi.
    La classe deve supportare la conversione in radianti, ottenibile
    con la scrittura
    >> v.rad
    Infine, deve supportare una stampa gradevole. Esempio:
    >> print(v)
    40°12’ 25’’
    NB Il simbolo °si ottiene con il carattere \xb0
'''


class gradi():
    def __new__(self, gradi, primi, secondi):
        if type(gradi) == type(primi) == type(secondi) == int:
            self.g = gradi
            self.p = primi
            self.s = secondi
            return super().__new__(self)

    @property
    def rad(self):
        import math
        return ((((self.s/60)+self.p)/60)+self.g)*(math.pi/180)
    
    def __str__(self):
        return f"{self.g}\xb0 {self.p}’ {self.s}’’"
    
v = gradi(40,12,25)
print(v.rad)
print(v)