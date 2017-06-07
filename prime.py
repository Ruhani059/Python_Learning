from math import sqrt

def isPrime (n):
    x = int (sqrt(n))
    isPrimeFlag = True
    for i in range (2,x+1):
        if n % i == 0:
            isPrimeFlag = False
            break
    return isPrimeFlag


print (2**31-1)
print isPrime(2**31-1)


