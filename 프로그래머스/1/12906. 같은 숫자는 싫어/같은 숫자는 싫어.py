def solution(arr):
    answer = []
    cache = None
    for val in arr:
        if val != cache:
            answer.append(val)
        cache = val
            
    return answer