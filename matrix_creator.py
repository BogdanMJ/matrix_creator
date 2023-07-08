from random import randint
import numpy
l1 = [randint(-5,5) for _ in range(5)]
l2 = [randint(-5,5) for _ in range(5)]
l3 = [randint(-5,5) for _ in range(5)]
l4 = [randint(-5,5) for _ in range(5)]
l5 = [randint(-5,5) for _ in range(5)]
m = numpy.array([[l1],
                 [l2],
                 [l3],
                 [l4],
                 [l5]])
print(m)

min = numpy.min(m, axis=1)

print(min)