"""
    @param nums:{[Integer]}
    @return :{String}
"""
def toCSVString(nums):
    return ','.join(str(num) for num in nums)
