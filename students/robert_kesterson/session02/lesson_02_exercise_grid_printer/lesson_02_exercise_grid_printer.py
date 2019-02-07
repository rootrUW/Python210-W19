# -------------------------------------------- #
# Title: Lesson 02 Exercise: Grid Printer
# Desc: Prints out grids of different sizes using different functions
# Change log: (who, when, what)
# RKesterson, 2019-01-22, Created file
# RKestesron, 2019-01-22, Stubbed out methods / parts
# RKesterson, 2019-01-22, Completed part one
# RKesterson, 2019-01-22, Completed part two
# RKesterson, 2019-01-22, Completed part three
# ---------------------------------------------- #

# Part one
levelOne = '+ - - - - + - - - - +'
levelTwo = '|         |         |'

print(levelOne)
print(levelTwo)
print(levelTwo)
print(levelTwo)
print(levelTwo)
print(levelOne)
print(levelTwo)
print(levelTwo)
print(levelTwo)
print(levelTwo)
print(levelOne)

# Part two
# Define the function
def print_grid(n):
    dashCount = int(n / 2)
    post = '+ '
    column = '| '
    floor = '- '
    openFloor = '  '
    levelOne = post + floor * dashCount + post + floor * dashCount + post
    levelTwo = column + openFloor * dashCount + column + openFloor * dashCount + column
    print(levelOne)
    i = 0
    while i < dashCount:
        print(levelTwo)
        i += 1
    print(levelOne)
    i = 0
    while i < dashCount:
        print(levelTwo)
        i += 1
    print(levelOne)

# Call the function
print_grid(15)

# Part three
# Define the function
def print_grid2(n, m):
    unitTop = '+ ' + '- ' * m
    unitTopFull = unitTop * n + '+'
    unitBottom = '| ' + '  ' * m
    unitBottomFull = unitBottom * n + '|'
    i = 0
    while i < n:
        print(unitTopFull)
        j = 0
        while j < m:
            print(unitBottomFull)
            j += 1
        i += 1
    print(unitTopFull)

# Call the function
print_grid2(5, 3)