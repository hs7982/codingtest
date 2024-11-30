def solution(a, b):
    add = 0
    if a>b: a, b=b, a
    for i in range(a,b+1):
        add = add + i
    return add