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

N = 29000
abuns = [i for i in range(1, N) if i < sum(facts(i))]
print(len(abuns))
s = set(range(N))
for k, i in enumerate(abuns):
    for j in abuns[k:]:
        x = i + j
        if x > N:
            break
        s -= {x}
print(s)
print(sum(s))
