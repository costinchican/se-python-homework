"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati un strign aleator cu numarul de caractere egal
    cu numarul intreg primit.

    exemplu:
        Veti primi: 5
        Veti printa: 'ashdj' (poate fi orice alt string)
"""

import random

x=input()
x=int(x)
l=[]
sir='abcdefghijklmnopqrstuwxyz'

for i in range(x):
    l.append(random.choice(sir)) #Folosim functia random.choice pentru a selecta un caracater random
                                 # din string si-l salvam intr-o lista
print(''.join(l))

