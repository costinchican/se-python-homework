"""
    Ex. 18: Scrieti o functie care sa intoarca suma unei liste de numere
    folosind recursivitate.

    Exemplu:
        - f([1,2,3])
            ---> 6
"""
def recursive(l):
    if len(l)==0:
        return 0
    return l[0]+recursive(l[1:]) #Adun primul element din lista si apoi aplic funtia pentru lista fara primul element,
                                 #pana cand lista ramane fara elemente.

l=[1,2,3]
print(recursive(l))
