from collections import Counter

def singleNumber(nums):
    count = Counter(nums) #dict
    for el, amount in count.items():
        if amount == 1:
            return el
    



print(singleNumber([1, 1, 2, 3, 3, 4, 4]))