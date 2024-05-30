def facts(x):
    yield 1
    for i in range(2, x):
        i2 = i ** 2
        if i2 < x:
            if not x % i:
                yield i
                yield x // i
        elif i2 == x:
            yield i
        else:
            break

r = set()
for i in range(1, 10000):
    s = sum(facts(i))
    t = sum(facts(s))
    if s != t == i:
        r |= {s, t}
        print(s, t)
print(sum(r))
