'''
   Scrivere un decoratore counter per funzioni NON ricorsive
   tale che le funzioni da esso decorate tengano conto del
   numero di chiamata. Esempio
   >> @counter
   ...def f(x,y):
   ...   return x+y
   >> f(1,1)
   2
   >> f(1,2)
   3
   >> f.count
   2
'''

#######################################################################################
#decoratore stardard senza controllo
'''
def counter(fun):
    def test(*args, **kwargs):
        test.count += 1
        return fun(*args, **kwargs)
    test.count = 0
    return test
'''
#######################################################################################



#aggiungo la correzzione
'''
   >> # Attenzione: il contatore non deve essere modificabile 
   >> # accidentalmente
   >> f.count = 10
   Traceback (most recent call last):
   File "/tmp/ipykernel_2778/1574805336.py", line 1, in <module>
     f.count=5
   File "/home/mauro/didattica/LD/20212022/LDPackage/esercizi_esame.py", line 335, in __set__
     raise AttributeError("attribute 'count' of 'counter' objects is not writable")
   AttributeError: attribute 'count' of 'counter' objects is not writable
'''


class counterdescr():
    def __get__(self, inst, cls):
        return inst._count

    def __set__(self, inst, val):
        if val == inst._counter__key:
            inst._count += 1 
        else:
            raise AttributeError('Errore, non si può modificare count')


class counter():
    count = counterdescr()
    __key = 'VALOREIMPOSTATOPERevitareLutilizzo'
    def __init__(self, fun):
        self._count = 0
        print(fun)
        self.settings = fun
        
    def __call__(self, *args, **kwds):
        self.count = self.__key
        return self.settings(*args, **kwds)

@counter
def f(x,y):
    return x+y

@counter
def f2(x,y):
    return x+y


print(f(1,2), f(2,1))
print(f.count)
print(f2(12,3))
print(f2.count, f.count)
