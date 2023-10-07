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
    rootExtrdD = math.sqrt( -d )
    appendFraction = False
    if ( -b % ( 2 * a ) == 0 ) and ( rootExtrdD % ( 2 * a ) == 0 ) :
        x1 = '\n' + str( -b / ( 2 * a ) ) + ' - ' + str( rootExtrdD / ( 2 * a ) ) + ' i'
        x2 = '\n' + str( -b / ( 2 * a ) ) + ' + ' + str( rootExtrdD / ( 2 * a ) ) + ' i'
    else :
        x1 = '\n' + str( -b ) + ' - ' + str( rootExtrdD ) + ' i\n---------\n   ' + str( 2 * a )
        x2 = '\n' + str( -b ) + ' + ' + str( rootExtrdD ) + ' i\n---------\n   ' + str( 2 * a )


print( "Your result:\nx1 = {}".format( x1 ) )

try:
    print( "\nx2 = {}".format( x2 ) )
finally:
    exit(0)