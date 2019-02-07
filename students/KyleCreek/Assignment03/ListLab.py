# ----------------------------- #
# Title: ListLab.py
# Desc: Written to Complete Assignment 03
# Change Log: (Who, When, What)
# KCreek, 1/25/2019, Created Script
# ----------------------------- #


#-- Data --#
# Declare Variables and Constants

#-- Processing --#
# Perform Tasks
def NumericInput(strMessage):
    """
    Asks the user to provide a numeric input.
    :param strMessage The message to be displayed to the user to obtain their
    desired input
    :return Numeric input provided by the user.
    """
    while True:
        try:
            userNumber = int(input(strMessage))
            if userNumber <= 0:
                print("Number must be greater than 0")
            else:
                break
        except ValueError:
            print("User Input Must be an integer")
    return userNumber


def FruitChoose(lstFruitChoices, intIndexChoice):
    """
    Function Written to return the fruit in the list based on the user choice
    :param lstFruitChoices is a list of provided fruit
    :param intIndexChoice is an integer for users index of list
    :return users desired index of list and associated fruit
    """
    if intIndexChoice > len(lstFruitChoices):
        return "Out of Index"
    else:
        return lstFruitChoices[intIndexChoice - 1]


def DoYouLike(FruitList):
    """
    """
    lstNewFruit = []
    for fruit in FruitList:
        while True:
            strQuestion = "Do you like {}? ".format(fruit)
            strUserInput = input(strQuestion).strip()
            strUserInput = strUserInput.lower()
            if strUserInput == "no":
                print("no", fruit)
                break
            elif strUserInput == "yes":
                print("yes", fruit)
                lstNewFruit.append(fruit)
                break
            else:
                print("Please answer question w/ 'yes' or 'no'")
    return lstNewFruit

# Presentation (Input/Output) --#
# Interact w/ the User

# --- Series 1 --- #

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
lstFruit = ["Apples", "Pears", "Oranges", "Peaches"]

# Display the list (plain old print() is fine…).
print(lstFruit)

# Ask the user for another fruit and add it to the end of the list.
strNewFruit = input("Please provide a new fruit: ")
lstFruit.append(strNewFruit.title())

# Display the list.
print(lstFruit)

# Ask the user for a number and display the number back to the user and
# the fruit corresponding to that number (on a 1-is-first basis).
# Remember that Python uses zero-based indexing, so you will need to correct.
intUserChoice = NumericInput("Please provide a number for Fruit in list: ")
strUserFruit = FruitChoose(lstFruit, intUserChoice)
print('Your Number is {}, the corresponding fruit is {}'.format(intUserChoice, strUserFruit))

# Add another fruit to the beginning of the list using “+” and display the list.
lstFruitAdd = ["Carrot"]
lstFruitAdd += lstFruit
print("\nHere are two lists {},{}".format(lstFruitAdd, lstFruit))
print("Here is is adding two lists using '+': ", lstFruitAdd)

# Add another fruit to the beginning of the list using insert() and display the list.
lstFruit.insert(0, "Tomato")
print("\nFruit List w/ 'insert() method: ", lstFruit)

# Display all the fruits that begin with “P”, using a for loop.
print("\nHere are all the fruits in the list that start with 'p'")
for fruit in lstFruit:
    if fruit[0].lower() == "p":
        print(fruit)

# --- Series2 --- #

# Using the list created in series 1 above:

# Display the list.
print("\nHere is the end list from Series 1: ", lstFruit)

# Remove the last fruit from the list.
del lstFruit[-1]

# Display the list.
print("\nHere is the last Element Removed", lstFruit)

# Ask the user for a fruit to delete, find it and delete it.
print("Here is your Current Fruit list: ")
for fruit in lstFruit:
    print(fruit)


strUserDelete = input("Please Determine which fruit to delete: ")
strUserDelete.strip()
strUserDelete.lower()

# Need to add function for "not in"
for fruit in lstFruit:
    if fruit.lower() == strUserDelete:
        lstFruit.remove(fruit)

print(lstFruit)

# --- Series 3 --- #

# Ask the user for input displaying a line like “Do you like apples?”
# for each fruit in the list (making the fruit all lowercase).
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, prompt the user to answer with one
# of those two values (a while loop is good here)
lstFruit = DoYouLike(lstFruit)

# Display the list.
print("\nSeries 3 Fruit List", lstFruit)

# --- Series 4 ---#
# Once more, using the list from series 1:
#
# Make a new list with the contents of the original, but with all the letters in each item reversed.
lstFruit = ["Apples", "Pears", "Oranges", "Peaches"]
lstNew = []
for fruit in lstFruit:
    strReverseWord = fruit[::-1]
    lstNew.append(strReverseWord)
print(lstNew)

# Delete the last item of the original list. Display the original list and the copy.
del lstFruit[-1]
print(lstFruit)
print(lstNew)