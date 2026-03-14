"""
    @param nums:{[Integer]}
    @return :{Integer}
"""
def findSecond(nums):
    nums.sort()
    for i in range(len(nums)-1, -1, -1):
        if nums[i] != max(nums):
            return nums[i]
