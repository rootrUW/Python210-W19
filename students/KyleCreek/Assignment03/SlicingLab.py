
# ----------------------------- #
# Title: SlicingLab.py
# Desc: Slicing lab to Complete Assignment03 of Python210
# Change Log: (Who, When, What)
# KCreek, 1/27/2019, Created Script
# ----------------------------- #


# -- Data --#
# Declare Variables and Constants

# Word that will be tested with all the functions required in the Assignment
a_string = 'This is a string'
a_tuple = (2, 54, 13, 12, 5, 32)

a_string2 ='aaaabcbcbcbcbcbcbcbbdddd'
a_tuple2 = (1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 ,18 ,19 ,20)

a_string3_1 = '123456789'
a_string3_2 = '123456789AB'

a_tuple3_1 = (1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9)
a_tuple3_2 = (1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11)

# -- Processing --#
# Perform Tasks

""" Write some functions that take a sequence as an argument, and return a copy of that sequence: """

""" With the first and last items exchanged. """
def FirstLast(dataInput):
    # Swaps First & Last for String Inputs
    if type(dataInput) == str:
        return dataInput[-1] + dataInput[1:-1] + dataInput[0]

    # Swaps First & Last for Tuple Data Types
    elif type(dataInput) == tuple:
        tplnew = (dataInput[-1]),
        for tpl in dataInput[1:-1]:
            tplnew += (tpl),
        tplnew += (dataInput[0]),
        return tplnew



""" With every other item removed. """
def EveryOtherItem(dataInput):

    # Every Other item for String Object 
    if type(dataInput) == str:
        n = 0
        newString = ""
        while n < len(dataInput):
            if n % 2 == 0:
                newString += dataInput[n]
                n += 1
            else:
                n += 1
        return newString

    # Everyother for Tuple Data Type
    elif type(dataInput) == tuple:
        n = 0
        tplNew = ()
        for data in dataInput:
            if n % 2 == 0:
                tplNew += (data),
                n += 1
            else:
                n += 1
        return tplNew


# test = EveryOtherItem(a_tuple)
# print(test)


""" With the first 4 and the last 4 items removed, and then every other item in the remaining sequence. """


def First4Last4(dataInput):
    # If block for String Input
    if type(dataInput) == str:
        strNew = dataInput[4:-4]
        print("This is the string less the first 4 and last 4", strNew)
        strNew = EveryOtherItem(strNew)
        print("Now Every Other Item has been Removed", strNew)
        return strNew

    # If block for tuple input
    elif type(dataInput) == tuple:
        tplNew = ()
        for item in dataInput[4:-4]:
            tplNew += (item),
        print("This is the Tuple less first and last 4", tplNew)
        tplNew = EveryOtherItem(tplNew)
        print("Now Every Other Item has been Removed", tplNew)
        return tplNew


""" With the elements reversed (just with slicing). """
def Reversed(dataInput):
    return dataInput[::-1]


""" With the last third, then first third, then the middle third in the new order. """

def Thirds(dataInput):

    if type(dataInput) == str:
        # Case Statement where string is Divisble by 3
        if len(dataInput) % 3 == 0:
            n = 0
            strFirst =''
            strSecond = ''
            strThird = ''
            intSlice = len(dataInput) / 3
            while n < intSlice:
                strFirst += dataInput[n]
                n += 1
            while n >= intSlice and n < 2 * intSlice:
                strSecond += dataInput[n]
                n += 1
            while n >= 2 * intSlice and n < len(dataInput):
                strThird += dataInput[n]
                n += 1
            return strThird + strFirst + strSecond
        # Case Statement Where String is NOT Divisible by 3
        else:
            n = 0
            strFirst = ''
            strSecond = ''
            strThird = ''
            intSlice = round(len(dataInput) / 3)
            while n < intSlice:
                strFirst += dataInput[n]
                n += 1
            while n >= intSlice and n < 2 * intSlice:
                strSecond += dataInput[n]
                n += 1
            while n >= 2 * intSlice and n < len(dataInput):
                strThird += dataInput[n]
                n += 1
            return strThird + strFirst + strSecond
    # Case Statement where tuple length is divisible by 3
    if type(dataInput) == tuple:
        if len(dataInput) % 3 == 0:
            n = 0
            tplFirst = ()
            tplSecond = ()
            tplThird = ()
            intSlice = len(dataInput) / 3
            while n < intSlice:
                tplFirst += (dataInput[n]),
                n += 1
            while n >= intSlice and n < 2 * intSlice:
                tplSecond += (dataInput[n]),
                n += 1
            while n >= 2 * intSlice and n < len(dataInput):
                tplThird += (dataInput[n]),
                n += 1
            return tplThird + tplFirst + tplSecond
        # Case Statment where tuple length is NOT divisible by 3.
        else:
            n = 0
            tplFirst = ()
            tplSecond = ()
            tplThird = ()
            intSlice = round(len(dataInput) / 3)
            while n < intSlice:
                tplFirst += (dataInput[n]),
                n += 1
            while n >= intSlice and n < 2 * intSlice:
                tplSecond += (dataInput[n]),
                n += 1
            while n >= 2 * intSlice and n < len(dataInput):
                tplThird += (dataInput[n]),
                n += 1
            return tplThird + tplFirst + tplSecond


# Presentation (Input/Output) --#
# Interact w/ the User

# --- Main --- #
print("#--- Exchange First and Last ---#")
print("\nOriginal String: ", a_string)
strFirstLast = FirstLast(a_string)
print("Altered String: ", strFirstLast)
print("\nOriginal Tuple: ", a_tuple)
tplFirstLast = FirstLast(a_tuple)
print("Altered Tuple: ", tplFirstLast)

print("\n#--- Every Other Item Removed ---#")
print("\nOriginal String: ", a_string)
strEveryOther = EveryOtherItem(a_string)
print("Altered String: ", strEveryOther)
print("\nOriginal Tuple: ", a_tuple)
tplEveryOther = EveryOtherItem(a_tuple)
print("Altered Tuple: ", tplEveryOther)

print("\n#--- First 4, Last 4 Removed, EveryOther ---#")
print("\nOriginal String: ", a_string2)
strFirst4Last4 = First4Last4(a_string2)
print("Altered String: ", strFirst4Last4)
print("\nOriginal Tuple: ", a_tuple2)
tplFirst4Last4 = First4Last4(a_tuple2)
print("Altered Tuple: ", tplFirst4Last4)

print("\n#--- Elements Reversed ---#")
print("\nOriginal String: ", a_string)
strReverse = Reversed(a_string)
print("Altered String: ", strReverse)
print("\nOriginal Tuple: ", a_tuple)
tplReverse = Reversed(a_tuple)
print("Altered Tuple: ", tplReverse)

print("\n#--- Last, First, and Middle Third New Order ---#")
print("\nOriginal String (Divisible by 3): ", a_string3_1)
strThirds_1 = Thirds(a_string3_1)
print("Altered String(Divisible by 3): ", strThirds_1)
print("\nOriginal String (NOT Divisible by 3): ", a_string3_2)
strThirds_2 = Thirds(a_string3_2)
print("Altered String(NOT Divisible by 3): ", strThirds_2)

print("\nOriginal Tuple (Divisible by 3): ", a_tuple3_1)
tplThirds_1 = Thirds(a_tuple3_1)
print("Altered Tuple (Divisible by 3): ", tplThirds_1)

print("\nOriginal Tuple (NOT Divisible by 3): ", a_tuple3_2)
tplThirds_2 = Thirds(a_tuple3_2)
print("Altered Tuple (NOT Divisible by 3): ", tplThirds_2)
