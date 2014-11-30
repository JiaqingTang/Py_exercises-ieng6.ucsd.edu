import numpy
# a = [[1 2 3 4 5]
# 	[6 7 8 9 10]
# 	[11 12 13 14 15]
# 	[16 17 18 19 20]]
# print a
b = numpy.array(range(25)).reshape((5,5))
print b
i = 0
j = 0
c = [i for i in range(5), j for j in range(5), []]
print c