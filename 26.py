

def removeDuplicates(nums):
    nums[:] = sorted(set(nums))
    return len(nums)


       
print(removeDuplicates([1, 1, 1, 3, 4, 5, 5]))
# [1, 3, 4, 5]
# k = 3