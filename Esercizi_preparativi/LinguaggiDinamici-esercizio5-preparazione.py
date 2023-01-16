'''
   Definire una classe derivata da dict che consenta l'accesso
   agli elementi sia mediante chiave sia mediante indice.
   Se D è un tale dizionario, la scrittura D[k] è il valore
   associato a k, nel caso in cui k non sia un numero intero,
   altrimenti è il valore corrispondente alla k-esima chiave 
   in ordine alfabetico.
'''  

class derDict(dict):
    '''
    per accedere con le [] bisogna utilizzare __getitem__
    '''
    def __getitem__(self, __key):
        if type(__key) is int:
            __key = sorted(self.keys())[__key]
        return super().__getitem__(__key)

l = derDict({'b':1, 'p':3, 'a':5, '0':4})
print(l[0])
