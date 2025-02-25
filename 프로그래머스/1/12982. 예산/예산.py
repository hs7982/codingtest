def solution(d, budget):
    result = 0
    d.sort()
    for i in d:
        if budget == 0:
            break
        if budget >= i:
            budget -= i
            result += 1
    return result