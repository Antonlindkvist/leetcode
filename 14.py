#find the longest prefix in all elements

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    strs.sort()
    prefix = ""
    str1 = strs[0]
    str2 = strs[-1]
    for i in range(min(len(str1), len(str2))):
        if str1[i] == str2[i]:
            prefix += str1[i]
        else:
            break
    return prefix



data = ["flower", "flow", "flight", "dsad"]
print(longestCommonPrefix(data))

