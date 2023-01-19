# 평균/중앙값

def average(lst):
    return sum(lst)//len(lst)

def mod(lst):
    lst.sort()
    mod_idx = len(lst) // 2
    return lst[mod_idx]

lst = []
while len(lst)<5:
    lst.append(int(input()))

print(average(lst))
print(mod(lst))