# import heapq
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     h = []
#     node = len(arr)
#     for num in arr:
#         heapq.heappush(h, num)
#     h = [0] + h
#     sum_v = 0
#     while node >=1:
#         node = node // 2
#         sum_v += h[node]
#
#
#     print(f'#{tc} {sum_v}')

def enq(item):
    global size
    size += 1
    heap[size] = item
    c = size
    p = c//2
    while p>0 and heap[c] < heap[p]:
        heap[c],heap[p] = heap[p],heap[c]
        c = p
        p = c//2
    return


T = int(input())
for tc in range(1, T+1):
    size = 0
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (N+1)
    for num in arr:
        enq(num)

    last = len(heap) - 1
    sum_v = 0
    while last >=1:
        last //= 2
        sum_v += heap[last]

    print(f'#{tc} {sum_v}')