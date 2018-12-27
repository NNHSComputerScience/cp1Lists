# nested lists starter notes
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


#2 Accessing nested elements


#3 Accessing an individual element within a nested element


# On your own: display each of the following...
#   The make of the 4th car in the row

#   The model of the 2nd car in the row

#   The make and model of the 3rd car in the row

# Challenge! Try changing the model of the Ford to an "F150" and then display it


input("Press Enter to Continue...")

# Challenge!
# Try printing the car make and model in column format
#   with two tabs in between:
print ("Make\t\tModel")


input("Press Enter to Continue...")

#4 Unpacking a sequence
#  Unpacking a sequence means assigning each element
#   its own variable in a single line of code.
print ("Make\t\tModel")


#5 Appending a new sequence
make = input("What is the car's make? ")
model = input("What is the car's model? ")


#6 Sorting a nested sequence


#7 Sorting a nested sequence by elements other than the first
#  We have a new module that we need to use... operator (and the itemgetter function).


#8 Reverse



#9 Searching IN
#   You have to loop through to find if an indvidual element is in a nested sequence



input("Press Enter to Exit")
