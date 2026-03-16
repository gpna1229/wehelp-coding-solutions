"""
    @param nums:{[Integer]}
    @return :{Integer}
"""
def findMaxProduct(nums):
    nums.sort()
    return max(nums[0] * nums[1], nums[-1] * nums[-2])
            
