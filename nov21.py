#!/usr/bin/env python

# Nov 21 Math homework
# Comments by Dax
# Code by Dad

from random import sample
from itertools import ifilter

def csv(numbers):
  return ", ".join([str(n) for n in numbers])

# write 2 digit numbers using the digits 0123456789.
# try to make 6 numbers less than 50.

numbers = sample(xrange(10,50), 6)
print "Six numbers: " + csv(numbers)

# sort the 2 digit numbers you created into odd and even numbers.

print "Even: " +  csv(ifilter(lambda x: x%2 == 0, numbers))

print "Odd: " +  csv(ifilter(lambda x: x%2, numbers))

# compare 3 sets of the 2 digit numbers you created, using the greater
# than/less than symbols.

for n in [numbers[i:i + 2] for i in xrange(0, len(numbers), 2)]:
  print str(n[0]) + (" < " if n[0] < n[1] else " > ") + str(n[1])
