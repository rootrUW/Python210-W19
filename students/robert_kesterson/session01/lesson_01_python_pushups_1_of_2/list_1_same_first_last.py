# Define the function
def same_first_last(nums):
    if len(nums) >= 1 and nums[0] == nums[len(nums) - 1]:
        return True
    else:
        return False

# Call the function
same_first_last([10])
