def sieve(n):
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
    acc = []
    numList = xrange(2,n)
    while numList:
        k = numList[0]
        acc.append(k)
        numList = filter(lambda x: x % k, numList)
    return acc

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n =100
    print 'There are {0} primes less than {1}'.format(len(sieve2(n)), n)

