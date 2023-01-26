'''
리스트 초기화 ex) [0] * 3
'''

# 3*4행 2차원 리스트
# n, m = map(int, input().split())

# my_list = [0 for _ in range(n)] # mylist = [0] * n
# for i in range(n):
#     my_list[i] = list(map(int, input().split()))

# print(my_list)

'''
List 순회
1. 행 우선 순회
2. 열 우선 순회
---------------이중 루프----
3. 지그재그 순회
행 우측 -> 행 좌측 -> 행 우측
n = len(arr)  행개수
m = len(arr[0]) 열개수
for i in range(n):
    for j in range(m):
        arr[i][j + (m - 1 - 2 * j) * (i % 2)]

4. 델타를 이용한 2차 리스트 탐색 : 한 좌표에서 네 방향의 인접 List 요소를 탐색할 때 사용
델타값은 한 좌표에서 네 방향의 좌표와 x, y의 차이를 저장한 List
델타값을 이용하여 특정 원소의 상하좌우에 위치한 원소에 접근 가능 
index의 범위에 주의
#arr[0...n-1][0...n-1] 2차원 List
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for x in range(len(arr)):
    for y in range(lend(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            print(arr[testX][testY])
5. 전치행렬
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

--------------------------------------------------------------
부분집합
#1
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)
#2 bit 연산자 사용 &, |, <<, >> ex) 1<<n : 2**n
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1<<n): # 1<<n : 부분 집합의 개수
    for j in range(n): #원소의 수 만큼 비트를 비교함
        if i&(1<<j): i의 j번쨰 비트가 1이면 j번째 원소 출력
            print(arr[j], end=',')
    print()
-----------------------------------------------------------------------
검색 : 저장되어 있는 자료 중에서 원하는 항목을 찾는 법
알고리즘 예시
1. 순차검색
일렬로 된 자료를 순서대로 검색, List나 연결List등 순차구조로 된 자료구조에서 유용
쉽지만 대상이 많은 경우 비효율
1-1. 정렬된 경우 : 도중에 key값보다 큰 원소를 만난다 -> 그 순간 검색 종료 실패 반환
1-2. 정렬 x
O(n)
def sequentialSearch(a, n, key):
    i = 0
    while i < n and a[i]!=key:
        i+=1
    if i < n : return i
    else: return -1
2. 이진검색
상대적으로 효율적
자료의 가운데 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속하는 방법
하지만 사전에 정렬된 자료가 필요 O(logn)

def binarySearch(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = start +(end - start) // 2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return False # 검색 실패

def binarySearch2(a, low, high, key):
    if low > high:
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binarySearch2(a, low, middle-1, key)
        elif a[middle] < key:
            return binarySearch2(a, middle+1, high, key)
인덱스
대량의 데이터를 매번 정렬하면, 프로그램의 반응은 느려질 수 밖에 없음. 이런 대량 데이터의 성능 저하 문제를 해결하기 위해
List 인덱스를 사용할 수 있음

셀렉션 알고리즘
저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
정렬 -> 원하는 순서의 자료
def select(list, k):
    for i in range(0, k):
        minindex = i
        for j in range(i+1, len(list)):
            minindex = j
        list[i],list[minindex] = list[minindex], list[i]
    return list[k-1]
선택정렬
주어진 자료들 중 가장 작은 값의 원소부터 차례로 선택하여 위치를 교환
1. List 중에서 최소값을 찾는다 2. 그 값을 List 맨 앞에 위치한 값과 교환한다. 3.맨 처음 위치를 제외한 나머지를 대상으로 반복
O(N^2)
'''


