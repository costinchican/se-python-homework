"""
    Ex. 16: Scrieti o functie upper care sa intoarca un text uppercase complet,
    primind un parametru my_str (string).
    --> f('cmi') --> 'CMI'

    Scrieti o functie lower care sa intoarca un text lowercase complet,
    primind un parametru my_str (string).
    --> f('CMI') --> 'cmi'

    Veti primi un input de la tastatura, un string.

    Scrieti o alta functie call_changers, care sa primeasca o functie ca si
    parametru, iar daca inputul are un numar par de caractere, va printa inputul
    cu uppercase, altfel, va printa inputut lowercase.

    Exemplu:
        - veti primi input: 'ceva'
            ---> CEVA
        - veti primi input: 'cEVa1'
            ---> ceva1
"""
def upper(my_string):
    l=[]
    for i in my_string:
        if ord(i)>=97 and ord(i)<=122:
            i=chr(ord(i)-32)
            l.append(i)
        else:
            l.append(i)
    return "".join(l)

def lower(my_string):
    l=[]
    for i in my_string:
        if ord(i)>=65 and ord(i)<=90:
            i=chr(ord(i)+32)
            l.append(i)
        else:
            l.append(i)
    return "".join(l)

def parity(my_string):
    if len(my_string)%2==0:
        return True
    else:
        return False

def call_changers(f,my_string):
    if f(my_string):
        print(upper(my_string))
    else:
        print(lower(my_string))

my_string=input()
call_changers(parity,my_string)
