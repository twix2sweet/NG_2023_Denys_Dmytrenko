print( "This program is a simple calculator." )

operationTypeInput = input( "What arithmetic operation do you want to perform?\n`*` - Multiplication\n`/` - Division\n`+` - Addition\n`-` - Subtraction\n`root` - Root\n`pow` - Raise to power" )

firstNumber = float( input( "Please enter first number: " ) )
secondNumber = float( input( "Please enter second number : " ) )

match operationTypeInput:
    case "*":
           result = firstNumber * secondNumber
    case "/":
           result = firstNumber / secondNumber
    case "+":
           result = firstNumber + secondNumber
    case "-":
           result = firstNumber - secondNumber
    case "root":
           result = firstNumber ** (1 / secondNumber)
    case "pow":
           result = pow( firstNumber, secondNumber )
    case _:
           print("Oh, dear...\n{} - is not an ariphmetic operation!".format( operationTypeInput ))
           exit()

print( "Your result: {}".format( result ) )