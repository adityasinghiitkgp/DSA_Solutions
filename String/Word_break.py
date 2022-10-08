def wordBreak(line, dictionary):
    if line in dictionary:
        return True
    for i in range(1,len(line)):
        if line[i:] in dictionary:
            word=line[0:i]
            if wordBreak(word,dictionary):
                return True
    return False
