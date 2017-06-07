
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

n = 27
x = int (sqrt(n))
list_prime = {}
for i in range (2,x+1):
    if isPrime(i) == True:
        cnt = 0
        while n % i == 0:
            cnt = cnt + 1
            print i, ;
            n = n / i
        list_prime[i] = cnt
print ' '
n = 403
sum = 0
while n != 0:
    sum += n % 10
    n = n / 10
print sum
print list_prime
