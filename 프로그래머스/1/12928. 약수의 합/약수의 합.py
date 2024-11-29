def solution(n):
    num = []
    
    for i in range(n):
        if n % (i+1) == 0:
            num.append(i+1)
    return sum(num)
    
    