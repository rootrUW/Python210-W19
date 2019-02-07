# Define function
def lucky_sum(a, b, c):
    sum = 0
    if a == 13:
        sum = 0
    elif b == 13:
        sum = a
    elif c == 13:
        sum = a + b
    else:
        sum = a + b + c
    return sum

# Call function
lucky_sum(2, 3, 5)