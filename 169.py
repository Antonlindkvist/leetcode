from collections import Counter

def majorityElement(nums) -> int:
    count = Counter(nums)
    for el, amount in count.items():
        if amount > (nums.size()/2):
            return el
        


