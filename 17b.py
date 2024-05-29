import re

s1_9 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
ty = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
llion = ["thousand", "million", "billion", "trillion"]

def jn(a, s, b):
    return f"{a}{s}{b}" if b else a

tys = [jn(ty, '-', o) for ty in ty for o in s1_9]
d1_99 = dict(enumerate(s1_9 + teen + tys))
llion_d = dict(reversed([(1000 ** i, l) for i, l in zip(range(1, 5), llion)]))

def to_eng(n):
    if n in d1_99:
        return d1_99[n]
    for p, s in llion_d.items():
        if n >= p:
            return jn(f"{to_eng(n // p)} {s}", ', ', to_eng(n % p))
    return jn(f"{to_eng(n // 100)} hundred", ' and ', to_eng(n % 100))

for i in [0, 1, 12, 43, 100, 1000, 100_001, 2 ** 32]:
    print(f"{i:_} #{to_eng(i)}#")

s = ''.join([to_eng(i + 1) for i in range(1000)])
s = re.sub(r'[- ,]', '', s)
print(len(s))
