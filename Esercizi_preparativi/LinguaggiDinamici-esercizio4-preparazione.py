'''
4) Definire una sottoclasse mystring di string che supporti
   i seguenti metodi:

   1) vowels, che restituisce il numero di vocali 
      (maiuscole, minuscole e accentate)

   2) consonants, che restituisce il numero di consonanti

   3) words, che restituisce il numero di words, definite come
      nell'utility wc di Linux
'''

class mystring(str):
    def vowels(self):
        test = 'A_E_U_I_O_a_e_u_i_o_à_ò_è_é_ù'.split('_')
        countVowels = 0
        for i in test:
            countVowels += self.count(i)
        return countVowels

    def consonants(self):
        return len(self)-self.vowels()
        
    def words(self):
        return len(self.split(' '))

    def spaces(self):
        return self.words()-1

l = mystring("Hi, my name is Samuele and I program this code.")

print(l.vowels(), l.consonants(), l.words(), l.spaces())


