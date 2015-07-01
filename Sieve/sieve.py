from itertools import ifilter
import numpy as np

def sieve(n):
    '''Recursive Sieve of Eratosthenes'''
    acc = []
    def aux(numList):
        try:
            k = numList[0]
            acc.append(k)
            aux(filter(lambda x: x % k, numList))
        except IndexError:
            pass
    aux(xrange(2,n))
    return acc

def sieve2(n):
    '''Iterative Sieve of Eratosthenes'''
    acc = []
    numList = xrange(2,n)
    while numList:
        k = numList[0]
        acc.append(k)
        numList = filter(lambda x: x % k, numList)
    return acc

def sieve3(n):
    '''Iterative Sieve of Eratosthenes using iterator'''
    acc = [] 
    numList = iter(xrange(2,n))
    try:
        while True:
            k = numList.next()
            acc.append(k)
            numList = ifilter(lambda x: # all(x % np.array(acc))
                reduce(lambda acc,a: acc and (x % a), acc, True)
                , numList)
    except StopIteration:
        pass
    return acc

def sieve4(n):
    '''Sieve of Eratosthenes in memory'''
    acc = []
    sieve_array = np.arange(2,n)
    next_index = 0
    for (i,k) in enumerate(sieve_array):
        if k != 0:
          sieve_array[sieve_array % k == 0] = 0
          sieve_array[i] = k # Store the prime back into the array 
    return sieve_array[sieve_array != 0]

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n =100
    print 'There are {0} primes less than {1}'.format(len(sieve2(n)), n)
