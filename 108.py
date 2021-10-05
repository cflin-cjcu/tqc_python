import math

x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())

print('( %s , %s )' % (str(x1), str(y1)))
print('( %s , %s )' % (str(x2), str(y2)))
print('Distance = %.4f' % math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
