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

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n =100
    print sieve(n)

