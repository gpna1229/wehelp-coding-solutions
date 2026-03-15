"""
    @param words:{[String]}
    @return :{[String]}
"""
def ffill(words):
    tmp = ""
    for i in range(len(words)):
        if (words[i] == "") and (tmp != ""):
            words[i] = tmp
        else:
            tmp = words[i]
    return words
