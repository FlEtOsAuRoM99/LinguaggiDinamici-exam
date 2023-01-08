

'''
Realizzare un iterabile per la sequenza di numeri interi:
a + (−1) −k · k, k = 0, 1, 2, . . .
dove a è un parametro passato all’inizializzatore. Il metodo init
richiede un ulteriore parametro n. L’iterabile pre-calcola i valori e li
inserisce in una cache, da dove vengono prelevati a seguito di ogni
richiesta. 
Inizialmente il numero di valori in cache è n, quantità che
viene ripristinata ogni volta che scende al di sotto di n/3.
'''

class iterabile_specificPattern:
    def __init__(self, a, n):
        self.a = a
        self.dim = n
        self.stopReset = self.dim/3
        self.resalt = 0.0

    def __iter__(self):
        return self
            
    def __next__(self):
        if self.__cache():
            self.resalt = (self.a + (self.dim/(pow(-1, self.dim))) ) #a + (−1)^−k · k, k = 0, 1, 2, . . . a + ((1/(-1^k)) * k)
            return self.resalt

    def __cache(self):
        self.dim -= 1
        if self.dim < self.stopReset:
            self.dim = self.stopReset * 3
            return False
        return True
        
            
            

A = iterabile_specificPattern(10, 10)

obj = iter(A)
i = next(obj)
while i != None:
    print(i)
    i = next(obj) 
