def solution(s):
    s = s.lower()
    answer = ""
    upper = True
    for i in list(s):
        if(i == " "):
            upper = False #뒤에서 반전시킬것이므로 false로 둠
        elif(upper):
            i = i.upper()

        answer += i
        upper = not upper
        
    return answer