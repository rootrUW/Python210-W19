# ----------------------------- #
# Title: Trigram
# Desc: Trigram Assignment for Python 210 Lesson04
# Change Log: (Who, When, What)
# KCreek, 2/1/2019, Created Script
# ----------------------------- #


#-- Data --#
# Declare Variables and Constants


strFileName = "sherlock_small.txt"
#strFileName = "sherlock.txt"

#-- Processing --#
# Perform Tasks

def RemovePunctuation(strText):
    """
    Function Written to remove punctuation from text
    :param strText: Input of a String of Text
    :return: Returns string without punctuation involved
    """
    # Imports String module
    import string
    # Create an empty string to return
    strReturn = ''
    # 'for' loop to parse between each letter in text and re-create string, so long as there is no punctuation
    for letter in strText:
        # 'if" statement replacing the punctuation with a space if it is in the punctuation library
        if letter in string.punctuation:
            strReturn += " "
        # 'if' statement to check if the punctuation is NOT in the library, adds it to the string
        elif letter not in string.punctuation:
            strReturn += letter
    return strReturn

def File2Text(strFileName):
    """
    Function Written to take in a file and return the text
    :param strFileName: File name in the form of a string
    :return:
    """
    import string
    # Create an empty list
    lstText = []
    # Create a file object based on the file name
    fileOBJ = open(strFileName,'r')
    # 'for' loop to handle the lines of text being passed to the function
    for line in fileOBJ:
        # Passes Each line to the Remove Punctuation Function to remove all punctuation
        line = RemovePunctuation(line)
        # Split line at the space between words
        line = line.split(" ")
        # 'for' loop to handle each line in the fileOBJ
        for word in line:
            # Strips the word of any whitespace
            word = word.strip()
            # Ensures not to add extra whitespace where character is a space
            if len(word) == 1:
                lstText.append(word)
            elif word == "":
                continue
            # Appends the list to add the word without whitespaces or punctuation
            else:
                word = word.lower()
                lstText.append(word)

    return lstText

def TriGramDictionary(lstWords):
    """
    Takes a list of words and places them into a dictionary w/ the Tuple as
    the Key and the value as the following word
    :param List of words to be extracted
    """
    # Create an Empty Dictionary to store data
    dicWords = {}
    # Create a Counter for words in list
    counter = 0

    if len(lstWords) < 3:
        print("There are not enough words")
    else:
        # While Loop based on length of words in list
        while counter < (len(lstWords) - 2):
            # Place the Words into Tuple:
            tplNew = (lstWords[counter], lstWords[(counter + 1)])

            # Case Statement where Key already exists in dictionary.
            if tplNew in dicWords.keys():
                dicWords[tplNew].append(lstWords[counter + 2])
                counter += 1
            # Case Statement where Key Does not exist
            else:
                lstNew = []
                lstNew.append(lstWords[counter + 2])
                dicWords[tplNew] = lstNew
                counter += 1
    return dicWords

def RandomWordChooser(lstWords, dicWords):
    """
    :return Returns a value from a provided dictionary using random keys.
    * Change Variable Names *
    """
    import random

    # Extract Available Keys from dictionary and store in a list
    lstKeys = []
    for key in dicWords.keys():
        lstKeys.append(key)

    # Create a Random Tuple Key
    tplRandomKey = random.choice(lstKeys)

    # Acess the words out based on the random key
    lstWordsOut = dicWords[tplRandomKey]

    # Return Random Word if the key has more than 1 value in the list.
    if len(lstWordsOut) > 0:
        # Create a random index to choose from based on the list of options
        intIndex = random.randint(0, (len(lstWordsOut) - 1))
        return lstWordsOut[intIndex]
    else:
        # Return the only word in the list of words
        return lstWordsOut[0]

def TriGramCreator(dicWords, lstWords, intTrigramLength=100):
    """
    Function Written to create a Trigram to complete Assignment 04
    :param dicWords: Dicitonary containing Key Value Pairings of words in a file
    :param lstWords: List of words within the file of text
    :param intTrigramLength: Number of words users want to include in the trigram text.
    :return: String out put of completed Trigram.
    """
    # Empty Counter and string to control actions and add to output
    counter = 0
    strOutPut = ''

    # 'While' loop to control additions based on users desired trigram word count
    while counter < intTrigramLength:
        # Case Statement to handle first word in the string
        if len(strOutPut) == 0:
            strOutPut += (RandomWordChooser(lstWords, dicWords).title() + " ")
            counter += 1
        # Case statement to handle all words in trigram that are not the first word
        elif len(strOutPut) > 1 and counter < len(strOutPut):
            strOutPut += (RandomWordChooser(lstWords, dicWords) + " ")
            counter += 1
    return strOutPut + "."

def main(strFileName):
    """
    Function to Create Trigrams
    :param strFileName: String of file Name
    :return: Prints Trigram to the screen
    """
    # Creates a list of words from the provided file
    lstFileText = File2Text(strFileName)
    print("Here is a list of all the text in the file", lstFileText)

    # Creates a dictionary based on the list of words from the file
    dicWords = TriGramDictionary(lstFileText)
    print("Here are all the dictionary words",dicWords)

    # Create a TriGram
    strTriGram = TriGramCreator(dicWords, lstFileText)

    # Print the Tri-Gram to the Screen
    print(strTriGram)

# Presentation (Input/Output) --#
# Interact w/ the User

main(strFileName)
