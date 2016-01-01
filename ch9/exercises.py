#!/usr/bin/env python3

print ('COMPREHENSIONS')
print ('LISTS')
input_string = ['1', '2', '3', '999']

output_int = []

for num in input_string:
    if len(num) < 3:
        output_int.append(int(num))

print (output_int)

output_int2 = [int(n) for n in input_string if len(n) < 3]
print output_int2

print ('SETS')
in_list = ['1', '2', '1']
in_set = {1, 2, 3, 3}
print set(in_list)
print in_set

from collections import namedtuple

print ('DICS')
nt = namedtuple('nt', 'name age')

d1 = {nt('tom', 36),
      nt('eva', 1),
      nt('tom', 2),
      nt('emma', 36)}

print d1

d2 = {n.name for n in d1 if n.age > 18}
d3 = {n.name: n for n in d1 if n.age > 18}

print d2
print d3

d4 = {1: 'a', 2: 'b', 3: 'c'}
print d4.values()

d5 = {d: True for d in d4}
print d5