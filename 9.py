N = 1000
for a in range(1, N + 1):
    for b in range(a, N + 1):
        c = N - a - b
        if c < b:
            break
        if a ** 2 + b ** 2 == c ** 2:
            print(a, b, c, a * b * c)
