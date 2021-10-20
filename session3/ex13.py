"""
    Ex. 13: Scrieti un decorator care sa modifice modul de functionare
    al functiei f. Puteti alege voi cum. Momentan, f intoarce 'cmi', un exemplu
    ar fi sa intoarca 'CmI' dupa aplicarea decoratorului.

"""
def dec(func):
    def wrapper():
        l=[]
        v='aeiou'
        for i in func():
            for j in v:
                if i==j:
                    l.append(i)
        return "".join(l)

    return wrapper

@dec
def f():
    return 'cmi'


print(f())