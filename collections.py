import collections
from collections import Counter

c = Counter('gallad')
print(c)
print(c['l'])
c = Counter(['a', 'a', 'b', 'c', 'c'])
print(c)
print(c['a'])
c = Counter({'a': 1, 'b': 2})
print(c['b'])
c = Counter(cats=4, dogs=7)
print(c['cats'])

print(list(c.elements()))
print(c.most_common(2))

c = Counter(a=4, b=2, c=0, d=-2)
d = ['a', 'b', 'b', 'c']
c.subtract(d)
print(c)

c.update(d)
print(c)

# intersection and union
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(['a', 'b', 'b', 'c'])
print(c+d)
print(c-d)

print(c & d)
print(c | d)
