def solution(n):
    three = []
    answer = 0
    while n > 0:
        n, mod = divmod(n, 3)
        three.append(mod)
    
    for idx, num in enumerate(three[::-1]):
        answer += 3 ** idx * num
    return answer