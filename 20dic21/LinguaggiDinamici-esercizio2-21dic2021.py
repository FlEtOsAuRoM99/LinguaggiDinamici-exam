'''
Scrivere una classe flexdict per implementare 
dizionari che supportano unione e intersezione sulla base delle chiavi. 
In particolare, se D1 `e un flexdict e D2 un generico dizionario,
allora D1.union(D2) aggiunge per side-effect a D1
le coppie chiave/valore di D2 la cui chiave non `e presente in D1,
mentre D1.intersect(D2) elimina da D1 le coppie chiave/valore
la cui chiave non `e presente in D2.
'''

class flexdict(dict):
    def __new__(self, d):
        if type(d) is dict:
            return super().__new__(self, d)
        raise ValueError('Only dict type')
    ##methods
    def union(self, d_temp):
        if type(d_temp) == flexdict:
            for i in d_temp.keys():
                try:
                    self[i]
                except:
                    self[i] = d_temp[i]

    def intersect(self, d_temp):
        if type(d_temp) == flexdict:
            for i in d_temp.keys():
                try:
                    self[i]
                    self.pop(i)
                except:
                    pass

d1 = flexdict({'e':[1,1,2], 'b':9})
d2 = flexdict({'e':[1,1,2], 'c':5})

d1.union(d2)
print(d1)
d1.intersect(d2)
print(d1)