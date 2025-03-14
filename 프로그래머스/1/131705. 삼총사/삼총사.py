def solution(number):
    result = 0
    n = len(number)
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if number[i] + number[j] + number[k] == 0:
                    result += 1
    
    return result