T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    set1 = set(str1) #중복 제거
    maxC = 0 #카운트
    for s in set1:
        cnt = str2.count(s)
        if maxC < cnt:
            maxC = cnt
    print(f'#{tc} {maxC}')
