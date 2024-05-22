n = 600851475143
for i in range(2, n + 1):
    if n == 1:
        break
    while not n % i:
        print(i)
        n /= i
