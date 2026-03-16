"""
    @param nums:{[Integer]}
    @param target:{Integer}
    @return :{[Integer]}
"""
def findIndexes(nums, target):
    indexes = []
    for i in range(len(nums)):
        if nums[i] == target:
            indexes.append(i)
    return indexes
