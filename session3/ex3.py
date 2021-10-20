"""
    Ex. 3: Completati functia de mai jos, in asa fel incat sa intoarca
    o lista cu elementele pana la X (X fiind un parametru al functiei).

    Observatii:
        - X este un numar intreg (intotdeauna)
        - nu aveti voie sa folositi range()

    Rezultatul trebuie sa arate asa:
        - pentru x = 3 --> [0, 1, 2]
"""


def func(x):
    x=int(x)
    l=list()
    x1=x
    while x1>0 :
        l.append(x-x1)
        x1-=1
    return l

print(func(3))
