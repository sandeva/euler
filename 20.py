from functools import reduce

print(sum(map(int, str(reduce(int.__mul__, range(1, 101))))))

