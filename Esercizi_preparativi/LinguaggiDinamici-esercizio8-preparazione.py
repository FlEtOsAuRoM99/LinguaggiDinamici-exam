'''
    Definire una classe intlist per rappresentare liste di
    soli numeri interi. Gli oggetti della classe devono poter
    essere utilizzati come chiavi in un dizionario.
    >> L = intlist([1,2,3])
    >> D = {L:'one'}
    >> L2 = intlist([0,3,3])
    >> hash(L) == hash(L2)
       True
    >> D[L2] = 'two'
    >> D
       {[1, 2, 3]: 'one', [0, 3, 3]: 'two'}
    Per eseguire questo esercizio può essere utile (ma non 
    necessario) conoscere la funzione all:
    all([x1,x2,....,xn]) == True se e solo se bool(xi) == True
    per ogni i.
'''


class intlist(list):
    def __new__(self, list_to_intlist):
        #questa più pythonica
        intlist.__testInteger(list_to_intlist)
        #questa più da C++
        '''
        for i in list_to_intlist:
            if type(i) is not int: 
                raise TypeError('List take only integer type')
        '''
        return super().__new__(self)


    def __hash__(self):
        return sum(self)
#################################################################################
    ##aggiungo anche le varie verifiche per le aggiunte di oggetti
    def append(self, __object):
        if not type(__object) == int:
            raise ValueError('Only integer')

        return super().append(__object)
    
    ##exetend
    def extend(self, __iterable):
        intlist.__testInteger(__iterable)
        return super().extend(__iterable)

    ##insert
    def insert(self, __index, __object):
        if not type(__object) == int:
            raise ValueError('Only integer')
        return super().insert(__index, __object)
#####################################################################################        
        
    def __testInteger(l):
        if not all([type(i)==int for i in l]):
            raise TypeError('List take only integer type')
        return True



L = intlist([1,2,3])
D = {L: 'one'}
print(D)
L2 = intlist([0,3,3])

print(L)
print(hash(L) == hash(L2))
D[L2] = 'two'
print(D)