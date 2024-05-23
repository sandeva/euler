from functools import reduce

def primes(lim):
    p = []
    for i in range(2, lim + 1):
        for j in p:
            if not i % j:
                break
        else:
            if i * i <= lim:
                p.append(i)
            yield i

print(sum(primes(2_000_000)))
