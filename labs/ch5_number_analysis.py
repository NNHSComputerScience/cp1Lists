numbers = []
for i in range(10):
    number = int(input("please enter a number: "))
    numbers.append(number)
print(numbers)

# find the lowest number in the list
lowest_num = numbers[0] # the first number is the lowest so far...
for num in numbers:
    if num < lowest_num:
        lowest_num = num
print("The lowest number is", lowest_num)