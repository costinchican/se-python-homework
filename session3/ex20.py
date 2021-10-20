"""
    Ex. 20: Deschideti fisierul .json creat la exercitiul anterior, cititi
    continutul si returnati un dictionar (dictionarul de acolo).

    Toate astea le veti face intr-o functie read_from_file(file), unde
    file este numele fisierului primit dat ca parametru.
"""
import json

def read_from_file(file):
    f=open(f"{file}")
    d=f.read()
    f.close()
    dictionar = json.loads(d)
    print(dictionar)
    return dictionar

read_from_file('exercitiul_19.json')

