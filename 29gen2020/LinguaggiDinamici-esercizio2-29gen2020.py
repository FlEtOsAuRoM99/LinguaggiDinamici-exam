'''
Esercizio 2) Definire una classe per rappresentare multi-insiemi, ovvero
“insiemi” in cui gli elementi possono comparire anche con molteplicità
maggiore di 1. La classe deve supportare almeno le due operazioni di
unione e intersezione di multi-insiemi. Le definizioni ricordano quelle
di mcm e MCD di interi:

> l’unione consiste degli elementi presenti in uno o entrambi gli in-
siemi con molteplicità pari al massimo delle due (se l’elemento non
è presente si può intendere che abbia molteplicità 0);

> l’intersezione consiste degli elementi presenti in entrambi gli in-
siemi con molteplicità pari al minimo delle due.

Le operazioni devono restituire nuovi multi-insiemi, senza modificare
gli operandi.
'''

# multi insieme: {a, a, a, b, b, c, ... ,z, z, x, ....} equivale a una lista di elementi [a, a, a, b, b, c, ... ,z, z, x, ....]

class multiInsiemi():
    def __init__(self, multi_insieme):
        self.lMultiInsieme = multi_insieme
    

    def unione(self, multiInsieme): 
        ltemp = multiInsiemi([])
        for i in self.lMultiInsieme + multiInsieme.lMultiInsieme:
            i1_mol = molteplicita(multiInsieme.lMultiInsieme, i)
            i2_mol = molteplicita(self.lMultiInsieme, i)
            # Ho interpretato il comando, non essendo chiaro lascio le due possibili soluzioni
            '''
            if i1_mol > 0 and i2_mol > 0:
                if molteplicita(ltemp.lMultiInsieme,i) < max(i1_mol, i2_mol):
                    ltemp.append(i)
            '''
            #seguendo il comportamento dell'unione aggiungo anche quelli con 1 solo elemento
            if molteplicita(ltemp.lMultiInsieme,i) < max(i1_mol, i2_mol):
                    ltemp.aggiungiElemento(i)
                
        return ltemp
        
    def intersezione(self, multiInsieme):
        ltemp = multiInsiemi([])
        for i in self.lMultiInsieme + multiInsieme.lMultiInsieme:
            i1_mol = molteplicita(multiInsieme.lMultiInsieme, i)
            i2_mol = molteplicita(self.lMultiInsieme, i)
            if i1_mol > 0 and i2_mol > 0:
                if molteplicita(ltemp.lMultiInsieme,i) < min(i1_mol, i2_mol):
                    ltemp.aggiungiElemento(i)
        return ltemp

    def aggiungiElemento(self, add):
        self.lMultiInsieme.append(add)

def molteplicita(l, var):
    # molteplicità è pari al conteggio degli elementi di una lista quindi esempio:        
    # [1, 1, 1, 3, 3, 5] m(1) = 3, m(3) = 2, m(5) = 5
    return len([i for i in range(0, len(l)) if l[i] == var ])



#la soluzione è solo su interi
l = [1, 3, 1, 5]
l2 = [1, 1, 3, 9, 9, 3, 3, 0]

A = multiInsiemi(l)
B = multiInsiemi(l2)

print((A.unione(B)).lMultiInsieme)

print((A.intersezione(B)).lMultiInsieme)
