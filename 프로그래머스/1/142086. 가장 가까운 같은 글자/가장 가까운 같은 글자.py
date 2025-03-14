def solution(s):
    result = []
    s = list(s)

    for i in range(len(s)):
        target = s[i]
        rev_s = list(s[:i].__reversed__())

        try:
            result.append(rev_s.index(target)+1)
        except ValueError:
            result.append(-1)
    
    return result