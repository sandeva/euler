def chk(p):
    s = str(p)
    return s == ''.join(reversed(s))

N = 1000
mx = 0
for i in range(N, 0, -1):
    for j in range(N, i, -1):
        p = i * j
        if p < mx:
            break
        if chk(p):
            mx = p
            print(i, j, p)

