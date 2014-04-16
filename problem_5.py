from problem_3 import find, sieve
from math import sqrt
from copy import deepcopy

# This algorigth may look a bit complicated but intuintion begind it is simple
# and whole problem can be solved without computer cause there are very few
# calculations done.

def factor(number):
	""" Returns list of primes which product is a given number.
		This method uses prepared list of primes below
		number/2 which are only potential divisors of number and 
		check whether they divide evenly """
	dividing_primes = sieve(number/2 + 1)
	factors = []
	
	while number != 1:	
		if not dividing_primes:
			return [number]

		next_divisor = min(dividing_primes)

		if not number % next_divisor:
			factors.append(next_divisor)
			number /= next_divisor
		else:
			dividing_primes.remove(next_divisor)

	return factors


def isProductOfNumbersInSeq(number, seq1):
	""" Returns list of primes which product is a given number.
		This method uses prepared list of primes below
		sqrt(number) which are only potential divisors of number and 
		check whether they divide evenly """
	seq = deepcopy(seq1)

	while number != 1:	
		if not seq:
			return False

		next_divisor = min(seq)

		if not number % next_divisor:
			number /= next_divisor
		
		seq.remove(next_divisor)

	return True

def solve():
	A = []
	for i in range(20, 1, -1):
		if not isProductOfNumbersInSeq(i, A):
			C = deepcopy(A)
			A += [i for i in factor(i) if not i in C or C.remove(i)]

 	return reduce(lambda x, y : x*y, A)

# Okay I just realized that in python functions should be "real"
# functions, that mean, they should not change supplied data.
# I am not sure if therefore using deepcopy here is an ugly workaround




