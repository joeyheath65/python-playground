#!/usr/local/bin/python3

import random
import collections

results = collections.Counter()


for __ in range(1000000):
    num1 = random.randint(1,54)

    results.update([ '%d' % (num1) ])


print()
print('6 most common numbers (1 mil drawings):', results.most_common(6))
print


print()
print('6 most common numbers:')
print()
for x in results.most_common(6):
    print('  %s - %d times' % x)

print('')    

