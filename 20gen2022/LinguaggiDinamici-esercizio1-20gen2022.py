'''
Implementare un iterabile wordfilter che
restituisce le parole (word) di una stringa la cui lunghezza `e non
minore di un valore assegnato.
Esempio
>> S = """ Lorem ipsum dolor sit amet, consectetur adipiscing
elit, sed do eiusmod tempor incididunt ut labore et dolore
magna aliqua.
"""
>> for w in wordfilter(S,minlen=6):
... print(w)

consectetur
adipiscing
eiusmod
incididunt
aliqua.
La definizione di word segue le regole (pi`u volte viste anche a
lezione) dell’utility Linux wc.
'''



S = """ Lorem ipsum dolor sit amet, consectetur adipiscing
elit, sed do eiusmod tempor incididunt ut labore et dolore
magna aliqua."""

class wordfilter():
    def __init__(self, s,  minlen=6):
        self.minlen = minlen

        self.s = s.replace('\n', ' ').replace('\t', ' ')

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        when = self.s.strip().split(' ')
        while self.i < len(when):
            if len(when[self.i]) > self.minlen:
                self.i += 1
                return when[self.i-1]
            self.i += 1
        raise StopIteration
        
c = ''
for w in wordfilter(S, minlen=6):
    print(w)