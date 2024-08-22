#배열의 크기 N, 숫자가 더해지는 횟수 M, 연속으로 더해지는 횟수 상한 K
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

#데이터를 정렬시켜 가장큰수, 그다음으로 큰수 저장
data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    #큰수를 K만큼 더하고
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    #그다음으로 큰 수를 한번 더하는 방법 반복
    result += second
    m -= 1

print(result)