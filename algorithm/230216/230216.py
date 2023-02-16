'''
A = [0, 1, 2]
N = len(A)
bit=[-1] * N
def f(i, k):
    if i == k:
        print(bit, end=' ')
        #[1, 1, 1] [1, 1, 0] [1, 0, 1] [1, 0, 0] [0, 1, 1] [0, 1, 0] [0, 0, 1] [0, 0, 0]
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j] #부분집합의 합
    else:
        bit[i] = 1 #(A[]에서 할일) #왼쪽 선택
        f(i+1, k) #반복 끝,
        bit[i] = 0 #오른쪽 선택
        f(i+1, k) #재귀 호출이 갈림길 만큼 생겼다.

f(0,N)

'''
'''
def f(i, k, s, t): #i: 원소, k: 집합의 크기, s: i-1까지의 부분집합의 합, t: 목표
    global cnt
    if s > t: #지금까지 계산한 원소의 합이 타겟보다 큰경우
        return
    elif s == t :#남은 원소 관계없이 목표치 도당
        return
    elif i == k: #모든 원소 고려했을때서야 도달
        if s == t:
            for j in range(k):
                if bit[j]:
                    print(A[j], end= ' ')
            print()
            cnt += 1
        return
    else:
        bit[i] = 1 #참고용
        f(i+1, k, s+A[i], t) #A[i]가 합에 포함
        bit[i] = 0 #참고용
        f(i+1, k, s, t) #A[i]가 합에 포함 X

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
key = 3
cnt = 0
bit = [0] * N

f(0, N, 0, key)
print(cnt)
'''
'''
#순열
def f(i, k):
    if i == k:
        print(p, end=' ') #[1, 2, 3] [1, 3, 2] [2, 1, 3] [2, 3, 1] [3, 2, 1] [3, 1, 2] 
    else:
        for j in range(i, k): #i부터 시작 = 중복상황 방지
            p[i], p[j] = p[j], p[i]
            #p[i]결정, p[i]와 관련된 작업 가능
            f(i+1, k)
            p[i], p[j] = p[j], p[i]

p = [1, 2, 3]
N = len(p)
f(0, N)

nums = [20, 30, 40]
N = len(nums)
def per(k): # k = 단계
    if k == N:
        print(a)
        for i in range(N):
            idx = a[i]
            print(nums[idx], end=' ')
        return
    for i in range(N):
        if not visitied[i]:
            visited[i] = True
            a[k] = i
            per(k+1)
            visited[i] = False

'''

nums = [20, 30, 40]
a = [0, 1, 2]
N = len(nums)
visited = [False] * N
def per(k): # k = 단계
    if k == N:
        print(a)
        for i in range(N): 
            idx = a[i]
            print(nums[idx], end=' ') #[0, 1, 2] 20 30 40 /[0, 2, 1]20 40 30 /[1, 0, 2]30 20 40 /[1, 2, 0]30 40 20 /[2, 0, 1]40 20 30 /[2, 1, 0]40 30 20 /
        print(end='/')
        return
    for i in range(N): #방문 안한 곳 순회하며 찾기
        if not visited[i]: 
            visited[i] = True
            a[k] = i #k번째에 방문 안한곳의 번호 넣기
            per(k+1)
            visited[i] = False

per(0)






'''
분할 정복 알고리즘 Divide-Conquer-Combine
ex) 퀵 정렬
def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)
'''
