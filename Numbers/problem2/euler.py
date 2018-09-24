from decimal import Decimal as Dec, getcontext as gc
from math import factorial as fact

gc().prec = 100


def calcEuler(n):
    e = Dec(0)
    numerator = Dec(1)
    for i in range(n):
        denomenator = fact(i)
        e += Dec(numerator)/Dec(denomenator)
    return e

def main():
    print calcEuler(100)

if __name__ == "__main__":
    main()
