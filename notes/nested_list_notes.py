# nested lists notes finished
# this program continues to use the idea of a row of cars as a list

# What are nested lists?
#   A nested list is a list containing other lists or sequences.
#   The more general term is a nested sequence (we can do this with tuples as well).

#1 Creating a nested list
row = [["Ford", "Fusion"], ["Audi", "A4"], ["BMW", "3 Series"],["Jeep", "Wrangler"]]
print (row)


#1b : A visually easier way of entering nested sequences
row = [["Ford", "Fusion"],
       ["Audi", "A4"],
       ["BMW", "3 Series"],
       ["Jeep", "Wrangler"]
       ]
print (row)

if "Ford" in row:
    print ("True")
else:
    print ("False")

#2 Accessing nested elements
print (row[0])
print (row[1])
print (row[2])
print (row[3])

#3 Accessing an individual element within a nested element
print (row[0][1])

# On your own: display each of the following...
#   The make of the 4th car in the row
print (row[3][0])

#   The model of the 2nd car in the row
print (row[1][1])

#   The make and model of the 3rd car in the row
print (row[2][0], row[2][1])

# Challenge! Try changing the model of the Ford to an "F150" and then display it
row[0][1] = "F150"
print (row[0][0], row[0][1])

input("Press Enter to Continue...")

# Challenge!
# Try printing the car make and model in column format
#   with a single tab in between:
print ("Make\t\tModel")
for car in row:
    print (car[0], "\t\t", car[1])

input("Press Enter to Continue...")

#4 Unpacking a sequence
#  Unpacking a sequence means assigning each element
#   its own variable in a single line of code.
print ("Make\t\tModel")
for car in row:
    make, model = car
    print (make, "\t\t", model)

#5 Appending a new sequence
make = input("What is the car's make? ")
model = input("What is the car's model? ")
entry = [make, model]
row.append(entry)
print (row)

#6 Sorting a nested sequence
row.sort()
print (row)

#7 Sorting a nested sequence by elements other than the first
#  We have a new module that we need to use... operator (and the itemgetter function).

from operator import itemgetter     # only importing the function we need
row.sort(key=itemgetter(1))
print (row)

#8 Reverse
row.sort(key=itemgetter(1), reverse=True)
print (row)

#9 Searching IN
#   You have to loop through to find if an indvidual element is in a nested sequence
count = 0
for car in row:
    if "VW" in car:
        print ("There is a VW in the row")
        count += 1
if count == 0:
    print("There is not a VW in the row")
       

input("Press Enter to Exit")
