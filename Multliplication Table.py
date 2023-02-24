#num = int(input("what is the number to multiply with"))
#mx = [x + 1 * num for x in range(20)]

#print (mx)


#deeper concept of multiplication table


num = int(input("what is the number to multiply with"))

mx = [x + 1 * num for x in range(20)]

## x is a variable, x is meant to be generated when the list value is decided by the range function
## which is range(20).. so x increments to 20
## the below complex code, wraps a string data type around x and concatenates x symbol to give 
## a multiplication fill (1 x 3 = 3, 2 x 3 = 6 and so on)
## (x + 1) is to start the multiplication number from 1 instead of 0


mx2 = [str(x + 1)+' x ' +str(num)+' = ' +str((x+1)*num) for x in range(20)]

##another method of achieving a multiplication table 
### with F expression..
### f within single coat and the curly brackets denotes that 
# python will read anythin within the curly brackets as code 
### and anything written outside python will read as text
##below the f start with ' and ends with '


mx3 = [f'{x + 1} x {num} = {(x+1)*num}' for x in range(20)]

print (mx3)

