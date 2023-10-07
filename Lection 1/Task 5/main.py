import math 

print( "This program is designed to solve quadratic equations.\n( a * x^2 ) + ( b * x ) + c = 0" )

a = float( input( "Please enter 'a': " ) )
b = float( input( "Please enter 'b': " ) )
c = float( input( "Please enter 'c': " ) )

d = pow( b, 2 ) - 4 * a * c
print( "Discriminant (D): {}\n".format( d ) )

if d > 0 :
    x1 = ( -b + math.sqrt( d ) ) / 2 * a
    x2 = ( -b - math.sqrt( d ) ) / 2 * a
elif d == 0 :
    x1 = ( -b + math.sqrt( d ) ) / 2 * a 
else :
    print('There is no values for x')
    exit()

print( "Your result:\nx1 = {}".format( x1 ) )

try:
    print( "\nx2 = {}".format( x2 ) )
finally:
    exit(0)