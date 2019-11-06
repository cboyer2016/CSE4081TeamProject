#extened euclid algorithm found via wikipedia and supporting online sources
def euclid_ext(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, xx, yy = euclid_ext(b, a % b)
        x = yy
        y = xx - (a / b) * yy
        return d, x, y


def inverse(a, n):
    return euclid_ext(a, n)[1]


def xab(x, a, b, base, value, prime, halfPrime):
    sub = x % 3
    if sub == 0:
        x = x*base % prime
        a = (a+1) % halfPrime

    if sub == 1:
        x = x * value % prime
        b = (b + 1) % halfPrime

    if sub == 2:
        x = x*x % prime
        a = a*2 % halfPrime
        b = b*2 % halfPrime

    return x, a, b


def rho(base, value,prime):

    halfPrime = (prime - 1)/2  
    x = base*value
    a = 1
    b = 1

    X = x
    A = a
    B = b

   
    for i in xrange(1,prime):
        x, a, b = xab(x, a, b, base, value, prime, halfPrime)
        X, A, B = xab(X, A, B, base, value, prime, halfPrime)
        X, A, B = xab(X, A, B, base, value, prime, halfPrime)
        if x == X:
            break
    s = a-A
    t = B-b
    res = (inverse(t, halfPrime) * s) % halfPrime
    if check(base, value, prime, res):
        return res
    return res + halfPrime


def check(base, value, prime, exponent):
    return pow(base,exponent,prime) == value

if __name__ == "__main__":
    base = 2
    value = 10
    prime = 1019
    exponent = rho(base,value,prime)
    print ("{}^{} = {} (mod {})".format(base,exponent,value,prime))
    print "Status: ", check(base,value,prime, exponent)

