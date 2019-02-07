# Define the function
def lone_sum(a, b, c):
    sum = 0
    if a != b and a != c and b !=c:
        sum = a + b + c
    elif a != b and b == c:
        sum = a
    elif a == b and b != c:
        sum = c
    elif a == c and b != c:
        sum = b
    return sum

# Call the function
lone_sum(2, 3, 5)