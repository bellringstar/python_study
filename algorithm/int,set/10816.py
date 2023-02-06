# N = int(input())
# N_list = list(map(int, input().split()))
# M = int(input())
# M_list = list(map(int, input().split()))

# N_list.sort()
# for m in M_list:
#     print(N_list.count(m), end=" ")
#-----------------------시간초과-----------------
def binaryS(lst,target,start,end,cnt=0):
    if start >= end:
        return cnt
    mid = (start + end) // 2
    if lst[mid] == target:
        cnt += 1
        binaryS(lst,target,start,mid-1,cnt)
        binaryS(lst, target,mid+1, end, cnt)
    elif lst[mid] > target:
        binaryS(lst, target,start,mid-1,cnt)
    else:
        binaryS(lst, target, mid+1, end, cnt)


N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
N_list.sort()


for num in M_list:
    a = binaryS(N_list, num, 0, N, 0)
    print(a)