# List Methods Notes
# METHOD - an ability that an object has.
#   Like strings, lists are objects that have their own special abilities, 
#     or list methods.

row = ["Ford", "Audi", "BMW", "Lexus", "Mercedes", "Jeep"]
print (row)

# 1: Append Method
#   adds an element to the end of a list
row.append("Ford")
print(row)

#append multiple is a trap!
#row.append("Ford", "Buick")
#print (row)

# 2: Pop method
#   removes an element by index value from a list and returns it
#   del keyword also removes by index (pop is preferred)
car = row.pop(1)
print(car)
print(row)

# 3: Remove method
#   removes an element from a list
row.remove("BMW")
print(row)
 
# this method removes the first occurance of an element
row.remove("Ford")
print(row)

 
# 4: Sort method
#   sorts a list in ascending order
row.sort()
print(row)

# 5: Reverse method
#   reverses the order of a list
row.reverse()
print(row)
row.reverse()
print(row)

# 6: Count method
#   counts the number of occurances of an element
row.append("Ford")
print(row)
print(row.count("Ford"))

# 7: Index method
#   displays the index value of an element
print(row.index("Lexus"))

# 8: Insert method
#   inserts an element at a specific index value
row.insert(2, "Kia")
print(row)


input("Press enter to exit.")
