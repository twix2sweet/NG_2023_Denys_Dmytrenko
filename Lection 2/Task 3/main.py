def getNumDivisors( number ) :
    divisors = []
    for i in range( 1, number + 1 ) :
        if number % i == 0 :
            divisors.append( i )
    return divisors

def getPrimesInRange( min, max ) :
    primes = []
    
    for num in range( min, max ):
        if num <= 1:
            continue

        prime = True
        for i in range( 2, num ):
            if num % i == 0 :
                prime = False
                break
        if prime :
            primes.append( num )     
                
    return primes

print( "This program will display table of each num before entered and its divisors and prime nums of range." )

userInput =  input( "Please enter the number: ")

while not userInput.isnumeric() :
    userInput = input( "Please enter the INT NUMBER!!! >:(  ")

positiveInput = abs( int( userInput ) )

for i in range( 1, positiveInput ) :
    print( '{}   |   {}'.format( i, getNumDivisors( i ) ) )
        
print( 'Prime numbers: {}'.format( getPrimesInRange( 1, positiveInput ) ) )


