def addn(s, n):
    return ord(s) + n

def solution(s, n):
    result = ""
    for i in list(s):
        if i == " ":
            result += i
        elif (i.isupper()):
            code = addn(i,n)
            result += chr(code - 26 if code > 90 else code)
        else:
            code = addn(i,n)
            result += chr(code - 26 if code > 122 else code)
    return result
        
        