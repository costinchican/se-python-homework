"""
    Ex. 6: Scrieti o functie cu un singur parametru (string) care
    intoarce un string cu toate literele stringului primit +1 (adica urmatoarea
    litera din alfabet)

    Raspuns:
        - func('aabbcc')
            ---> 'bbccdd'
"""
def f_increment(string):
    return "".join([chr(ord(i)+1) for i in string])

print(f_increment('aabbcc'))