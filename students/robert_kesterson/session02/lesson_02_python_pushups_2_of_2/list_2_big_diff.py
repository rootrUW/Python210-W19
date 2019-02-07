# Define the function
def big_diff(nums):
    largestObserved = nums[0]
    smallestObserved = nums[0]
    iCounter = 1
    while iCounter < len(nums):
        smallestObserved = min(smallestObserved, nums[iCounter])
        largestObserved = max(largestObserved, nums[iCounter])
        iCounter += 1
    difference = largestObserved - smallestObserved
    return difference

# Call the function
big_diff([10, 2])