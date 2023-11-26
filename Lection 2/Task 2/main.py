print( "This program will count how many elements of user input are numbers. Please enter elements and separated with space ' '." )

userInput = input( "Please enter the values: ")

numbers = 0
for item in userInput.split( ' ' ) :
    try:
        float( item )
        numbers += 1
    except ValueError:
        continue

if ( numbers > 0 ) :
    print( "There are {} numbers in this list".format( numbers ) )
else :
    print( "There are no numbers in list..." )
