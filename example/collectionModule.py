# -*- coding: utf-8 -*-
from collections import namedtuple
Point = namedtuple('Point',['x','y'])#内部名称随意无影响？
p = Point(1,2)
print('(',p.x,',',p.y,')')
print(Point.__doc__)

from collections import deque
q = deque(['a','b','c'])
q.append('last')
q.appendleft('first')
print(q)

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
print(dd['key'])

from collections import OrderedDict
d = dict([('a',1),('s',2),('d',3)])
od = OrderedDict([('a',1),('s',2),('d',3)])
print(d,'\n',od)

from collections import Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1

print(c)