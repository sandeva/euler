def facts(x):
    for i in range(1, x):
        i2 = i ** 2
        if i2 < x:
            if not x % i:
                yield i
                yield x // i
        elif i2 == x:
            yield i
        else:
            break

m = (0, 0)
for i in range(1, 100000):
    v = i * (i + 1) // 2
    l = list(facts(v))
    m = max(m, (len(l), v))
    if m[0] > 500:
        break
print(*m)
