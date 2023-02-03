'''
선택한 비트를 결정하면 그 이후도 다 같아짐.초기상태(0000)에서원래상태로 복귀하는데 걸린 최소횟수
input = 메모리 원래 값
메모리 길이 1이상 50 이하
'''
'''
1.처음으로 1이 나오는 위치기록
2.그 위치 이후로 1의 위치와 0의 위치를 나눠서 기록
3.해당 값의 위치가 원하는 값과 일치하는가? 일치하지 않으면 작업
'''
T = int(input())
for tc in range(1,T+1):
    Mlst = list(map(int,input()))
    Zlst = [0] * len(Mlst)
    start_idx = 0
    num = []
    for idx in range(len(Mlst)):
        if Mlst[idx] == 1:
            start_idx = idx
            break
    for i in range(idx,len(Mlst)):
        if Mlst[i] == 1:
            num.append((i,1))
        else:
            num.append((i,0))
    cnt = 0
    for t in num:
        if Zlst == Mlst:
            break
        if Zlst[t[0]] != t[1]:
            for j in range(t[0],len(Zlst)):
                Zlst[j] = t[1]
            cnt += 1
            if Zlst == Mlst:
                break

        elif Zlst[t[0]] != t[1]:
            for k in range(t[o],len(Zlst)):
                Zlst[k] = t[1]
            cnt += 1
            if Zlst == Mlst:
                break
    print(f'#{tc} {cnt}')

