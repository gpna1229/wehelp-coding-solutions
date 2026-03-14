"""
    @param s:{String}
    @return :{Boolean}
"""
def checkHTTPS(s):
    str = "https://"
    if str == s[0:len(str)].lower():
        return True
    else:
        return False
