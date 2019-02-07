# Define the function
def count_evens(nums):
    evenCount = 0
    indexI = 0
    while indexI < len(nums):
        if nums[indexI] % 2 == 0:
            evenCount += 1
        indexI += 1
    return evenCount

# Call the function
count_evens([2, 7, 1, 4])