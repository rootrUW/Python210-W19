#---------------------------------------- #
# Title: GridPrinter.py *In Work*
# Change Log: KCreek, 1/15/2018, Rev New
# KCreek, 1/15/2019, Created File
# KCreek, 1/17/2019, Added Comments and DocString
#---------------------------------------- #



def gridPrint1():

    """
    Function that Prints a Grid to the Screen .
    This is written to meet the first portion of requirements
    for assignment02.

    """

    # Print each part of grid line by line.

    print('+', '-'*4, '+', '-'*4, '+')
    print('|', ' '*4, '|', ' '*4, '|')
    print('|', ' '*4, '|', ' '*4, '|')
    print('|', ' '*4, '|', ' '*4, '|')
    print('|', ' '*4, '|', ' '*4, '|')
    print('+', '-'*4, '+', '-'*4, '+')
    print('|', ' '*4, '|', ' '*4, '|')
    print('|', ' '*4, '|', ' '*4, '|')
    print('|', ' '*4, '|', ' '*4, '|')
    print('|', ' '*4, '|', ' '*4, '|')
    print('+', '-'*4, '+', '-'*4, '+')

print("Presenting: GridPrint1: ")
gridPrint1()

# Part2 of GridPrinter Assignment

def gridPrint2(n):

    """
    Prints a Grid sized according to a user provided argument.
    This is written to meet the second portion of requirements
    for assignment02.

    :param n: User Provided Argument to determine Scale for Grid Size
    :return: Prints Grid to user, no return value provided
    """

    # Define the header and spacer sections to be printed out.
    # The space is set by the scale provided by the user.

    line1 = '+' + '-'*2*n + '+' + '-'*2*n + '+'
    line2 = '|' + ' '*2*n + '|' + ' '*2*n + '|'

   # Prints the header to the screen.
    print(line1)


    # 'While' loop to print the portion of the grid between the header and footer.

    i = 0
    while i < n:
        print(line2)
        i +=1

    print(line1)
    i = 0
    while i < n:
        print(line2)
        i += 1

    # Print the footer of the grid, which matches the header
    print(line1)


# Call the second grid printer function.
print("Presenting GridPrint2: ")
gridPrint2(10)


# Part 3 of GridPrinter Assignment

def gridPrint3(columns,rows):

    """
    Prints a Grid with based on the columns and rows provided by the user.
    THis is meant to achieve the third portion of assignment02.

    :param columns: Number of Columns desired by user
    :param rows: Number or Rows desired by user
    :return: Prints a grid to the user based on their inputs"""

    # Assign Variables to establish header and spacing lines based on the
    # user inputs.

    columnHeader = '+ - - - - ' * columns + '+'
    rowSpacer = ('|         ' * columns + '|')

    # While loop to print each row and spacer to the screen. Loop ends when
    # The desired amount of rows have been printed to the screen to create a
    # body

    rowCounter = 0
    while rowCounter < rows:
        print(columnHeader)
        i = 0
        while i < 3:
            print(rowSpacer)
            i += 1
        rowCounter += 1

    # Print the column header to create a footer by the grid.
    print(columnHeader)


# Call the third grid printer function for a variety of rows and columns.
print("Presenting 2 different GridPrint3 Functions: ")
#gridPrint3(3, 3)
gridPrint3(2, 5)
gridPrint3(8, 4)
