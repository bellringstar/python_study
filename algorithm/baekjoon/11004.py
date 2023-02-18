import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

# A.sort()
# print(A[K-1])

# def partition(arr, s, e):
#     p = e
#     i = s - 1
#     for j in range(s,e):
#         if arr[j] <= arr[p]:
#             i += 1
#             arr[i],arr[j] = arr[j],arr[i]
#     arr[i+1],arr[p] = arr[p],arr[i+1]
#
#     return i+1


def quickSort(S,E,K):
    if S<E:
        pivot = partition(S, E)
        if pivot == K:
            return
        elif K < pivot:
            quickSort(S, pivot-1, K)
        else:
            quickSort(pivot+1, E, K)

def swap(i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(S,E):
    if S + 1 == E:
        if A[S] > A[E]:
            swap(S, E)
        return E

    M = (S + E) // 2
    swap(S, M)
    pivot = A[S]
    i = S + 1
    j = E
    while i <= j:
        while pivot < A[j] and j >0:
            j -= 1
        while pivot > A[i] and i < len(A) - 1:
            i += 1
        if i <= j:
            swap(i,j)
            i += 1
            j -= 1

        A[S] = A[j]
        A[j] = pivot
        return j

quickSort(0, N-1, K-1)
print(A[K-1])