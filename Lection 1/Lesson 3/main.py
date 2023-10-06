print( "This program will convert temperature from Celsium to Fahrenheit and vice versa." )

initialUnitInput = input( "Which unit of measurement do you want to convert to:\nF - Fahrenheit\nC - Celsium\n" )

if initialUnitInput == 'C' or initialUnitInput == 'c':
    initialUnitName = 'Fahrenheit'
elif initialUnitInput == 'F' or initialUnitInput == 'f':
    initialUnitName = 'Celsium'
else:
    print( "Dude... Rly?" )
    exit()

unitsQuantity = float( input( "How many degrees {} should be converted?\n".format( initialUnitName ) ) )
if initialUnitInput == 'C':
    result = ( unitsQuantity - 32 ) / 1.8
elif initialUnitInput == 'F':
    result = ( unitsQuantity * 1.8 ) + 32

print( "Your result: {}".format( result ) )
