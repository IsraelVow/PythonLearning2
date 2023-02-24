
##create a csv file and input todays date inside

from datetime import date
import csv

dt = date.today()
#to format date to a proper format - strftime is a function used to convert a datetime value
# to a specific string e.g text function in excel or format function in Dax/vba
dt = dt.strftime("%d/%m/%Y")

filename = "test.csv"
###this is opening the file and specifying that youre opening the file in writing mode
# every computer language requires that you specify what mode youre reading a file with
# either, on view only, edit mode or both 
 


exp = []

stopped = False

#with open(filename, 'w') as file:

## 'a' appends any new entry with the previous ones and then newline = "" 
# removes the entra line that the open functions sets as default whenever an entry is made to the csv false

with open(filename, 'a',newline = "") as file:
    #csv.writer this takes a file you open and tells the computer how to create the csv file
    csvwriter = csv.writer(file)
    while not stopped:
        xp = int(input("enter all the expense, type 0 to exit"))

        if xp==0:
            stopped = True
        else:

            #pass the date variable(dt) as a list, each item of the list will become one value of the csv
            csvwriter.writerow([dt, xp])
            exp.append(xp)

file.close()

print("Your expenses today is: ", exp)
print("Your total expenses is: ", sum(exp))

