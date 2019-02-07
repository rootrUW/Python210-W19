#---------------------------------------- #
# Title: FibonacciSeries.py
# Change Log: KCreek, 1/15/2018, Rev New
# KCreek, 1/15/2019, Created File
# KCreek, 1/17/2018, Added Comments and DocString
#---------------------------------------- #

def fibonacci(n):

    """
    Function Used to print the 'nth' value of the fibonacci series
    as provided by the user.
    :param n: Describes the nth value of the Fibonacci Series.
    :return: Returns the 'nth' value of the Fibonacci
    Series.
    """

    # Case Statements to handle the first two values of the Fibonacci Series

    if n == 1:
        return 0
    elif n == 2:
        return 1

    # Case Statement to handle recursive functions after the first two values of the
    # Fibonacci Series

    else:
        while n > 2:
            return fibonacci(n - 2) + fibonacci(n - 1)


test = fibonacci(15)
print(test)



test = fibonacci(10)
print(test)
