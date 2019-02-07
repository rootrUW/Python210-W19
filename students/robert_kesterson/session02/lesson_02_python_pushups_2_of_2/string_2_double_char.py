# Define the function
def double_char(str):
    result = ''
    for i in range(len(str)):
        result = result + str[i] * 2
    return result

# Call the function
double_char('cow-a-bunga')