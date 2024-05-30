days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
n = 2
c = 0
for i in range(1901, 2001):
    _days = list(days)
    if not i % 4:
        _days[1] = 29
    for m in _days:
        if not n % 7:
            c += 1
        n += m
print(c)

