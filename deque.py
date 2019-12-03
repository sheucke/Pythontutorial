import collections
from collections import deque

# adding to end of list

d = deque("hello")
print(d)
d.append('4')
d.append(5)
print(d)
d.appendleft(5)
print(d)
d.pop()
d.popleft()
print(d)
d.clear
print(d)
d.extend('456')
print(d)
d.extendleft('hey')
print(d)
d.rotate(-1)
print(d)
d.rotate(-2)
print(d)

d = deque('hello', maxlen=5)
print(d)
d.append(1)
print(d)
