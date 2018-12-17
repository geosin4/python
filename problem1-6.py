#calculating quadratic roots of equation ax² + bx + c = 0
import math
a = int(input('Input a:'))
b = int(input('Input b:'))
c = int(input('Input c:'))
print('x1 = ' + str((-b + math.sqrt(b**2 - 4*a*c))/2*a) + '\n' + 'x2 = ' + str((-b - math.sqrt(b**2 - 4*a*c))/2*a))
