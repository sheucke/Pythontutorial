import collections
from collections import namedtuple

point = namedtuple('Point', 'x y z')

newP = point(3, 4, 5)
print(newP)

Point = namedtuple('Point', {'x': 0, 'y': 0, 'z': 0})
newP = Point(10, 1, 2)
print(newP)
print(newP.x)
print(newP._fields)

p2 = Point._make(['a', 'b', 'c'])
print(p2)
