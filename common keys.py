import collections
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = collections.Counter(d1) + collections.Counter(d2)
print(d)
