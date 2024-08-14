#reverse every word in the string
#remove extra spaaces
#return the string
def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    return ' '.join(s.split()[::-1])
    

print(reverseWords("   hej    nej     okej "))