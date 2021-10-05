"""
    Veti primi un string de la tastatura, care reprezinta o succesiune de
    paranteze rotunde, drepte si acolade. Va trebui sa spuneti daca parantezele
    sunt inchise corect, sau nu. (boolean - True|False)

    exemplu:
        Veti primi: '(([])){}'
        Veti printa: True

        Veti primi: '(()]'
        Veti printa: False
"""
s=input()
d=0
d1=0
p=0
p1=0
a=0
a1=0
for i in s:  #Verific daca numarul de paranteze inchise=numarul de paranteze deschise
 if i=='(' :
   d=d+1
 elif i==')':
   d1=d1+1
 if i=='[' :
   p=p+1
 elif i==']':
   p1=p1+1
 if i=='{' :
   a=a+1
 elif i=='}':
   a1=a1+1

b=True
if d==d1 and p==p1 and a==a1:
 b=True
else: b=False
print(b)