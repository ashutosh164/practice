import collections
from collections import Counter

c = Counter('ashutosh')
print(c)
c = Counter(['a', 'a', 'b', 'c', 'c'])
print(c)
c = Counter({'a': 1, 'b': 2})
print(c)
c = Counter(cats=4, dog=7)
print(c['dog'])

print(list(c.elements()))
print(c.most_common(2))











