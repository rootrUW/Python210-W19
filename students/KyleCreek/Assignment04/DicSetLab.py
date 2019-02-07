# ----------------------------- #
# Title: Dictionary And Set Lab
# Desc: Dictionary And Set Lab Assignment for Python210
# Change Log: (Who, When, What)
# KCreek, 2/2/2019, Created Script
# ----------------------------- #
# --- Dictionaries 1 --- #
print("\n# --- Entering Dictionaries 1 --- #")
# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from
# “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)

dic1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

# Display the dictionary.
print("\nHere is the Dictionary: ", dic1)

# Delete the entry for “cake”.
del dic1["cake"]

# Display the dictionary.
print("\nHere is the Dictionary without 'cake': ", dic1)

# Add an entry for “fruit” with “Mango” and display the dictionary.
dic1["fruit"] = "Mango"
print("\nHere is the dictionary with 'fruit' added: ", dic1)

# Display the dictionary keys.
print("\n Here are the Dicitonary Keys: ")
for key in dic1.keys():
    print(key)

# Display the dictionary values.
print("\nHere are the dictionary Values: ")
for key, value in dic1.items():
    print(value)
# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
lstEmpty = []
for item in dic1.keys():
    lstEmpty.append(item)
if "cake" in lstEmpty:
    print("'cake' is a key in the dictionary")
else:
    print("'cake' is not a key in the dictionary")
# Display whether or not “Mango” is a value in the dictionary (i.e. True).
lstEmpty2 = []
for key, value in dic1.items():
    lstEmpty2.append(value)
if "Mango" in lstEmpty2:
    print("'Mango' is a value in the dictionary")
else:
    print("'Mango' is not a value in the dictionary")

# --- Dictionaries 2 --- #
print("\n# --- Entering Dictionaries 2 --- #")


# Using the dictionary from item 1: Make a dictionary using the same keys but
# with the number of ‘t’s in each value as the value (consider upper and lower case?).

def Tsort(dic1):
    """
    Function Written to create a new dictionary, replacing the input
    dictionary values with the number of 't's in the original value
    :param dic1 is an input dictionary
    :return new dicitonary with same keys and number of 't's as value
    """
    dicNew = {}
    for key, value in dic1.items():
        strValue = value.lower()
        i = 0
        for letter in strValue:
            if letter == "t":
                i += 1
        dicNew[key] = i
    return dicNew


dic2 = Tsort(dic1)
print("\nHere is the original Dictionary: ", dic1)
print("\nHere is the new Dictionary with number of t's as values: ", dic2)

# --- Sets --- #
print("\n# --- Entering Sets 1 --- #")


# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
def SetMaker(intDivisibility):
    """
    Function Written to create sets for Set Lab
    :param intDivisibility is the integer the values must be divisible by
    :return a set of numbers between 0 & 20 divisble by provided value
    """
    s = set()
    for i in range(0, 21):
        if i % intDivisibility == 0:
            s.update([i])
    return s


s2 = SetMaker(2)
s3 = SetMaker(3)
s4 = SetMaker(4)

# Display the sets.
print("\nHere are the sets:")
print("\ns2", s2, "\ns3", s3, "\ns4", s4)

# Display if s3 is a subset of s2 (False) and if s4 is a subset of s2 (True).
print("\nIs s3 a subset of s2?", s3.issubset(s2))
print("\nIs s4 a subset of s2?", s4.issubset(s2))

# --- Sets 2 --- #
print("\n# --- Entering Sets 2 --- #")
# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
s = set('Python')
print("\nHere is the original set: ", s)

s.add('i')
print("\nHere is the Updated set with the addition of 'i': ", s)

# Create a frozenset with the letters in ‘marathon’.
s2 = frozenset("Marathon")
print("\nHere is the Frozen Set: ", s2)

# display the union and intersection of the two sets.
union = s2.union(s)
print("\n Here is the union of the Set and Frozen Set: ", union)

intersection = s2.intersection(s)
print("\nHere is the intersection between the set and Frozen Set: ", intersection)