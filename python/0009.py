"""
    @param words:{[String]}
    @param value:{String}
    @return :{[String]}
"""
def fill(words, value):
    for i in range(len(words)):
        if words[i] == "":
            words[i] = value
    return words
