# Define the function
def date_fashion(you, date):
    if you >= 8 and date >= 3:
        return 2
    elif you >= 3 and date >= 8:
      return 2
    elif you <= 2 or date <= 2:
        return 0
    else:
        return 1

# Call the function
date_fashion(2, 9)
