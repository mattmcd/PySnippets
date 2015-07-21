# Fizz Buzz with and without decorators
# Algorithm: convert input list of intergers to (x, '') tuples, then map
# fizz buzz functions over the tuples, appending the the string part if the
# required condition is met (fizz: x % 3 == 0, buzz: x % 5 ==0).  Finally,
# extract the string part and print, or print the number if string is empty

def tuplizer(x):
    return (x, '')


def detuplizer(x):
    if x[1]:
        return x[1]
    else:
        return str(x[0])


def make_filter(k, msg):
    def f(x):
        if x[0] % k == 0:
            out = (x[0], x[1] + msg)
        else:
            out = x
        return out
    return f


def make_decorator(f):
    def f_decorator(func):
        def inner(x):
            return f(func(x))
        return inner
    return f_decorator


def fb(x):
    """FizzBuzz using composition"""
    f = make_filter(3, 'fizz')
    b = make_filter(5, 'buzz')
    return detuplizer(b(f(tuplizer(x))))


@make_decorator(detuplizer)
@make_decorator(make_filter(5, 'buzz'))
@make_decorator(make_filter(3, 'fizz'))
@make_decorator(tuplizer)
def fb_dec(x):
    """FizzBuzz using decorators"""
    return x


def fizzbuzz(n):
    def aux(x):
        print fb_dec(x),
    map( aux, xrange(1,n+1));
    print


if __name__ == '__main__':
    fizzbuzz(20)
