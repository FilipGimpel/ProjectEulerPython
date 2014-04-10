import math

# Lets get the dummiest primality test algorithm and succesively improve it
# Number n is prime when it can only be divided with no reminder by 1 and n

def isPrimeDumb(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

# We may notice that checking even numbers or number over n/2 is redundant
# Next observation is that numbers over sqrt(n) are just multiplications 
# of previous prime factors
# considering this we get:

def isPrime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    max_divisor = int(n ** 0.5) # square root of n
    divisor = 5
    while divisor <= max_divisor:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6
    return True

# we can also use prepared list of primes to check for primarility 
# before actually pasing number to isPrime method
# to prepare list of primes, lets use erasthotenes sieve!

def sieve(limit):
    primeList = [x for x in range(2, limit)]
    nextPrime = 2;

    primeLimit = int(math.sqrt(limit))

    for k in range(0, primeLimit):        
        for x in primeList:
            if (x % nextPrime == 0 and x != nextPrime):
                primeList.remove(x)

        nextPrime = find(lambda z : z > nextPrime, primeList)
        #print p

    return primeList


# this is small utility method which I found when searching for a
# nice way of retrieving element that satisfies condition f
# from an iterator (thanks to http://tomayko.com/writings/cleanest-python-find-in-list-function)
# I wanted some kind of oneliner, such as reduce(f, peeps), but this requires to iterate over whole
# set

def find(f, seq):
    """Return first item in sequence where f(item) == True."""
    for item in seq:
        if f(item): 
            return item

    return None

def largestPrimeFactor(n):
    start = int(math.sqrt(n))
    isPrimeFactor = lambda x: n % x == 0 and isPrime(x)

    for i in range(start, 1, -1): #oprimize
        if isPrimeFactor(i):
            return i

    return None

toBeFactored = 600851475143

print largestPrimeFactor(toBeFactored)

