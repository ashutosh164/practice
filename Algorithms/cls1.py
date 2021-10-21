# FIND THE GREATEST COMMON DENOMINATOR OF TWO NUMERS
# USING EUCLID'S ALGORITHM

def alg(a, b):
    while (b != 0):
        t = a
        a = b
        b = t % b
    return a

print(alg(20,8))








