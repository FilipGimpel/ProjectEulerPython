# the trick: there is no trick, althought in fibbonaci sequence, 
# even nubers occur alternately, so we can avoid checking if 
# number is even and just add together only one in two 

def fib(maxval):
    i = 1
    j = 2
    while (i <= maxval):
        if (i % 2 == 0): yield i
        tmp = i
        i = j
        j = tmp + j


def solve():
	print sum(fib(4000000))