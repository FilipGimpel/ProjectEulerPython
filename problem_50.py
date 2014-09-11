import itertools as it
""" To see solution just run test(4000)
	this problem solution is to be improved

	Work on method test2()
	TODO: while loop stop condition (warunek stopu)
	TODO: ommiting  unnecesary subchains"""


def test2():
	"""  """
	primes_list = []
	prime_generator = erat3()
	primes_list.append(prime_generator.next())
	limit = 1000000

	max_chain_len = 0
	max_prime = 0
	max_chain = []

	min_chain_len = 500
	i = 0
	j = i + min_chain_len -1

	guard = True
	counter = 0

	while(guard):	
		primes_list.append(prime_generator.next())
		curr_chain = primes_list[i:j+1]
		consec_prim_sum = sum(curr_chain)

		j += 1
		if consec_prim_sum > limit:
			print primes_list[i:j+1]
			i += 1
			j = i + min_chain_len -1

		if isprime(consec_prim_sum):
			print curr_chain, consec_prim_sum
			if max_chain_len < j-i+1:
				max_chain_len = j-i+1
				max_prime = consec_prim_sum
				max_chain = primes_list[i:j+1]

		if sum(primes_list[i:j+1]) > limit:
			#print primes_list[i:j+1]
			print "-------------------------------------------------------------"
			print "prime: {0}, chain length {1}".format(max_prime, max_chain_len)
			print "chain: {0}".format(max_chain)
			break

		# counter += 1
		# if counter > 10000:
		# 	print "GUARD STOP"
		# 	guard = False


def primes(n):
    """ Returns  a list of primes < n 
    	use erat3 instead """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]


def isprime(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
    else:
        return True


def erat3( ):
	""" see http://stackoverflow.com/a/3796442 """
    D = { 9: 3, 25: 5 }
    yield 2
    yield 3
    yield 5
    MASK= 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS= frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )

    for q in it.compress(
            it.islice(it.count(7), 0, None, 2),
            it.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D or (x%30) not in MODULOS:
                x += 2*p
            D[x] = p


def get_max_len(n):
	prime_sum = 0
	counter = 0
	for i in erat3():
		prime_sum += i
		counter += 1
		if (prime_sum > n):
			return counter


def test(n):
	""" this solution really sucks because:
		1. it takes arbitrary argument n which describes how big initial primes list shall be
		2. it takes artitrary min_len argument 
		3. it takes 15 sec to run
		"""
	primes_ = primes(n)
	max_chain_len = 0
	max_prime = 0
	max_chain = []

	last_i = 0
	last_j = 0

	# ommit chains shorter that min_len
	# no need to ommit chains that are too long because they will be 
	# ommited automaticaly by break instruction when their sum goes 
	# to big
	min_len = 500
	for i in range(0, len(primes_)):
		for j in range(i+1 + min_len , len(primes_)):
			consec_prim_sum = sum(primes_[i:j+1])

			if consec_prim_sum > 1000000:
				break

			if isprime(consec_prim_sum):
				if  j-i+1 > max_chain_len:
					max_chain_len = j-i+1
					max_prime = consec_prim_sum
					max_chain = primes_[i:j+1]
					last_i = i
					last_j = j

	print "prime: {0}, chain length {1}".format(max_prime, max_chain_len)
	print "chain: {0}".format(max_chain)
	print last_i, last_j





def check(elements):
	""" prints all sub-chains of list given as argument 
		Using for loop """
	for i in range(0, len(elements)):
		for j in range(i, len(elements)):
			print elements[i:j+1], i, j


def check2(primes_list):
	""" prints all sub-chains of list given as argument 
		using while loop """
	i = 0
	j = i
	while(i<len(primes_list) and j < len(primes_list)):
		print primes_list[i:j+1], i, j
		j += 1
		if j > len(primes_list)-1:
			i += 1
			j = i





test()