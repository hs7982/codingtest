def solution(absolutes, signs):
    for idx, val in enumerate(absolutes):
        if not signs[idx]:
            absolutes[idx] = -val

    return sum(absolutes)