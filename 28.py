
def strStr(haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


strStr("leetcode", "code")
print(len("leetcode"), len("code"))




