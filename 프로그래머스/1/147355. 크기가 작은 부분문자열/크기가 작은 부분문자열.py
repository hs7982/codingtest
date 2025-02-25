def solution(t, p):
    count = 0
    
    for i in range(0, len(t) - len(p) +1):
        part = t[i:i+len(p)]
        if part <= p:
            count += 1
    return count
    
     
    