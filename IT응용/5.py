# 정수로 이루어진 배열과 목표 값 target이 주어질 때, 배열에서 두 수의 합이 target이 되는 두 수를 찾
# 아 반환하시오. 존재하지 않으면 0을 반환한다. (단, 배열의 길이는 2 이상 10,000 이하)

nums = list(map(int, input().split(",")))
target = int(input())

for i, num in enumerate(nums):
    indexTarget = target - num
    try:
        result = nums.index(indexTarget, i+1)
        print([num, nums[result]])
        break
    except ValueError:
        continue
else:
    print(0)