"""
    Veti primi un string de la tastatura.
    Veti primi doua numere intregi de la tastatura, x, y.
    Va trebui sa printati substringul de la indexul x la indexul y (inclusiv).

    exemplu:
        Veti primi: 'Center for Intelligent Machines', 2, 5
        Veti printa: 'nter'
"""
s=input();
x=input();
y=input();
x=int(x);
y=int(y);
r=" "
for i in range(x,y+1):
    r=r+s[i]

print(r)