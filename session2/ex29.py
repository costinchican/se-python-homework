"""
    Veti primi un string de la tastatura.
    Va trebui sa printati numarul de vocale si numarul de consoane din
    acel string.

    exemplu:
        Veti primi: 'center'
        Veti printa:
        2 (pentru vocale)
        4 (pentru consoane)
"""
v='aeiou'
c=0

s=input()
for i in range(len(s)):
    for j in range (len(v)):
        if s[i]==v[j]:
               c=c+1
b=len(s)-c
print('',c,'\n',b)