def solve(n):
	print sum([i for i in range(0, n+1)])**2 - sum([i**2 for i in range(0, n+1)])

print solve(100)