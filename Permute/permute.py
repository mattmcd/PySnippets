from math import factorial


def permute(i, n):
    """i-th permutiation of n-elements
     Permutations are arranged in lexical order e.g.
     [1,2,3], [1,3,2], [2,1,3], ... , [3,2,1]
    Args:
        i: index of permutation in list of sorted permutations
        n: number of elements

    Returns:
        list of permuted elements
    """
    i %= factorial(n)
    els = range(n)
    acc = []
    while len(els) > 1:
        b = factorial(len(els) - 1)
        q = i // b
        r = i % b
        acc.append(els[q])
        del els[q]
        i = r
    acc.append(els[0])
    return acc


def index(p):
    """Given a permutation return its index in sorted list of permutations

    Args:
        p: permutation as a list e.g. [3,2,1]

    Returns:
        Index in sorted list of permutations
    """
    n = len(p)
    acc = 0
    for i in range(n):
        acc += factorial(n-1-i)*sorted(p[i:]).index(p[i])
    return acc


def multiply(i, j, n):
    """Return index of permutation obtained by multiplying two permutations
    Args:
        i: index of left permutation
        j: index of right permutation
        n: number of elements permuted

    Returns:
        index of resulting permutation
    """
    a = permute(i, n)
    b = permute(j, n)
    c = index([a[b[k]] for k in range(n)])
    return c


def table(n):
    # Multiplication table for permutations of n symbols
    np = factorial(n)
    return [[1 + multiply(i, j, n)
             for j in range(np)]
            for i in range(np)]
