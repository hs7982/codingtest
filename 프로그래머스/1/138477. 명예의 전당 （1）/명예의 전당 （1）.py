def solution(k, score):
    answer = []
    rank = []
    for i in score:
        rank.append(i)
        rank.sort(reverse=True)
        answer.append(min(rank[:k]))
    return answer