"""
    Veti primi un string de la tastatura.
    Va trebui sa afisati acel string cu o litera mare/una mica.

    exemplu:
        Veti primi: 'center'
        Veti printa: 'CeNtEr'
"""
s=input()
l=list(s)

for i in range(len(s)):
    if i%2==0:
        if l[i].islower()==True:   #Literele de pe pozitii pare devin uppercase
            l[i] = l[i].upper()

    elif i%2==1:
        if l[i].isupper()==True:   #Literele de pe pozitii impare devin lowercase
            l[i] = l[i].lower()

print(''.join(l))
