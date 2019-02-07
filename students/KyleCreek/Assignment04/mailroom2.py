# ----------------------------- #
# Title: mailroom2.py
# Desc: Program Written to Complete Assignments of Python210
# Change Log: (Who, When, What)
# KCreek, 2/2/2019, Created Script for Part 2
# KCreek, 2/3/2019, Updated Letter Writing Template to demonstrate more
#                   Gratitude to the donors.
# ----------------------------- #


# -- Data --#
# Declare Variables and Constants

# Database list containing Tuples of donators and their associated donations.
dicDonorDB = {"William Gates, III": [653772.32, 12.17],
              "Jeff Bezos": [877.33],
              "Paul Allen": [663.23, 43.87, 1.32],
              "Mark Zuckerberg": [1663.23, 4300.87, 10432.0]}


# -- Processing --#
# Perform Tasks

# --- Main --- #
def main():
    """
    Main Program Loop
    :return:
    """
    if __name__ == '__main__':
        flag = True
    else:
        flag = False

    dicSwitchCase = {1: SendThankYouSingle,
                     2: CreateReport,
                     3: SendLettersAllDonors}
    while flag:

        # Obtain User's Choice
        intUserChoice = MenuDisplay()

        # Use Switch Statement to Call Function
        if intUserChoice <= 3:
            dicSwitchCase.get(intUserChoice)(dicDonorDB)

        # Case Statement to Exit the Program
        else:
            break


def MenuDisplay():
    """
    Function Written to Provide user with a list of mail room options
    and return their option for subsequent case statements
    :return: User Choice from the menu of options
    """
    print("""
    Please Choose from the Available Options:
    1: Send a Thank You to a Single Donor
    2: Create a Report
    3: Send Letters to ALL Donors
    4: Quit""")

    # 'While' loop queries user until the program is provided with an acceptable input.
    while True:
        try:
            intMenuChoice = int(input("\nChoose Option Here: "))
            if intMenuChoice < 1 or intMenuChoice > 4:
                print("That is our of Range, Please Try Again")
            else:
                return intMenuChoice

        except ValueError:
            print("That is not an acceptable input")


def DonorNameInput():
    """
    """
    strDonorName = input('''Please Provide Donor Full Name, or 'list' to display all donors: 
''').strip()
    strDonorName = strDonorName.strip()
    strDonorName = strDonorName.title()
    return strDonorName


# --- Case Statement 1 --- #
def StringFormatter(strText):
    """
    Function Written to format strings for processing
    """
    import string

    # Strip Punctuation
    for c in string.punctuation:
        strText = strText.replace(c, "")
    # Strip White Space
    strText = strText.strip()
    # Make Name a title
    strText = strText.lower()
    return strText


def DonorListView(dicDonorDB):
    """
    Function Written to print the list of Donors in the donor database
    to the screen
    :param dicDonorDB is a Dictionary containing the donors information
    :return prints the list of Donors to the screen
    """
    # 'for' loop printing each of the items in the provided list
    for key, value in dicDonorDB.items():
        print(key)


def CheckDonor(strDonorName, dicDonorDB):
    """
    Function Written to Determine if the donor provided is currently in donor Database
    :param strDonorName: Donor Name provided by the user
    :param lstDonors: Dictionary containing Donors Information
    :return:
    """
    import string

    strDonorNameCheck = StringFormatter(strDonorName)
    # ---  Extract Donor Names from Database --- #
    # 'for' loop to evaluate the keys of the dictionary
    for strName in dicDonorDB.keys():
        # Format the name to remove punctuation and make all lower case
        strDBNameCheck = StringFormatter(strName)
        if strDBNameCheck == strDonorNameCheck:
            print("This name is in the DataBase")
            # Note, This will return the Key to the dictionary
            return strName, dicDonorDB
    else:
        print("This is not in the database")
        # Note, This wil return the new Key Entry
        dicDonorDB[strDonorName.title()] = []
        return strDonorName.title(), dicDonorDB


def AddDonation(strDonorName, dicDonorDB):
    """
    Function Written to add donation to the Donors history
    :param strDonotName
    :param dicDonorDB
    :return:
    """
    # 'while' loop continuously queries users for information until an acceptable response
    # has been obtained
    while True:
        try:
            fltDonationAmount = float(input("Provide amount Donated: "))
            break
        except ValueError:
            print("That is not an acceptable input, please try again")

    dicDonorDB[strDonorName] += [fltDonationAmount]

    return dicDonorDB


def SendThankYouSingle(dicDonorDB):
    """
    Function written to process donors and send thank you letters for
    Their donations.
    :param dicDonorDB is a Dictionary containing Donors and their data
    :return: Returns a thank you note to the user.
    """
    import string

    while True:

        strDonorName = DonorNameInput()

        if strDonorName == 'List':
            # Lists the Donors in the Donor Database to the Screen
            DonorListView(dicDonorDB)
        else:
            # Determine if donor is in database, otherwise create
            # New Donor and update database
            strDonorName, dicDonorDB = CheckDonor(strDonorName, dicDonorDB)

            # Adds the Donors contribution to their history
            dicDonorDB = AddDonation(strDonorName, dicDonorDB)

            # Prints a Thank you note to the Donor for their contribution
            # PrintThankYou(tplDonor,fltDonationAmount)
            PrintThankYou(strDonorName, dicDonorDB)

            break


def PrintThankYou(strDonorName, dicDonorDB):
    '''
    Function Written to take the Name of the donor and their donation
    amount and returns a print statement thanking the donor.
    :param strDonorName is a string of the Donor's Name
    :param dicDonorDB is the Dictionary of all donors.
    :return: Print a thank you letter to the screen
    '''
    lstDonations = dicDonorDB[strDonorName]
    strRecentDonation = lstDonations[-1]
    strThankYouText = 'Dear {},\nThank you for your kind donation of ${}. ' \
                      'With help of your donation a poor Engineer at Boeing ' \
                      'will be able to pass Python 210 and continue' \
                      'to persue their dream of becoming dirty rich.' \
                      'Thank you!'.format(strDonorName, strRecentDonation)

    print(strThankYouText)


# --- Case Statement 2 --- #
def FloatFormatter(intFloat):
    """
    Function Written to format floating points into 2 decimal strings
    :param intFloat: floating point integer
    :return: String of Floating Point to two decimals
    """
    return '{0:.2f}'.format(intFloat)


def ReportInformation(strDonorName, dicDonorDB):
    """ Function Written to obtain donors statistics based on donations

    :param dicDonorDB is a Database containing all Donors and their information
    :param strDonorName is the name of the donor in the database
    :return Gift Total Amount, Number of Gifts, and Average Gift Cost in two decimal strings"""

    fltGiftTotal = 0
    lstDonations = dicDonorDB.get(strDonorName)

    # Calculate gift total by summing list
    for donation in lstDonations:
        fltGiftTotal += donation
    strGiftTotal = FloatFormatter(fltGiftTotal)

    # Calculate the number of donations given
    fltNumGift = len(lstDonations)

    strNumGift = str(fltNumGift)

    # Calculate the average cost per donation
    try:
        fltAverageGift = fltGiftTotal / fltNumGift
    except ZeroDivisionError:
        fltAverageGift = 0

    strAverageGift = FloatFormatter(fltAverageGift)

    return strGiftTotal, strNumGift, strAverageGift


def CreateReport(dicDonorDB):
    """
    Function Written to Create Report of Donors
    :param dicDonorDB is a dictionary containing all donors and their donations
    :return: prints report of donor information to the screen
    """
    intColumnWidth = 0
    # Determine the Maximum Column Width
    for person in dicDonorDB.keys():
        if len(person) > intColumnWidth:
            intColumnWidth = len(person)

    # Create a Table Header
    strHeaderName = '{name:<{width}}'.format(name='Donor Name', width=intColumnWidth + 5)
    strHeaderAmtGiven = '{name:>{width}}'.format(name='Total Given', width=15)
    strHeaderNumGift = '{name:>{width}}'.format(name='Num Gifts', width=15)
    strHeaderAvgGift = '{name:>{width}}'.format(name='AVG Gift', width=12)
    strHeader = strHeaderName + strHeaderAmtGiven + strHeaderNumGift + strHeaderAvgGift
    print(strHeader)
    print('-' * (len(strHeader) + 5))

    # Create a 'for' loop to write information in dictionary into text format
    for person in dicDonorDB.keys():
        strGiftTotal, strNumGift, strAverageGift = ReportInformation(person, dicDonorDB)
        strNameText = '{name:<{width}}'.format(name=person, width=intColumnWidth + 5)
        strTotalGiven = '${total:>{width}}'.format(total=strGiftTotal, width=15)
        strNumGift = '{num:^{width}}'.format(num=strNumGift, width=15)
        strAvgGift = '${avg:>{width}}'.format(avg=strAverageGift, width=12)

        strOutPut = strNameText + strTotalGiven + strNumGift + strAvgGift
        print(strOutPut)


# --- Case Statement 3 --- #
def FileNameFormatter(strText):
    """
    Function written to create text for a file name
    :param strText: input string of text
    :return: returns the text with all special characters stripped + '.txt'
    """
    import string
    # Strip text of punctuation
    for c in string.punctuation:
        strText = strText.replace(c, "")
    # Strip WhiteSpaces from FileName
    if " " in strText:
        strText = strText.replace(" ", "_") + ".txt"
    return strText


def SendLettersAllDonors(dicDonorDB):
    """
    Function Written to send All Donors Thank you letters
    :param dicDonorDB: Dictionary containing all Donors Information
    :return: Saves Thank you letters to all donors in database to file.
    """
    for person, donations in dicDonorDB.items():
        # Create File Name
        strFileName = FileNameFormatter(person)
        strFileText = LetterTemplate(person, donations)

        # Write Letter to text file
        with open(strFileName, 'w') as f:
            f.write(strFileText)
            f.close()


def FormatAlign(strAlignment, strText, intWidth=100):
    """
    Function Written to center Align text in Letter Template
    :param strText is a string of text
    :return The same line of text, but center aligned
    """
    return '{strText:{strAlignment}{intWidth}}'.format(strText=strText, strAlignment=strAlignment, intWidth=intWidth)


def LetterTemplate(strDonorName, lstDonations):
    """
    Function written to creat template letter to donors
    :param dicDonorDB is a database containing donors and their donation amounts
    :return a string of text displaying gratification.
    """
    strNumGift = ''
    strGiftAverage = ''
    # Text for greeting
    strGreeting = "Dear {},\n".format(strDonorName)
    strGreeting = FormatAlign('<', strGreeting)

    # Text for most Recent donation
    strBodyText1 = "Thank you for your very generous Donoation of {intDonation:.2f}".format(
        intDonation=lstDonations[-1])
    strBodyText1 = FormatAlign("^", strBodyText1)

    # Calculate Donation Information
    strNumGift = FloatFormatter(len(lstDonations))
    intGiftTotal = 0
    for donation in lstDonations:
        intGiftTotal += donation
    strGiftTotal = FloatFormatter(intGiftTotal)
    strGiftAverage = FloatFormatter((intGiftTotal / len(lstDonations)))

    # Build Transition Text
    strBodyText2 = "Since we're on the topic of giving, lets talk about your entire history donating with us!"
    strBodyText2 = FormatAlign('^', strBodyText2)

    # Stats
    strBodyText3 = "You have donated {} number of gifts for a total of ${} and average of ${}".format(strNumGift,
                                                                                                      strGiftTotal,
                                                                                                      strGiftAverage)
    strBodyText3 = FormatAlign("^", strBodyText3)

    # Talk about Giving Habits
    if intGiftTotal < 100 and len(lstDonations) < 2:
        strBodyText4 = "Those are pretty pathetic donations, you CAN and SHOULD do better"
        strBodyText4 = FormatAlign("^", strBodyText4)
    elif intGiftTotal > 100000 and len(lstDonations) > 2:
        strBodyText4 = "Wow, you are so generous! You've donated more than most make in a year!"
        strBodyText4 = FormatAlign("^", strBodyText4)
    elif intGiftTotal > 50000 and len(lstDonations) < 2:
        strBodyText4 = "Be honest, you're rich and need a tax write off, don't mask this as charity"
        strBodytext4 = FormatAlign("^", strBodyText4)
    else:
        strBodyText4 = "We are proud of your average work and appreciate all that you can give."
        strBodyText4 = FormatAlign("^", strBodyText4)

    # Closing
    strClosing1 = "Sincerely"
    strClosing1 = "\n" + FormatAlign(">", strClosing1, 75)

    strClosing2 = "-The Team"
    strClosing2 = "\n" + FormatAlign(">", strClosing2, 80)

    # Join text and maintain formatting
    lstOutPut = [strGreeting, strBodyText1, strBodyText2, strBodyText3, strBodyText4, strClosing1, strClosing2]
    r = "\n"
    r = r.join(lstOutPut)
    return r


# Presentation (Input/Output) --#
# Interact w/ the User
main()