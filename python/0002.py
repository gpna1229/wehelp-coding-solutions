"""
    @param n:{Integer}
    @return :{Boolean}
"""
def checkMoney(n):
    if n % 100 != 0:
        return False
    elif n < 100:
        return False
    elif n > 100000:
        return False
    else:
        return True
