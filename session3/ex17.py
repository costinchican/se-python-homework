"""
    Ex. 17: Scrieti un decorator care scrie outputul unei functii intr-un fisier
    "output17.data", dar sa nu suprascrie fisierul daca scriptul e rulat de
    mai multe ori, iar contentul nou sa fie pe o noua linie.

    Scrieti o functie f care sa primeasca un intreg (x) ca parametru si sa
    genereze un string aleator din x litere.

    Decorati f cu decoratorul de mai sus.

    Exemplu:
        la prima rulare, x = 3, stringul generat = 'cmi', fisierul arata asa:
            cmi
        la a doua rulare, x = 6, stringul generat = 'cmicmi', fisierul arata:
            cmi
            cmicmi
        la a treia rulare, x = 1, stringul generat = 'b', fisierul arata asa:
            cmi
            cmicmi
            b
"""
"""
    Ex. 17: Scrieti un decorator care scrie outputul unei functii intr-un fisier
    "output17.data", dar sa nu suprascrie fisierul daca scriptul e rulat de
    mai multe ori, iar contentul nou sa fie pe o noua linie.

    Scrieti o functie f care sa primeasca un intreg (x) ca parametru si sa
    genereze un string aleator din x litere.

    Decorati f cu decoratorul de mai sus.
"""
import random

def non_overwrite(f):
    def wrapper(x):
        sir=f(x)
        file=open("output17.data", "a")
        file.write(sir)
        file.write('\n')
        file.close()
    return wrapper

@non_overwrite
def sir_random(x):
    alfabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l=[]
    for i in range(x):
        l.append(random.choice(alfabet))
    print("".join(l))
    return "".join(l)

x=int(input())
sir_random(x)
