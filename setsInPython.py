# sets store unique elements

s = {1, 2, 3, 4, 4}
print(type(s))

l = [1, 2, 3, 4, 5]
print(type(l))

s.add(3)
print(s)

s.remove(3)
print(s)

l = [x for x in range(100)]  # O(n)
s = {x for x in range(100)}

lookingFor = 98
for i, el in enumerate(l):
    if el == lookingFor:
        print(i)

lookingFor in l
lookingFor in s  # O(1)

# fast check for duplicates by using sets
s = [1, 1, 1, 13, 4, 6, 5]
dup = len(set(s)) == len(s)
print(dup)
