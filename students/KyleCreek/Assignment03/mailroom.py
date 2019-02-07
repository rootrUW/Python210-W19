# ----------------------------- #
# Title: mailroom.py
# Desc: Program Written to Complete Assignments of Python210
# Change Log: (Who, When, What)
# KCreek, 1/27/2019, Created Script for Part 1
# KCreek, 1/28/2019, Added DatabaseUpdate Function
# ----------------------------- #


#-- Data --#
# Declare Variables and Constants

# Database list containing Tuples of donators and thei associated donations.

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])]

#-- Processing --#
# Perform Tasks

def MenuDisplay():
    """
    Function Written to Provide user with a list of mail room options
    and return their option for subsequent case statements
    :return: User Choice from the menu of options
    """
    print("""
    Please Choose from the Available Options:
    1: Send a Thank You
    2. Create a Report
    3. Quit""")

    # 'While' loop queries user until the program is provided with an acceptable input.
    while True:
        try:
            intMenuChoice = int(input("\nChoose Option Here: "))
            if intMenuChoice < 1 or intMenuChoice > 3:
                print("That is our of Range, Please Try Again")
            else:
                return intMenuChoice

        except ValueError:
            print("That is not an acceptable input")

def DonorListView(lstDonors):
    """
    Function Written to print the list of Donors in the donor database
    to the screen
    :param lstDonors is a list containing the donors information
    :return prints the list of Donors to the screen
    """
    # 'for' loop printing each of the items in the provided list
    for name in lstDonors:
        print(name[0])

def CheckDonor(strDonorName,lstDonors):
    """
    Function Written to Determine if the donor provided is currently in donor Database
    :param strDonorName: Donor Name provided by the user
    :param lstDonors: List containing information about donors currently stored in a database
    :return: Returns a tuple for the provided user and updated list of donor information
    """
    # Split the user provided name into a list
    lstDonorName = strDonorName.split(" ")

    # 'for' loop to check if the provided name is in the donor database
    while True:
        for tplDonor in lstDonors:
            # Create a string from the Tuple in the Donor Database
            strDonorDB = tplDonor[0]
            # Create a list from the string of the Donor in the Donors Database
            lstDonorDB = strDonorDB.split(" ")
            if ',' in lstDonorDB[1]:
                lstDonorDB[1] = lstDonorDB[1].replace(",","")
            if ',' in lstDonorName[1]:
                lstDonorName[1] = lstDonorName[1].replace(",","")
            # Checks to ensure the provided name matches the first and last name from the data base
            if lstDonorName[0] == lstDonorDB[0] and lstDonorName[1] == lstDonorDB[1]:
                print("This Donor is already in the DataBase")
                # Returns the donor's tuple information and the list without any revisions
                return tplDonor,lstDonors
        else:
            print("This is a new Donor")
            # Create new tuple for new donor
            tplNewDonor = (strDonorName,[])
            # Append database to include new donor
            lstDonors.append(tplNewDonor)
            # Return the new tuple information and a revised list.
            return tplNewDonor,lstDonors

def DonationAmount():
    """
    Function Written to query for Donation amount provided by Donor
    :return  Returns the amount of money Donated by Donor
    """
    # 'while' loop continuously queries users for information until an acceptable response
    # has been obtained
    while True:
        try:
            fltDonationAmount = float(input("Provide amount Donated: "))
            return fltDonationAmount
        except ValueError:
            print("That is not an acceptable input, please try again")

def AddDonation(tplDonor,fltDonationAmount):
    """
    Function Written to add donation to the Donors history
    :param tplDonor: Tuple containing the donors information
    :param fltDonationAmount: amount of money being donated by donor
    :return: New Tuple with appended user information
    """
    # Empty list to store the donors donations
    lstDonations = []

    # 'for' loop to handle each item in the current tuples list
    for item in tplDonor[1]:
        # Appends the current information to the new empty list
        lstDonations.append(item)
    # Appends the new donation amount to the donations list
    lstDonations.append(fltDonationAmount)
    return (tplDonor[0], lstDonations)

def PrintThankYou(tplDonor, fltDonationAmount):
    '''
    Function Written to take the Name of the donor and their donation
    amount and returns a print statement thanking the donor.
    :param tplDonor: Tuple containing the Donors information
    :param fltDonationAmount: Amount the donor is donating.
    :return: Print a thank you letter to the screen
    '''
    strThankYouText = 'Dear {},\nThank you for your kind donation of ${}. ' \
                      'With help of your donation a poor Engineer at Boeing ' \
                      'will be able to pass Python 210 and continue' \
                      'to persue their dream of becoming dirty rich.' \
                      'Thank you!'.format(tplDonor[0], fltDonationAmount)

    print(strThankYouText)

def SendThankYou(lstDonors):
    """
    Function written to process donors and send thank you letters for
    Their donations.
    :param lstDonors: List conataining all the donor information
    :return: Returns a thank you note to the user.
    """
    while True:

        strDonorName = input('''Please Provide Donor Full Name, or 'list' to display all donors: ''').strip()
        strDonorName = strDonorName.title()

        if strDonorName == 'List':
            # Lists the Donors in the Donor Database to the Screen
            DonorListView(lstDonors)
        else:
            # Determine if donor is in database, otherwise create
            # New Donor
            tplDonor,lstDonors = CheckDonor(strDonorName,donor_db)

            # Obtain the Donors Donation Amount
            fltDonationAmount = DonationAmount()

            # Adds the Donors contribution to their history
            tplDonor = AddDonation(tplDonor,fltDonationAmount)

            # Updates the provided list with updated donor information
            lstNewDatabase = DatabaseUpdate(donor_db,tplDonor)


            # Prints a Thank you note to the Donor for their contribution
            PrintThankYou(tplDonor,fltDonationAmount)

            break

def DatabaseUpdate(donor_db, tplNewDonorInfo):
    """
    Function Written to Update Donor Databased once a donation has occurred
    :param donor_db: Database of original donor information
    :param tplNewDonorInfo:  New Tuple being added to the list
    :return: Updated list of donor information
    """
    # Unpack New Donor Tuple and split on Space
    strDonorName, lstNewDonation = tplNewDonorInfo
    if "," in strDonorName:
        strDonorName.replace(",","")
    lstDonorName = strDonorName.split(" ")

    for tpl in donor_db:
        # Unpack Tuple, split on space, remove comma
        strName, lstDonations = tpl
        if "," in strName:
            strName = strName.replace(",","")
        lstNameDB = strName.split(" ")
        # Check list to see if first and last match, if they do, the old tiple is replaced
        # with the new tuple in the list
        if lstDonorName[0] == lstNameDB[0] and lstDonorName[1] == lstNameDB[1]:
            # Removes the old tuple of donor information and replaces it with a new one
            donor_db.remove(tpl)
            donor_db.append(tplNewDonorInfo)

    return donor_db

def ReportInformation(lstDonations):
    """ Function Written to obtain donors statistics based on donations
    :param lstDonations: List containing all donor information
    :return Gift Total Amount, Number of Gifts, and Average Gift Cost"""

    fltGiftTotal = 0
    # Calculate gift total by summing list
    for donation in lstDonations:
        fltGiftTotal += donation

    fltNumGift = len(lstDonations)
    try:
        fltAverageGift = fltGiftTotal / fltNumGift
    except ZeroDivisionError:
        fltAverageGift = 0
    return fltGiftTotal, fltNumGift, fltAverageGift

def CreateReport(lstPeople):

    """
    Function Written to Create Report of Donors
    :param lstPeople: list containing donor information
    :return: prints report of donor information to the screen
    """
    intColumnWidth = 0
    # Determine the Maximum Column Width
    for tplPerson in lstPeople:
        # Unpack Tuple into Variable Names
        strName, lstDonation = tplPerson
        if len(strName) > intColumnWidth:
            intColumnWidth = len(strName)


    # Create a Table Header
    strHeaderName = '{name:<{width}}'.format(name='Donor Name',width=intColumnWidth+5)
    strHeaderAmtGiven = '{name:>{width}}'.format(name='Total Given', width=15)
    strHeaderNumGift = '{name:>{width}}'.format(name='Num Gifts', width=15)
    strHeaderAvgGift = '{name:>{width}}'.format(name='AVG Gift', width=12)
    strHeader = strHeaderName +strHeaderAmtGiven + strHeaderNumGift + strHeaderAvgGift
    print(strHeader)
    print('-'*(len(strHeader)+5))

    # Create a 'for' loop to write information in Tuple into text format
    for tplPerson in lstPeople:
        strName, lstDonation = tplPerson
        fltGiftTotal, fltNumGift, fltAverageGift = ReportInformation(lstDonation)
        strNameText = '{name:<{width}}'.format(name=strName,width=intColumnWidth+5)
        strTotalGiven = '${total:>{width}.2f}'.format(total=fltGiftTotal,width=15)
        strNumGift = '{num:^{width}}'.format(num=fltNumGift,width=15)
        strAvgGift = '${avg:>{width}.2f}'.format(avg=fltAverageGift,width=12)

        strOutPut = strNameText + strTotalGiven + strNumGift + strAvgGift
        print(strOutPut)

def main():
    """
    Main Program Loop
    :return:
    """
    if __name__ == '__main__':
        flag = True
    else:
        flag = False


    while flag:

        intUserChoice = MenuDisplay()

        # Case Statement to Send a Thank You Note
        if intUserChoice == 1:
            SendThankYou(donor_db)

        # Case Statement to Create a Report
        elif intUserChoice == 2:
            CreateReport(donor_db)

        # Case Statement to Exit the Program
        else:
            break

# Presentation (Input/Output) --#
# Interact w/ the User

main()

