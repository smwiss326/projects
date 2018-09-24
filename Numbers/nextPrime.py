
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

    
def nextPrime():
    i = 0;
    nextPrime = True
    while nextPrime:
        userChoice = raw_input("Would you like to find the next prime?   ")
        if userChoice == 'y':
            nextPrime = True
            while( not is_prime(i)):
                i+=1
            print(str(i) + " is prime!")
            i+=1
            continue
        else:
            nextPrime = False


def main():
    nextPrime()

if __name__ == "__main__":
    main()
