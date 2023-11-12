print( "This program will count how many elements of user input are numbers. Please eneter element and press Enter to continue filling data. Enter 'finish' to finish:)" )


inputList = []
userInput = input( "Please enter the first value: ")

while( userInput != 'finish' ) :
    inputList.append( userInput )
    userInput = input( "Please enter the next value: " )

numbers = 0
for item in inputList :
    try:
        float( item )
        numbers += 1
    except ValueError:
        continue

if ( numbers > 0 ) :
    print( "There are {} numbers in this list".format( numbers ) )
else :
    print( "There are no numbers in list..." )
