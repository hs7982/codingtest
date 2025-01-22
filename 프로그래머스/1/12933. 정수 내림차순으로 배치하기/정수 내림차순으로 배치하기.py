def solution(n):
    nums = sorted(list(map(str, str(n))), reverse=True)
    return int(''.join(nums))