def solution(haystack, needle):
    if haystack not needle:
        return 0  # Empty needle matches at the beginning

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    
    return -1
