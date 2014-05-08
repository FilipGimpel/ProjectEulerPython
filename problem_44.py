from itertools import combinations
from math import sqrt

def p_n(n):
	return n*(3*n-1) / 2

# It is simply a bruteforce solution, with improved method
# of checking whether difference/sum of numbers is a pentagonal number 

# For a given number n we check if quadratic eqation
# n = x*(3*x-1) / 2 
# has positive, whole roots
def isPentagonal(n):
	root = (1 + sqrt(24*n + 1))/6
	return root.is_integer()

# this solution method might need to be improved
# as it takes arbitrary "size" argument, which we provide
# which in an elegant solution would be unnecessary
def solve(size):
	pentagonal_numbers = [ p_n(n) for n in range(1, size + 1)]
	results = []

	for i in combinations(pentagonal_numbers, 2):
		p_j = i[0]
		p_k = i[1]
		#if p_j + p_k in pentagonal_numbers:
		if isPentagonal(p_j + p_k):
			print p_j, p_k
			p_big =	p_j if p_j > p_k else p_k 
			p_small = p_j if p_j < p_k else p_k
			#if (p_big - p_small in pentagonal_numbers):
			if (isPentagonal(p_big - p_small)):
				results.append( (p_big, p_small) )

	return results, counter

# print solve(2450) # about one milion checks 1450

