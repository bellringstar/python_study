def MaxValue(lst):
    maxV = 0
    for num in lst:
        if maxV < num:
            maxV = num
    return maxV

def counting_Sort(lst):
    cnts = [0] * (MaxValue(lst) + 1)
    for num in lst:
        cnts[num] += 1

    for i in range(1, len(cnts)):
        cnts[i] += cnts[i-1]

    temp = [0] * len(lst)

    for i in range(len(lst)-1, -1, -1):
        idx = lst[i]
        temp[cnts[idx] - 1] = idx
    return temp


lst = [1, 5, 2, 1 ,3]
print(counting_Sort(lst))
