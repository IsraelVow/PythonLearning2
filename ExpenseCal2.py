exp = []
stopped = False

while not stopped:
    e = int(input("what is the expense (type 0 to stop)"))
    if e!=0:
        exp.append(e)
    else:
        stopped = True

print (exp)
print ("total of expense: " + str(sum(exp)))
print ("Max of expense: ", max(exp))
print ("Minimum of expense: ", min(exp))
