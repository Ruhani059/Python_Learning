from math import sqrt

def isPrime (n):
    x = int (sqrt(n))
    for i in range (2,x+1):
        if n % i == 0:
            return False
    return True


print (2**31-1)
print isPrime(2**31-1)


