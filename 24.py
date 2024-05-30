from math import factorial

def p(l, n):
    if not l:
        return ''
    i, j = divmod(n, factorial(len(l) - 1))
    return f'{l.pop(i)}{p(l, j)}'

print(p(list(range(10)), 999_999))
