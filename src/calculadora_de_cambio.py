from math import floor

def converter(valor, taxa):
    if valor <= 0:
        return 0
    total = valor / taxa
    if total <= 0.01:
        return 0.01
    return floor(total * 100) / 100
