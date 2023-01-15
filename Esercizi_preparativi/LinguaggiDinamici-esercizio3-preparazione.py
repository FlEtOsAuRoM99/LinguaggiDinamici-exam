'''
3) Definire una classe matrix per rappresentare
   matrici a due dimensioni. Un oggetto matrix deve  
   supportare almeno l'operazione di addizione (elemento
   per elemento) oltre ad una rappresentazione esterna "gradevole".

   Una matrice può essere inizializzata in due modi.
   1) Passando come parametri due interi positivi, 
      m ed n; in tal caso la matrice (mxn) sarà
      composta di tutti zeri.
   2) Passando come unico parametri una lista di liste
      numeriche tutte della stessa dimensione.
      Ad esempio: [[1, 2, 3], [4, 5, 6]]
   Non è richiesto (anche se preferibile) che
   il metodo di inizializzazione utilizzato esegua il 
   controllo di correttezza dei parametri (vedi es. precedente)
'''


class matrix(list):
    def __init__(self, *args):
        if len(args) == 1:
            self.extend(args[0])
            self.m = len(args[0])
            self.n = len(args[0][0])
        elif len(args) == 2:
            self.extend([[0 for _ in range(args[1])] for _ in range(args[0])])
            self.m = args[0]
            self.n = args[1]
    def __add__(self, mat):
        if type(mat) == matrix:
            return matrix([[x+y for x, y in zip(self[i], mat[i])] for i in range(self.m)])
        else:
            raise 'Error, it is impossible calculate this match'
    
    def __str__(self) -> str:
        matrixString = ''
        for row in range(self.m):
            for column in self[row]:
                matrixString += '\t' + str(column)
            matrixString += '\n'
        return matrixString
        

        
m = matrix([[1, 2, 3], [4, 5, 6]])

print(m)

m2 = matrix(2, 3)#m = 2 and n = 3
print(m2)

m3 = matrix([[8, 7, 6], [0, 4, 3]])
print(m+m2)
print((m+m))



