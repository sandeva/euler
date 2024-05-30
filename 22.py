l = open('22.txt').read()
l = l.replace('"', "").split(',')
l.sort()
print(sum((i + 1) * sum([ord(x)-64 for x in n]) for i, n in enumerate(l)))
