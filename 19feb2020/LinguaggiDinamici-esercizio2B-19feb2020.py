'''
Esercizio 2) Implementare una funzione quadratura che, ricevuta in input
una funzione f , due valori reali a e b e un intero nstep, restituisce
un’approssimazione dell’area compresa fra il grafico di f e l’asse x
nell’intervallo [a, b]. Al riguardo, si suppone che f sia non negativa
in tale intervallo.
L’approssimazione viene fatta tabulando la funzione in nstep punti
xi di [a, b] equispaziati. La somma delle quantità ottenute moltipli-
cando i valori tabulati per l’incremento costante dx = xi+1 − xi fornisce
l’approssimazione cercata (la più semplice, non la migliore...)
'''

def quadratura(f, a, b, nstep):
    res=0.0
    i = a

    while i <= b:
        res = res + f(i)*(i+1-i)
        i += nstep

    return res

print(quadratura(lambda x:(x*9*x+2), 9, 60, 2))
