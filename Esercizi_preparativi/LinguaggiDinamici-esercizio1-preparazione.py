'''
1) Implementare un iterabile per la sequenza dei numeri 
   del tipo a+b**i, i = 0,1,2,...
   Opzionalmente, l'iterabile riceve in ingresso, oltre ai 
   parametri a e b, un intero n positivo che indica il numero di
   iterazioni prima di sollevare l'eccezione StopIteration.
'''

class funzioneIterabile():
    def __init__(self, a, b, n=1) -> None:
        self.a = a
        self.b = b
        try:
            if n > 0:
                self.n = int(n)
            else:
                print('Il valore inserito è negativo, il valore inserito sarà 1')
                self.n = 1
        except:
            print('Hai inserito un valore non intero, il valore inserito sarà 1')
            self.n = 1

    def __iter__(self): 
        self.i = 0
        return self

    def __next__(self):
        res = 0
        while self.i <= self.n:
            res = self.a + self.b**self.i
            self.i += 1
            return res
        raise StopIteration

p = funzioneIterabile(1,2)

for i  in p:
    print(i)
