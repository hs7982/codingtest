def solution(s):
    answer = True
    
    p,y=0,0
    
    for i in list(s.lower()):
        if i == "p":
            p+=1
        elif i == "y":
            y+=1

    if p != y:
        answer = False
    
    return answer