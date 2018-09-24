import math

def is_prime(n):
    if n < 2:
         return False;
    if n % 2 == 0:
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

def pf(n):
    if(not is_prime(n)):
        for i in range(int(math.sqrt(n))+1):
            if is_prime(i) and n%i == 0:
                print str(i) + ", ",
                if is_prime(n/i):
                    print str(n/i) + ", ",
                else:
                    pf(n/i)
                    print " | ",
    else:
        print  str(n) + " is prime."

def main():
    pf(97)
if __name__ == "__main__":
    main()
