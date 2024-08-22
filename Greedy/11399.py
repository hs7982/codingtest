n = int(input())
time = list(map(int, input().split()))

time.sort()
wait = 0
result = 0

for i in range(n):
    wait += time[i]
    result += wait

print(result)