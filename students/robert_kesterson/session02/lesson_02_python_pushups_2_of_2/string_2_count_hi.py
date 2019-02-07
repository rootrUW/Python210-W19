# Define the function
def count_hi(str):
    count = 0
    iCounter = 0
    while (iCounter < len(str)):
        if str[iCounter:iCounter + 2] == 'hi':
            count += 1
        iCounter += 1
    return count

# Call the function
count_hi('hihellofromMadagascarhi')