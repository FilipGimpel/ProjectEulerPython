from problem_3 import isPrime

def solve():
    counter = 1
    i = 1
    while (counter <= 10001):
        i += 2 
        if isPrime(i):
            lastprime = i
            counter += 1
    return lastprime
    	

print solve()