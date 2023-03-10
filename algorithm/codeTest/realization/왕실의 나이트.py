'''
8x8 평면
L자형태 이동 수평2칸+수직1칸 or 수직2칸+수평1칸
'''

arr = [[0] * 8 for _ in range(8)]

position = {'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

s = input()
start = (position[s[0]]-1, int(s[1])-1)


cnt = 0
for dr,dc in ((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)):
    new_r = start[1] + dr
    new_c = start[0] + dc
    if 0<=new_r<8 and 0<=new_c<8:
        cnt += 1

print(cnt)