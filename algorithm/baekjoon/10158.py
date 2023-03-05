import sys
input = sys.stdin.readline

d = ((1,1), (-1,1), (-1, -1), (-1,1))

w, h = map(int, input().split()) #w = 가로 h = 세로
p, q = map(int, input().split())
t = int(input())

# n = 0
# cnt = 0
# while True:
#     if cnt == t:
#         print(p,q)
#         break
#     p = p + d[n][0]
#     q = q + d[n][1]
#     if 0<=p<=w and 0<=q<=h:
#         cnt += 1
#         continue
#     else:
#         p = p - d[n][0]
#         q = q - d[n][1]
#         n = (n+1)%4


x = (t - (w-p)) % w
if ((t - (w-p)) // w) % 2 == 0:
    x = w-x
y = (t - (h-q)) % h
if ((t - (h-q)) // h) % 2 == 0:
    y =h - y
print(x,y)