def mergeSort(lst, left, right):
    if left == right:
        return 
    mid = (left + right)//2
    mergeSort(lst, left, mid)
    mergeSort(lst, mid+1, right)


'''


'''