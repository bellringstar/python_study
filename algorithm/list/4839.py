'''
이진탐색 지정된 페이지 찾기
ex) 400페이지 책 -> start = 0, end = 400 mid = (400 + 0) / 2

'''
def binaryS(start,end,target): 
    cnt = 0
    mid = (start + end) // 2 
    while mid != target:
        cnt += 1
        mid = (start + end) // 2 
        if target > mid: 
            start = mid
        elif target < mid: 
            end = mid

    return cnt


T = int(input())
for test in range(T):
    P, A, B = map(int, input().split()) # 400 300 350
    count_A = binaryS(0, P, A)
    count_B = binaryS(0, P, B)

    if count_A < count_B:
        print(f'#{test+1} A')
    elif count_A > count_B:
        print(f'#{test+1} B')
    else:
        print(f'#{test+1} 0')