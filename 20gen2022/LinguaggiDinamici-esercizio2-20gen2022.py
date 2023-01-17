'''
Scrivere una funzione triples che, dato in
input un intero positivo N , restituisce la lista di tutte le terne
pitagoriche composte da numeri interi positivi minori di N .
Ovvero terne (x, y, z) tali che:
 - z**2= x**2 + y**2
 - 0 < x,y,z < N
 - x < y
Esempio
>> triples(15)
[(3, 4, 5), (6, 8, 10), (5, 12, 13)]
'''


def triples(N):
    if type(N) is int:
        import math
        return [(x, y, int(math.isqrt(x**2+y**2))) for x in range(3, N-1) for y in range(x+1, N-1) if math.sqrt(x**2+y**2).is_integer() and math.sqrt(x**2+y**2) < 15]
        
print(triples(15))