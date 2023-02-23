import sys,heapq
input = sys.stdin.readline
# def enq(item):
#     global size
#     size += 1
#     h[size] = item
#     c = size
#     p = c//2
#     while p>0 and h[c] > h[p]:
#         h[c],h[p] = h[p],h[c]
#         c = p
#         p = c//2


N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = int(input())
size = 0
h = []
for num in arr:
    heapq.heappush(h,num)

rst = 0
while len(h) > 1:
    tmp = heapq.heappop(h) + heapq.heappop(h)
    heapq.heappush(h,tmp)
    rst += tmp

print(rst)

