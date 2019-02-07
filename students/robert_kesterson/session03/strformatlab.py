#!/usr/bin/env python3

# -------------------------------------------- #
# Title: Lesson 03 Exercise: String formatting lab
# Desc: This is a lab where we will learn about string formatting in Python
# Change log: (who, when, what)
# RKesterson, 2019-01-28, Created file
# RKestesron, 2019-01-28, Stubbed out methods / parts
# RKesterson, 2019-01-28, Completed task one
# RKesterson, 2019-01-28, Started task two
# RKesterson, 2019-01-28, Completed task three
# RKesterson, 2019-01-28, Completed task four
# RKesterson, 2019-01-28, Completed task five
# RKesterson, 2019-01-28, Started task six
# ---------------------------------------------- #

# Task one
'''
Method definition erroneously added below
def formatFunction(x):
    filenumber = x[0]
    filename = ""
    if filenumber < 10:
        filename = "file00{:d}".format(filenumber)
    elif 10 <= filenumber < 100:
        filename = "file0{:d}".format(filenumber)
    else:
        filename = "file{:d}".format(filenumber)
    print(filename)
    firstnumber = '%.2f' % x[1]
    print(firstnumber)
    secondnumber = "{:.2e}".format(x[2])
    print(secondnumber)
    thirdnumber = "{:.2e}".format(x[3])
    print(thirdnumber)
'''
tupleOne = (2, 123.4567, 10000, 12345.67)
formatString = "file00{:d} {:.2f} {:.2e} {:.2e}".format(tupleOne[0], tupleOne[1], tupleOne[2], tupleOne[3])
#print(formatString)

# Task two
# Will return

# Task three
def formatmethod(input_tuple):
    setlength = len(t)
    # return ", ".join(["{}"] * setlength).format(*input_tuple)
    # return "the {} elements are: ".format(setlength)
    return ("the {} elements are: " + ", ".join(["{}"] * setlength)).format(setlength, *input_tuple)

t = (1, 2, 3, 4, 5, 7)
#print(formatmethod(t))

# Task four
tupleFour = (4, 30, 2017, 2, 27)
stringFour = ("0{} {} {} 0{} {}").format(tupleFour[3], tupleFour[4], tupleFour[2], tupleFour[0], tupleFour[1])
#print(stringFour)

# '02 27 2017 04 30'

# Task five
tupleFive = ['oranges', 1.3, 'lemons', 1.1]
firstFruit = tupleFive[0]
firstFruit = firstFruit[:-1]
firstWeight = tupleFive[1]
secondFruit = tupleFive[2]
secondFruit = secondFruit[:-1]
secondWeight = tupleFive[3]
print(f"The weight of an {firstFruit} is {firstWeight} and the weight of a {secondFruit} is {secondWeight}")

print(f"The weight of an {firstFruit.upper()} is {firstWeight * 1.2} and the weight of a {secondFruit.upper()} is {secondWeight * 1.2}")
# The weight of an orange is 1.3 and the weight of a lemon is 1.1

# Task six
# Will return