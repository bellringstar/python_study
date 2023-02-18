def merge_sort(lst):
    if len(lst)<=1:
        return lst

    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    global ans
    rst = []
    i = j = 0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            rst.append(left[i])
            i += 1
        else:
            rst.append(right[j])
            # ans += j + len(left) - i
            j += 1


    rst += left[i:]
    rst += right[j:]

    return rst


ans = 0
N = int(input())
A = list(map(int, input().split()))
merge_sort(A)

print(ans)