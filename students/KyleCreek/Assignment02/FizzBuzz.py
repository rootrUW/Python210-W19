#---------------------------------------- #
# Title: FizzBuzz.py
# Change Log: KCreek, 1/15/2018, Rev New
# KCreek, 1/15/2019, Created File
# KCreek, 1/17/2019, Added Comments and DocString
# KCreek, 1/18/2019, Added Second Fizz Buzz Function
#---------------------------------------- #

def FizzBuzz():

    """
    A Function Written to print numbers 1-100 Inclusive.
    For Multiples of 3, 'Fizz' is printed in lieu of number
    For Multiples of 5, 'Buzz' is printed in lieu of number
    For Multiples of 15, 'FizzBuzz" is printed in lieu of number.
    :return: No Values are returned by the Function

    """
    # Create Counting Flag to for 'while' loop.
    # Note: performing a 'for' loop from range(1:100) was also
    # Considered, but I got this working and didn't have time to write
    # an additional function.

    count = 0
    while count < 100:

        # Case Statement to handle values divisible by both 3 & 5
        if count % 3 == 0 and count % 5 == 0:
            print('FizzBuzz')
            count +=1

        # Case Statement to handle values divisible by 3 ONLY
        elif count % 3 == 0:
            print('Fizz')
            count += 1

        # Case statement to handle values divisible by 5 ONLY
        elif count % 5 == 0:
            print('Buzz')
            count += 1

        # Case statement where values are neither divisible by 3, 5, or
        # both 3 & 5.
        else:
            print(count)
            count += 1

# Call Fizzbuzz function
FizzBuzz()


def FizzBuzz2():
    """
    A Second Function Written to print numbers 1-100 Inclusive.
    For Multiples of 3, 'Fizz' is printed in lieu of number
    For Multiples of 5, 'Buzz' is printed in lieu of number
    For Multiples of 15, 'FizzBuzz" is printed in lieu of number.
    :return: No Values are returned by the Function

    """
    # 'for' loop to perform an action for numbers between range
    # of 0 - 100
    for number in range(100):

        # Case Statement to handle values divisible by both 3 and 5
        if number % 3 == 0 and number % 5 == 0:
            print(number, "FizzBuzz")

        # Case Statement to handle values divisible by 3 only
        elif number % 3 == 0:
            print(number, "Fizz")

        # Case Statement to Handle values divisible by 5 only
        elif number % 5 == 0:
            print(number, "Buzz")

        # Case statement to handle values that are neither divisible by 3, 5,
        # or 3 & 5
        else:
            print(number)


# Call the FizzBuzz Function.
FizzBuzz2()

