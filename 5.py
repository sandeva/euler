from functools import reduce

N = 20
def primes(lim):
    p = []
    for i in range(2, lim + 1):
        for j in p:
            if not i % j:
                break
        else:
            p.append(i)
            yield i

def pow(p, N):
    r = p
    while r <= N:
        r *= p
    return r // p

ps = list(primes(N))
print(ps)
ps = [pow(x, N) for x in ps]
print(ps)
print(reduce(int.__mul__, ps))
