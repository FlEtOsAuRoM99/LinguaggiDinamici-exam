'''
Esercizio 1) Fornire almeno due implementazioni “sostanzialmente” diffe-
renti per la funzione multipli che, ricevuta in input una lista (o una
tupla) di interi positivi, conta e restituisce il numero di coppie non or-
dinate di elementi distinti tali che uno dei due elementi della coppia sia
multiplo intero dell’altro. Ad esempio, se la lista fosse:
[2 , 3 , 6 , 9 ]
la funzione dovrebbe restituire come risultato 3 (le coppie sono (2,6),
(3,6) e (3,9)).
'''

def multipli(l_number):
    '''
    1: controllo la lista da destra verso sinistra
    2: preso il primo elemento controllo con il successivo e così via fino alla fine della lista, senza controllare i precedenti (sono già stati contati)
    '''
    count = 0
    for i in range(0, len(l_number), 1):
        if (l_number[i] != 0):
            if l_number[i] == 1:
                count += ((len(l_number))-(i+1))
            else:
                for j in range(i+1, len(l_number), 1):
                    if l_number[j]%l_number[i] == 0:
                        #print('(', l_number[j], " % ", l_number[i], " == " , l_number[j]%l_number[i], ")")
                        count += 1
    return count


    
def multipli_secondMethod(l_number):

    return len([(i,j) for i in range(0, len(l_number), 1) if l_number[i] != 0 for j in range(i+1, len(l_number), 1) if (l_number[j]%l_number[i] == 0)])


##LIST
l = [2, 3, 6, 9]

print(multipli(l))
print(multipli_secondMethod(l))

##TUPLE
l = (2, 3, 0, 6, 9)

print(multipli(l))
print(multipli_secondMethod(l))