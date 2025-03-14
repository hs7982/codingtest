def solution(food):
    answer = ''
    
    for i in range(1,len(food)):
        food[i] = food[i] // 2
        answer += str(i) * food[i]
    
    return answer + "0" + answer[::-1]