def solution(sizes):
    w_max = 0
    h_max = 0
    for i in sizes:
        i.sort(reverse=True)
        w_max = max(w_max, i[0])
        h_max = max(h_max, i[1])
        
    return w_max * h_max