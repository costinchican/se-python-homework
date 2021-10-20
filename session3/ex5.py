"""
    Ex. 5: Scrieti o functie cu un singur parametru (o lista) care sa
    adauge 1 tuturor elementelor din lista.

    Raspunsul corect:
        - func([1, 2, 3])
            ---> [2, 3, 4]

    Observatii:
        - functia trebuie sa fie MAXIM o linie de cod (2, daca luam in calcul
        si definitia functiei)
        - hint: list comprehensions (google it if you don't know it already)
"""

def increment_list(l):
      return list(map(lambda x:x+1,l)) #Utilizand functia lambda


def increment_list1(l):
    return [x+1 for x in l] #Utilizand list comprehension

print(increment_list([0,1,2]))
print(increment_list1([0,1,2]))



