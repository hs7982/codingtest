# 숫자 카드 게임

n, m = map(int, input().split())

result = 0

#한줄씩 입력받은뒤 확인까지 함
for i in range(n):
    data = list(map(int, input().split()))

    min_data = min(data) #한 줄에서 가장 작은 값 찾기

    result = max(min_data, result) #줄마다 가장 작은값중에 가장 큰 값을 판단

print(result)