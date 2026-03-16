"""
    @param nums:{[Integer]}
    @param target:{Integer}
    @return :{Integer}
"""
def findIndex(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
