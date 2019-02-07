#!/usr/bin/env python3

# -------------------------------------------- #
# Title: Lesson 03 Exercise: Slicing lab
# Desc: This is a lab where we will learn about slicing
# Change log: (who, when, what)
# RKesterson, 2019-01-29, Created file
# RKestesron, 2019-01-29, Stubbed out methods / parts
# RKesterson, 2019-01-29, Started task one (asked question about this in lesson 03 code chat forum)
# RKesterson, 2019-01-29, Completed task two
# RKesterson, 2019-01-29, Completed task three
# RKesterson, 2019-01-29, Completed task four
# RKesterson, 2019-01-29, Completed task five
# ---------------------------------------------- #

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

# Task one
def exchange_first_last(seq):
    return seq[-1] + seq[1:-1] + seq[0]

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

# Task two
def remove_every_other(seq):
    return seq[0:len(seq):2]

assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) == (2, 13, 5)

# Task three
def remove_four_starting_and_end(seq):
    return seq[4:-4]

assert remove_four_starting_and_end(a_string) == " is a st"
assert remove_four_starting_and_end(a_tuple) == ()

# Task four
def reverse_sequence(seq):
    return seq[::-1]

assert reverse_sequence(a_string) == "gnirts a si siht"
assert reverse_sequence(a_tuple) == (32, 5, 12, 13, 54, 2)

# Task five
def thirds_manipulator(seq):
    length = len(seq)
    thirds = int(length / 3)
    return seq[thirds * 2: length] + seq[0: thirds] + seq[thirds: thirds * 2]

assert thirds_manipulator(a_string) == "stringthis is a "
assert thirds_manipulator(a_tuple) == (5, 32, 2, 54, 13, 12)