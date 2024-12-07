#문자열 s가 주어졌을 때, 각 위치마다 자신보다 앞에 나왔으면서 자신과 가장 가까운 동일한 문자가 어
#디 있는지 구하려고 한다. 만약 해당 문자가 처음 등장했다면 -1로 표시한다.

s = list(input())
result = []

for i in range(len(s)):
    target = s[i]
    rev_s = list(s[:i].__reversed__())

    try:
        result.append(rev_s.index(target)+1)
    except ValueError:
        result.append(-1)

print(result)