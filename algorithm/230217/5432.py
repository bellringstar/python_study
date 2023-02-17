'''
쇠막대기 자르기
'''
T = int(input())
for tc in range(1, T+1):
    st = input()
    cnt = ans = 0

    for i in range(len(st)):
        if st[i] == '(': #막대 시작 or 레이저
            cnt += 1
        else : #')' = 이전것을 확인해야함
            cnt -= 1
            if st[i-1] == '(':#레이저
                ans += cnt
            else: #막대기의 끝
                ans += 1


    print(f'#{tc} {ans}')