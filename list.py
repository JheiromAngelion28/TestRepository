

numbers = [10,20,30,40,50]
print("First element:", numbers[0])
print ('Last element:', numbers[-1])

animals = ["cat","dog","bird"]
animals[2] = "snake"
print(animals)

colors = []
colors.append("Green")
colors.append("Blue")
colors.append("Yellow")
colors.append("Red")
print(colors)

names = ["Alice", "Bob", "Charlie", "Diana"]
print("length of the list", len(names))

numbers1 =  ["10","2","5","6","8"]
total_sum = sum(numbers)
print("Sum of elements:", total_sum)

ages = [ "40", "32", "45", "70m", "60",]
print("maximum age:", max(ages))
print("minimum age:", min(ages))

numbers3 = [1, 2, 3, 4, 5, 6, 7,]
if 5 in numbers:
    print("Found")
else:
    print("Not Found")


items = [1,2,3,4,5,5,5,6,6,6,7,7,7,]
count_of_7 = items.count(4)
print("Count of 4:", count_of_7)


list1 = [1,3,4,5,7,9,5,]
list2 = [2,3,7,9,6,3,5,9]

list1.extend(list2)
print(list1)

list1.reverse()
print(list1)