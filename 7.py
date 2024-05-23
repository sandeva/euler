i, c, p = 1, 0, []
while True:
    i += 1
    for j in p:
        if not i % j:
            break
    else:
        p.append(i)
        c += 1
        if c == 10001:
            break
print(i)
