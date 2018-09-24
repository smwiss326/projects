from decimal import Decimal as Dec, getcontext as gc
from math import factorial as fact
gc().prec = 100

def PI(n):
    pi = Dec(0)
    num = Dec(0)
    denom = Dec(0)
    for k in range(n):
        num = ((-1) ** k) * (fact(6 * k)) * ((545140134 * k) + 13591409)
        denom = (fact(3 * k)) * ((fact(k)) ** 3) * (640320 ** (3 * k ))
        pi += Dec(num)/Dec(denom)
    pi = pi * Dec(12)/Dec(640320**(Dec(1.5)))
    pi = 1/pi
    return pi

def main():
    print PI(10)


if __name__ == "__main__":
    main()
