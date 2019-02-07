# Define the function
def first_last6(nums):
    if nums[0] == 6 or nums[len(nums) - 1] == 6:
        return True
    else:
        return False

# Call the function
first_last6(10, 8)
