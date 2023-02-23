'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
'''
def preorder(i):
    if i: # 존재하는 정점
        print(i, end=' ')
        preorder(left_c[i])
        preorder(right_c[i])


V = int(input())
arr = list(map(int, input().split()))
E = V - 1
#부모를 인덱스로 하는 자식번호 저장 배열
left_c = [0] * (V + 1) #왼쪽자식
right_c = [0] * (V + 1) #오른쪽자식
parent = [0] * (V + 1) #자식을 인덱스로 부모 노드 저장
# child = [[] for _ in range(V+1)] 인접리스트 형태

for i in range(E):
    p, c = arr[2*i], arr[2*i+1]
    if left_c[p] == 0:
        left_c[p] = c
    else:
        right_c[p] = c
    parent[c] = p

root = 1
while parent[root] != 0 : #루트인지 확인 -> 루트라면 부모가 없다.
    root += 1

preorder(root)
'''

'''
이진탐색트리
모든 원소는 서로 다른 유일한 키를 갖는다.
key(왼쪽 서브트리)<key(루트노드)<key(오른쪽 서브트리)
중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있다.

탁색연산
루트에서 시작한다.
탐색할 키 값 x를 루트 노드의 키 값과 비교한다.
키값 x = 루트노드 키 값 : 탑색 성공
키값 x < 루트노드 키 값 : 루트 노드의 왼쪽 서브트리 탐색
키값 x > 루트노드 키 값 : 루트 노드의 오른쪽 서브트리 탐색
탐색, 삽입, 삭제 시간은 트리의 높이 만큼 시간이 걸린다. O(h)
이진트리가 균형적으로 생성된 경우 O(logn)
최악의 경우: 한쪽으로 치우친 경사 이진트리, O(n) 순타탐색과 차이가 없다.

'''
'''
힙(heap)
'완전 이진 트리'에 있는 노드 중에서 키 값이 가장 큰 노드나 키값이 갖아 작은 노드를 찾기 위해서 만든 자료구조
최대 힘(max heap)
키값이 가장 큰 노드를 찾기 위한 완전 이진 트리
부모노드의 키값> 자식노드의 키값
루트 노드: 키값이 가장 큰 노드
최소힙(min heap)
키값이 가장 작은 노드를 찾기 위한 와전 이진 트리
부모노드의 키값 < 자식노드의 키값
루트노드: 키값이 가장 작은노드

힙에서는 루트에 있는 원소만 꺼낼 수 있다.
루투 노드의 원소를 삭제하여 반환한다.
힙의 종류에 따라 최대값 또는 최소값을 구할 수 있다.
1. 루트 노드의 원소를 삭제 -> 마지막 위치의 노드를 루트로 이동(완전이진트리 조건) -> 크기 비교를 통해 자리 조정
'''
'''
#최대 100개의 key, 최대힙


def enq(n):
    global last
    last += 1 #완전이진트리를 위해 마지막 정점에 추가
    heap[last] = n #마지막 위치에 저장
    # 부모노드와 비교 : 부모가 있고 , 부모<자식인 상태다 -> 교환
    c = last #현재 자식 위치
    p = c//2 #현재 자식의 부모 위치
    while p>0 and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p #부모 자식 갱신: 교환된 후 계속해서 비교하기위해
        p = c // 2
    return

def deq():
    global last
    tmp = heap[1] #루트 임시 저장
    heap[1] = heap[last] #마지막 노드의 값을 루트로 이동
    last -= 1 #노드 개수 하나 삭제: 마지막 정점 삭제
    p = 1
    c = p * 2 #왼쪽 자식 번호
    while c <= last: #자식이 하나 이상 있으면
        if c + 1 <= last and heap[c] < heap[c+1]: #오른쪽 자식존재, 오른쪽 자식이 왼쪽 자식보다 크다
            c += 1 #비교 대상을 오른쪽 자식으로 변경
        if heap[c] > heap[p]:
            heap[c],heap[p] = heap[p],heap[c]
            p = c #자식 위치로 이동
            c = p * 2 #새로운 자식과 비교
        else:
            break
    return tmp



heap = [0] * 101 #완전 이진트리 = 1번->100번 인덱스 준비
last = 0 #완전 이진트리의 현 상태에서의 마지막 정점 번호
enq(5)
print(heap[1])
enq(15)
print(heap[1])
enq(8)
print(heap[1])
enq(20)
print(heap[1])

while last>0:
    print(deq())
'''

def insert(item):
    pos = 1
    while tree[pos] != 0:
        if tree[pos] == item:
            return
        if tree[pos] < item:
            pos = 2*pos + 1
        else:
            pos = 2*pos

    tree[pos] = item

def find(key):
    pos = 1
    while tree[pos] != 0:
        if tree[pos] == key:
            return pos
        elif tree[pos] < key:
            pos = pos * 2 + 1
        else:
            tree[pos] > key:
            pos = pos * 2
    return -1


tree = [0] * 100
lst = [9, 4, 12, 3, 6, 15, 13, 17]
for item in lst:
    insert(item)
    # print(tree)