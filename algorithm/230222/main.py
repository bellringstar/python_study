'''
트리
비선형 구조
원소들 간에 1:n 관계
원소들 간에 계층관계를 가지는 계층형 자료구조
상위 원소에서 하위 원소로 내려가면서 확장되는 트리모양의 구조


node = 트리의 원소
edge(간선) = 노드를 연결하느 선, 부모 노드와 자식 노드를 연결
root = 노드 중 최상위 노드
leaf = 트리의 마지막 단말노드, 차수가 0인 노드, 자식 노드가 없는 노드
subtree = 트리 내부의 노드를 root로 하는 또 다른 tree
sibling node(형제노드) = 같은 부모 노드의 자식 노드들
degree(차수) = 노드에 연결된 자식 노드의 수
트리의 차수 = 트리에 있는 노드의 차수 중에서 가장 큰 값


이진트리
모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
각 노드가 자식 노드를 '최대한' 2개 까지만 가질 수 있는 트리
레벨 i에서 노드의 최대 개수는 2**i개
높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는(h+1)개, 최대는 (2**(h+1)-1)


Full Binary Tree(포화 이진 트리)
모든 레벨에 노드가 포화상태로 차 있는 이진 트리
높이가 h일 때, 최대의 노드 개수인 (2**(h+1)-1) 의 노드를 가진 이진 트리
루트를 1번으로 하여 (2**(h+1)-1)까지 정해진 위치에 대한 노드 번호를 가짐

Complete Binary Tree(완전 이진 트리)
노드수가 n일 때 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리

이진트리 - 순회
순회란 트리의 각 노드를 중복되지 않게 전부 방문 하는 것을 말하는데 트리는 비 선형 구조이기 떄문에
선형구조에서와 같이 선후 연결 관계를 알 수 없다.
따라서 특별한 방법이 필요하다.
1. 전위순회(preorder traversal):VLR
부모노드 방문 후 자식노드를 좌, 우 순서로 방문한다.
2. 중위순회(inorder traversal):LVR
왼쪽 자식노드, 부모노드, 오른쪽 자식 노드 순으로 방문한다.
3. 후휘순회(postorder traversal):LRV
자식노드를 좌우 순서로 방문한 후 부모노드를 반문한다.

전위순회
1. 현재 노드 n을 반문하여 처리한다 -> V
2. 현재 노드 n의 왼족 서브트리로 이동한다 -> L
3. 현재 노드 n의 오른쪽 서브트리로 이동한다 -> R

def preorder_traverse(T):
    if T:
        visit(T)
        preorder_traverse(T.left)
        preorder_traverse(T.right)

중위순회
1. 현재 노드 n의 왼쪽 서브트리로 이동:L
2. 현재 노드 n을 방문하여 처리: V
3. ㅎㄴ재 노드 n의 오른쪽 서브트리로 이동:R
def inorder(T):
    if T:
        inorder(T.left)
        visit(T)
        inorder(T.right)

후위순위
1. 현재 노드 n의 왼쪽 서브 트리로 이동한다:L
2. 현재 노드 n의 오른쪽 서브트리로 이동한다:R
3. 현재 노드 n을 방문하여 처리한다:V

def postorder(T):
    if T:
        postorder(T.left)
        postorder(T.right)
        visiti(T)

배열을 이용한 이진 트리의 표현
이진 트리에 각 노드 번호를 부여
루트의 번호를 1로 함
레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 2**n 부터 2**(n+1) -1 까지 번호를 차례로 부여
왼쪽 자식 노드 = 2*p 오른쪽 자식 노드 2*p+1
1

'''
'''
def preorder(root):
    print(root)
    if len(Tree[root]):
        preorder(Tree[root][0])
    if len(Tree[root]) >=2:
        preorder(Tree[root][1])


N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, s.split()))
Tree = [[] for _ in range(N+1)]
for idx in range(0,len(lst),2):
    p = lst[idx]
    c = lst[idx+1]
    Tree[p].append(c)

preorder(1)
# print(Tree)
'''
def preorder(root):
    if root:
        print(root)
        # if leftC[root]:
        preorder(leftC[root])
        # if rightC[root]:
        preorder(rightC[root])
def findA(c):
    p = parent[c]
    if p != 0:
        print(p)
        findA(p)


N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, s.split()))
leftC = [0] * (N+1)
rightC = [0] * (N+1)
parent =[0] * (N+1)
for idx in range(0, len(lst), 2):
    p = lst[idx]
    c = lst[idx+1]
    if leftC[p] == 0:
        leftC[p] = c
    else:
        rightC[p] = c
    parent[c] = p
print(leftC)
print(rightC)
print(parent)
# preorder(1)
findA(12)
