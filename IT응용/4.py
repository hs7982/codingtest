#단어 s의 가운데 글자를 반환하는 함수, solution을 만드시오. (단어의 길이가 짝수라면 가운데 두글자를
#반환, 1 ≤ s ≤100, s는 영어임 )

s = input()
mid = len(s) // 2

if len(s) % 2 == 0:
    print(s[mid-1]+s[mid])
else:
    print(s[mid])