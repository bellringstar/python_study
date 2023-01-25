'''
ex)T = 3 노선 수
K=3 N=10 M=5  N = 목적지 K = 1회당 최대 몇칸
M개의 정류장번호(충전소 존재)
1 3 5 7 9 
최소 몇 번을 충전해야하는가
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
[o, x, x, o, x, o, x, o, x, o, x]
'''
# import sys
# T = int(input())
# for i in range(T):
#     k,n,m = map(int,sys.stdin.readline().split())
#     st = list(map(int, sys.stdin.readline().split()))

#[0] -> [0+3] == 1? ok [0+3] != 1 -> [0+2] == 1 or != 1? ==1인 순간부터 다시 반복

k,n,m = 3, 10, 5
st = [1, 3, 7, 8, 9]
count = [0] * (n+1)
for i in st:
    count[i] = 1
charge_list=[]
def charge(x):
    if count[x] != 1:
        return charge(x-1)
    elif x:
        return charge_list.append(x)

while k < n:
    charge(k)
    k = 2 + k

print(charge_list)

    
    

        


