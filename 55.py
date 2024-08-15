def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    pos = 0
    n = len(nums)-1 #4
    jump = None
    while pos < n:
        if jump == 0 and pos != n:
            return False
        if nums[pos] == 0:
            jump = sum(nums[:pos])
        else:
            jump = nums[pos]
            print(f"pos:{pos} jump:{jump}")
        pos += jump
        print(f"pos:{pos}")
    return True

print(canJump([2,5,0,0]))

    