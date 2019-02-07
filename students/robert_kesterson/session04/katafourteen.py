#!/usr/bin/env python3

# -------------------------------------------- #
# Title: Lesson 04 Assignment: Kata Fourteen: Tom Swift Under Milk Wood
# Desc: Trigrams can be used to mutate text into new, surreal, forms. But what heuristics do we apply to get a
# reasonable result?
# Change log: (who, when, what)
# RKesterson, 2019-01-30, Created file
# RKestesron, 2019-02-05, Stubbed out methods / parts
# RKestesron, 2019-02-05, Completed katafourteen.py

# Note - Commit to FebUpdates branch when creating pull request this week
# ---------------------------------------------- #

import random

# For this function, we want to read in the data and strip out different characters
def read_in_data(filename):
    in_data = ""
    fileStart = False
    fileEnd = False
    for line in open(filename):
        if line.startswith("*** END OF THIS PROJECT GUTENBERG EBOOK"):
            fileEnd = True
        # Need to account for produced by line
        if fileStart == True and fileEnd != True:
            line = line.lower()
            line = line.replace('\n', '')
            line = line.replace('\r', ' ')
            line = line.replace('.', '')
            line = line.replace('\"', '')
            line = line.replace('\'', '')
            line = line.replace('?', '')
            line = line.replace(',', '')
            line = line.replace(')', '')
            line = line.replace('(', '')
            line = line.replace('!', '')
            in_data += line
        if line.startswith("*** START OF THIS PROJECT GUTENBERG EBOOK"):
            fileStart = True

    return in_data

# We want to return a string of words that has been split
def make_words(in_data):
    # words = "I wish I may I wish I might".split()
    words = in_data.split(' ')
    return words

def build_trigram_dict(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    # build up the dict here!
    for i in range(len(words) - 2):  # why -2 ? Because you have to stop when you
        pair = words[i:i + 2]
        stringpair = "{:s} {:s}".format(pair[0], pair[1])
        follower = words[i + 2]
        if stringpair in trigrams:
            valuelist = trigrams[stringpair]
            valuelist.append(follower)
        else:
            valuelist = [follower]
            trigrams[stringpair] = valuelist
    return trigrams

def build_text(word_pairs):
    maxlength = 500
    counter = 0
    keylist = []
    for i in word_pairs.keys():
        keylist.append(i)
    startword = random.choice(keylist)
    new_text = "" + startword
    while counter < maxlength:
        # If the startword is not in the keys for word_pairs dictionary, select one at random to use
        if startword not in word_pairs:
            startword = random.choice(keylist)
        valuelist = word_pairs[startword]
        chosenint = 0
        # If there is more than one value, select one at random
        if len(valuelist) > 1:
            chosenint = random.randint(0, len(valuelist)) - 1
        chosenvalue = valuelist[chosenint]
        new_text += " {:s}".format(chosenvalue)
        splitstring = startword.split(' ')
        startword = splitstring[1] + " " + chosenvalue
        counter += 1
    return new_text

if __name__ == "__main__":
    filename = ""
    try:
        filename = input("Choose a filename to use")
    except IndexError:
        print("You must pass in a filename")
        exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram_dict(words)
    new_text = build_text(word_pairs)

    print(new_text)