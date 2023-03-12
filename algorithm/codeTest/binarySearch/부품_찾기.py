N = int(input())

lst1 = list(map(int, input().split()))

M = int(input())

lst2 = list(map(int, input().split()))

lst1.sort()
lst2.sort()


def binary_search(lst, target, start, end):
    while start <= end:
        mid = (start+end)//2

        if lst[mid] == target:
            return True

        elif lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False

for item in lst2:
    if binary_search(lst1, item, 0, N-1):
        print("yes", end=" ")
    else:
        print("no", end=" ")

