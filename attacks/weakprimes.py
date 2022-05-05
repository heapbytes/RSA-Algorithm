from sage.all import factor, ecm

def weakprimes(n):
    return str(factor(n)).split(' * ')

