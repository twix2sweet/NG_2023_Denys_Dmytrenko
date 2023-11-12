print( "This program will show only unique elements of user input. Please eneter element and press Enter to continue filling data. Enter 'finish' to finish:)" )


inputList = []
userInput = input( "Please enter the first value: ")

while( userInput != 'finish' ) :
    if ( userInput not in inputList and userInput != '' ) :
        inputList.append(userInput)
    userInput = input( "Please enter the next value: ")

if ( len( inputList ) > 0 ) :
    print( "Sorted list: {}".format( inputList ) )
else :
    print( "You're didn't input anything...")
