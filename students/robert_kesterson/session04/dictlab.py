#!/usr/bin/env python3

# -------------------------------------------- #
# Title: Lesson 04 Activities: Dictionary and Set Lab
# Desc: Learn the basic ins and outs of Python dictionaries and sets.
# Change log: (who, when, what)
# RKesterson, 2019-01-30, Created file
# RKestesron, 2019-01-30, Stubbed out methods / parts
# RKestesron, 2019-02-03, Completed dictionaries

# Note - Commit to FebUpdates branch when creating pull request this week
# ---------------------------------------------- #

# Dictionaries
dictOne = {
    'name': 'Chris',
    'city': 'Seattle',
    'cake': 'Chocolate'
}
for i in dictOne.keys():
    print("Key: {:s} | Value: {:s}".format(i, dictOne[i]))

del dictOne['cake']
for i in dictOne.keys():
    print("{:s}: {:s}".format(i, dictOne[i]))

dictOne['fruit'] = 'Mango'
print(dictOne.keys())
print(dictOne.values())
print('cake' in dictOne)
print('Mango' in dictOne.values())

# Dictionaries 2
dictTwo = {}
for i in dictOne:
    dictTwo[i] = dictOne[i].lower().count('t')

# Sets
s2 = set([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
s3 = set([3, 6, 9, 12, 15, 18])
s4 = set([4, 8, 12, 16, 20])

print("s2:")
for i in s2:
    print("{:d}".format(i))

print("s3:")
for i in s3:
    print("{:d}".format(i))

print("s4:")
for i in s4:
    print("{:d}".format(i))

print(s3 < s2)
print(s4 < s2)

# Sets 2
pyset = set(["p", "y", "t", "h", "o", "n"])
pyset.add("i")
froz = frozenset(["m", "a", "r", "t", "h", "o", "n"])

print(pyset.union(froz))
print(pyset.intersection(froz))