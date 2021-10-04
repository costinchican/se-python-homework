"""
    Veti primi un string de la tastatura.
    Veti primi un intreg de la tastatura, x.
    Va trebui sa printati acel string, concatenat de x ori.

    exemplu:
        Veti primi: 'cmi', 5
        Veti printa: 'cmicmicmicmicmi'
"""
s=input();
x=input();
x=int(x);
r=" "

for i in range(x):
    r=r+s;

print(r)