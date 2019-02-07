#!/usr/bin/env python3

# -------------------------------------------- #
# Title: Lesson 03 Exercise: List Lab
# Desc: This is a lab where we will learn about list manipulation
# Change log: (who, when, what)
# RKesterson, 2019-01-27, Created file
# RKestesron, 2019-01-27, Stubbed out methods / parts
# RKesterson, 2019-01-28, Completed series one (question about this to be posted to forum)
# RKesterson, 2019-01-28, Completed series two
# RKesterson, 2019-01-28, Completed series three
# RKesterson, 2019-01-28, Completed series four
# ---------------------------------------------- #

# Series one
listSeriesOne = ["Apples", "Pears", "Oranges", "Peaches"]
print(listSeriesOne)
response = input("Choose a fruit to add to the list: ")
listSeriesOne.append(response)
print(listSeriesOne)
response = input("Select a fruit by number: ")
fruitSelection = int(response)
print("Fruit number " + response + " - " + listSeriesOne[fruitSelection - 1])
listSeriesTwo = ["eggplant"]
listSeriesOne = listSeriesTwo + listSeriesOne
print(listSeriesOne)
listSeriesOne.insert(0, "Strawberries")
print(listSeriesOne)

# Series two
print(listSeriesOne)
listSeriesOne = listSeriesOne[:-1]
print(listSeriesOne)
response = input("Choose a fruit to delete from the list: ")
listSeriesOne.remove(response)
print(listSeriesOne)

# Series three
for fruit in listSeriesOne:
    response = input("Do you like " + fruit.lower() + " ? (yes / no) ")
    if response == "no":
        listSeriesOne.remove(fruit)
    while response != "yes" and response != "no":
        response = input("Answer must be \"yes\" or \"no\". Do you like " + fruit.lower() + " ? (yes / no) ")
print(listSeriesOne)

# Series four
def recursiveReverse(input):
    if len(input) == 0:
        return input
    else:
        return recursiveReverse(input[1:]) + input[0]

listSeriesFour = []
for fruit in listSeriesOne:
    listSeriesFour.append(recursiveReverse(fruit))

listSeriesOne = listSeriesOne[:-1]
print(listSeriesOne)
print(listSeriesFour)