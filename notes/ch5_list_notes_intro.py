# List Notes 1
# Lists are:
#     Sequences of any type
#     Like tuples, except they can be modified (mutable)
#     Can do everything tuples can, plus more

# 1: Creating a list
# empty list
row = [ ]


#list with elements
row = ["Ford", "Audi", "BMW", "Lexus", "Mercedes", "Jeep"]
print(row)

# 2: Using len() and in with lists
# len()
print(len(row))


# in
if "Audi" in row:
    print("An Audi is in the row.")

# 3: Indexing and slicing
# indexing
print("The first car in the list is", row[0], \
      "and the last car is", row[-1])

# slicing
print("The cars in the middle of the row are", row[1:-1])

# 4: Concatenating lists
new = ["Toyota", "Nissan"]
row += new
print(row)


# LIST MUTABILITY
#     lists can be changed (mutable)
#     elements can be added and removed

# 5: Assigning a new list element by index
row[0] = "Honda"
print(row)
# ['Honda', 'Audi', 'BMW', 'Lexus', 'Mercedes', 'Jeep', 'Toyota', 'Nissan']

# 6: Assigning a new list element by slice
row[3:5] = ["Chevy", "Tesla"]
print(row)
# ['Honda', 'Audi', 'BMW', 'Chevy', 'Tesla', 'Jeep', 'Toyota', 'Nissan']
#   0        1       2      3        4           5       6         7

#can also replace multiple elements with only 1 element
row[1:3] = ["Buick"]
print(row)

# TRAP
#row[1:3] = "Buick"
#print(row)


# 7: Deleting a list element
del row[0]
print(row)

# 8: Deleting a slice
del row[1:3]
print(row)

# 9: REVIEW CHALLENGE
# DISPLAYING ELEMENTS FROM MULTIPLE LISTS w/ Headings
# first we need a second list to work with
model = ["Regal", "Wrangler", "Prius", "Altima"]
print("Make\tModel")
for i in range(len(row)):
    print(row[i], "\t", model[i])
    
    
input("\nPress enter to exit.")
