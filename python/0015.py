"""
    @param s:{String}
    @return :{Boolean}
"""
def checkPassword(s):
    if len(s) < 8 or len(s) > 16:
        return False
    flag1 = flag2 = flag3 = flag4 = 0
    symbol = ["!", "@", "#", "$", "%"]
    for i in range(len(s)):
        if s[i].isupper():
            flag1 = 1
        elif s[i].islower():
            flag2 = 1
        elif s[i].isdigit():
            flag3 = 1
        elif s[i] in symbol:
            flag4 = 1
        else:
            return False
    if flag1 + flag2 + flag3 + flag4 == 4:
        return True
    else:
        return False
