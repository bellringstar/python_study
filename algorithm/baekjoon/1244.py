'''
스위치 켜짐 상태
1~스위치 개수 이하인 자연수
남학생: 스위치 번호 = 자기가 받은 수의 배수 => 스위치 상태를 바꾼다.
ex)3을 받았다 => 3,6의 상태 전환
여학생: 받은 번호와 같은 스위치 중심 좌우 대칭 최대(홀수). 상태 모두 전환

'''

N = int(input())#스위치
arr = [0] + list(map(int, input().split()))
M = int(input())#학생
for _ in range(M):
    a, b = map(int, input().split()) #a:성별, b:번호
    if a == 1:
        for i in range(b, N+1, b):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1
    else:
        if arr[b] == 1:
            arr[b] = 0
        else:
            arr[b] = 1
        s = b-1
        e = b+1
        while 1<=s and e<=N and arr[s] == arr[e]:
            if arr[s] == 1:
                arr[s] = arr[e] = 0
            else:
                arr[s] = arr[e] = 1
            s -= 1
            e += 1
arr = arr[1:]
k = 0
while k<N:
    print(arr[k], end=' ')
    k += 1
    if k%20 == 0:
        print()


