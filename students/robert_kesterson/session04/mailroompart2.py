#!/usr/bin/env python3

# -------------------------------------------- #
# Title: Lesson 04 Assignment: Mailroom, Part 2
# Desc: Incorporate file writing and dictionary use.
# Change log: (who, when, what)
# RKesterson, 2019-01-30, Created file
# RKestesron, 2019-02-05, Stubbed out methods / parts
# RKestesron, 2019-02-05, Updated code to use a dict to switch between the user’s selections
# RKestesron, 2019-02-05, Converted main donor data structure to be a dict
# RKestesron, 2019-02-05, Updated code to produce the letter as one big template, rather than building up a
# big string that produces the letter in parts
# RKestesron, 2019-02-05, Added "send letters to all donors" feature
# RKestesron, 2019-02-05, Updated "send letter to all donors" feature to write to files in working dir
# RKestesron, 2019-02-05, Updated "create a report" feature to work correctly
# Note - Commit to FebUpdates branch when creating pull request this week
# ---------------------------------------------- #

donationdict = {}

def load_donation_dict():
    global donationdict
    donationdict = {
        'Winston Churchill': [20, 50],
        'Hunter S. Thompson': [50, 500, 5000],
        'Richard Garfield': [300, 400],
        'Simon Illyan': [100],
        'Theodore Roosevelt': [50, 100]
    }

def send_thank_you():
    global donationdict
    tyresponse = input("Please enter a full name. list provides all names")
    while True:
        if tyresponse == "list":
            for i in donationdict.keys():
                print("{:s}".format(i))
            tyresponse = input("Please enter a full name. List provides all names")
        else:
            donation = input("Enter a donation amount")
            donation = int(donation)
            if tyresponse in donationdict.keys():
                donvalue = donationdict[tyresponse]
                donvalue.append(donation)
                donationdict[tyresponse] = donvalue
            else:
                donvalue = []
                donvalue.append(donation)
                donationdict[tyresponse] = donvalue
            print("Thank you {:s} for your generous donation of {:d} dollars".format(tyresponse, donation))
            break

def sort_key(donor):
    return donor[1]

def create_a_report():
    donationlist = []
    for i in donationdict.keys():
        donationcount = 0
        donationtotal = 0
        donationvalue = donationdict[i]
        for j in donationvalue:
            donationtotal += int(j)
            donationcount += 1
        averagedonation = donationtotal / donationcount
        tupleone = (i, donationtotal, donationcount, averagedonation)
        donationlist.append(tupleone)
    sorteddonorlist = sorted(donationlist, key=sort_key)
    sorteddonorlist.reverse()
    print("Donor Name | Total Given | Num Gifts | Average Gift")
    print("---------------------------------------------------")
    for k in sorteddonorlist:
        print("{:s} ${:d} {:d} ${:.2f}".format(k[0], k[1], k[2], k[3]))
    '''
    i = 1
    reportlist = []
    currentname = ""
    totalgiven = 0
    numberofgifts = 0
    donationlist.sort()
    # If the currentname is the empty set, we have not started to iterate yet
    for tupleobject in donationlist:
        if currentname == "":
            currentname = tupleobject[0]
            totalgiven = tupleobject[1]
            numberofgifts = 1
        # If we encounter a different name from the current name, we know we have reached a new donor
        elif currentname != tupleobject[0]:
            reporttuple = (totalgiven, currentname, numberofgifts)
            reportlist.append(reporttuple)
            currentname = tupleobject[0]
            totalgiven = tupleobject[1]
            numberofgifts = 1
        # If we encounter the same name, we want to add to the information about said donor
        else:
            totalgiven += tupleobject[1]
            numberofgifts += 1

    # Now that the tuples are totaled, we can sort and print them
    reportlist.sort()
    reportlist.reverse()
    for tupleobject in reportlist:
        print("{:s} {:d} {:d}")
    '''

def break_function():
    exit()

def send_letters_to_all_donors():
    global donationdict
    for i in donationdict.keys():
        filename = "{:s}.txt".format(i)
        outfile = open(filename, 'w')
        donationtotal = 0
        donationvalue = donationdict[i]
        for j in donationvalue:
            donationtotal += int(j)
        messagestring = "Dear {:s}, \r\n\n    Thank you for your very kind donation of ${:d}.\r\n\n    It will be put" \
                        " to very good use.\r\n\n            Sincerely,\r\n                -The Team".format(i, donationtotal)
        outfile.write(messagestring)
        outfile.close()

def load_selection_list():
    switch_function_dict = {
        '1 - Send a Thank You to a single donor.': send_thank_you,
        '2 - Create a Report.': create_a_report,
        '3 - Send letters to all donors.': send_letters_to_all_donors,
        '4 - Quit': break_function
    }
    return switch_function_dict

if __name__ == '__main__':
    switch_function_dict = load_selection_list()
    load_donation_dict()

    while True:
        print("Chose an action: \r\n")
        for i in switch_function_dict.keys():
            print("{:s}".format(i))
        response = input("")
        if response not in switch_function_dict.keys():
            print("You must chose an action from the approved list. Actions are: \r\n")
            for i in switch_function_dict.keys():
                print("{:s}".format(i))
            response = input("")
        else:
            switch_function_dict.get(response)()
