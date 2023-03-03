'''
1~N번 전구
i 번 스위치 = i의 배수의 전수 상태 반전
모든 전구를 끄기 위해 스위치를 몇번 눌러야하는가
'''
def swap(i):
    global N
    for j in range(i, N, i):
        if arr[j] == 'Y':
            arr[j] = 'N'
        else:
            arr[j] = 'Y'


arr = [0] + list(input())
N = len(arr)
cnt = 0
for idx in range(1,N):
    if arr[idx] == 'Y':
        swap(idx)
        cnt += 1
    if 'Y' not in arr:
        print(cnt)
        break
else:
    if 'Y' in arr:
        print(-1)
