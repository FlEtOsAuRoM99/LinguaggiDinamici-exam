
'''
Esercizio 2) Scrivere due funzioni con le seguenti caratteristiche.
1. La funzione dadi riceve in input parametri keyword, n ed f , con
i seguenti valori default: n = 2, f = 6. Restituisce il punteg-
gio ottenuto simulando il lancio di n dadi, ciascuno con f facce
numerate da 1 a f .

2. La funzione statistiche, che riceve in input gli stessi parametri di
dadi più un terzo parametro keyword numexp = 1000. La fun-
zione restituisce un dizionario in cui: (a) le chiavi sono i possibili
esiti del lancio dei dadi; (b) i valori sono il corrispondente numero
di volte che ogni particolare esito si è verificato.
'''
import random

def dadi(n=2, f=6): 
    i = 0
    punteggio = 0
    while i < n:
        d = random.randint(1,f)
        punteggio += d
        i += 1
    return punteggio

def statistiche(n=2, f=6, numexp=1000):
    d = {}
    for k in range(1, f+1):
        d[k] = 0
    i = 0
    while i < n:
        rand = random.randint(1, f)
        d[rand] += 1
        i += 1
    return d

print(dadi())

print(statistiche(80))