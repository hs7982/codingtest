def solution(s):
    s_len = len(s)
    return True if ((4 == s_len) or (s_len == 6)) and s.isdecimal() else False 