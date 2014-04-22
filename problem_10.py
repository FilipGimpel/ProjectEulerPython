from problem_3 import isPrime

# I don't have to keep all numbers in memory, only their current sum
# I don't have to check all numbers, I know some of them are not primes
# Its not really a great solution but I find the problem boring
# another way would be to modify the sieve method


def solve():
	sum_of_primes = 2 # consider 2 as already added to sum

	for i in range(1, 2000000, 2):
		if isPrime(i):
			sum_of_primes += i

	return sum_of_primes

print solve()