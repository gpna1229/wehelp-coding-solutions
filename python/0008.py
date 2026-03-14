"""
    @param min:{Integer}
    @param max:{Integer}
    @param differ:{Integer}
    @return :{Integer}
"""
def sumOfArithmeticSequence(min, max, differ):
    sum = 0
    for i in range(min, max+1, differ):
        sum += i
    return sum
