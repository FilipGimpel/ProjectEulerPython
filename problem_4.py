# this is explained soultion for PE fourth problem
# I noticed that some solutions applied here are simply 
# explendable to different numeral systems and decided
# to add apriopriate additional 'base' parameter to few methods
# enjoy!

# method for checking whether number is a palindrome
def isPalindrome(number, base):
    """" Check whether given number is a palindrome in given numeral system """
    length = getNumberLenght(number, base)
    for i in range(0, length//2):
        if getDigit(number, i, base) != getDigit(number, (length - 1)-i, base):
            return False
    return True

def getDigit(number, digit, base):
    """ Returns digit of given number in numeral system given by base argument """
    return number % base**(digit+1) // base**digit


def getNumberLenght(number, base):
    """ Returns number length in numeral system based on base argument """
    lenght = 1
    while(number // base):
        number = number // base
        lenght += 1

    return lenght


def yieldMeSomeFunkyStuff(loweLimitInclusive, upperLimitInclusive):
    """ This method iterates over products of i and j 
        (where i and j are combinations without repetitions
         of numbers from range defined by arguments),
         yielding ones being palindrome numbers """
    # double loop that yields i and j combinations with repetitions
    for i in range(loweLimitInclusive, upperLimitInclusive + 1):
        for j in range(upperLimitInclusive + 1, loweLimitInclusive, -1):
            product = i*j;
            if isPalindrome(product, 10): yield product, i, j

# the solution:
#print max([i for i in yieldMeSomeFunkyStuff(100, 999)])

# okay, we found the solution, on my machine it runs in 2.4 seconds
# can we improve our approach so that its faster?
# notice that in above code we check all products for being pallindrome
# but we search for only th biggest one!

# lets create method similar to yieldMeSomeFunkyStuff 
# that yields all products no matter whether they are palindrome numbers

def yieldMeStuff(loweLimitInclusive, upperLimitInclusive):
    """ This method iterates over products of i and j 
        (where i and j are combinations without repetitions
         of numbers from range defined by arguments),
         yielding ones being palindrome numbers """
    # double loop that yields i and j combinations with repetitions
    for i in range(loweLimitInclusive, upperLimitInclusive + 1):
        for j in range(upperLimitInclusive + 1, loweLimitInclusive, -1):
            product = i*j;
            yield i * j



def solve():
    # now A is a list of products of all three digit numbers,
    A = [ i for i in yieldMeStuff(100, 999)]

    # sorted descending
    A.sort(reverse=True)

    # lets search for a pallindrome, starting from biggest number
    # when we find one, checking others is redundant
    for i in A:
        if isPalindrome(i, 10):
            print i
            break

# found the soution in 0.6 seconds!