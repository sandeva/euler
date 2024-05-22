def fib(lim):
    a, b = 1, 2
    while a < lim:
        yield a
        a, b = b, a + b

print(sum([f for f in fib(4_000_000) if not f % 2]))
