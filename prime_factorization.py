from math import sqrt

def isPrime (n):
    x = int (sqrt(n))
    for i in range (2,x+1):
        if n % i == 0:
            return False
    return True

n = a = 24
x = int (sqrt(n))
list_prime = {}
for i in range (2,x+1):
    if isPrime(i) == True:
        cnt = 0
        while n % i == 0:
            cnt = cnt + 1
            n = n / i
        list_prime[i] = cnt

# printing the prime factorization in format 24 = 2 (3), 3 (1),
# print list_prime
print a," = ",;
for item in list_prime:
    if list_prime[item] != 0:
        print item , "(" , list_prime[item] , "),",
print ''
#print list_prime
