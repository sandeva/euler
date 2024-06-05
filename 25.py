a, b = 1, 1
for i in range(10_000):
    if len(str(a)) >= 1000:
        print(i + 1, a, )
        break
    a, b = b, a + b
