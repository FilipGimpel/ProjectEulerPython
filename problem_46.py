import math

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]


def check(number, prime):
	""" checks if there is whole humber that 
		solves number = prime + 2*x^2 for x """
	value = math.sqrt((float(number) - prime)/2)
	return float(value).is_integer()


def goldbachs_ohter_conjecture(n):
	primes_list = primes(n)
	i = 1

	while(True):
		curr_smallest = primes_list[-i]
		if not check(n, curr_smallest):
			if i < len(primes_list):
				i+=1
			else:
				print "We'll, I Guess we, have found our man"
				print "YEEEAH!!! " + str(n)
				return True

		else:
			value = int(math.sqrt((n - curr_smallest)/2))
			print '{0} = {1} + 2 x {2}^2'.format(n, curr_smallest, value)
			return False


def solve(range_param):
	primes_list = primes(range_param)

	odd_composite_numbers = [i for i in range(3, range_param, 2) if i not in primes_list]

	for i in odd_composite_numbers:
		if goldbachs_ohter_conjecture(i):
			break

#solve(20000)