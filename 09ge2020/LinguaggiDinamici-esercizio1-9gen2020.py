

'''
Esercizio 1)
Fornire almeno due implementazioni “sostanzialmente” differenti 
per la funzione coppiepari che, ricevuto in input un intero positivo
n, restituisce la lista “ordinata” di coppie (x, y) 
tale che x e y sono interi
positivi pari che soddisfano le diseguaglianze:
n ≥ x>y> 0
Ad esempio, se n = 9, la lista restituita deve essere:
coppiepari(9) 
return [ (4 , 2 ) ,(6 , 2 ) ,(6 , 4 ) ,(8 , 2 ) ,(8 , 4 ) ,(8 , 6 ) ] 
'''


def coppiepari(n):

    '''
    n>=x>y>0 
    [(x, y)...(x_n,y_n)]--> lista di tuple
    x%2 == 0 && y%2 == 0
    x<n o x==n
    '''

    if n < 4: 
        #when the input is less than 4 can't calculete because
        # it is impossible this solution x > y > 0 
        # then we can't write [(2, 0)] then we return [(None, None)]
        return [(None, None)]
    x = 4
    y = 2

    l_CoppiePari = [(x,y)]
    while x <= n:
        x = x+2
        while y < x:
            if x == n or x < n:
                l_CoppiePari.append((x,y))
            y = y+2
        y = 2
    return l_CoppiePari

def coppiepari_secondMethod(n):
    '''
    usare le lists compriencions
    '''
    if n < 4: 
        return [(None, None)]
    return [(x, y) for x in range(2, n+1, 2) for y in range(2, x, 2)]


print(coppiepari(4))
print(coppiepari_secondMethod(10))