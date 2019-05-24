#user interface

class GeenCijferIngegevenError(Exception):
    pass

class NulIngegevenAlsDeler(Exception):
    pass

def groet(name):
    print(f"Hallo {naam}")

def vraag_2_getallen():
    try:
        a = int(input("Geef getal 1: "))
        b = int(input("Geef getal 2: "))
        if b == 0:
            raise NulIngegevenAlsDeler
    except ValueError:
        raise GeenCijferIngegevenError
    return a, b

print('ui layer initialized')