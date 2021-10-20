"""
    Ex. 12: Scrieti un decorator pt f care sa scrie outputul lui f intr-un
    fisier, "output12.data".

    Observatii: f nu e la fel ca la ex 11.

"""
def logger(f):
    def wrapper(x):
        fisier=open("output12.data","w")
        fisier.write(x)
        fisier.close()
        f(x)
    return wrapper


@logger
def f(x):
    print(x)

f('exercitiul_12')
