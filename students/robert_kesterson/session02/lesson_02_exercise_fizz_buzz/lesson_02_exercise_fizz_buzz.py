# -------------------------------------------- #
# Title: Lesson 02 Exercise: Fizz Buzz
# Desc: The classic fizz buzz interview question, spoken of in song and story
# Change log: (who, when, what)
# RKesterson, 2019-01-22, Created file
# RKestesron, 2019-01-22, Stubbed out methods / parts
# RKesterson, 2019-01-22, Completed program
# ---------------------------------------------- #

# Define the function
def fizzBuzz():
    i = 1
    while i < 101:
        if (i % 3 == 0 and i % 5 == 0):
            print('FizzBuzz')
        elif (i % 3 == 0 and i % 5 != 0):
            print('Fizz')
        elif (i % 3 != 0 and i % 5 == 0):
            print('Buzz')
        else:
            print(i)
        i += 1

# Call the function
fizzBuzz()