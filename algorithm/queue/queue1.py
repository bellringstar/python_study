'''
Queue
뒤에서 삽입 앞에서 삭제
선입선출 ex)대기줄
enQueue: 삽입
deQueue: 삭제
최초 빈 큐 =front = rear = -1
원소 추가시 rear +=1
원소 삭제시 front +=1
-> front == rear : 큐가 비어있다.

1. 선형 큐 : 리스트
보통 1차원 리스트로 규현
def enQueue(item):
    global rear
    if isFull(): print('Queue_Full')
    else:
        rear += 1
        Q[rear] = item
def deQueue():
    global front
    if isEmpty(): print('Queue_Empty')
    else:
        front += 1
        return Q[front]
def isEmpty():
    return front == rear
def isFull():
    return rear == len(Q) -1
def Qpeek():
    if isEmpty(): print('Queue_Empty')
    else: return Q[front+1]

선형큐의 문제점
1. 삽입,삭제를 계속할 경우 리스트의 앞부분에 활용할 수 있는 공간이 있음에도, rear=n-1인 상태 즉, 포화상태로 인식
2. 더 이상의 삽입을 수행할 수 없음
-> 메모리 낭비가 심함

2. 원형 큐 : 리스트
1차원 리스트를 사용하되, 논리적으로 리스트의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용함
원형 큐의 논리적 구조

front = rear = 0
index의 순환이 필요 : front와 rear의 위치가 리스트의 마지막 인덱스인 n-1을 가리킨 후, 논리적 순환을 이루어 리스트의 처음 인덱스인 0으로 이동해야 함
이를 위해 나머지 연산자 % 사용
공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠
선형 큐 : 삽입 : rear +=1 삭제: front += 1
원형 큐 : rear = (rear + 1) % n 삭제: front = (front + 1) % n
def isEmpty():
    return front == rear

def isFull():
    return (rear + 1)%len(cQ) == front

def enQueue(item):
    global rear
    if isFull():
        print('Queue_Full')
    else:
        rear = (rear + 1) % len(cQ)
        cQ[rear] = item

def deQueue:
    global front
    if isEmpty():
        print('Queue_Empty')
    else:
        front = (front + 1) % len(cQ)
        return cQ[front]

리스트를 사용한 구현 (메모리 공간 동적으로 사용 가능 하지만 삽입 삭제등에 시간이 많이든다)
def enQueue(item):
    queue.append(item)
def deQueue():
    if isEmpty():
        print('Queue_Empty')
    else:
        return queue.pop(0)
def isEmpty():
    return len(queue) == 0
def Qpeek():
    if isEmpty():
        print('Queue_Empty')
    else:
        return queue[0]

queue = []
#front = -1 ; rear = len(queue) - 1


3. 연결 큐 : 연결리스트
앞선 큐들의 단점 보완
큐의 원소 : 단순 연결 리스트의 노드
큐의 원소 순서 : 노드의 연결 순서, 링크로 연결되어 잇음
front : 첫 번째 노드를 가리키는 링크
rear : 마지막 노드를 가리키는 링크
초기상태, 공백상태 : front = rear = None

def createLinkedQueue():
    front = None
    rear = None

def isEmpty():
    return front == None

def enQueue(item):
    global front,rear
    newNode = Node(item)
    if isEmpty():
        front = newNode
    else:
        rear.next = newNode
    rear = newNode

def deQueue():
    global front, rear
    if isEmpty():
        print('Queue_Empty')
        return None
    item = front.item
    front = front.next
    if isEmpty():
        rear = None
    return item

큐 모듈을 사용해 큐를 사용할 수 있다.
queue.Queue(maxsize): 선입선출 큐 객체를 생성
queue.LifoQueue(maxsize): 스택 개념의 후입선출 큐 객체 생성
queue.PriorityQueue(maxsize): 우선순위 큐 객체를 생성, 입력되는 아이템의 형식은 (순위,아이템)의 튜플로 입력되며, 우선순위는 숫자가 작을수록 높은 순위
maxsize는 최대 아이템수, 지정하지 않거나 음수이면 내용만큼 늘어남

해당 클래스들의 메서드
qsize() : 큐 객체에 입력된 아이템의 개수 반환
put(item[, block[,timeout]]): 큐 객체에 아이템을 입력
get([block[, timeout]]): 생성된 큐 객체 특성에 맞추어 아이템 1개를 반환
empty(): 큐 객체가 비어있으면 True 리턴
full(): 큐 객체가 꽉차있으면 True 리턴

import queue

q = queue.Queue() # FIFO 구고 큐 생성
q.put('A')
q.put('B')
q.pup('C')

while not q.empty():
    print(q.get())


4. 우선순위 큐
우선순위를 가진 항목들을 저장하는 큐
FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 됨
시뮬레이션 시스템, 네트워크 트래픽 제어, 운영체제의 태스크 스케쥴링등에 사용됨

enQueue : 우선순위에 맞는 위치에 삽입 / deQueue: 우선순위가 가장 높은 것을 삭제
1. 리스트를 이용한 구현
최고순위 원소 = 가장 앞에 위치
하지만 삽입,삭제의 연산시에 원소의 재배치 -> 낭비가 심함
2. 연결리스트를 쓰더라도 비교연산이 많다
-> 해결하기 위해 PriorityQueue(maxsize) 클래스 사용 / 힙 자료구조 사용

5. 버퍼
데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
버퍼링: 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미
일반적으로 입출력 및 네트워크와 관련된 기능에서 이용
순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐가 활용됨
물리적인 장치의 처리속도에서 대기시간을 감소시키기 위한 방법
ex) 키보드 버퍼
키보드 입력 -> 키보드 입력 버퍼 -> 키보드 입력버퍼에 Enter키 입력이 들어오면 -> 프로그램 실행 영역으로 이동 , 연산


BFS 너비 우선 탐색
DFS vs BFS
DFS: stack 활용
BFS: queue 활용
시작점의 인접한 정점들을 모두 차례로 방문한 후 방문했던 정점을 시작점으로 하여 다시 인접한 장점들을 차례로 방문하는 방식
인접한 정점들을 탐색한 후, 차례로 BFS를 진행해야 하므로, 선입선출 형태의 자료구조인 큐 활용

def BFS(G, v): #G:그래프, v:시작점
    visited = [0] * n # 정점의 개수
    queue = [] #큐 생성
    queue.append(v) #시작점 v를 큐에 삽입
    while queue: #큐가 비어있지 않는 경우
        t = queue.pop(0) #큐의 첫번째 원소 반환
        if not visited[t]: #방문되지 않은 곳이라면
            visited[t] = True #방문한 것으로 표시
            visit(t)
        for i in G[t]: #t와 연결된 모든 선에 대해
            if not visited[i]: #방문되지 않은 곳이라면
                queue.append(i) #큐에 넣기

'''