# T = int(input())
# for tc in range(1, T+1):
#     A, B = input().split()
#     A_idx = []
#     n = len(A)
#     rst = n
#     for i in range(len(A)):
#         if A[i] == B[0] :
#             A_idx.append(i)
#     if A_idx:
#         for idx in A_idx:
#             for j in range(1,len(B)):
#                 if idx+j < n and A[idx+j] == B[j]:
#                     continue
#                 else:
#                     break
#             else:
#                 rst = rst - len(B) + 1
#
#
#     print(f'#{tc} {rst}')

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    t = len(A) #텍스트 길이
    p = len(B)  #패턴 길이
    i = 0 #텍스트 인덱스
    j = 0 #패턴 인덱스
    rst = t
    while j<p and i<t:
        if A[i] != B[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == p:
            rst = rst - p + 1
            j = 0
    print(f'#{tc} {rst}')







