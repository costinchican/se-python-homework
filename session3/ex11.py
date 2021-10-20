"""
    Ex. 11: Scrieti un decorator care sa logheze outputul unei functii
    pe care o decoreaza, intr-un fisier "output11.data".

    https://www.w3schools.com/python/python_file_write.asp

    Functia decorata este f.
"""
def logger(f):
    def wrapper():
        fisier=open("output11.data","w")
        fisier.write(f())
        fisier.close()
        f()
    return wrapper


@logger# decorate me
def f():
    return "CMI"

f()
