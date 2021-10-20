"""
    Ex. 19: Scrieti o functie care primeste un string ca si parametru,
    creeaza un fisier cu numele parametrului primit (.json) si scrie in el
    un dictionar de 4 elemente aleatoare unde key = int, iar value = string,
    iar stringul sa aiba intre 3 si 6 caractere si key sa fie intre 0 si 10.

    Exemplu:
        f('ceva')
        ---> generez ceva.json ca si fisier
        ---> generez un dictionar
            {
                1: 'blabla',
                5: 'cmi',
                7: 'cmi22',
                10: 'balqef'
            }

"""
import random
import json

def json_gen(string):
    file=open(f"{string}.json","w")
    d={}
    def string_gen():
       alfabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
       string_len=[3,4,5,6]
       l=[]
       for i in range(random.choice(string_len)):
           l.append(random.choice(alfabet))
       return "".join(l)

    while len(d)<4:                                      #Bucla este repetata pana cand se aleg 4 valori distincte
            d[random.choice(range(11))] = string_gen()   #pentru chei, astfel incat sa nu se suprascrie valori din dictionar.

    file.write(json.dumps(d,indent=1,sort_keys=True))
    file.close()
    print(json.dumps(d,indent=1,sort_keys=True))
    return d

json_gen('exercitiul_19')