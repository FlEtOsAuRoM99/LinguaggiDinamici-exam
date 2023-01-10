
'''
Esercizio 1) Implementare una metaclasse mymeta con le carateristiche de-
scritte di seguito:

1. Se pwd_protected è una classe di tipo mymeta, appena pwd protected
viene definita l’utente riceve un messaggio in cui viene chiesto (due
volte, con conferma) di digitare una nuova password.

2. Ogni volta che il programma istanzia la classe pwd protected, all’utente
viene chiesto di digitare la password.

3. Se la password è errata l’oggetto non deve essere creato e deve
essere visualizzato un opportuno messaggio di errore.

Si possono ignorare (senza alcuna penalizzazione sul voto) tutte le que-
stioni di sicurezza. In particolare, le password possono essere visibili
mentre vengono digitate.
'''
'''
class mymeta(type):
    
    def __call__(cls, pwd):
        pwd = str(input('Insert password: '))

        if str(input('Insert password: ')) == pwd:
            return super().__call__(pwd)
        return super().__call__(None)

class pwd_protected(metaclass=mymeta):
    pwd = None
    def __new__(self, pwd) -> None:
        if pwd != None:
            self.pwd = pwd
        else:
            print('Password is not correct!')
'''
class mymeta(type):
    def __call__(self):
        self.pwd = input("Insert password: ")
        if input("Insert password: ") != self.pwd:
            self.pwd = None
        return super().__call__()


class pwd_protected(metaclass=mymeta):
    def __new__(self) -> None:
        if self.pwd == None:
            print('Error, password is not correct')
        else:
            return super(pwd_protected, self).__new__(self)


#due utenti
p = pwd_protected()
p2 = pwd_protected()


try:
    p.pwd
    print(p.pwd, end='')
except:
    print('your class was not instanced')
try:
    p2.pwd
    print(' ', p2.pwd)
except:
    print('your class was not instanced')
