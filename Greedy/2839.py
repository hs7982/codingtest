kg = int(input())

type = [5, 3]
result = 0

while kg >= 0:
    if kg % 5 == 0:
        result += kg // 5
        break
    kg -= 3
    result += 1
else:
    result = -1
print(result)