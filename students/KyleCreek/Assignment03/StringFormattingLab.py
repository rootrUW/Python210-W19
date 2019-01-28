# ----------------------------- #
# Title: StringFormattingLab.py
# Desc: String Formatting lab to Complete Assignment03 of Python 210
# Change Log: (Who, When, What)
# KCreek, 1/27/2019, Created Script
# ----------------------------- #


#-- Data --#
# Declare Variables and Constants

#-- Processing --#
# Perform Tasks

def Task1(tplInput):

    # Unpack the Tuple to variable names
    strFileName, fltTwoDecimal, intSciTwoDecimal, fltSciThreeDecimal = tplInput
    fltSciThreeDecimal = round(fltSciThreeDecimal,-2)

    return 'file_{:03d} : {:.2f}, {:.2e}, {:.2e}'.format(strFileName,fltTwoDecimal,intSciTwoDecimal,fltSciThreeDecimal)

def Task2(tplInput):
    # Unpack the Tuple to variable names
    strFileName, fltTwoDecimal, intSciTwoDecimal, fltSciThreeDecimal = tplInput
    fltSciThreeDecimal = round(fltSciThreeDecimal,-2)

    return f'file_{strFileName:03d} : {fltTwoDecimal:.2f}, {intSciTwoDecimal:.2e}, {fltSciThreeDecimal:.2e}'

def Task3(tplInput):
    intLength = len(tplInput)
    strText = "The {} numbers are: " + '{:d}, '*len(tplInput)
    return strText.format(intLength, *tplInput)

def Task4(tplInput):
    return '{:02d} {} {} {:02d} {}'.format(tplInput[3], tplInput[-1],tplInput[2],tplInput[0], tplInput[1])

def Task5_1(lstInput):

    strOrange = lstInput[0]
    strOrange = strOrange.replace("s","")
    intOrangeWeight = lstInput[1]
    strLemon = lstInput[2]
    strLemon = strLemon.replace("s","")
    intLemonWeight = lstInput[3]
    return f"the weight of an {strOrange} is {intOrangeWeight} and the weight of a {strLemon} is {intLemonWeight}"

def Task5_2(lstInput):

    strOrange = lstInput[0]
    strOrange = strOrange.replace("s","")
    intOrangeWeight = lstInput[1]
    strLemon = lstInput[2]
    strLemon = strLemon.replace("s","")
    intLemonWeight = lstInput[3]
    return f"the weight of an {strOrange.upper()} is {intOrangeWeight*1.2} and the weight of a {strLemon.upper()} is {intLemonWeight*1.2}"

def Task6(lstPeople):
    intColumnWidth = 0
    # Determine the Maximum Column Width
    for tplPerson in lstPeople:
        # Unpack Tuple into Variable Names
        name, age, cost = tplPerson
        if len(name) > intColumnWidth:
            intColumnWidth = len(name)


    # Create a Table Header
    strHeaderName = '{name:<{width}}'.format(name='Name',width=intColumnWidth)
    strHeaderAge = '{age:^{width}}'.format(age='Age',width=4)
    strHeaderCost = '{cost:>{width}}'.format(cost='Cost',width=10)
    strHeader = strHeaderName + strHeaderAge + strHeaderCost
    print(strHeader)
    print('-'*len(strHeader))

    # Create a 'for' loop to write information in Tuple into text format
    for tplPerson in lstPeople:
        name, age, cost = tplPerson
        strNameText = '{name:<{width}}'.format(name=name,width=intColumnWidth)
        strAgeText = '{age:^{width}}'.format(age=age,width=4)
        strCostText = '{cost:>{width}}'.format(cost=cost,width=10)
        strOutPut = strNameText + strAgeText + "$" +strCostText
        print(strOutPut)

# Presentation (Input/Output) --#
# Interact w/ the User

# Main
# --- Task 1 --- #

"""
Write a format string that will take the following four element tuple:
 ( 2, 123.4567, 10000, 12345.67)
 and produce:
 'file_002 :   123.46, 1.00e+04, 1.23e+04'
 """

tplTask1 = (2, 123.4567, 10000, 12345.67)
strResultTask1 = Task1(tplTask1)
print("\n--- Task 1 ---")
print("Here is the Original Tuple: ", tplTask1)
print("Here is the Altered Tuple: ", strResultTask1)


# --- Task 2 --- #


tplTask2 = (2, 123.4567, 10000, 12345.67)
strResultTask2 = Task2(tplTask2)
print("\n--- Task 2 ---")
print("Here is the Original Tuple: ", tplTask2)
print("Here is the Altered Tuple: ", strResultTask2)



# --- Task 3 --- #

"""Rewrite:
"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
to take an arbitrary number of values. """

tplTask3_1 = (1,2,3,4,5,6)
strResultTask3_1 = Task3(tplTask3_1)

tplTask3_2 = (100,77,89)
strResultTask3_2 = Task3(tplTask3_2)

print("\n--- Task 3 ---")
print("Here is the Original Tuple: ", tplTask3_1)
print("Here is the Altered Tuple: ", strResultTask3_1)

print("Here is another Original Tuple: ", tplTask3_2)
print("Here is another Altered Tuple: ", strResultTask3_2)



# --- Task 4 --- #
""" Given a 5 element tuple:
( 4, 30, 2017, 2, 27)
use string formating to print:
'02 27 2017 04 30' """

tplTask4 = (4,30,2017,2,27)
strResultTask4 = Task4(tplTask4)

print("\n--- Task 4 ---")
print("Here is the Original Tuple: ", tplTask4)
print("Here is the Altered Tuple: ", strResultTask4)

# --- Task 5 --- #

""" 
Here’s a task for you: Given the following four element list:
['oranges', 1.3, 'lemons', 1.1]
Write an f-string that will display:
The weight of an orange is 1.3 and the weight of a lemon is 1.1 """

lstTask5_1 = ['oranges', 1.3, 'lemons', 1.1]
strResultTask5_1 = Task5_1(lstTask5_1)

print("\n--- Task 5.1 ---")
print("Here is the Original Tuple: ", lstTask5_1)
print("Here is the Altered Tuple: ", strResultTask5_1)

"""Now see if you can change the f-string so that it displays the names of the fruit in upper case, 
and the weight 20% higher (that is 1.2 times higher)."""


lstTask5_2 = ['oranges', 1.3, 'lemons', 1.1]
strResultTask5_2 = Task5_2(lstTask5_2)

print("\n--- Task 5.2 ---")
print("Here is the Original Tuple: ", lstTask5_2)
print("Here is the Altered Tuple: ", strResultTask5_2)


# --- Task 6 --- #

"""Write some Python code to print a table of several rows, each with a name, an age and a cost. 
Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print 
the tuple in columns that are 5 charaters wide? It can be done on one short line!"""

lstInformation = [("Lebron James", 32, 10000000),
                  ("Kyle Creek", 27, 100000),
                  ("Homeless Andy", 40, 45),
                  ("Ruth Bader-Ginsberg", 85, 7823)]

print("\n--- Task 6 ---")
print("Here is the Original List of Information: ", lstInformation)
print("\nHere is the Resulting Table: ")
Task6(lstInformation)

