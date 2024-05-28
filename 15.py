N = 20
l = [1 for i in range(N + 1)]
for i in range(N):
    l = [sum(l[i:]) for i in range(N + 1)]
print(l[0])
