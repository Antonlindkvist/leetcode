def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    word = []
    i = (len(s)-1)
    while s[i] == ' ':
        i -= 1
    while s[i] != ' ' and i >= 0:
        word.append(s[i])
        i -= 1
    return len(word)

def lengthOfLastWord2(s):
    #faster
    """
    :type s: str
    :rtype: int
    """
    return len(s.split()[-1])


print(lengthOfLastWord("hello hello  "))
print(lengthOfLastWord2("hello hello "))
        

    

