from collections import defaultdict

a = defaultdict(lambda : defaultdict(lambda : 1))

print(a[5][6])