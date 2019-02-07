#!/usr/bin/env python3

# -------------------------------------------- #
# Title: Lesson 03 Exercise: Mailroom, part 1
# Desc: First major assignment
# Change log: (who, when, what)
# RKesterson, 2019-01-29, Created file
# RKestesron, 2019-01-29, Stubbed out methods / parts
# RKesterson, 2019-01-29, Started defining load_donation_list
# ---------------------------------------------- #

donationlist = []

def load_donation_list():
    global donationlist
    firstdonation = ("Winston Churchill", 2)
    donationlist.append(firstdonation)
    firstdonation = ("Winston Churchill", 20)
    donationlist.append(firstdonation)
    firstdonation = ("Hunter S. Thompson", 50)
    donationlist.append(firstdonation)
    firstdonation = ("Hunter S. Thompson", 500)
    donationlist.append(firstdonation)
    firstdonation = ("Hunter S. Thompson", 5000)
    donationlist.append(firstdonation)
    firstdonation = ("Richard Garfield", 300)
    donationlist.append(firstdonation)
    firstdonation = ("Richard Garfield", 400)
    donationlist.append(firstdonation)
    firstdonation = ("Simon Illyan", 100)
    donationlist.append(firstdonation)
    firstdonation = ("Theodore Roosevelt", 50)
    donationlist.append(firstdonation)
    firstdonation = ("Theodore Roosevelt", 100)
    donationlist.append(firstdonation)

def send_thank_you():
    global donationlist
    tyresponse = input("Please enter a full name. list provides all names")
    while True:
        if tyresponse == "list":
            donationlist.sort()
            namelist = ""
            for tupleobject in donationlist:
                if tupleobject[0] not in namelist and namelist == "":
                    namelist = namelist + "{:s}".format(tupleobject[0])
                elif tupleobject[0] not in namelist:
                    namelist = namelist + ",{:s}".format(tupleobject[0])
            print(namelist)
            tyresponse = input("Please enter a full name. List provides all names")
        else:
            donation = input("Enter a donation amount")
            donation = int(donation)
            newdonation = (tyresponse, donation)
            print("Thank you {:s} for your generous donation of {:d} dollars".format(newdonation[0], newdonation[1]))
            donationlist.append(newdonation)
            break

def create_a_report():
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


if __name__ == '__main__':
    load_donation_list()

    response = input("Choose an action: Send a Thank You, Create a Report, quit")
    while True:
        if response == "Send a Thank You":
            send_thank_you()
            response = input("Choose an action: Send a Thank You, Create a Report, quit")
        elif response == "Create a Report":
            create_a_report()
            response = input("Choose an action: Send a Thank You, Create a Report, quit")
        elif response == "quit":
            break
        else:
            response = input("You must chose an action from the approved list. Actions are: Send a Thank you, "
                             "Create a Report, quit")
