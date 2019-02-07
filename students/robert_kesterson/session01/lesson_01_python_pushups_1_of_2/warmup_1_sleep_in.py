# Define the function
def sleep_in(weekday, vacation):
    if vacation or weekday is False:
        return True
    else:
        return False

# Call the function
sleep_in(False, True)
