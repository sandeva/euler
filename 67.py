s = open('67.txt').read().strip()
ll = [[int(x) for x in l.split()] for l in s.split('\n')]
m = []
for l in ll:
    m = [x + max(a, b) for x, a, b in zip(l, [0] + m, m + [0])]
print(max(m))
