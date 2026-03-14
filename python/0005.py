"""
    @param n1:{Integer}
    @param n2:{Integer}
    @return :{Boolean}
"""
def findGCD(n1, n2):
    if n2 == 0:
        return n1
    else: 
        return findGCD(n2, n1 % n2)
