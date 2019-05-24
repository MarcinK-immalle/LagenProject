#business intelligence

class DelingMisluktError(Exception):
    pass

def deling_en_rest(a,b):
    "berekend de gehele deling en rest van a en b"
    try:
        deling = a // b
        rest = a % b
    except ZeroDivisionError:
        raise DelingMisluktError
    return deling, rest 

print('bi layer initialized')