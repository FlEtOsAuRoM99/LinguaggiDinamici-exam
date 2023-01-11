'''
2) Definiamo vettore riga semplicemente una lista i cui 
   elementi siano tutti numerici. La lunghezza della lista
   è detta dimensione del vettore.
   Definiamo poi matrice (bi-dimensionale) una lista i cui 
   elementi siano tutti vettori riga della stessa lunghezza.
   La lunghezza della lista è il numero di righe della matrice
   mentre la lunghezza (comune) di ogni vettore riga 
   componente è il numero di colonne. Una matrice mxn ha
   m righe ed n colonne.
   
   Esempi
   A = [[1,3.14,-5]]             matrice 1x3
   B = [[1,0,0],[0,1,0],[0,0,1]] matrice 3x3
   C = [[1],[2],[3]]             matrice 3x1
   C = [[1,2,'a']]               Non è una matrice
   D = [[1,2,3],[4,5],[6,7,8]]   Non è una matrice
   Definire una funzione checkmatrix che restituisce True in
   caso di input sintatticamente corretto e genera un errore
   di tipo MatrixSyntax altrimenti.
'''

class MatrixSyntax(Exception):
    def __init__(self, msg='Generic error'):
        print(msg)
    pass
    
def empty(matrix):
    if type(matrix) == list:
        if len(matrix) == 0:
            return True
        return False
    raise MatrixSyntax('This is not a vector or matrix')

def calcMatCol(matrix):
    if not empty(matrix):
        mTemp = matrix[0]
        for i in matrix:
            if not empty(i) and len(i) != len(mTemp):
                raise MatrixSyntax('Error lenght')

        return len(mTemp)
    return 0

def checkmatrix(matrix):
    calcMatCol(matrix)
    for i in matrix:
        for j in i:
            if type(j) != type(int()):
                raise MatrixSyntax('Matrix is not only integer')
    return True


m =[[1, 90, 0],[0,1,0],[0,0,1]]
print(checkmatrix(m))