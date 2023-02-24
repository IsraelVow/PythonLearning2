
exp = -1
total = 0

maxexp = 0
minexp = 0

while exp!=0:
    exp = int(input("what is the expense? (Type 0 to stop)"))
    total = total + exp

    if exp>maxexp:
        maxexp = exp

    if exp<maxexp:
        minexp = exp

print("Your total expenditure is ", total)
print("Your Maximum expenditure is ", maxexp)
print("Your Minimum expenditure is ", minexp)