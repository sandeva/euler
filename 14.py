from functools import cache

@cache
def col(x):
    if x == 1:
        return 1
    if 1 & x:
        return 1 + col(3 * x + 1)
    return 1 + col(x >> 1)

m = (0, 0)
for i in range(1, 1_000_000):
    m = max(m, (col(i), i))
print(*m)
